from typing import Any, Dict, List, Optional

import httpx
import pytest

from mixedbread import APIStatusError, UnprocessableEntityError
from mixedbread.lib import MultipartUploadOptions
from mixedbread.lib.file_batches import FileBatchHelpers, AsyncFileBatchHelpers
from mixedbread.types.file_object import FileObject
from mixedbread.types.stores.store_file_batch import Data, StoreFileBatch


def _status_error(cls: Any, status: int, body: object) -> APIStatusError:
    response = httpx.Response(status, request=httpx.Request("POST", "https://api.test/v1/files"))
    return cls("Error code: %d" % status, response=response, body=body)  # type: ignore[no-any-return]


_INVALID = _status_error(UnprocessableEntityError, 422, {"code": "file_invalid_error", "message": "Invalid file"})


class _Files:
    def __init__(self, failures: Optional[Dict[str, Exception]] = None) -> None:
        self.calls: List[Dict[str, Any]] = []
        self.failures = failures or {}

    def create(self, **kwargs: Any) -> FileObject:
        self.calls.append(kwargs)
        name = kwargs["file"][0]
        if name in self.failures:
            raise self.failures[name]
        return FileObject.construct(id=f"file_{name}")


class _AsyncFiles(_Files):
    async def create(self, **kwargs: Any) -> FileObject:  # type: ignore[override]
        return super().create(**kwargs)


class _Client:
    def __init__(self, files: _Files) -> None:
        self.files = files


def _added(files: List[Dict[str, Any]]) -> StoreFileBatch:
    data = [Data.construct(file_id=f["file_id"], external_id=f.get("external_id"), status="pending") for f in files]
    return StoreFileBatch.construct(data=data)


class _FileBatches(FileBatchHelpers):
    def __init__(self, failures: Optional[Dict[str, Exception]] = None) -> None:
        self.files = _Files(failures)
        self._client = _Client(self.files)  # type: ignore[assignment]
        self.batches: List[List[Dict[str, Any]]] = []

    def create(self, _store_identifier: str, *, files: List[Dict[str, Any]], **_: Any) -> StoreFileBatch:  # type: ignore[override]
        self.batches.append(files)
        return _added(files)


class _AsyncFileBatches(AsyncFileBatchHelpers):
    def __init__(self, failures: Optional[Dict[str, Exception]] = None) -> None:
        self.files = _AsyncFiles(failures)
        self._client = _Client(self.files)  # type: ignore[assignment]
        self.batches: List[List[Dict[str, Any]]] = []

    async def create(self, _store_identifier: str, *, files: List[Dict[str, Any]], **_: Any) -> StoreFileBatch:  # type: ignore[override]
        self.batches.append(files)
        return _added(files)


def test_upload_adds_per_file_fields_and_uses_multipart_for_large_files() -> None:
    batches = _FileBatches()

    files: List[Any] = [
        ("a", b"x"),
        {"file": ("b", b"x" * 5 * 1024 * 1024), "external_id": "doc-b", "metadata": {"deal": "acme"}},
    ]

    batches.upload("store", files=files)

    modes = {c["file"][0]: c["multipart_upload"] for c in batches.files.calls}
    assert modes["a"] is False
    assert isinstance(modes["b"], MultipartUploadOptions)
    assert batches.batches == [
        [
            {"file_id": "file_a"},
            {"file_id": "file_b", "external_id": "doc-b", "metadata": {"deal": "acme"}},
        ]
    ]


def test_more_than_100_files_are_rejected_before_anything_is_uploaded() -> None:
    batches = _FileBatches()

    with pytest.raises(ValueError, match="1 to 100"):
        batches.upload("store", files=[(str(i), b"x") for i in range(101)])
    assert batches.files.calls == []


@pytest.mark.asyncio
async def test_async_upload_adds_files_in_order() -> None:
    batches = _AsyncFileBatches()

    await batches.upload("store", files=[(str(i), b"x") for i in range(20)], max_concurrency=3)

    assert batches.batches == [[{"file_id": f"file_{i}"} for i in range(20)]]


def test_custom_multipart_options_keep_their_threshold() -> None:
    batches = _FileBatches()
    options = MultipartUploadOptions(threshold=10 * 1024 * 1024, concurrency=2)

    batches.upload(
        "store", files=[("small", b"x" * 6 * 1024 * 1024), ("large", b"x" * 10 * 1024 * 1024)], multipart_upload=options
    )

    modes = {c["file"][0]: c["multipart_upload"] for c in batches.files.calls}
    assert modes == {"small": False, "large": options}


def test_a_failed_upload_is_reported_in_place_and_the_other_files_are_still_added() -> None:
    batches = _FileBatches(failures={"bad.txt": _INVALID})

    result = batches.upload(
        "store",
        files=[("a.txt", b"x"), {"file": ("bad.txt", b""), "external_id": "doc-bad"}, ("c.txt", b"x")],
    )

    assert batches.batches == [[{"file_id": "file_a.txt"}, {"file_id": "file_c.txt"}]]
    assert result.object == "store.file_batch"
    added_a, failed, added_c = result.data
    assert (added_a.file_id, added_c.file_id) == ("file_a.txt", "file_c.txt")
    assert (failed.file_id, failed.external_id, failed.status) == ("", "doc-bad", None)
    assert failed.error is not None
    assert (failed.error.code, failed.error.message) == ("file_invalid_error", _INVALID.message)


def test_when_every_upload_fails_nothing_is_added() -> None:
    batches = _FileBatches(failures={"bad.txt": _INVALID})

    result = batches.upload("store", files=[("bad.txt", b"")])

    assert batches.batches == []
    assert [d.error.code for d in result.data if d.error] == ["file_invalid_error"]


def test_a_failed_multipart_transfer_is_reported_in_place() -> None:
    request = httpx.Request("PUT", "https://storage.test/part")
    broken = httpx.HTTPStatusError("part upload failed", request=request, response=httpx.Response(503, request=request))
    batches = _FileBatches(failures={"big.pdf": broken})

    result = batches.upload("store", files=[("a.txt", b"x"), ("big.pdf", b"x")])

    assert batches.batches == [[{"file_id": "file_a.txt"}]]
    assert result.data[1].error is not None
    assert result.data[1].error.code == "upload_error"


@pytest.mark.asyncio
async def test_async_upload_reports_a_failed_upload_in_place() -> None:
    batches = _AsyncFileBatches(failures={"1": _INVALID})

    result = await batches.upload("store", files=[(str(i), b"x") for i in range(3)])

    assert [d.file_id for d in result.data] == ["file_0", "", "file_2"]
    assert batches.batches == [[{"file_id": "file_0"}, {"file_id": "file_2"}]]


def test_an_empty_file_list_is_rejected() -> None:
    with pytest.raises(ValueError, match="1 to 100"):
        _FileBatches().upload("store", files=[])
