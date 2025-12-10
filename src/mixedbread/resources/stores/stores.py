# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional

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
    store_list_params,
    store_create_params,
    store_search_params,
    store_update_params,
    store_metadata_facets_params,
    store_question_answering_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.store import Store
from ..._base_client import AsyncPaginator, make_request_options
from ...types.expires_after_param import ExpiresAfterParam
from ...types.store_delete_response import StoreDeleteResponse
from ...types.store_search_response import StoreSearchResponse
from ...types.store_metadata_facets_response import StoreMetadataFacetsResponse
from ...types.store_chunk_search_options_param import StoreChunkSearchOptionsParam
from ...types.store_question_answering_response import StoreQuestionAnsweringResponse

__all__ = ["StoresResource", "AsyncStoresResource"]


class StoresResource(SyncAPIResource):
    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> StoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return StoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return StoresResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        is_public: bool | Omit = omit,
        expires_after: Optional[ExpiresAfterParam] | Omit = omit,
        metadata: object | Omit = omit,
        config: Optional[store_create_params.Config] | Omit = omit,
        file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Store:
        """
        Create a new vector store.

        Args: vector_store_create: VectorStoreCreate object containing the name,
        description, and metadata.

        Returns: VectorStore: The response containing the created vector store details.

        Args:
          name: Name for the new store. Can only contain lowercase letters, numbers, periods
              (.), and hyphens (-).

          description: Description of the store

          is_public: Whether the store can be accessed by anyone with valid login credentials

          expires_after: Represents an expiration policy for a store.

          metadata: Optional metadata key-value pairs

          config: Configuration for a store.

          file_ids: Optional list of file IDs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/stores",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "is_public": is_public,
                    "expires_after": expires_after,
                    "metadata": metadata,
                    "config": config,
                    "file_ids": file_ids,
                },
                store_create_params.StoreCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Store,
        )

    def retrieve(
        self,
        store_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Store:
        """
        Get a store by ID or name.

        Args: store_identifier: The ID or name of the store to retrieve.

        Returns: Store: The response containing the store details.

        Args:
          store_identifier: The ID or name of the store

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not store_identifier:
            raise ValueError(f"Expected a non-empty value for `store_identifier` but received {store_identifier!r}")
        return self._get(
            f"/v1/stores/{store_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Store,
        )

    def update(
        self,
        store_identifier: str,
        *,
        name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        is_public: Optional[bool] | Omit = omit,
        expires_after: Optional[ExpiresAfterParam] | Omit = omit,
        metadata: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Store:
        """
        Update a store by ID or name.

        Args: store_identifier: The ID or name of the store to update. store_update:
        StoreCreate object containing the name, description, and metadata.

        Returns: Store: The response containing the updated store details.

        Args:
          store_identifier: The ID or name of the store

          name: New name for the store. Can only contain lowercase letters, numbers, periods
              (.), and hyphens (-).

          description: New description

          is_public: Whether the store can be accessed by anyone with valid login credentials

          expires_after: Represents an expiration policy for a store.

          metadata: Optional metadata key-value pairs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not store_identifier:
            raise ValueError(f"Expected a non-empty value for `store_identifier` but received {store_identifier!r}")
        return self._put(
            f"/v1/stores/{store_identifier}",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "is_public": is_public,
                    "expires_after": expires_after,
                    "metadata": metadata,
                },
                store_update_params.StoreUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Store,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        include_total: bool | Omit = omit,
        q: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[Store]:
        """List all stores with optional search.

        Args: pagination: The pagination options.

        q: Optional search query to filter
        vector stores.

        Returns: StoreListResponse: The list of stores.

        Args:
          limit: Maximum number of items to return per page (1-100)

          after: Cursor for forward pagination - get items after this position. Use last_cursor
              from previous response.

          before: Cursor for backward pagination - get items before this position. Use
              first_cursor from previous response.

          include_total: Whether to include total count in response (expensive operation)

          q: Search query for fuzzy matching over name and description fields

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/stores",
            page=SyncCursor[Store],
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
                        "q": q,
                    },
                    store_list_params.StoreListParams,
                ),
            ),
            model=Store,
        )

    def delete(
        self,
        store_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoreDeleteResponse:
        """
        Delete a store by ID or name.

        Args: store_identifier: The ID or name of the store to delete.

        Returns: Store: The response containing the deleted store details.

        Args:
          store_identifier: The ID or name of the store to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not store_identifier:
            raise ValueError(f"Expected a non-empty value for `store_identifier` but received {store_identifier!r}")
        return self._delete(
            f"/v1/stores/{store_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoreDeleteResponse,
        )

    def metadata_facets(
        self,
        *,
        query: Optional[str] | Omit = omit,
        store_identifiers: SequenceNotStr[str],
        top_k: int | Omit = omit,
        filters: Optional[store_metadata_facets_params.Filters] | Omit = omit,
        file_ids: Union[Iterable[object], SequenceNotStr[str], None] | Omit = omit,
        search_options: StoreChunkSearchOptionsParam | Omit = omit,
        facets: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoreMetadataFacetsResponse:
        """
        Get metadata facets

        Args:
          query: Search query text

          store_identifiers: IDs or names of stores to search

          top_k: Number of results to return

          filters: Optional filter conditions

          file_ids: Optional list of file IDs to filter chunks by (inclusion filter)

          search_options: Search configuration options

          facets: Optional list of facets to return. Use dot for nested fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/stores/metadata-facets",
            body=maybe_transform(
                {
                    "query": query,
                    "store_identifiers": store_identifiers,
                    "top_k": top_k,
                    "filters": filters,
                    "file_ids": file_ids,
                    "search_options": search_options,
                    "facets": facets,
                },
                store_metadata_facets_params.StoreMetadataFacetsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoreMetadataFacetsResponse,
        )

    def question_answering(
        self,
        *,
        query: str | Omit = omit,
        store_identifiers: SequenceNotStr[str],
        top_k: int | Omit = omit,
        filters: Optional[store_question_answering_params.Filters] | Omit = omit,
        file_ids: Union[Iterable[object], SequenceNotStr[str], None] | Omit = omit,
        search_options: StoreChunkSearchOptionsParam | Omit = omit,
        stream: bool | Omit = omit,
        qa_options: store_question_answering_params.QaOptions | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoreQuestionAnsweringResponse:
        """Question answering

        Args:
          query: Question to answer.

        If not provided, the question will be extracted from the
              passed messages.

          store_identifiers: IDs or names of stores to search

          top_k: Number of results to return

          filters: Optional filter conditions

          file_ids: Optional list of file IDs to filter chunks by (inclusion filter)

          search_options: Search configuration options

          stream: Whether to stream the answer

          qa_options: Question answering configuration options

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/stores/question-answering",
            body=maybe_transform(
                {
                    "query": query,
                    "store_identifiers": store_identifiers,
                    "top_k": top_k,
                    "filters": filters,
                    "file_ids": file_ids,
                    "search_options": search_options,
                    "stream": stream,
                    "qa_options": qa_options,
                },
                store_question_answering_params.StoreQuestionAnsweringParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoreQuestionAnsweringResponse,
        )

    def search(
        self,
        *,
        query: str,
        store_identifiers: SequenceNotStr[str],
        top_k: int | Omit = omit,
        filters: Optional[store_search_params.Filters] | Omit = omit,
        file_ids: Union[Iterable[object], SequenceNotStr[str], None] | Omit = omit,
        search_options: StoreChunkSearchOptionsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoreSearchResponse:
        """
        Perform semantic search across store chunks.

        This endpoint searches through store chunks using semantic similarity matching.
        It supports complex search queries with filters and returns relevance-scored
        results.

        Args: search_params: Search configuration including: - query text or
        embeddings - store_identifiers: List of store identifiers to search - file_ids:
        Optional list of file IDs to filter chunks by (or tuple of list and condition
        operator) - metadata filters - pagination parameters - sorting preferences
        \\__state: API state dependency \\__ctx: Service context dependency

        Returns: StoreSearchResponse containing: - List of matched chunks with relevance
        scores - Pagination details including total result count

        Raises: HTTPException (400): If search parameters are invalid HTTPException
        (404): If no vector stores are found to search

        Args:
          query: Search query text

          store_identifiers: IDs or names of stores to search

          top_k: Number of results to return

          filters: Optional filter conditions

          file_ids: Optional list of file IDs to filter chunks by (inclusion filter)

          search_options: Search configuration options

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/stores/search",
            body=maybe_transform(
                {
                    "query": query,
                    "store_identifiers": store_identifiers,
                    "top_k": top_k,
                    "filters": filters,
                    "file_ids": file_ids,
                    "search_options": search_options,
                },
                store_search_params.StoreSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoreSearchResponse,
        )


class AsyncStoresResource(AsyncAPIResource):
    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStoresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStoresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return AsyncStoresResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        is_public: bool | Omit = omit,
        expires_after: Optional[ExpiresAfterParam] | Omit = omit,
        metadata: object | Omit = omit,
        config: Optional[store_create_params.Config] | Omit = omit,
        file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Store:
        """
        Create a new vector store.

        Args: vector_store_create: VectorStoreCreate object containing the name,
        description, and metadata.

        Returns: VectorStore: The response containing the created vector store details.

        Args:
          name: Name for the new store. Can only contain lowercase letters, numbers, periods
              (.), and hyphens (-).

          description: Description of the store

          is_public: Whether the store can be accessed by anyone with valid login credentials

          expires_after: Represents an expiration policy for a store.

          metadata: Optional metadata key-value pairs

          config: Configuration for a store.

          file_ids: Optional list of file IDs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/stores",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "is_public": is_public,
                    "expires_after": expires_after,
                    "metadata": metadata,
                    "config": config,
                    "file_ids": file_ids,
                },
                store_create_params.StoreCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Store,
        )

    async def retrieve(
        self,
        store_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Store:
        """
        Get a store by ID or name.

        Args: store_identifier: The ID or name of the store to retrieve.

        Returns: Store: The response containing the store details.

        Args:
          store_identifier: The ID or name of the store

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not store_identifier:
            raise ValueError(f"Expected a non-empty value for `store_identifier` but received {store_identifier!r}")
        return await self._get(
            f"/v1/stores/{store_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Store,
        )

    async def update(
        self,
        store_identifier: str,
        *,
        name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        is_public: Optional[bool] | Omit = omit,
        expires_after: Optional[ExpiresAfterParam] | Omit = omit,
        metadata: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Store:
        """
        Update a store by ID or name.

        Args: store_identifier: The ID or name of the store to update. store_update:
        StoreCreate object containing the name, description, and metadata.

        Returns: Store: The response containing the updated store details.

        Args:
          store_identifier: The ID or name of the store

          name: New name for the store. Can only contain lowercase letters, numbers, periods
              (.), and hyphens (-).

          description: New description

          is_public: Whether the store can be accessed by anyone with valid login credentials

          expires_after: Represents an expiration policy for a store.

          metadata: Optional metadata key-value pairs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not store_identifier:
            raise ValueError(f"Expected a non-empty value for `store_identifier` but received {store_identifier!r}")
        return await self._put(
            f"/v1/stores/{store_identifier}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "is_public": is_public,
                    "expires_after": expires_after,
                    "metadata": metadata,
                },
                store_update_params.StoreUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Store,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        include_total: bool | Omit = omit,
        q: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Store, AsyncCursor[Store]]:
        """List all stores with optional search.

        Args: pagination: The pagination options.

        q: Optional search query to filter
        vector stores.

        Returns: StoreListResponse: The list of stores.

        Args:
          limit: Maximum number of items to return per page (1-100)

          after: Cursor for forward pagination - get items after this position. Use last_cursor
              from previous response.

          before: Cursor for backward pagination - get items before this position. Use
              first_cursor from previous response.

          include_total: Whether to include total count in response (expensive operation)

          q: Search query for fuzzy matching over name and description fields

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/stores",
            page=AsyncCursor[Store],
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
                        "q": q,
                    },
                    store_list_params.StoreListParams,
                ),
            ),
            model=Store,
        )

    async def delete(
        self,
        store_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoreDeleteResponse:
        """
        Delete a store by ID or name.

        Args: store_identifier: The ID or name of the store to delete.

        Returns: Store: The response containing the deleted store details.

        Args:
          store_identifier: The ID or name of the store to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not store_identifier:
            raise ValueError(f"Expected a non-empty value for `store_identifier` but received {store_identifier!r}")
        return await self._delete(
            f"/v1/stores/{store_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoreDeleteResponse,
        )

    async def metadata_facets(
        self,
        *,
        query: Optional[str] | Omit = omit,
        store_identifiers: SequenceNotStr[str],
        top_k: int | Omit = omit,
        filters: Optional[store_metadata_facets_params.Filters] | Omit = omit,
        file_ids: Union[Iterable[object], SequenceNotStr[str], None] | Omit = omit,
        search_options: StoreChunkSearchOptionsParam | Omit = omit,
        facets: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoreMetadataFacetsResponse:
        """
        Get metadata facets

        Args:
          query: Search query text

          store_identifiers: IDs or names of stores to search

          top_k: Number of results to return

          filters: Optional filter conditions

          file_ids: Optional list of file IDs to filter chunks by (inclusion filter)

          search_options: Search configuration options

          facets: Optional list of facets to return. Use dot for nested fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/stores/metadata-facets",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "store_identifiers": store_identifiers,
                    "top_k": top_k,
                    "filters": filters,
                    "file_ids": file_ids,
                    "search_options": search_options,
                    "facets": facets,
                },
                store_metadata_facets_params.StoreMetadataFacetsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoreMetadataFacetsResponse,
        )

    async def question_answering(
        self,
        *,
        query: str | Omit = omit,
        store_identifiers: SequenceNotStr[str],
        top_k: int | Omit = omit,
        filters: Optional[store_question_answering_params.Filters] | Omit = omit,
        file_ids: Union[Iterable[object], SequenceNotStr[str], None] | Omit = omit,
        search_options: StoreChunkSearchOptionsParam | Omit = omit,
        stream: bool | Omit = omit,
        qa_options: store_question_answering_params.QaOptions | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoreQuestionAnsweringResponse:
        """Question answering

        Args:
          query: Question to answer.

        If not provided, the question will be extracted from the
              passed messages.

          store_identifiers: IDs or names of stores to search

          top_k: Number of results to return

          filters: Optional filter conditions

          file_ids: Optional list of file IDs to filter chunks by (inclusion filter)

          search_options: Search configuration options

          stream: Whether to stream the answer

          qa_options: Question answering configuration options

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/stores/question-answering",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "store_identifiers": store_identifiers,
                    "top_k": top_k,
                    "filters": filters,
                    "file_ids": file_ids,
                    "search_options": search_options,
                    "stream": stream,
                    "qa_options": qa_options,
                },
                store_question_answering_params.StoreQuestionAnsweringParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoreQuestionAnsweringResponse,
        )

    async def search(
        self,
        *,
        query: str,
        store_identifiers: SequenceNotStr[str],
        top_k: int | Omit = omit,
        filters: Optional[store_search_params.Filters] | Omit = omit,
        file_ids: Union[Iterable[object], SequenceNotStr[str], None] | Omit = omit,
        search_options: StoreChunkSearchOptionsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoreSearchResponse:
        """
        Perform semantic search across store chunks.

        This endpoint searches through store chunks using semantic similarity matching.
        It supports complex search queries with filters and returns relevance-scored
        results.

        Args: search_params: Search configuration including: - query text or
        embeddings - store_identifiers: List of store identifiers to search - file_ids:
        Optional list of file IDs to filter chunks by (or tuple of list and condition
        operator) - metadata filters - pagination parameters - sorting preferences
        \\__state: API state dependency \\__ctx: Service context dependency

        Returns: StoreSearchResponse containing: - List of matched chunks with relevance
        scores - Pagination details including total result count

        Raises: HTTPException (400): If search parameters are invalid HTTPException
        (404): If no vector stores are found to search

        Args:
          query: Search query text

          store_identifiers: IDs or names of stores to search

          top_k: Number of results to return

          filters: Optional filter conditions

          file_ids: Optional list of file IDs to filter chunks by (inclusion filter)

          search_options: Search configuration options

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/stores/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "store_identifiers": store_identifiers,
                    "top_k": top_k,
                    "filters": filters,
                    "file_ids": file_ids,
                    "search_options": search_options,
                },
                store_search_params.StoreSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoreSearchResponse,
        )


class StoresResourceWithRawResponse:
    def __init__(self, stores: StoresResource) -> None:
        self._stores = stores

        self.create = to_raw_response_wrapper(
            stores.create,
        )
        self.retrieve = to_raw_response_wrapper(
            stores.retrieve,
        )
        self.update = to_raw_response_wrapper(
            stores.update,
        )
        self.list = to_raw_response_wrapper(
            stores.list,
        )
        self.delete = to_raw_response_wrapper(
            stores.delete,
        )
        self.metadata_facets = to_raw_response_wrapper(
            stores.metadata_facets,
        )
        self.question_answering = to_raw_response_wrapper(
            stores.question_answering,
        )
        self.search = to_raw_response_wrapper(
            stores.search,
        )

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._stores.files)


class AsyncStoresResourceWithRawResponse:
    def __init__(self, stores: AsyncStoresResource) -> None:
        self._stores = stores

        self.create = async_to_raw_response_wrapper(
            stores.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            stores.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            stores.update,
        )
        self.list = async_to_raw_response_wrapper(
            stores.list,
        )
        self.delete = async_to_raw_response_wrapper(
            stores.delete,
        )
        self.metadata_facets = async_to_raw_response_wrapper(
            stores.metadata_facets,
        )
        self.question_answering = async_to_raw_response_wrapper(
            stores.question_answering,
        )
        self.search = async_to_raw_response_wrapper(
            stores.search,
        )

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._stores.files)


class StoresResourceWithStreamingResponse:
    def __init__(self, stores: StoresResource) -> None:
        self._stores = stores

        self.create = to_streamed_response_wrapper(
            stores.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            stores.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            stores.update,
        )
        self.list = to_streamed_response_wrapper(
            stores.list,
        )
        self.delete = to_streamed_response_wrapper(
            stores.delete,
        )
        self.metadata_facets = to_streamed_response_wrapper(
            stores.metadata_facets,
        )
        self.question_answering = to_streamed_response_wrapper(
            stores.question_answering,
        )
        self.search = to_streamed_response_wrapper(
            stores.search,
        )

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._stores.files)


class AsyncStoresResourceWithStreamingResponse:
    def __init__(self, stores: AsyncStoresResource) -> None:
        self._stores = stores

        self.create = async_to_streamed_response_wrapper(
            stores.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            stores.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            stores.update,
        )
        self.list = async_to_streamed_response_wrapper(
            stores.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            stores.delete,
        )
        self.metadata_facets = async_to_streamed_response_wrapper(
            stores.metadata_facets,
        )
        self.question_answering = async_to_streamed_response_wrapper(
            stores.question_answering,
        )
        self.search = async_to_streamed_response_wrapper(
            stores.search,
        )

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._stores.files)
