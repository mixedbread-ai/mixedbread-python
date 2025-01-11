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
from ..types.info_response import InfoResponse

__all__ = ["ServiceInfoResource", "AsyncServiceInfoResource"]


class ServiceInfoResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServiceInfoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return ServiceInfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServiceInfoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#with_streaming_response
        """
        return ServiceInfoResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InfoResponse:
        """
        Returns service information, including name and version.

        Returns: InfoResponse: A response containing the service name and version.
        """
        return self._get(
            "/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InfoResponse,
        )


class AsyncServiceInfoResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServiceInfoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return AsyncServiceInfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServiceInfoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#with_streaming_response
        """
        return AsyncServiceInfoResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InfoResponse:
        """
        Returns service information, including name and version.

        Returns: InfoResponse: A response containing the service name and version.
        """
        return await self._get(
            "/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InfoResponse,
        )


class ServiceInfoResourceWithRawResponse:
    def __init__(self, service_info: ServiceInfoResource) -> None:
        self._service_info = service_info

        self.retrieve = to_raw_response_wrapper(
            service_info.retrieve,
        )


class AsyncServiceInfoResourceWithRawResponse:
    def __init__(self, service_info: AsyncServiceInfoResource) -> None:
        self._service_info = service_info

        self.retrieve = async_to_raw_response_wrapper(
            service_info.retrieve,
        )


class ServiceInfoResourceWithStreamingResponse:
    def __init__(self, service_info: ServiceInfoResource) -> None:
        self._service_info = service_info

        self.retrieve = to_streamed_response_wrapper(
            service_info.retrieve,
        )


class AsyncServiceInfoResourceWithStreamingResponse:
    def __init__(self, service_info: AsyncServiceInfoResource) -> None:
        self._service_info = service_info

        self.retrieve = async_to_streamed_response_wrapper(
            service_info.retrieve,
        )
