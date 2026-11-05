"""Hand-written helpers mixed into the generated ``stores.file_batches`` resource.

The generator emits ``FileBatchesResourceBase``/``AsyncFileBatchesResourceBase`` with the API
methods and declares ``FileBatchesResource(FileBatchHelpers, FileBatchesResourceBase)``, so
anything defined here is part of ``client.stores.file_batches`` and may call the generated methods
through ``self``.
"""

from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Any, Dict, List, Union, Iterable, Optional, cast
from typing_extensions import Required, TypedDict
from concurrent.futures import ThreadPoolExecutor

import httpx

from .._types import FileTypes
from .._exceptions import APIError
from .multipart_upload import MultipartUploadOptions, get_file_size
from ..types.stores.store_file_batch import Data, DataError, StoreFileBatch
from ..types.stores.store_file_config_param import StoreFileConfigParam
from ..types.stores.file_batch_create_params import File as FileBatchItem

if TYPE_CHECKING:
    from ..resources.stores.file_batches import FileBatchesResourceBase, AsyncFileBatchesResourceBase

    _SyncBase = FileBatchesResourceBase
    _AsyncBase = AsyncFileBatchesResourceBase
else:
    _SyncBase = object
    _AsyncBase = object

# Backfills are mostly documents of a few MB; multipart sends them straight to storage.
_MULTIPART_THRESHOLD = 5 * 1024 * 1024
_MAX_FILES = 100


def _multipart(
    file: FileTypes, multipart_upload: bool | MultipartUploadOptions | None
) -> bool | MultipartUploadOptions | None:
    # ``files.create`` treats options as "always multipart", so the size check happens here.
    if isinstance(multipart_upload, bool):
        return multipart_upload
    options = multipart_upload or MultipartUploadOptions(threshold=_MULTIPART_THRESHOLD)
    try:
        return options if get_file_size(file) >= options.threshold else False
    except (TypeError, OSError):
        return None


class FileBatchUploadItem(TypedDict, total=False):
    """A file with the store fields to add it with."""

    file: Required[FileTypes]
    external_id: Optional[str]
    metadata: object
    config: StoreFileConfigParam


def _as_items(files: Iterable[Union[FileTypes, FileBatchUploadItem]]) -> List[FileBatchUploadItem]:
    items: List[FileBatchUploadItem] = [f if isinstance(f, dict) else {"file": f} for f in files]
    if not 1 <= len(items) <= _MAX_FILES:
        raise ValueError(f"A batch takes 1 to {_MAX_FILES} files, got {len(items)}")
    return items


def _batch_items(items: List[FileBatchUploadItem], file_ids: Iterable[str]) -> List[FileBatchItem]:
    batch: List[FileBatchItem] = []
    for item, file_id in zip(items, file_ids):
        entry: FileBatchItem = {"file_id": file_id}
        if "external_id" in item:
            entry["external_id"] = item["external_id"]
        if "metadata" in item:
            entry["metadata"] = item["metadata"]
        if "config" in item:
            entry["config"] = item["config"]
        batch.append(entry)
    return batch


# A multipart part goes straight to storage, so its failure is an httpx error rather than an APIError.
_UPLOAD_ERRORS = (APIError, httpx.HTTPError)


def _upload_failed(item: FileBatchUploadItem, error: Exception) -> Data:
    body: object = error.body if isinstance(error, APIError) else None
    code = cast(Dict[str, object], body).get("code") if isinstance(body, dict) else None
    return Data.construct(
        file_id="",
        external_id=item.get("external_id"),
        error=DataError.construct(code=code if isinstance(code, str) else "upload_error", message=str(error)),
    )


def _uploaded(items: List[FileBatchUploadItem], uploaded: List[Union[str, Data]]) -> List[FileBatchItem]:
    ok = [(item, u) for item, u in zip(items, uploaded) if isinstance(u, str)]
    return _batch_items([item for item, _ in ok], [u for _, u in ok])


def _merge(uploaded: List[Union[str, Data]], added: Optional[StoreFileBatch]) -> StoreFileBatch:
    """Put each failed upload back at its position among the batch's results."""
    results = iter(added.data if added else [])
    data = [next(results) if isinstance(u, str) else u for u in uploaded]
    return StoreFileBatch.construct(data=data, object="store.file_batch")


class FileBatchHelpers(_SyncBase):
    def upload(
        self,
        store_identifier: str,
        *,
        files: Iterable[Union[FileTypes, FileBatchUploadItem]],
        multipart_upload: bool | MultipartUploadOptions | None = None,
        max_concurrency: int = 5,
        **kwargs: Any,
    ) -> StoreFileBatch:
        """Upload up to 100 files to the ``files`` API and add them to the store in one batch.

        Each entry is a file or a ``FileBatchUploadItem`` with its own ``external_id``, ``metadata``
        and ``config``.
        Files are uploaded ``max_concurrency`` at a time and processed asynchronously.
        ``multipart_upload`` controls the upload: ``None`` uses multipart above 5MB, ``True``/``False``
        force or disable multipart, ``MultipartUploadOptions`` customises it (its threshold included).
        ``data[i]`` is the outcome of ``files[i]``; a failed upload has an empty ``file_id`` and its error.
        """

        items = _as_items(files)

        def upload_one(item: FileBatchUploadItem) -> Union[str, Data]:
            file = item["file"]
            try:
                return self._client.files.create(
                    file=file, multipart_upload=_multipart(file, multipart_upload), **kwargs
                ).id
            except _UPLOAD_ERRORS as e:
                return _upload_failed(item, e)

        with ThreadPoolExecutor(max(1, max_concurrency)) as pool:
            uploaded = list(pool.map(upload_one, items))
        batch = _uploaded(items, uploaded)
        return _merge(uploaded, self.create(store_identifier, files=batch, **kwargs) if batch else None)


class AsyncFileBatchHelpers(_AsyncBase):
    async def upload(
        self,
        store_identifier: str,
        *,
        files: Iterable[Union[FileTypes, FileBatchUploadItem]],
        multipart_upload: bool | MultipartUploadOptions | None = None,
        max_concurrency: int = 5,
        **kwargs: Any,
    ) -> StoreFileBatch:
        """Upload up to 100 files and add them to the store in one batch (see ``FileBatchHelpers.upload``)."""
        items = _as_items(files)
        slots = asyncio.Semaphore(max(1, max_concurrency))

        async def upload_one(item: FileBatchUploadItem) -> Union[str, Data]:
            file = item["file"]
            async with slots:
                opts = _multipart(file, multipart_upload)
                try:
                    return (await self._client.files.create(file=file, multipart_upload=opts, **kwargs)).id
                except _UPLOAD_ERRORS as e:
                    return _upload_failed(item, e)

        uploaded = list(await asyncio.gather(*(upload_one(i) for i in items)))
        batch = _uploaded(items, uploaded)
        return _merge(uploaded, await self.create(store_identifier, files=batch, **kwargs) if batch else None)
