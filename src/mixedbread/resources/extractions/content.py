# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.extractions import content_create_params
from ...types.extractions.extraction_result import ExtractionResult

__all__ = ["ContentResource", "AsyncContentResource"]


class ContentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return ContentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#with_streaming_response
        """
        return ContentResourceWithStreamingResponse(self)

    def create(
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
    ) -> ExtractionResult:
        """
        Extract content from a string using the provided schema.

        Args: params: The parameters for extracting content from a string.

        Returns: The extracted content.

        Args:
          content: The content to extract from

          json_schema: The JSON schema to use for extraction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/extractions/content",
            body=maybe_transform(
                {
                    "content": content,
                    "json_schema": json_schema,
                },
                content_create_params.ContentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractionResult,
        )


class AsyncContentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#with_streaming_response
        """
        return AsyncContentResourceWithStreamingResponse(self)

    async def create(
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
    ) -> ExtractionResult:
        """
        Extract content from a string using the provided schema.

        Args: params: The parameters for extracting content from a string.

        Returns: The extracted content.

        Args:
          content: The content to extract from

          json_schema: The JSON schema to use for extraction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/extractions/content",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "json_schema": json_schema,
                },
                content_create_params.ContentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractionResult,
        )


class ContentResourceWithRawResponse:
    def __init__(self, content: ContentResource) -> None:
        self._content = content

        self.create = to_raw_response_wrapper(
            content.create,
        )


class AsyncContentResourceWithRawResponse:
    def __init__(self, content: AsyncContentResource) -> None:
        self._content = content

        self.create = async_to_raw_response_wrapper(
            content.create,
        )


class ContentResourceWithStreamingResponse:
    def __init__(self, content: ContentResource) -> None:
        self._content = content

        self.create = to_streamed_response_wrapper(
            content.create,
        )


class AsyncContentResourceWithStreamingResponse:
    def __init__(self, content: AsyncContentResource) -> None:
        self._content = content

        self.create = async_to_streamed_response_wrapper(
            content.create,
        )
