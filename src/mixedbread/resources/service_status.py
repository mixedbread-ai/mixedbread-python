# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional

import httpx

from ..types import service_status_rerank_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ..types.service_status_rerank_response import ServiceStatusRerankResponse

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

    def rerank(
        self,
        *,
        input: Union[List[str], Iterable[object]],
        query: service_status_rerank_params.Query,
        model: str | NotGiven = NOT_GIVEN,
        rank_fields: Optional[List[str]] | NotGiven = NOT_GIVEN,
        return_input: bool | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceStatusRerankResponse:
        """
        Rerank different kind of documents for a given query

        Args:
          input: The text input documents to rerank.

          query: The query to rerank the documents.

          model: The model to use for reranking documents.

          rank_fields: The fields of the documents to rank.

          return_input: Whether to return the documents.

          top_k: The number of documents to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/v1/reranking",
            body=maybe_transform(
                {
                    "input": input,
                    "query": query,
                    "model": model,
                    "rank_fields": rank_fields,
                    "return_input": return_input,
                    "top_k": top_k,
                },
                service_status_rerank_params.ServiceStatusRerankParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceStatusRerankResponse,
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

    async def rerank(
        self,
        *,
        input: Union[List[str], Iterable[object]],
        query: service_status_rerank_params.Query,
        model: str | NotGiven = NOT_GIVEN,
        rank_fields: Optional[List[str]] | NotGiven = NOT_GIVEN,
        return_input: bool | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceStatusRerankResponse:
        """
        Rerank different kind of documents for a given query

        Args:
          input: The text input documents to rerank.

          query: The query to rerank the documents.

          model: The model to use for reranking documents.

          rank_fields: The fields of the documents to rank.

          return_input: Whether to return the documents.

          top_k: The number of documents to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/v1/reranking",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "query": query,
                    "model": model,
                    "rank_fields": rank_fields,
                    "return_input": return_input,
                    "top_k": top_k,
                },
                service_status_rerank_params.ServiceStatusRerankParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceStatusRerankResponse,
        )


class ServiceStatusResourceWithRawResponse:
    def __init__(self, service_status: ServiceStatusResource) -> None:
        self._service_status = service_status

        self.retrieve = to_raw_response_wrapper(
            service_status.retrieve,
        )
        self.rerank = to_raw_response_wrapper(
            service_status.rerank,
        )


class AsyncServiceStatusResourceWithRawResponse:
    def __init__(self, service_status: AsyncServiceStatusResource) -> None:
        self._service_status = service_status

        self.retrieve = async_to_raw_response_wrapper(
            service_status.retrieve,
        )
        self.rerank = async_to_raw_response_wrapper(
            service_status.rerank,
        )


class ServiceStatusResourceWithStreamingResponse:
    def __init__(self, service_status: ServiceStatusResource) -> None:
        self._service_status = service_status

        self.retrieve = to_streamed_response_wrapper(
            service_status.retrieve,
        )
        self.rerank = to_streamed_response_wrapper(
            service_status.rerank,
        )


class AsyncServiceStatusResourceWithStreamingResponse:
    def __init__(self, service_status: AsyncServiceStatusResource) -> None:
        self._service_status = service_status

        self.retrieve = async_to_streamed_response_wrapper(
            service_status.retrieve,
        )
        self.rerank = async_to_streamed_response_wrapper(
            service_status.rerank,
        )
