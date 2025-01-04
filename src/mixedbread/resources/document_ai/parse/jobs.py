# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.document_ai.parse import job_create_params
from ....types.document_ai.parse.job_create_response import JobCreateResponse
from ....types.document_ai.parse.job_retrieve_response import JobRetrieveResponse

__all__ = ["JobsResource", "AsyncJobsResource"]


class JobsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobCreateResponse:
        """
        Start a parse job for the provided file.

        Args: params: ParseJobCreateParams The parameters for creating a parse job.

        Returns: ParsingJob: The created parse job.

        Args:
          file_id: The ID of the file to parse

          chunking_strategy: The strategy to use for chunking the content

          element_types: The elements to extract from the document

          return_format: The format of the returned content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            JobCreateResponse,
            self._post(
                "/v1/document-ai/parse",
                body=maybe_transform(
                    {
                        "file_id": file_id,
                        "chunking_strategy": chunking_strategy,
                        "element_types": element_types,
                        "return_format": return_format,
                    },
                    job_create_params.JobCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, JobCreateResponse),  # Union types cannot be passed in as arguments in the type system
            ),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobRetrieveResponse:
        """
        Get detailed information about a specific parse job.

        Args: job_id: The ID of the parse job.

        Returns: ParsingJob: Detailed information about the parse job.

        Args:
          job_id: The ID of the parse job to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return cast(
            JobRetrieveResponse,
            self._get(
                f"/v1/document-ai/parse/{job_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, JobRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncJobsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobCreateResponse:
        """
        Start a parse job for the provided file.

        Args: params: ParseJobCreateParams The parameters for creating a parse job.

        Returns: ParsingJob: The created parse job.

        Args:
          file_id: The ID of the file to parse

          chunking_strategy: The strategy to use for chunking the content

          element_types: The elements to extract from the document

          return_format: The format of the returned content

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            JobCreateResponse,
            await self._post(
                "/v1/document-ai/parse",
                body=await async_maybe_transform(
                    {
                        "file_id": file_id,
                        "chunking_strategy": chunking_strategy,
                        "element_types": element_types,
                        "return_format": return_format,
                    },
                    job_create_params.JobCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, JobCreateResponse),  # Union types cannot be passed in as arguments in the type system
            ),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobRetrieveResponse:
        """
        Get detailed information about a specific parse job.

        Args: job_id: The ID of the parse job.

        Returns: ParsingJob: Detailed information about the parse job.

        Args:
          job_id: The ID of the parse job to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return cast(
            JobRetrieveResponse,
            await self._get(
                f"/v1/document-ai/parse/{job_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, JobRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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


class AsyncJobsResourceWithRawResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.create = async_to_raw_response_wrapper(
            jobs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            jobs.retrieve,
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


class AsyncJobsResourceWithStreamingResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.create = async_to_streamed_response_wrapper(
            jobs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            jobs.retrieve,
        )
