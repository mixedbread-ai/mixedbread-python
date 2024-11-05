# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.base_status_response import BaseStatusResponse

__all__ = ["BaseResource", "AsyncBaseResource"]


class BaseResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BaseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return BaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BaseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#with_streaming_response
        """
        return BaseResourceWithStreamingResponse(self)

    def status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BaseStatusResponse:
        """
        Perform a base search to check the service status and configuration.

        Args: state: The application state.

        Returns: dict: A dictionary containing the service status and public
        configuration details.
        """
        return self._get(
            "/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BaseStatusResponse,
        )


class AsyncBaseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBaseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBaseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#with_streaming_response
        """
        return AsyncBaseResourceWithStreamingResponse(self)

    async def status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BaseStatusResponse:
        """
        Perform a base search to check the service status and configuration.

        Args: state: The application state.

        Returns: dict: A dictionary containing the service status and public
        configuration details.
        """
        return await self._get(
            "/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BaseStatusResponse,
        )


class BaseResourceWithRawResponse:
    def __init__(self, base: BaseResource) -> None:
        self._base = base

        self.status = to_raw_response_wrapper(
            base.status,
        )


class AsyncBaseResourceWithRawResponse:
    def __init__(self, base: AsyncBaseResource) -> None:
        self._base = base

        self.status = async_to_raw_response_wrapper(
            base.status,
        )


class BaseResourceWithStreamingResponse:
    def __init__(self, base: BaseResource) -> None:
        self._base = base

        self.status = to_streamed_response_wrapper(
            base.status,
        )


class AsyncBaseResourceWithStreamingResponse:
    def __init__(self, base: AsyncBaseResource) -> None:
        self._base = base

        self.status = async_to_streamed_response_wrapper(
            base.status,
        )
