"""Hand-written helpers mixed into the generated ``files`` resource.

``create`` is overridden to switch to a presigned multipart upload for large files; everything
else is delegated to the generated ``FilesResourceBase``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from .._types import Body, Query, Headers, NotGiven, FileTypes, not_given
from .multipart_upload import MultipartUploadOptions, get_file_size, multipart_create_sync, multipart_create_async
from ..types.file_object import FileObject

if TYPE_CHECKING:
    from ..resources.files.files import FilesResourceBase, AsyncFilesResourceBase

    _SyncBase = FilesResourceBase
    _AsyncBase = AsyncFilesResourceBase
else:
    _SyncBase = object
    _AsyncBase = object


def _resolve(file: FileTypes, multipart_upload: bool | MultipartUploadOptions | None) -> MultipartUploadOptions | None:
    """The multipart options to use, or ``None`` for a plain upload."""
    if multipart_upload is False:
        return None
    if isinstance(multipart_upload, MultipartUploadOptions):
        return multipart_upload
    opts = MultipartUploadOptions()
    if multipart_upload is True:
        return opts
    try:
        return opts if get_file_size(file) >= opts.threshold else None
    except (TypeError, OSError):
        return None


class FileHelpers(_SyncBase):
    def create(  # type: ignore[override]
        self,
        *,
        file: FileTypes,
        multipart_upload: bool | MultipartUploadOptions | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileObject:
        """Upload a new file.

        Large files (above 100MB by default) are uploaded as presigned multipart uploads.
        ``multipart_upload``: ``None`` auto-detects by size, ``True``/``False`` force or disable
        multipart, ``MultipartUploadOptions`` customises threshold, part size and concurrency.
        """
        opts = _resolve(file, multipart_upload)
        if opts is not None:
            return multipart_create_sync(
                self.uploads,
                file,
                opts,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )
        return super().create(
            file=file, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )


class AsyncFileHelpers(_AsyncBase):
    async def create(  # type: ignore[override]
        self,
        *,
        file: FileTypes,
        multipart_upload: bool | MultipartUploadOptions | None = None,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileObject:
        """Upload a new file (see ``FileHelpers.create``)."""
        opts = _resolve(file, multipart_upload)
        if opts is not None:
            return await multipart_create_async(
                self.uploads,
                file,
                opts,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )
        return await super().create(
            file=file, extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
        )
