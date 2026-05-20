# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal

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
    store_grep_params,
    store_list_params,
    store_create_params,
    store_search_params,
    store_update_params,
    store_metadata_facets_params,
    store_question_answering_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
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
from ...types.store_config_param import StoreConfigParam
from ...types.expires_after_param import ExpiresAfterParam
from ...types.store_grep_response import StoreGrepResponse
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
        license: Optional[str] | Omit = omit,
        expires_after: Optional[ExpiresAfterParam] | Omit = omit,
        metadata: object | Omit = omit,
        config: Optional[StoreConfigParam] | Omit = omit,
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

          license: License for public stores

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
                    "license": license,
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
            path_template("/v1/stores/{store_identifier}", store_identifier=store_identifier),
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
        license: Optional[str] | Omit = omit,
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

          license: License for public stores

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
            path_template("/v1/stores/{store_identifier}", store_identifier=store_identifier),
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "is_public": is_public,
                    "license": license,
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
            path_template("/v1/stores/{store_identifier}", store_identifier=store_identifier),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoreDeleteResponse,
        )

    def grep(
        self,
        *,
        store_identifiers: SequenceNotStr[str],
        top_k: int | Omit = omit,
        filters: Optional[store_grep_params.Filters] | Omit = omit,
        file_ids: Union[Iterable[object], SequenceNotStr[str], None] | Omit = omit,
        pattern: str,
        targets: List[Literal["text", "generated"]] | Omit = omit,
        case_sensitive: bool | Omit = omit,
        return_metadata: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoreGrepResponse:
        """
        Match store chunks against a regular expression.

        Unlike `/stores/search`, this performs exact text matching — no embeddings, no
        semantic similarity, no reranking. Use it to find chunks containing a specific
        token, identifier, error code, or literal phrase.

        grep targets a single store and does not support pagination; raise `top_k` to
        retrieve more matches.

        Args: grep_params: Grep configuration including: - pattern: RE2 regular
        expression matched against chunk text - targets: chunk content groups to match
        (`text`, `generated`) - case_sensitive: whether the pattern is case-sensitive -
        store_identifiers: the single store to grep - file_ids: optional list of file
        IDs to filter chunks by - filters: optional metadata filter conditions - top_k:
        number of matches to return

        Returns: StoreGrepResponse containing the list of matching chunks.

        Raises: HTTPException (400): If grep parameters are invalid HTTPException (404):
        If the store is not found

        Args:
          store_identifiers: IDs or names of stores

          top_k: Number of results to return

          filters: Optional filter conditions

          file_ids: Optional list of file IDs to filter chunks by (inclusion filter)

          pattern: Regular expression (RE2 syntax) matched against chunk text

          targets: Chunk content groups to match against. `text` matches the original text of text
              chunks; `generated` matches ingestion-derived fields (transcription, OCR text,
              summaries).

          case_sensitive: Whether the regular expression is case-sensitive

          return_metadata: Whether to return file metadata

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/stores/grep",
            body=maybe_transform(
                {
                    "store_identifiers": store_identifiers,
                    "top_k": top_k,
                    "filters": filters,
                    "file_ids": file_ids,
                    "pattern": pattern,
                    "targets": targets,
                    "case_sensitive": case_sensitive,
                    "return_metadata": return_metadata,
                },
                store_grep_params.StoreGrepParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoreGrepResponse,
        )

    def metadata_facets(
        self,
        *,
        store_identifiers: SequenceNotStr[str],
        top_k: int | Omit = omit,
        filters: Optional[store_metadata_facets_params.Filters] | Omit = omit,
        file_ids: Union[Iterable[object], SequenceNotStr[str], None] | Omit = omit,
        query: Optional[str] | Omit = omit,
        search_options: StoreChunkSearchOptionsParam | Omit = omit,
        facets: Optional[SequenceNotStr[str]] | Omit = omit,
        max_fields: int | Omit = omit,
        max_values_per_field: int | Omit = omit,
        max_files: int | Omit = omit,
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
          store_identifiers: IDs or names of stores

          top_k: Number of results to return

          filters: Optional filter conditions

          file_ids: Optional list of file IDs to filter chunks by (inclusion filter)

          query: Search query text

          search_options: Search configuration options

          facets: Optional list of facets to return. Use dot for nested fields.

          max_fields: Maximum number of distinct metadata fields (keys) to return.

          max_values_per_field: Maximum number of distinct values returned per field, ranked by count.

          max_files: Maximum number of store files scanned to compute facets.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/stores/metadata-facets",
            body=maybe_transform(
                {
                    "store_identifiers": store_identifiers,
                    "top_k": top_k,
                    "filters": filters,
                    "file_ids": file_ids,
                    "query": query,
                    "search_options": search_options,
                    "facets": facets,
                    "max_fields": max_fields,
                    "max_values_per_field": max_values_per_field,
                    "max_files": max_files,
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
        store_identifiers: SequenceNotStr[str],
        top_k: int | Omit = omit,
        filters: Optional[store_question_answering_params.Filters] | Omit = omit,
        file_ids: Union[Iterable[object], SequenceNotStr[str], None] | Omit = omit,
        query: str | Omit = omit,
        search_options: StoreChunkSearchOptionsParam | Omit = omit,
        stream: bool | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        qa_options: store_question_answering_params.QaOptions | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoreQuestionAnsweringResponse:
        """
        Question answering

        Args:
          store_identifiers: IDs or names of stores

          top_k: Number of results to return

          filters: Optional filter conditions

          file_ids: Optional list of file IDs to filter chunks by (inclusion filter)

          query: Question to answer. If not provided, the question will be extracted from the
              passed messages.

          search_options: Search configuration options

          stream: Whether to stream the answer

          instructions: Additional custom instructions (followed only when not in conflict with existing
              rules)

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
                    "store_identifiers": store_identifiers,
                    "top_k": top_k,
                    "filters": filters,
                    "file_ids": file_ids,
                    "query": query,
                    "search_options": search_options,
                    "stream": stream,
                    "instructions": instructions,
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
        store_identifiers: SequenceNotStr[str],
        top_k: int | Omit = omit,
        filters: Optional[store_search_params.Filters] | Omit = omit,
        file_ids: Union[Iterable[object], SequenceNotStr[str], None] | Omit = omit,
        query: store_search_params.Query,
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

        For the special 'mixedbread/web' store, this endpoint performs web search using
        a mixture of different providers instead of semantic search. Web search results
        are always reranked for consistent scoring.

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
          store_identifiers: IDs or names of stores

          top_k: Number of results to return

          filters: Optional filter conditions

          file_ids: Optional list of file IDs to filter chunks by (inclusion filter)

          query: Search query text

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
                    "store_identifiers": store_identifiers,
                    "top_k": top_k,
                    "filters": filters,
                    "file_ids": file_ids,
                    "query": query,
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
        license: Optional[str] | Omit = omit,
        expires_after: Optional[ExpiresAfterParam] | Omit = omit,
        metadata: object | Omit = omit,
        config: Optional[StoreConfigParam] | Omit = omit,
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

          license: License for public stores

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
                    "license": license,
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
            path_template("/v1/stores/{store_identifier}", store_identifier=store_identifier),
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
        license: Optional[str] | Omit = omit,
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

          license: License for public stores

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
            path_template("/v1/stores/{store_identifier}", store_identifier=store_identifier),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "is_public": is_public,
                    "license": license,
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
            path_template("/v1/stores/{store_identifier}", store_identifier=store_identifier),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoreDeleteResponse,
        )

    async def grep(
        self,
        *,
        store_identifiers: SequenceNotStr[str],
        top_k: int | Omit = omit,
        filters: Optional[store_grep_params.Filters] | Omit = omit,
        file_ids: Union[Iterable[object], SequenceNotStr[str], None] | Omit = omit,
        pattern: str,
        targets: List[Literal["text", "generated"]] | Omit = omit,
        case_sensitive: bool | Omit = omit,
        return_metadata: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoreGrepResponse:
        """
        Match store chunks against a regular expression.

        Unlike `/stores/search`, this performs exact text matching — no embeddings, no
        semantic similarity, no reranking. Use it to find chunks containing a specific
        token, identifier, error code, or literal phrase.

        grep targets a single store and does not support pagination; raise `top_k` to
        retrieve more matches.

        Args: grep_params: Grep configuration including: - pattern: RE2 regular
        expression matched against chunk text - targets: chunk content groups to match
        (`text`, `generated`) - case_sensitive: whether the pattern is case-sensitive -
        store_identifiers: the single store to grep - file_ids: optional list of file
        IDs to filter chunks by - filters: optional metadata filter conditions - top_k:
        number of matches to return

        Returns: StoreGrepResponse containing the list of matching chunks.

        Raises: HTTPException (400): If grep parameters are invalid HTTPException (404):
        If the store is not found

        Args:
          store_identifiers: IDs or names of stores

          top_k: Number of results to return

          filters: Optional filter conditions

          file_ids: Optional list of file IDs to filter chunks by (inclusion filter)

          pattern: Regular expression (RE2 syntax) matched against chunk text

          targets: Chunk content groups to match against. `text` matches the original text of text
              chunks; `generated` matches ingestion-derived fields (transcription, OCR text,
              summaries).

          case_sensitive: Whether the regular expression is case-sensitive

          return_metadata: Whether to return file metadata

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/stores/grep",
            body=await async_maybe_transform(
                {
                    "store_identifiers": store_identifiers,
                    "top_k": top_k,
                    "filters": filters,
                    "file_ids": file_ids,
                    "pattern": pattern,
                    "targets": targets,
                    "case_sensitive": case_sensitive,
                    "return_metadata": return_metadata,
                },
                store_grep_params.StoreGrepParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoreGrepResponse,
        )

    async def metadata_facets(
        self,
        *,
        store_identifiers: SequenceNotStr[str],
        top_k: int | Omit = omit,
        filters: Optional[store_metadata_facets_params.Filters] | Omit = omit,
        file_ids: Union[Iterable[object], SequenceNotStr[str], None] | Omit = omit,
        query: Optional[str] | Omit = omit,
        search_options: StoreChunkSearchOptionsParam | Omit = omit,
        facets: Optional[SequenceNotStr[str]] | Omit = omit,
        max_fields: int | Omit = omit,
        max_values_per_field: int | Omit = omit,
        max_files: int | Omit = omit,
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
          store_identifiers: IDs or names of stores

          top_k: Number of results to return

          filters: Optional filter conditions

          file_ids: Optional list of file IDs to filter chunks by (inclusion filter)

          query: Search query text

          search_options: Search configuration options

          facets: Optional list of facets to return. Use dot for nested fields.

          max_fields: Maximum number of distinct metadata fields (keys) to return.

          max_values_per_field: Maximum number of distinct values returned per field, ranked by count.

          max_files: Maximum number of store files scanned to compute facets.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/stores/metadata-facets",
            body=await async_maybe_transform(
                {
                    "store_identifiers": store_identifiers,
                    "top_k": top_k,
                    "filters": filters,
                    "file_ids": file_ids,
                    "query": query,
                    "search_options": search_options,
                    "facets": facets,
                    "max_fields": max_fields,
                    "max_values_per_field": max_values_per_field,
                    "max_files": max_files,
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
        store_identifiers: SequenceNotStr[str],
        top_k: int | Omit = omit,
        filters: Optional[store_question_answering_params.Filters] | Omit = omit,
        file_ids: Union[Iterable[object], SequenceNotStr[str], None] | Omit = omit,
        query: str | Omit = omit,
        search_options: StoreChunkSearchOptionsParam | Omit = omit,
        stream: bool | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        qa_options: store_question_answering_params.QaOptions | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoreQuestionAnsweringResponse:
        """
        Question answering

        Args:
          store_identifiers: IDs or names of stores

          top_k: Number of results to return

          filters: Optional filter conditions

          file_ids: Optional list of file IDs to filter chunks by (inclusion filter)

          query: Question to answer. If not provided, the question will be extracted from the
              passed messages.

          search_options: Search configuration options

          stream: Whether to stream the answer

          instructions: Additional custom instructions (followed only when not in conflict with existing
              rules)

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
                    "store_identifiers": store_identifiers,
                    "top_k": top_k,
                    "filters": filters,
                    "file_ids": file_ids,
                    "query": query,
                    "search_options": search_options,
                    "stream": stream,
                    "instructions": instructions,
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
        store_identifiers: SequenceNotStr[str],
        top_k: int | Omit = omit,
        filters: Optional[store_search_params.Filters] | Omit = omit,
        file_ids: Union[Iterable[object], SequenceNotStr[str], None] | Omit = omit,
        query: store_search_params.Query,
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

        For the special 'mixedbread/web' store, this endpoint performs web search using
        a mixture of different providers instead of semantic search. Web search results
        are always reranked for consistent scoring.

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
          store_identifiers: IDs or names of stores

          top_k: Number of results to return

          filters: Optional filter conditions

          file_ids: Optional list of file IDs to filter chunks by (inclusion filter)

          query: Search query text

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
                    "store_identifiers": store_identifiers,
                    "top_k": top_k,
                    "filters": filters,
                    "file_ids": file_ids,
                    "query": query,
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
        self.grep = to_raw_response_wrapper(
            stores.grep,
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
        self.grep = async_to_raw_response_wrapper(
            stores.grep,
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
        self.grep = to_streamed_response_wrapper(
            stores.grep,
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
        self.grep = async_to_streamed_response_wrapper(
            stores.grep,
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
