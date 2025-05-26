# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

import httpx

from .files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from ...types import (
    vector_store_list_params,
    vector_store_create_params,
    vector_store_search_params,
    vector_store_update_params,
    vector_store_question_answering_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncLimitOffset, AsyncLimitOffset
from ..._base_client import AsyncPaginator, make_request_options
from ...types.vector_store import VectorStore
from ...types.expires_after_param import ExpiresAfterParam
from ...types.vector_store_delete_response import VectorStoreDeleteResponse
from ...types.vector_store_search_response import VectorStoreSearchResponse
from ...types.vector_store_chunk_search_options_param import VectorStoreChunkSearchOptionsParam
from ...types.vector_store_question_answering_response import VectorStoreQuestionAnsweringResponse

__all__ = ["VectorStoresResource", "AsyncVectorStoresResource"]


class VectorStoresResource(SyncAPIResource):
    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> VectorStoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return VectorStoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VectorStoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return VectorStoresResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        expires_after: Optional[ExpiresAfterParam] | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        file_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStore:
        """
        Create a new vector store.

        Args: vector_store_create: VectorStoreCreate object containing the name,
        description, and metadata.

        Returns: VectorStore: The response containing the created vector store details.

        Args:
          name: Name for the new vector store

          description: Description of the vector store

          expires_after: Represents an expiration policy for a vector store.

          metadata: Optional metadata key-value pairs

          file_ids: Optional list of file IDs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/vector_stores",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "expires_after": expires_after,
                    "metadata": metadata,
                    "file_ids": file_ids,
                },
                vector_store_create_params.VectorStoreCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStore,
        )

    def retrieve(
        self,
        vector_store_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStore:
        """
        Get a vector store by ID.

        Args: vector_store_id: The ID of the vector store to retrieve.

        Returns: VectorStore: The response containing the vector store details.

        Args:
          vector_store_id: The ID of the vector store

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return self._get(
            f"/v1/vector_stores/{vector_store_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStore,
        )

    def update(
        self,
        vector_store_id: str,
        *,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        expires_after: Optional[ExpiresAfterParam] | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStore:
        """
        Update a vector store by ID.

        Args: vector_store_id: The ID of the vector store to update.
        vector_store_update: VectorStoreCreate object containing the name, description,
        and metadata.

        Returns: VectorStore: The response containing the updated vector store details.

        Args:
          vector_store_id: The ID of the vector store

          name: New name for the vector store

          description: New description

          expires_after: Represents an expiration policy for a vector store.

          metadata: Optional metadata key-value pairs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return self._put(
            f"/v1/vector_stores/{vector_store_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "expires_after": expires_after,
                    "metadata": metadata,
                },
                vector_store_update_params.VectorStoreUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStore,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncLimitOffset[VectorStore]:
        """
        List all vector stores.

        Args: pagination: The pagination options.

        Returns: VectorStoreListResponse: The list of vector stores.

        Args:
          limit: Maximum number of items to return per page

          offset: Offset of the first item to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/vector_stores",
            page=SyncLimitOffset[VectorStore],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    vector_store_list_params.VectorStoreListParams,
                ),
            ),
            model=VectorStore,
        )

    def delete(
        self,
        vector_store_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreDeleteResponse:
        """
        Delete a vector store by ID.

        Args: vector_store_id: The ID of the vector store to delete.

        Returns: VectorStore: The response containing the deleted vector store details.

        Args:
          vector_store_id: The ID of the vector store to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return self._delete(
            f"/v1/vector_stores/{vector_store_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreDeleteResponse,
        )

    def question_answering(
        self,
        *,
        query: str | NotGiven = NOT_GIVEN,
        vector_store_ids: List[str],
        top_k: int | NotGiven = NOT_GIVEN,
        filters: Optional[vector_store_question_answering_params.Filters] | NotGiven = NOT_GIVEN,
        search_options: VectorStoreChunkSearchOptionsParam | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        qa_options: vector_store_question_answering_params.QaOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreQuestionAnsweringResponse:
        """Question answering

        Args:
          query: Question to answer.

        If not provided, the question will be extracted from the
              passed messages.

          vector_store_ids: IDs of vector stores to search

          top_k: Number of results to return

          filters: Optional filter conditions

          search_options: Search configuration options

          stream: Whether to stream the answer

          qa_options: Question answering configuration options

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/vector_stores/question-answering",
            body=maybe_transform(
                {
                    "query": query,
                    "vector_store_ids": vector_store_ids,
                    "top_k": top_k,
                    "filters": filters,
                    "search_options": search_options,
                    "stream": stream,
                    "qa_options": qa_options,
                },
                vector_store_question_answering_params.VectorStoreQuestionAnsweringParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreQuestionAnsweringResponse,
        )

    def search(
        self,
        *,
        query: str,
        vector_store_ids: List[str],
        top_k: int | NotGiven = NOT_GIVEN,
        filters: Optional[vector_store_search_params.Filters] | NotGiven = NOT_GIVEN,
        search_options: VectorStoreChunkSearchOptionsParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreSearchResponse:
        """
        Perform semantic search across vector store chunks.

        This endpoint searches through vector store chunks using semantic similarity
        matching. It supports complex search queries with filters and returns
        relevance-scored results.

        Args: search_params: Search configuration including: - query text or
        embeddings - metadata filters - pagination parameters - sorting preferences
        \\__state: API state dependency \\__ctx: Service context dependency

        Returns: VectorStoreSearchChunkResponse containing: - List of matched chunks
        with relevance scores - Pagination details including total result count

        Raises: HTTPException (400): If search parameters are invalid HTTPException
        (404): If no vector stores are found to search

        Args:
          query: Search query text

          vector_store_ids: IDs of vector stores to search

          top_k: Number of results to return

          filters: Optional filter conditions

          search_options: Search configuration options

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/vector_stores/search",
            body=maybe_transform(
                {
                    "query": query,
                    "vector_store_ids": vector_store_ids,
                    "top_k": top_k,
                    "filters": filters,
                    "search_options": search_options,
                },
                vector_store_search_params.VectorStoreSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreSearchResponse,
        )


class AsyncVectorStoresResource(AsyncAPIResource):
    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVectorStoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVectorStoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVectorStoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return AsyncVectorStoresResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        expires_after: Optional[ExpiresAfterParam] | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        file_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStore:
        """
        Create a new vector store.

        Args: vector_store_create: VectorStoreCreate object containing the name,
        description, and metadata.

        Returns: VectorStore: The response containing the created vector store details.

        Args:
          name: Name for the new vector store

          description: Description of the vector store

          expires_after: Represents an expiration policy for a vector store.

          metadata: Optional metadata key-value pairs

          file_ids: Optional list of file IDs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/vector_stores",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "expires_after": expires_after,
                    "metadata": metadata,
                    "file_ids": file_ids,
                },
                vector_store_create_params.VectorStoreCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStore,
        )

    async def retrieve(
        self,
        vector_store_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStore:
        """
        Get a vector store by ID.

        Args: vector_store_id: The ID of the vector store to retrieve.

        Returns: VectorStore: The response containing the vector store details.

        Args:
          vector_store_id: The ID of the vector store

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return await self._get(
            f"/v1/vector_stores/{vector_store_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStore,
        )

    async def update(
        self,
        vector_store_id: str,
        *,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        expires_after: Optional[ExpiresAfterParam] | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStore:
        """
        Update a vector store by ID.

        Args: vector_store_id: The ID of the vector store to update.
        vector_store_update: VectorStoreCreate object containing the name, description,
        and metadata.

        Returns: VectorStore: The response containing the updated vector store details.

        Args:
          vector_store_id: The ID of the vector store

          name: New name for the vector store

          description: New description

          expires_after: Represents an expiration policy for a vector store.

          metadata: Optional metadata key-value pairs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return await self._put(
            f"/v1/vector_stores/{vector_store_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "expires_after": expires_after,
                    "metadata": metadata,
                },
                vector_store_update_params.VectorStoreUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStore,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[VectorStore, AsyncLimitOffset[VectorStore]]:
        """
        List all vector stores.

        Args: pagination: The pagination options.

        Returns: VectorStoreListResponse: The list of vector stores.

        Args:
          limit: Maximum number of items to return per page

          offset: Offset of the first item to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/vector_stores",
            page=AsyncLimitOffset[VectorStore],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    vector_store_list_params.VectorStoreListParams,
                ),
            ),
            model=VectorStore,
        )

    async def delete(
        self,
        vector_store_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreDeleteResponse:
        """
        Delete a vector store by ID.

        Args: vector_store_id: The ID of the vector store to delete.

        Returns: VectorStore: The response containing the deleted vector store details.

        Args:
          vector_store_id: The ID of the vector store to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return await self._delete(
            f"/v1/vector_stores/{vector_store_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreDeleteResponse,
        )

    async def question_answering(
        self,
        *,
        query: str | NotGiven = NOT_GIVEN,
        vector_store_ids: List[str],
        top_k: int | NotGiven = NOT_GIVEN,
        filters: Optional[vector_store_question_answering_params.Filters] | NotGiven = NOT_GIVEN,
        search_options: VectorStoreChunkSearchOptionsParam | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        qa_options: vector_store_question_answering_params.QaOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreQuestionAnsweringResponse:
        """Question answering

        Args:
          query: Question to answer.

        If not provided, the question will be extracted from the
              passed messages.

          vector_store_ids: IDs of vector stores to search

          top_k: Number of results to return

          filters: Optional filter conditions

          search_options: Search configuration options

          stream: Whether to stream the answer

          qa_options: Question answering configuration options

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/vector_stores/question-answering",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "vector_store_ids": vector_store_ids,
                    "top_k": top_k,
                    "filters": filters,
                    "search_options": search_options,
                    "stream": stream,
                    "qa_options": qa_options,
                },
                vector_store_question_answering_params.VectorStoreQuestionAnsweringParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreQuestionAnsweringResponse,
        )

    async def search(
        self,
        *,
        query: str,
        vector_store_ids: List[str],
        top_k: int | NotGiven = NOT_GIVEN,
        filters: Optional[vector_store_search_params.Filters] | NotGiven = NOT_GIVEN,
        search_options: VectorStoreChunkSearchOptionsParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreSearchResponse:
        """
        Perform semantic search across vector store chunks.

        This endpoint searches through vector store chunks using semantic similarity
        matching. It supports complex search queries with filters and returns
        relevance-scored results.

        Args: search_params: Search configuration including: - query text or
        embeddings - metadata filters - pagination parameters - sorting preferences
        \\__state: API state dependency \\__ctx: Service context dependency

        Returns: VectorStoreSearchChunkResponse containing: - List of matched chunks
        with relevance scores - Pagination details including total result count

        Raises: HTTPException (400): If search parameters are invalid HTTPException
        (404): If no vector stores are found to search

        Args:
          query: Search query text

          vector_store_ids: IDs of vector stores to search

          top_k: Number of results to return

          filters: Optional filter conditions

          search_options: Search configuration options

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/vector_stores/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "vector_store_ids": vector_store_ids,
                    "top_k": top_k,
                    "filters": filters,
                    "search_options": search_options,
                },
                vector_store_search_params.VectorStoreSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreSearchResponse,
        )


class VectorStoresResourceWithRawResponse:
    def __init__(self, vector_stores: VectorStoresResource) -> None:
        self._vector_stores = vector_stores

        self.create = to_raw_response_wrapper(
            vector_stores.create,
        )
        self.retrieve = to_raw_response_wrapper(
            vector_stores.retrieve,
        )
        self.update = to_raw_response_wrapper(
            vector_stores.update,
        )
        self.list = to_raw_response_wrapper(
            vector_stores.list,
        )
        self.delete = to_raw_response_wrapper(
            vector_stores.delete,
        )
        self.question_answering = to_raw_response_wrapper(
            vector_stores.question_answering,
        )
        self.search = to_raw_response_wrapper(
            vector_stores.search,
        )

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._vector_stores.files)


class AsyncVectorStoresResourceWithRawResponse:
    def __init__(self, vector_stores: AsyncVectorStoresResource) -> None:
        self._vector_stores = vector_stores

        self.create = async_to_raw_response_wrapper(
            vector_stores.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            vector_stores.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            vector_stores.update,
        )
        self.list = async_to_raw_response_wrapper(
            vector_stores.list,
        )
        self.delete = async_to_raw_response_wrapper(
            vector_stores.delete,
        )
        self.question_answering = async_to_raw_response_wrapper(
            vector_stores.question_answering,
        )
        self.search = async_to_raw_response_wrapper(
            vector_stores.search,
        )

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._vector_stores.files)


class VectorStoresResourceWithStreamingResponse:
    def __init__(self, vector_stores: VectorStoresResource) -> None:
        self._vector_stores = vector_stores

        self.create = to_streamed_response_wrapper(
            vector_stores.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            vector_stores.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            vector_stores.update,
        )
        self.list = to_streamed_response_wrapper(
            vector_stores.list,
        )
        self.delete = to_streamed_response_wrapper(
            vector_stores.delete,
        )
        self.question_answering = to_streamed_response_wrapper(
            vector_stores.question_answering,
        )
        self.search = to_streamed_response_wrapper(
            vector_stores.search,
        )

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._vector_stores.files)


class AsyncVectorStoresResourceWithStreamingResponse:
    def __init__(self, vector_stores: AsyncVectorStoresResource) -> None:
        self._vector_stores = vector_stores

        self.create = async_to_streamed_response_wrapper(
            vector_stores.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            vector_stores.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            vector_stores.update,
        )
        self.list = async_to_streamed_response_wrapper(
            vector_stores.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            vector_stores.delete,
        )
        self.question_answering = async_to_streamed_response_wrapper(
            vector_stores.question_answering,
        )
        self.search = async_to_streamed_response_wrapper(
            vector_stores.search,
        )

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._vector_stores.files)
