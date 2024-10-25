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

__all__ = ["ServiceStatusResource", "AsyncServiceStatusResource"]


class ServiceStatusResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServiceStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return ServiceStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServiceStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#with_streaming_response
        """
        return ServiceStatusResourceWithStreamingResponse(self)

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
            cast_to=InfoResponse,
        )


class AsyncServiceStatusResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServiceStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return AsyncServiceStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServiceStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#with_streaming_response
        """
        return AsyncServiceStatusResourceWithStreamingResponse(self)

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
            cast_to=InfoResponse,
        )


class ServiceStatusResourceWithRawResponse:
    def __init__(self, service_status: ServiceStatusResource) -> None:
        self._service_status = service_status

        self.retrieve = to_raw_response_wrapper(
            service_status.retrieve,
        )


class AsyncServiceStatusResourceWithRawResponse:
    def __init__(self, service_status: AsyncServiceStatusResource) -> None:
        self._service_status = service_status

        self.retrieve = async_to_raw_response_wrapper(
            service_status.retrieve,
        )


class ServiceStatusResourceWithStreamingResponse:
    def __init__(self, service_status: ServiceStatusResource) -> None:
        self._service_status = service_status

        self.retrieve = to_streamed_response_wrapper(
            service_status.retrieve,
        )


class AsyncServiceStatusResourceWithStreamingResponse:
    def __init__(self, service_status: AsyncServiceStatusResource) -> None:
        self._service_status = service_status

        self.retrieve = async_to_streamed_response_wrapper(
            service_status.retrieve,
        )
