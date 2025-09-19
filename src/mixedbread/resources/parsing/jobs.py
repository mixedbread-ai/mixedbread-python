# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import functools
from typing import Any, List, Optional
from typing_extensions import Literal

import httpx

from ...lib import polling
from ..._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursor, AsyncCursor
from ..._base_client import AsyncPaginator, make_request_options
from ...types.parsing import ReturnFormat, ChunkingStrategy, job_list_params, job_create_params
from ...types.parsing.parsing_job import ParsingJob
from ...types.parsing.element_type import ElementType
from ...types.parsing.return_format import ReturnFormat
from ...types.parsing.chunking_strategy import ChunkingStrategy
from ...types.parsing.job_list_response import JobListResponse
from ...types.parsing.parsing_job_status import ParsingJobStatus
from ...types.parsing.job_delete_response import JobDeleteResponse

__all__ = ["JobsResource", "AsyncJobsResource"]


class JobsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return JobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return JobsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        file_id: str,
        element_types: Optional[List[ElementType]] | Omit = omit,
        chunking_strategy: ChunkingStrategy | Omit = omit,
        return_format: ReturnFormat | Omit = omit,
        mode: Literal["fast", "high_quality"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingJob:
        """
        Start a parse job for the provided file.

        Args: params: The parameters for creating a parse job.

        Returns: The created parsing job.

        Args:
          file_id: The ID of the file to parse

          element_types: The elements to extract from the document

          chunking_strategy: The strategy to use for chunking the content

          return_format: The format of the returned content

          mode: The strategy to use for OCR

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/parsing/jobs",
            body=maybe_transform(
                {
                    "file_id": file_id,
                    "element_types": element_types,
                    "chunking_strategy": chunking_strategy,
                    "return_format": return_format,
                    "mode": mode,
                },
                job_create_params.JobCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParsingJob,
        )

    def retrieve(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingJob:
        """
        Get detailed information about a specific parse job.

        Args: job_id: The ID of the parse job.

        Returns: Detailed information about the parse job.

        Args:
          job_id: The ID of the parse job to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/v1/parsing/jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParsingJob,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        include_total: bool | Omit = omit,
        statuses: Optional[List[ParsingJobStatus]] | Omit = omit,
        q: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[JobListResponse]:
        """List parsing jobs with pagination.

        Args: limit: The number of items to return.

        offset: The number of items to skip.

        Returns: List of parsing jobs with pagination.

        Args:
          limit: Maximum number of items to return per page (1-100)

          after: Cursor for forward pagination - get items after this position. Use last_cursor
              from previous response.

          before: Cursor for backward pagination - get items before this position. Use
              first_cursor from previous response.

          include_total: Whether to include total count in response (expensive operation)

          statuses: Status to filter by

          q: Search query to filter by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/parsing/jobs",
            page=SyncCursor[JobListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "after": after,
                        "before": before,
                        "include_total": include_total,
                        "statuses": statuses,
                        "q": q,
                    },
                    job_list_params.JobListParams,
                ),
            ),
            model=JobListResponse,
        )

    def delete(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobDeleteResponse:
        """
        Delete a specific parse job.

        Args: job_id: The ID of the parse job to delete.

        Returns: The deleted parsing job.

        Args:
          job_id: The ID of the parse job to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._delete(
            f"/v1/parsing/jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobDeleteResponse,
        )

    def cancel(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingJob:
        """
        Cancel a specific parse job.

        Args: job_id: The ID of the parse job to cancel.

        Returns: The cancelled parsing job.

        Args:
          job_id: The ID of the parse job to cancel

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._patch(
            f"/v1/parsing/jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParsingJob,
        )

    def poll(
        self,
        job_id: str,
        *,
        poll_interval_ms: int | NotGiven = NOT_GIVEN,
        poll_timeout_ms: float | NotGiven = NOT_GIVEN,
        **kwargs: Any,
    ) -> ParsingJob:
        """
        Poll for a job's status until it reaches a terminal state.
        Args:
            job_id: The ID of the job to poll
            poll_interval_ms: The interval between polls in milliseconds
            poll_timeout_ms: The maximum time to poll for in milliseconds
        Returns:
            The job object once it reaches a terminal state
        """
        polling_interval_ms = poll_interval_ms or 500
        polling_timeout_ms = poll_timeout_ms or None
        return polling.poll(
            fn=functools.partial(self.retrieve, job_id, **kwargs),
            condition=lambda res: res.status == "completed" or res.status == "failed" or res.status == "cancelled",
            interval_seconds=polling_interval_ms / 1000,
            timeout_seconds=polling_timeout_ms / 1000 if polling_timeout_ms else None,
        )

    def create_and_poll(
        self,
        *,
        file_id: str,
        chunking_strategy: Literal["page"] | NotGiven = NOT_GIVEN,
        element_types: Optional[
            List[
                Literal[
                    "caption",
                    "footnote",
                    "formula",
                    "list-item",
                    "page-footer",
                    "page-header",
                    "picture",
                    "section-header",
                    "table",
                    "text",
                    "title",
                ]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        return_format: Literal["html", "markdown", "plain"] | NotGiven = NOT_GIVEN,
        poll_interval_ms: int | NotGiven = NOT_GIVEN,
        poll_timeout_ms: float | NotGiven = NOT_GIVEN,
        **kwargs: Any,
    ) -> ParsingJob:
        """
        Create a parsing job and wait for it to complete.
        Args:
            file_id: The ID of the file to parse
            chunking_strategy: The strategy to use for chunking the content
            element_types: The elements to extract from the document
            return_format: The format of the returned content
            poll_interval_ms: The interval between polls in milliseconds
            poll_timeout_ms: The maximum time to poll for in milliseconds
        Returns:
            The job object once it reaches a terminal state
        """
        job = self.create(
            file_id=file_id,
            chunking_strategy=chunking_strategy,
            element_types=element_types,
            return_format=return_format,
            **kwargs,
        )
        return self.poll(
            job.id,
            poll_interval_ms=poll_interval_ms,
            poll_timeout_ms=poll_timeout_ms,
            **kwargs,
        )

    def upload(
        self,
        *,
        file: FileTypes,
        chunking_strategy: Literal["page"] | NotGiven = NOT_GIVEN,
        element_types: Optional[
            List[
                Literal[
                    "caption",
                    "footnote",
                    "formula",
                    "list-item",
                    "page-footer",
                    "page-header",
                    "picture",
                    "section-header",
                    "table",
                    "text",
                    "title",
                ]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        return_format: Literal["html", "markdown", "plain"] | NotGiven = NOT_GIVEN,
        **kwargs: Any,
    ) -> ParsingJob:
        """Upload a file to the `files` API and then create a parsing job for it.
        Note the job will be asynchronously processed (you can use the alternative
        polling helper method to wait for processing to complete).
        """
        file_obj = self._client.files.create(file=file, **kwargs)
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
        chunking_strategy: Literal["page"] | NotGiven = NOT_GIVEN,
        element_types: Optional[
            List[
                Literal[
                    "caption",
                    "footnote",
                    "formula",
                    "list-item",
                    "page-footer",
                    "page-header",
                    "picture",
                    "section-header",
                    "table",
                    "text",
                    "title",
                ]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        return_format: Literal["html", "markdown", "plain"] | NotGiven = NOT_GIVEN,
        poll_interval_ms: int | NotGiven = NOT_GIVEN,
        **kwargs: Any,
    ) -> ParsingJob:
        """Upload a file and create a parsing job, then poll until processing is complete."""
        file_obj = self._client.files.create(file=file, **kwargs)
        return self.create_and_poll(
            file_id=file_obj.id,
            chunking_strategy=chunking_strategy,
            element_types=element_types,
            return_format=return_format,
            poll_interval_ms=poll_interval_ms,
            **kwargs,
        )


class AsyncJobsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return AsyncJobsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        file_id: str,
        element_types: Optional[List[ElementType]] | Omit = omit,
        chunking_strategy: ChunkingStrategy | Omit = omit,
        return_format: ReturnFormat | Omit = omit,
        mode: Literal["fast", "high_quality"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingJob:
        """
        Start a parse job for the provided file.

        Args: params: The parameters for creating a parse job.

        Returns: The created parsing job.

        Args:
          file_id: The ID of the file to parse

          element_types: The elements to extract from the document

          chunking_strategy: The strategy to use for chunking the content

          return_format: The format of the returned content

          mode: The strategy to use for OCR

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/parsing/jobs",
            body=await async_maybe_transform(
                {
                    "file_id": file_id,
                    "element_types": element_types,
                    "chunking_strategy": chunking_strategy,
                    "return_format": return_format,
                    "mode": mode,
                },
                job_create_params.JobCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParsingJob,
        )

    async def retrieve(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingJob:
        """
        Get detailed information about a specific parse job.

        Args: job_id: The ID of the parse job.

        Returns: Detailed information about the parse job.

        Args:
          job_id: The ID of the parse job to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/v1/parsing/jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParsingJob,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        include_total: bool | Omit = omit,
        statuses: Optional[List[ParsingJobStatus]] | Omit = omit,
        q: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[JobListResponse, AsyncCursor[JobListResponse]]:
        """List parsing jobs with pagination.

        Args: limit: The number of items to return.

        offset: The number of items to skip.

        Returns: List of parsing jobs with pagination.

        Args:
          limit: Maximum number of items to return per page (1-100)

          after: Cursor for forward pagination - get items after this position. Use last_cursor
              from previous response.

          before: Cursor for backward pagination - get items before this position. Use
              first_cursor from previous response.

          include_total: Whether to include total count in response (expensive operation)

          statuses: Status to filter by

          q: Search query to filter by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/parsing/jobs",
            page=AsyncCursor[JobListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "after": after,
                        "before": before,
                        "include_total": include_total,
                        "statuses": statuses,
                        "q": q,
                    },
                    job_list_params.JobListParams,
                ),
            ),
            model=JobListResponse,
        )

    async def delete(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobDeleteResponse:
        """
        Delete a specific parse job.

        Args: job_id: The ID of the parse job to delete.

        Returns: The deleted parsing job.

        Args:
          job_id: The ID of the parse job to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._delete(
            f"/v1/parsing/jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JobDeleteResponse,
        )

    async def cancel(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingJob:
        """
        Cancel a specific parse job.

        Args: job_id: The ID of the parse job to cancel.

        Returns: The cancelled parsing job.

        Args:
          job_id: The ID of the parse job to cancel

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._patch(
            f"/v1/parsing/jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParsingJob,
        )

    async def poll(
        self,
        job_id: str,
        *,
        poll_interval_ms: int | NotGiven = NOT_GIVEN,
        poll_timeout_ms: float | NotGiven = NOT_GIVEN,
        **kwargs: Any,
    ) -> ParsingJob:
        """
        Poll for a job's status until it reaches a terminal state.
        Args:
            job_id: The ID of the job to poll
            poll_interval_ms: The interval between polls in milliseconds
            poll_timeout_ms: The maximum time to poll for in milliseconds
        Returns:
            The job object once it reaches a terminal state
        """
        polling_interval_ms = poll_interval_ms or 500
        polling_timeout_ms = poll_timeout_ms or None
        return await polling.poll_async(
            fn=functools.partial(self.retrieve, job_id, **kwargs),
            condition=lambda res: res.status == "completed" or res.status == "failed" or res.status == "cancelled",
            interval_seconds=polling_interval_ms / 1000,
            timeout_seconds=polling_timeout_ms / 1000 if polling_timeout_ms else None,
        )

    async def create_and_poll(
        self,
        *,
        file_id: str,
        chunking_strategy: Literal["page"] | NotGiven = NOT_GIVEN,
        element_types: Optional[
            List[
                Literal[
                    "caption",
                    "footnote",
                    "formula",
                    "list-item",
                    "page-footer",
                    "page-header",
                    "picture",
                    "section-header",
                    "table",
                    "text",
                    "title",
                ]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        return_format: Literal["html", "markdown", "plain"] | NotGiven = NOT_GIVEN,
        poll_interval_ms: int | NotGiven = NOT_GIVEN,
        poll_timeout_ms: float | NotGiven = NOT_GIVEN,
        **kwargs: Any,
    ) -> ParsingJob:
        """
        Create a parsing job and wait for it to complete.
        Args:
            file_id: The ID of the file to parse
            chunking_strategy: The strategy to use for chunking the content
            element_types: The elements to extract from the document
            return_format: The format of the returned content
            poll_interval_ms: The interval between polls in milliseconds
            poll_timeout_ms: The maximum time to poll for in milliseconds
        Returns:
            The job object once it reaches a terminal state
        """
        job = await self.create(
            file_id=file_id,
            chunking_strategy=chunking_strategy,
            element_types=element_types,
            return_format=return_format,
            **kwargs,
        )
        return await self.poll(
            job.id,
            poll_interval_ms=poll_interval_ms,
            poll_timeout_ms=poll_timeout_ms,
            **kwargs,
        )

    async def upload(
        self,
        *,
        file: FileTypes,
        chunking_strategy: Literal["page"] | NotGiven = NOT_GIVEN,
        element_types: Optional[
            List[
                Literal[
                    "caption",
                    "footnote",
                    "formula",
                    "list-item",
                    "page-footer",
                    "page-header",
                    "picture",
                    "section-header",
                    "table",
                    "text",
                    "title",
                ]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        return_format: Literal["html", "markdown", "plain"] | NotGiven = NOT_GIVEN,
        **kwargs: Any,
    ) -> ParsingJob:
        """Upload a file to the `files` API and then create a parsing job for it.
        Note the job will be asynchronously processed (you can use the alternative
        polling helper method to wait for processing to complete).
        """
        file_obj = await self._client.files.create(file=file, **kwargs)
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
        chunking_strategy: Literal["page"] | NotGiven = NOT_GIVEN,
        element_types: Optional[
            List[
                Literal[
                    "caption",
                    "footnote",
                    "formula",
                    "list-item",
                    "page-footer",
                    "page-header",
                    "picture",
                    "section-header",
                    "table",
                    "text",
                    "title",
                ]
            ]
        ]
        | NotGiven = NOT_GIVEN,
        return_format: Literal["html", "markdown", "plain"] | NotGiven = NOT_GIVEN,
        poll_interval_ms: int | NotGiven = NOT_GIVEN,
        **kwargs: Any,
    ) -> ParsingJob:
        """Upload a file and create a parsing job, then poll until processing is complete."""
        file_obj = await self._client.files.create(file=file, **kwargs)
        return await self.create_and_poll(
            file_id=file_obj.id,
            chunking_strategy=chunking_strategy,
            element_types=element_types,
            return_format=return_format,
            poll_interval_ms=poll_interval_ms,
            **kwargs,
        )


class JobsResourceWithRawResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.create = to_raw_response_wrapper(
            jobs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            jobs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            jobs.list,
        )
        self.delete = to_raw_response_wrapper(
            jobs.delete,
        )
        self.cancel = to_raw_response_wrapper(
            jobs.cancel,
        )


class AsyncJobsResourceWithRawResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.create = async_to_raw_response_wrapper(
            jobs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            jobs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            jobs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            jobs.delete,
        )
        self.cancel = async_to_raw_response_wrapper(
            jobs.cancel,
        )


class JobsResourceWithStreamingResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.create = to_streamed_response_wrapper(
            jobs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            jobs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            jobs.list,
        )
        self.delete = to_streamed_response_wrapper(
            jobs.delete,
        )
        self.cancel = to_streamed_response_wrapper(
            jobs.cancel,
        )


class AsyncJobsResourceWithStreamingResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.create = async_to_streamed_response_wrapper(
            jobs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            jobs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            jobs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            jobs.delete,
        )
        self.cancel = async_to_streamed_response_wrapper(
            jobs.cancel,
        )
