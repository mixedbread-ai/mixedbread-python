"""Hand-written helpers mixed into the generated ``parsing.jobs`` resource (see store_files.py)."""

from __future__ import annotations

import functools
from typing import TYPE_CHECKING, Any, List, Optional

from . import polling
from .._types import Omit, NotGiven, FileTypes, omit, not_given
from .multipart_upload import MultipartUploadOptions
from ..types.parsing.parsing_job import ParsingJob
from ..types.parsing.element_type import ElementType
from ..types.parsing.return_format import ReturnFormat
from ..types.parsing.chunking_strategy import ChunkingStrategy

if TYPE_CHECKING:
    from ..resources.parsing.jobs import JobsResourceBase, AsyncJobsResourceBase

    _SyncBase = JobsResourceBase
    _AsyncBase = AsyncJobsResourceBase
else:
    _SyncBase = object
    _AsyncBase = object

_TERMINAL = ("completed", "failed", "cancelled")


class ParsingJobHelpers(_SyncBase):
    def poll(
        self,
        job_id: str,
        *,
        poll_interval_ms: int | NotGiven = not_given,
        poll_timeout_ms: float | NotGiven = not_given,
        **kwargs: Any,
    ) -> ParsingJob:
        """Poll a job's status until it reaches a terminal state."""
        polling_interval_ms = poll_interval_ms or 500
        polling_timeout_ms = poll_timeout_ms or None
        return polling.poll(
            fn=functools.partial(self.retrieve, job_id, **kwargs),
            condition=lambda res: res.status in _TERMINAL,
            interval_seconds=polling_interval_ms / 1000,
            timeout_seconds=polling_timeout_ms / 1000 if polling_timeout_ms else None,
        )

    def create_and_poll(
        self,
        *,
        file_id: str,
        chunking_strategy: ChunkingStrategy | Omit = omit,
        element_types: Optional[List[ElementType]] | Omit = omit,
        return_format: ReturnFormat | Omit = omit,
        poll_interval_ms: int | NotGiven = not_given,
        poll_timeout_ms: float | NotGiven = not_given,
        **kwargs: Any,
    ) -> ParsingJob:
        """Create a parsing job and wait for it to complete."""
        job = self.create(
            file_id=file_id,
            chunking_strategy=chunking_strategy,
            element_types=element_types,
            return_format=return_format,
            **kwargs,
        )
        return self.poll(job.id, poll_interval_ms=poll_interval_ms, poll_timeout_ms=poll_timeout_ms, **kwargs)

    def upload(
        self,
        *,
        file: FileTypes,
        chunking_strategy: ChunkingStrategy | Omit = omit,
        element_types: Optional[List[ElementType]] | Omit = omit,
        return_format: ReturnFormat | Omit = omit,
        multipart_upload: bool | MultipartUploadOptions | None = None,
        **kwargs: Any,
    ) -> ParsingJob:
        """Upload a file to the ``files`` API and create a parsing job for it.

        The job is processed asynchronously; use ``upload_and_poll`` to wait for it.
        """
        file_obj = self._client.files.create(file=file, multipart_upload=multipart_upload, **kwargs)
        return self.create(
            file_id=file_obj.id,
            chunking_strategy=chunking_strategy,
            element_types=element_types,
            return_format=return_format,
            **kwargs,
        )

    def upload_and_poll(
        self,
        *,
        file: FileTypes,
        chunking_strategy: ChunkingStrategy | Omit = omit,
        element_types: Optional[List[ElementType]] | Omit = omit,
        return_format: ReturnFormat | Omit = omit,
        multipart_upload: bool | MultipartUploadOptions | None = None,
        poll_interval_ms: int | NotGiven = not_given,
        poll_timeout_ms: float | NotGiven = not_given,
        **kwargs: Any,
    ) -> ParsingJob:
        """Upload a file, create a parsing job and poll until processing is complete."""
        file_obj = self._client.files.create(file=file, multipart_upload=multipart_upload, **kwargs)
        return self.create_and_poll(
            file_id=file_obj.id,
            chunking_strategy=chunking_strategy,
            element_types=element_types,
            return_format=return_format,
            poll_interval_ms=poll_interval_ms,
            poll_timeout_ms=poll_timeout_ms,
            **kwargs,
        )


class AsyncParsingJobHelpers(_AsyncBase):
    async def poll(
        self,
        job_id: str,
        *,
        poll_interval_ms: int | NotGiven = not_given,
        poll_timeout_ms: float | NotGiven = not_given,
        **kwargs: Any,
    ) -> ParsingJob:
        """Poll a job's status until it reaches a terminal state."""
        polling_interval_ms = poll_interval_ms or 500
        polling_timeout_ms = poll_timeout_ms or None
        return await polling.poll_async(
            fn=functools.partial(self.retrieve, job_id, **kwargs),
            condition=lambda res: res.status in _TERMINAL,
            interval_seconds=polling_interval_ms / 1000,
            timeout_seconds=polling_timeout_ms / 1000 if polling_timeout_ms else None,
        )

    async def create_and_poll(
        self,
        *,
        file_id: str,
        chunking_strategy: ChunkingStrategy | Omit = omit,
        element_types: Optional[List[ElementType]] | Omit = omit,
        return_format: ReturnFormat | Omit = omit,
        poll_interval_ms: int | NotGiven = not_given,
        poll_timeout_ms: float | NotGiven = not_given,
        **kwargs: Any,
    ) -> ParsingJob:
        """Create a parsing job and wait for it to complete."""
        job = await self.create(
            file_id=file_id,
            chunking_strategy=chunking_strategy,
            element_types=element_types,
            return_format=return_format,
            **kwargs,
        )
        return await self.poll(job.id, poll_interval_ms=poll_interval_ms, poll_timeout_ms=poll_timeout_ms, **kwargs)

    async def upload(
        self,
        *,
        file: FileTypes,
        chunking_strategy: ChunkingStrategy | Omit = omit,
        element_types: Optional[List[ElementType]] | Omit = omit,
        return_format: ReturnFormat | Omit = omit,
        multipart_upload: bool | MultipartUploadOptions | None = None,
        **kwargs: Any,
    ) -> ParsingJob:
        """Upload a file to the ``files`` API and create a parsing job for it."""
        file_obj = await self._client.files.create(file=file, multipart_upload=multipart_upload, **kwargs)
        return await self.create(
            file_id=file_obj.id,
            chunking_strategy=chunking_strategy,
            element_types=element_types,
            return_format=return_format,
            **kwargs,
        )

    async def upload_and_poll(
        self,
        *,
        file: FileTypes,
        chunking_strategy: ChunkingStrategy | Omit = omit,
        element_types: Optional[List[ElementType]] | Omit = omit,
        return_format: ReturnFormat | Omit = omit,
        multipart_upload: bool | MultipartUploadOptions | None = None,
        poll_interval_ms: int | NotGiven = not_given,
        poll_timeout_ms: float | NotGiven = not_given,
        **kwargs: Any,
    ) -> ParsingJob:
        """Upload a file, create a parsing job and poll until processing is complete."""
        file_obj = await self._client.files.create(file=file, multipart_upload=multipart_upload, **kwargs)
        return await self.create_and_poll(
            file_id=file_obj.id,
            chunking_strategy=chunking_strategy,
            element_types=element_types,
            return_format=return_format,
            poll_interval_ms=poll_interval_ms,
            poll_timeout_ms=poll_timeout_ms,
            **kwargs,
        )
