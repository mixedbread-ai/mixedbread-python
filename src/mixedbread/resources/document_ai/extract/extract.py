# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

import httpx

from .schema import (
    SchemaResource,
    AsyncSchemaResource,
    SchemaResourceWithRawResponse,
    AsyncSchemaResourceWithRawResponse,
    SchemaResourceWithStreamingResponse,
    AsyncSchemaResourceWithStreamingResponse,
)
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
from ....types.document_ai import extract_content_params, extract_create_job_params
from ....types.document_ai.result import Result
from ....types.document_ai.extract_create_job_response import ExtractCreateJobResponse
from ....types.document_ai.extract_retrieve_job_response import ExtractRetrieveJobResponse

__all__ = ["ExtractResource", "AsyncExtractResource"]


class ExtractResource(SyncAPIResource):
    @cached_property
    def schema(self) -> SchemaResource:
        return SchemaResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExtractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return ExtractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return ExtractResourceWithStreamingResponse(self)

    def content(
        self,
        *,
        content: str,
        json_schema: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Result:
        """
        Extract content from a string using the provided schema.

        Args: params: ExtractContentCreateParams The parameters for extracting content
        from a string.

        Returns: ExtractionResult: The extracted content.

        Args:
          content: The text content to extract structured data from

          json_schema: The schema definition to use for extraction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/document-ai/extract/content",
            body=maybe_transform(
                {
                    "content": content,
                    "json_schema": json_schema,
                },
                extract_content_params.ExtractContentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Result,
        )

    def create_job(
        self,
        *,
        file_id: str,
        json_schema: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtractCreateJobResponse:
        """
        Start an extraction job for the provided file and schema.

        Args: params: ExtractJobCreateParams The parameters for creating an extraction
        job.

        Returns: ExtractionJob: The created extraction job.

        Args:
          file_id: The file ID to extract data from

          json_schema: The schema definition to use for extraction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            ExtractCreateJobResponse,
            self._post(
                "/v1/document-ai/extract",
                body=maybe_transform(
                    {
                        "file_id": file_id,
                        "json_schema": json_schema,
                    },
                    extract_create_job_params.ExtractCreateJobParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ExtractCreateJobResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def retrieve_job(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtractRetrieveJobResponse:
        """
        Get detailed information about a specific extraction job.

        Args: job_id: The ID of the extraction job.

        Returns: ExtractionJob: Detailed information about the extraction job.

        Args:
          job_id: The ID of the extraction job to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return cast(
            ExtractRetrieveJobResponse,
            self._get(
                f"/v1/document-ai/extract/{job_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ExtractRetrieveJobResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncExtractResource(AsyncAPIResource):
    @cached_property
    def schema(self) -> AsyncSchemaResource:
        return AsyncSchemaResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExtractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExtractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return AsyncExtractResourceWithStreamingResponse(self)

    async def content(
        self,
        *,
        content: str,
        json_schema: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Result:
        """
        Extract content from a string using the provided schema.

        Args: params: ExtractContentCreateParams The parameters for extracting content
        from a string.

        Returns: ExtractionResult: The extracted content.

        Args:
          content: The text content to extract structured data from

          json_schema: The schema definition to use for extraction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/document-ai/extract/content",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "json_schema": json_schema,
                },
                extract_content_params.ExtractContentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Result,
        )

    async def create_job(
        self,
        *,
        file_id: str,
        json_schema: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtractCreateJobResponse:
        """
        Start an extraction job for the provided file and schema.

        Args: params: ExtractJobCreateParams The parameters for creating an extraction
        job.

        Returns: ExtractionJob: The created extraction job.

        Args:
          file_id: The file ID to extract data from

          json_schema: The schema definition to use for extraction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            ExtractCreateJobResponse,
            await self._post(
                "/v1/document-ai/extract",
                body=await async_maybe_transform(
                    {
                        "file_id": file_id,
                        "json_schema": json_schema,
                    },
                    extract_create_job_params.ExtractCreateJobParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ExtractCreateJobResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def retrieve_job(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtractRetrieveJobResponse:
        """
        Get detailed information about a specific extraction job.

        Args: job_id: The ID of the extraction job.

        Returns: ExtractionJob: Detailed information about the extraction job.

        Args:
          job_id: The ID of the extraction job to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return cast(
            ExtractRetrieveJobResponse,
            await self._get(
                f"/v1/document-ai/extract/{job_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ExtractRetrieveJobResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ExtractResourceWithRawResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

        self.content = to_raw_response_wrapper(
            extract.content,
        )
        self.create_job = to_raw_response_wrapper(
            extract.create_job,
        )
        self.retrieve_job = to_raw_response_wrapper(
            extract.retrieve_job,
        )

    @cached_property
    def schema(self) -> SchemaResourceWithRawResponse:
        return SchemaResourceWithRawResponse(self._extract.schema)


class AsyncExtractResourceWithRawResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

        self.content = async_to_raw_response_wrapper(
            extract.content,
        )
        self.create_job = async_to_raw_response_wrapper(
            extract.create_job,
        )
        self.retrieve_job = async_to_raw_response_wrapper(
            extract.retrieve_job,
        )

    @cached_property
    def schema(self) -> AsyncSchemaResourceWithRawResponse:
        return AsyncSchemaResourceWithRawResponse(self._extract.schema)


class ExtractResourceWithStreamingResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

        self.content = to_streamed_response_wrapper(
            extract.content,
        )
        self.create_job = to_streamed_response_wrapper(
            extract.create_job,
        )
        self.retrieve_job = to_streamed_response_wrapper(
            extract.retrieve_job,
        )

    @cached_property
    def schema(self) -> SchemaResourceWithStreamingResponse:
        return SchemaResourceWithStreamingResponse(self._extract.schema)


class AsyncExtractResourceWithStreamingResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

        self.content = async_to_streamed_response_wrapper(
            extract.content,
        )
        self.create_job = async_to_streamed_response_wrapper(
            extract.create_job,
        )
        self.retrieve_job = async_to_streamed_response_wrapper(
            extract.retrieve_job,
        )

    @cached_property
    def schema(self) -> AsyncSchemaResourceWithStreamingResponse:
        return AsyncSchemaResourceWithStreamingResponse(self._extract.schema)
