# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

import httpx

from ..types import reranking_create_params
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
from ..types.reranking_create_response import RerankingCreateResponse

__all__ = ["RerankingsResource", "AsyncRerankingsResource"]


class RerankingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RerankingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return RerankingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RerankingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return RerankingsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        input: object,
        query: str,
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
    ) -> RerankingCreateResponse:
        """
        Rerank different kind of documents for a given query.

        Args: params: RerankingCreateParams: The parameters for reranking.

        Returns: RerankingCreateResponse: The reranked documents for the input query.

        Args:
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
            "/v1/reranking",
            body=maybe_transform(
                {
                    "input": input,
                    "query": query,
                    "model": model,
                    "rank_fields": rank_fields,
                    "return_input": return_input,
                    "top_k": top_k,
                },
                reranking_create_params.RerankingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RerankingCreateResponse,
        )


class AsyncRerankingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRerankingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRerankingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRerankingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return AsyncRerankingsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        input: object,
        query: str,
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
    ) -> RerankingCreateResponse:
        """
        Rerank different kind of documents for a given query.

        Args: params: RerankingCreateParams: The parameters for reranking.

        Returns: RerankingCreateResponse: The reranked documents for the input query.

        Args:
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
            "/v1/reranking",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "query": query,
                    "model": model,
                    "rank_fields": rank_fields,
                    "return_input": return_input,
                    "top_k": top_k,
                },
                reranking_create_params.RerankingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RerankingCreateResponse,
        )


class RerankingsResourceWithRawResponse:
    def __init__(self, rerankings: RerankingsResource) -> None:
        self._rerankings = rerankings

        self.create = to_raw_response_wrapper(
            rerankings.create,
        )


class AsyncRerankingsResourceWithRawResponse:
    def __init__(self, rerankings: AsyncRerankingsResource) -> None:
        self._rerankings = rerankings

        self.create = async_to_raw_response_wrapper(
            rerankings.create,
        )


class RerankingsResourceWithStreamingResponse:
    def __init__(self, rerankings: RerankingsResource) -> None:
        self._rerankings = rerankings

        self.create = to_streamed_response_wrapper(
            rerankings.create,
        )


class AsyncRerankingsResourceWithStreamingResponse:
    def __init__(self, rerankings: AsyncRerankingsResource) -> None:
        self._rerankings = rerankings

        self.create = async_to_streamed_response_wrapper(
            rerankings.create,
        )
