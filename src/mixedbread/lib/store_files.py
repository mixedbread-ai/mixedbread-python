"""Hand-written helpers mixed into the generated ``stores.files`` resource.

The generator emits ``FilesResourceBase``/``AsyncFilesResourceBase`` with the API methods and
declares ``FilesResource(StoreFileHelpers, FilesResourceBase)``, so anything defined here is part
of ``client.stores.files`` and may call the generated methods through ``self``.
"""

from __future__ import annotations

import functools
from typing import TYPE_CHECKING, Any, Optional

from . import polling
from .._types import Omit, NotGiven, FileTypes, omit, not_given
from .._utils import is_given
from .multipart_upload import MultipartUploadOptions
from ..types.stores.store_file import StoreFile
from ..types.stores.store_file_config_param import StoreFileConfigParam

if TYPE_CHECKING:
    from ..resources.stores.files import FilesResourceBase, AsyncFilesResourceBase

    _SyncBase = FilesResourceBase
    _AsyncBase = AsyncFilesResourceBase
else:
    _SyncBase = object
    _AsyncBase = object

_TERMINAL = ("completed", "failed", "cancelled")


class StoreFileHelpers(_SyncBase):
    def poll(
        self,
        file_identifier: str,
        *,
        store_identifier: str,
        poll_interval_ms: int | NotGiven = not_given,
        poll_timeout_ms: float | NotGiven = not_given,
        **kwargs: Any,
    ) -> StoreFile:
        """Poll a file's status until it reaches a terminal state.

        Args:
            file_identifier: The ID or external_id of the file to poll
            store_identifier: The ID of the store
            poll_interval_ms: The interval between polls in milliseconds (default 500)
            poll_timeout_ms: The maximum time to poll for in milliseconds (default: no timeout)
        Returns:
            The file object once it reaches a terminal state
        """
        polling_interval_ms = poll_interval_ms if is_given(poll_interval_ms) else 500
        polling_timeout_ms = poll_timeout_ms if is_given(poll_timeout_ms) else None
        return polling.poll(
            fn=functools.partial(self.retrieve, file_identifier, store_identifier=store_identifier, **kwargs),
            condition=lambda res: res.status in _TERMINAL,
            interval_seconds=polling_interval_ms / 1000,
            timeout_seconds=polling_timeout_ms / 1000 if polling_timeout_ms is not None else None,
        )

    def create_and_poll(
        self,
        file_id: str,
        *,
        store_identifier: str,
        metadata: Optional[object] | Omit = omit,
        config: StoreFileConfigParam | Omit = omit,
        external_id: Optional[str] | Omit = omit,
        overwrite: bool | Omit = omit,
        experimental: Optional[StoreFileConfigParam] | Omit = omit,
        poll_interval_ms: int | NotGiven = not_given,
        poll_timeout_ms: float | NotGiven = not_given,
        **kwargs: Any,
    ) -> StoreFile:
        """Attach a file to the given store and wait for it to be processed."""
        self.create(
            store_identifier=store_identifier,
            file_id=file_id,
            metadata=metadata,
            config=config,
            external_id=external_id,
            overwrite=overwrite,
            experimental=experimental,
            **kwargs,
        )
        return self.poll(
            file_id,
            store_identifier=store_identifier,
            poll_interval_ms=poll_interval_ms,
            poll_timeout_ms=poll_timeout_ms,
            **kwargs,
        )

    def upload(
        self,
        *,
        store_identifier: str,
        file: FileTypes,
        metadata: Optional[object] | Omit = omit,
        config: StoreFileConfigParam | Omit = omit,
        external_id: Optional[str] | Omit = omit,
        overwrite: bool | Omit = omit,
        experimental: Optional[StoreFileConfigParam] | Omit = omit,
        multipart_upload: bool | MultipartUploadOptions | None = None,
        **kwargs: Any,
    ) -> StoreFile:
        """Upload a file to the ``files`` API and then attach it to the given store.

        The file is processed asynchronously; use ``upload_and_poll`` to wait for it.
        ``multipart_upload`` controls the upload: ``None`` auto-detects by size, ``True``/``False``
        force or disable multipart, ``MultipartUploadOptions`` customises it.
        """
        file_obj = self._client.files.create(file=file, multipart_upload=multipart_upload, **kwargs)
        return self.create(
            store_identifier=store_identifier,
            file_id=file_obj.id,
            metadata=metadata,
            config=config,
            external_id=external_id,
            overwrite=overwrite,
            experimental=experimental,
            **kwargs,
        )

    def upload_and_poll(
        self,
        *,
        store_identifier: str,
        file: FileTypes,
        metadata: Optional[object] | Omit = omit,
        config: StoreFileConfigParam | Omit = omit,
        external_id: Optional[str] | Omit = omit,
        overwrite: bool | Omit = omit,
        experimental: Optional[StoreFileConfigParam] | Omit = omit,
        multipart_upload: bool | MultipartUploadOptions | None = None,
        poll_interval_ms: int | NotGiven = not_given,
        poll_timeout_ms: float | NotGiven = not_given,
        **kwargs: Any,
    ) -> StoreFile:
        """Upload a file, attach it to the store and poll until processing is complete."""
        file_obj = self._client.files.create(file=file, multipart_upload=multipart_upload, **kwargs)
        return self.create_and_poll(
            store_identifier=store_identifier,
            file_id=file_obj.id,
            metadata=metadata,
            config=config,
            external_id=external_id,
            overwrite=overwrite,
            experimental=experimental,
            poll_interval_ms=poll_interval_ms,
            poll_timeout_ms=poll_timeout_ms,
            **kwargs,
        )


class AsyncStoreFileHelpers(_AsyncBase):
    async def poll(
        self,
        file_identifier: str,
        *,
        store_identifier: str,
        poll_interval_ms: int | NotGiven = not_given,
        poll_timeout_ms: float | NotGiven = not_given,
        **kwargs: Any,
    ) -> StoreFile:
        """Poll a file's status until it reaches a terminal state."""
        polling_interval_ms = poll_interval_ms if is_given(poll_interval_ms) else 500
        polling_timeout_ms = poll_timeout_ms if is_given(poll_timeout_ms) else None
        return await polling.poll_async(
            fn=functools.partial(self.retrieve, file_identifier, store_identifier=store_identifier, **kwargs),
            condition=lambda res: res.status in _TERMINAL,
            interval_seconds=polling_interval_ms / 1000,
            timeout_seconds=polling_timeout_ms / 1000 if polling_timeout_ms is not None else None,
        )

    async def create_and_poll(
        self,
        file_id: str,
        *,
        store_identifier: str,
        metadata: Optional[object] | Omit = omit,
        config: StoreFileConfigParam | Omit = omit,
        external_id: Optional[str] | Omit = omit,
        overwrite: bool | Omit = omit,
        experimental: Optional[StoreFileConfigParam] | Omit = omit,
        poll_interval_ms: int | NotGiven = not_given,
        poll_timeout_ms: float | NotGiven = not_given,
        **kwargs: Any,
    ) -> StoreFile:
        """Attach a file to the given store and wait for it to be processed."""
        await self.create(
            store_identifier=store_identifier,
            file_id=file_id,
            metadata=metadata,
            config=config,
            external_id=external_id,
            overwrite=overwrite,
            experimental=experimental,
            **kwargs,
        )
        return await self.poll(
            file_id,
            store_identifier=store_identifier,
            poll_interval_ms=poll_interval_ms,
            poll_timeout_ms=poll_timeout_ms,
            **kwargs,
        )

    async def upload(
        self,
        *,
        store_identifier: str,
        file: FileTypes,
        metadata: Optional[object] | Omit = omit,
        config: StoreFileConfigParam | Omit = omit,
        external_id: Optional[str] | Omit = omit,
        overwrite: bool | Omit = omit,
        experimental: Optional[StoreFileConfigParam] | Omit = omit,
        multipart_upload: bool | MultipartUploadOptions | None = None,
        **kwargs: Any,
    ) -> StoreFile:
        """Upload a file to the ``files`` API and then attach it to the given store."""
        file_obj = await self._client.files.create(file=file, multipart_upload=multipart_upload, **kwargs)
        return await self.create(
            store_identifier=store_identifier,
            file_id=file_obj.id,
            metadata=metadata,
            config=config,
            external_id=external_id,
            overwrite=overwrite,
            experimental=experimental,
            **kwargs,
        )

    async def upload_and_poll(
        self,
        *,
        store_identifier: str,
        file: FileTypes,
        metadata: Optional[object] | Omit = omit,
        config: StoreFileConfigParam | Omit = omit,
        external_id: Optional[str] | Omit = omit,
        overwrite: bool | Omit = omit,
        experimental: Optional[StoreFileConfigParam] | Omit = omit,
        multipart_upload: bool | MultipartUploadOptions | None = None,
        poll_interval_ms: int | NotGiven = not_given,
        poll_timeout_ms: float | NotGiven = not_given,
        **kwargs: Any,
    ) -> StoreFile:
        """Upload a file, attach it to the store and poll until processing is complete."""
        file_obj = await self._client.files.create(file=file, multipart_upload=multipart_upload, **kwargs)
        return await self.create_and_poll(
            store_identifier=store_identifier,
            file_id=file_obj.id,
            metadata=metadata,
            config=config,
            external_id=external_id,
            overwrite=overwrite,
            experimental=experimental,
            poll_interval_ms=poll_interval_ms,
            poll_timeout_ms=poll_timeout_ms,
            **kwargs,
        )
