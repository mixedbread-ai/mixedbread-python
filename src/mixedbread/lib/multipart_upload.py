from __future__ import annotations

import os
import math
import asyncio
import mimetypes
import threading
from typing import TYPE_CHECKING, Any, List, Union, Callable, Optional
from pathlib import Path
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor

import httpx

if TYPE_CHECKING:
    from .._types import FileTypes, FileContent
    from ..resources.files.uploads import UploadsResource, AsyncUploadsResource

from ..types.file_object import FileObject
from ..types.files.multipart_upload_part_param import MultipartUploadPartParam

DEFAULT_THRESHOLD = 100 * 1024 * 1024  # 100 MB
DEFAULT_PART_SIZE = 100 * 1024 * 1024  # 100 MB
DEFAULT_CONCURRENCY = 5
UPLOAD_TIMEOUT = 300  # 5 minutes


@dataclass
class PartUploadEvent:
    """Event emitted after each part is uploaded."""

    part_number: int
    total_parts: int
    part_size: int
    uploaded_bytes: int
    total_bytes: int


@dataclass
class MultipartUploadOptions:
    """Options for controlling multipart upload behavior."""

    threshold: int = DEFAULT_THRESHOLD
    part_size: int = DEFAULT_PART_SIZE
    concurrency: int = DEFAULT_CONCURRENCY
    on_part_upload: Optional[Callable[[PartUploadEvent], None]] = None


@dataclass
class _ResolvedFile:
    """Internal resolved file representation."""

    data: Union[bytes, Path]
    file_size: int
    filename: str
    mime_type: str


def _get_file_size(file: FileTypes) -> int:
    """Get file size without reading the entire file into memory.

    Raises TypeError if the size cannot be determined.
    """
    # Handle tuple forms: (filename, content, ...)
    if isinstance(file, tuple):
        file_content = file[1]
    else:
        file_content = file

    if isinstance(file_content, bytes):
        return len(file_content)

    if isinstance(file_content, os.PathLike):
        return os.stat(file_content).st_size

    # IO[bytes] - try seek-based size detection
    if hasattr(file_content, "seek") and hasattr(file_content, "tell"):
        current = file_content.tell()
        file_content.seek(0, 2)
        size = file_content.tell()
        file_content.seek(current)
        return size

    raise TypeError(f"Cannot determine file size for {type(file_content)}")


def _resolve_file_input(file: FileTypes) -> _ResolvedFile:
    """Resolve a FileTypes input into a normalized representation."""
    filename: Optional[str] = None
    mime_type: Optional[str] = None
    file_content: FileContent

    if isinstance(file, tuple):
        filename = file[0]
        file_content = file[1]
        if len(file) >= 3:
            mime_type = file[2]  # type: ignore[misc]
    else:
        file_content = file

    # Resolve file content to bytes or Path
    data: Union[bytes, Path]
    if isinstance(file_content, bytes):
        data = file_content
        file_size = len(file_content)
        if filename is None:
            filename = "upload"
    elif isinstance(file_content, os.PathLike):
        path = Path(file_content)
        data = path
        file_size = os.stat(path).st_size
        if filename is None:
            filename = path.name
    elif hasattr(file_content, "read"):
        # IO[bytes] - read into memory
        data = file_content.read()
        file_size = len(data)
        if filename is None:
            name = getattr(file_content, "name", None)
            if name:
                filename = os.path.basename(name)
            else:
                filename = "upload"
    else:
        raise TypeError(f"Unsupported file type: {type(file_content)}")

    # Resolve mime type
    if not mime_type and filename:
        guessed, _ = mimetypes.guess_type(filename)
        mime_type = guessed or "application/octet-stream"
    elif not mime_type:
        mime_type = "application/octet-stream"

    return _ResolvedFile(
        data=data,
        file_size=file_size,
        filename=filename or "upload",
        mime_type=mime_type,
    )


def _read_part(resolved: _ResolvedFile, part_number: int, part_size: int) -> bytes:
    """Read a specific part from the resolved file data.

    For bytes data, slices directly. For PathLike, opens its own file handle
    (thread-safe for concurrent uploads).
    """
    offset = (part_number - 1) * part_size  # parts are 1-based

    if isinstance(resolved.data, bytes):
        return resolved.data[offset : offset + part_size]

    # PathLike - each caller gets its own file handle
    with open(resolved.data, "rb") as f:
        f.seek(offset)
        return f.read(part_size)


def _upload_single_part(
    url: str,
    data: bytes,
    http_client: httpx.Client,
) -> str:
    """Upload a single part to its presigned URL. Returns the ETag."""
    response = http_client.put(url, content=data)
    response.raise_for_status()
    return response.headers.get("etag", "")


async def _async_upload_single_part(
    url: str,
    data: bytes,
    http_client: httpx.AsyncClient,
) -> str:
    """Upload a single part to its presigned URL asynchronously. Returns the ETag."""
    response = await http_client.put(url, content=data)
    response.raise_for_status()
    return response.headers.get("etag", "")


def multipart_create_sync(
    uploads: UploadsResource,
    file: FileTypes,
    options: MultipartUploadOptions,
) -> FileObject:
    """Perform a multipart upload synchronously."""
    resolved = _resolve_file_input(file)
    part_count = max(1, math.ceil(resolved.file_size / options.part_size))

    # Step 1: Initiate the multipart upload
    upload = uploads.create(
        filename=resolved.filename,
        file_size=resolved.file_size,
        mime_type=resolved.mime_type,
        part_count=part_count,
    )
    upload_id = upload.id

    try:
        # Step 2: Upload parts concurrently
        completed_parts: List[MultipartUploadPartParam] = []

        uploaded_bytes_total = 0
        upload_lock = threading.Lock()

        with httpx.Client(timeout=httpx.Timeout(UPLOAD_TIMEOUT)) as http_client:

            def _do_upload(part_url: Any) -> MultipartUploadPartParam:
                nonlocal uploaded_bytes_total
                part_data = _read_part(resolved, part_url.part_number, options.part_size)
                etag = _upload_single_part(part_url.url, part_data, http_client)

                if options.on_part_upload:
                    with upload_lock:
                        uploaded_bytes_total += len(part_data)
                        uploaded_bytes = uploaded_bytes_total
                    options.on_part_upload(
                        PartUploadEvent(
                            part_number=part_url.part_number,
                            total_parts=part_count,
                            part_size=len(part_data),
                            uploaded_bytes=uploaded_bytes,
                            total_bytes=resolved.file_size,
                        )
                    )

                return MultipartUploadPartParam(part_number=part_url.part_number, etag=etag)

            with ThreadPoolExecutor(max_workers=options.concurrency) as executor:
                futures = [executor.submit(_do_upload, pu) for pu in upload.part_urls]
                for future in futures:
                    completed_parts.append(future.result())

        # Sort by part number
        completed_parts.sort(key=lambda p: p["part_number"])

        # Step 3: Complete the upload
        return uploads.complete(
            upload_id=upload_id,
            parts=completed_parts,
        )

    except BaseException:
        # Abort on any failure (including KeyboardInterrupt, CancelledError)
        try:
            uploads.abort(upload_id=upload_id)
        except Exception:
            pass  # Best effort abort
        raise


async def multipart_create_async(
    uploads: AsyncUploadsResource,
    file: FileTypes,
    options: MultipartUploadOptions,
) -> FileObject:
    """Perform a multipart upload asynchronously."""
    resolved = await asyncio.to_thread(_resolve_file_input, file)
    part_count = max(1, math.ceil(resolved.file_size / options.part_size))

    # Step 1: Initiate the multipart upload
    upload = await uploads.create(
        filename=resolved.filename,
        file_size=resolved.file_size,
        mime_type=resolved.mime_type,
        part_count=part_count,
    )
    upload_id = upload.id

    try:
        # Step 2: Upload parts concurrently
        semaphore = asyncio.Semaphore(options.concurrency)
        uploaded_bytes_total = 0

        async with httpx.AsyncClient(timeout=httpx.Timeout(UPLOAD_TIMEOUT)) as http_client:

            async def _do_upload(part_url: Any) -> MultipartUploadPartParam:
                nonlocal uploaded_bytes_total
                async with semaphore:
                    part_data = await asyncio.to_thread(_read_part, resolved, part_url.part_number, options.part_size)
                    etag = await _async_upload_single_part(part_url.url, part_data, http_client)

                    if options.on_part_upload:
                        uploaded_bytes_total += len(part_data)
                        options.on_part_upload(
                            PartUploadEvent(
                                part_number=part_url.part_number,
                                total_parts=part_count,
                                part_size=len(part_data),
                                uploaded_bytes=uploaded_bytes_total,
                                total_bytes=resolved.file_size,
                            )
                        )

                    return MultipartUploadPartParam(part_number=part_url.part_number, etag=etag)

            completed_parts: List[MultipartUploadPartParam] = list(
                await asyncio.gather(*[_do_upload(pu) for pu in upload.part_urls])
            )

        # Sort by part number
        completed_parts.sort(key=lambda p: p["part_number"])

        # Step 3: Complete the upload
        return await uploads.complete(
            upload_id=upload_id,
            parts=completed_parts,
        )

    except BaseException:
        # Abort on any failure (including KeyboardInterrupt, CancelledError)
        try:
            await uploads.abort(upload_id=upload_id)
        except Exception:
            pass  # Best effort abort
        raise
