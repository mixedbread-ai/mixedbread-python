"""Hand-written helpers mixed into the generated ``stores.file_batches`` resource.

The generator emits ``FileBatchesResourceBase``/``AsyncFileBatchesResourceBase`` with the API
methods and declares ``FileBatchesResource(FileBatchHelpers, FileBatchesResourceBase)``, so
anything defined here is part of ``client.stores.file_batches`` and may call the generated methods
through ``self``.
"""

from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Any, List, Union, Iterable, Optional
from typing_extensions import Required, TypedDict
from concurrent.futures import ThreadPoolExecutor

from .._types import FileTypes
from .multipart_upload import MultipartUploadOptions, get_file_size
from ..types.stores.store_file_batch import StoreFileBatch
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
    if len(items) > _MAX_FILES:
        raise ValueError(f"A batch takes at most {_MAX_FILES} files, got {len(items)}")
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
        """

        items = _as_items(files)

        def upload_one(item: FileBatchUploadItem) -> str:
            file = item["file"]
            return self._client.files.create(
                file=file, multipart_upload=_multipart(file, multipart_upload), **kwargs
            ).id

        with ThreadPoolExecutor(max(1, max_concurrency)) as pool:
            file_ids = list(pool.map(upload_one, items))
        return self.create(store_identifier, files=_batch_items(items, file_ids), **kwargs)


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

        async def upload_one(item: FileBatchUploadItem) -> str:
            file = item["file"]
            async with slots:
                opts = _multipart(file, multipart_upload)
                return (await self._client.files.create(file=file, multipart_upload=opts, **kwargs)).id

        file_ids = await asyncio.gather(*(upload_one(i) for i in items))
        return await self.create(store_identifier, files=_batch_items(items, file_ids), **kwargs)
