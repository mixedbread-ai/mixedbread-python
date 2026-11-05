from typing import Any, Dict, List

import pytest

from mixedbread.lib import MultipartUploadOptions
from mixedbread.lib.file_batches import FileBatchHelpers, AsyncFileBatchHelpers
from mixedbread.types.file_object import FileObject
from mixedbread.types.stores.store_file_batch import StoreFileBatch


class _Files:
    def __init__(self) -> None:
        self.calls: List[Dict[str, Any]] = []

    def create(self, **kwargs: Any) -> FileObject:
        self.calls.append(kwargs)
        return FileObject.construct(id=f"file_{kwargs['file'][0]}")


class _AsyncFiles(_Files):
    async def create(self, **kwargs: Any) -> FileObject:  # type: ignore[override]
        return super().create(**kwargs)


class _Client:
    def __init__(self, files: _Files) -> None:
        self.files = files


class _FileBatches(FileBatchHelpers):
    def __init__(self) -> None:
        self.files = _Files()
        self._client = _Client(self.files)  # type: ignore[assignment]
        self.batches: List[List[Dict[str, Any]]] = []

    def create(self, _store_identifier: str, *, files: List[Dict[str, Any]], **_: Any) -> StoreFileBatch:  # type: ignore[override]
        self.batches.append(files)
        return StoreFileBatch.construct(data=[])


class _AsyncFileBatches(AsyncFileBatchHelpers):
    def __init__(self) -> None:
        self.files = _AsyncFiles()
        self._client = _Client(self.files)  # type: ignore[assignment]
        self.batches: List[List[Dict[str, Any]]] = []

    async def create(self, _store_identifier: str, *, files: List[Dict[str, Any]], **_: Any) -> StoreFileBatch:  # type: ignore[override]
        self.batches.append(files)
        return StoreFileBatch.construct(data=[])


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

    with pytest.raises(ValueError, match="at most 100"):
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
