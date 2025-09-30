# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
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
    vector_store_list_params,
    vector_store_create_params,
    vector_store_search_params,
    vector_store_update_params,
    vector_store_question_answering_params,
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

    @typing_extensions.deprecated("deprecated")
    def create(
        self,
        *,
        name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        is_public: bool | Omit = omit,
        expires_after: Optional[ExpiresAfterParam] | Omit = omit,
        metadata: object | Omit = omit,
        file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStore:
        """
        DEPRECATED: Use POST /stores instead

        Args:
          name: Name for the new vector store

          description: Description of the vector store

          is_public: Whether the vector store can be accessed by anyone with valid login credentials

          expires_after: Represents an expiration policy for a store.

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
                    "is_public": is_public,
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

    @typing_extensions.deprecated("deprecated")
    def retrieve(
        self,
        vector_store_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStore:
        """
        DEPRECATED: Use GET /stores/{store_identifier} instead

        Args:
          vector_store_identifier: The ID or name of the vector store

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_identifier:
            raise ValueError(
                f"Expected a non-empty value for `vector_store_identifier` but received {vector_store_identifier!r}"
            )
        return self._get(
            f"/v1/vector_stores/{vector_store_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStore,
        )

    @typing_extensions.deprecated("deprecated")
    def update(
        self,
        vector_store_identifier: str,
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
    ) -> VectorStore:
        """
        DEPRECATED: Use PUT /stores/{store_identifier} instead

        Args:
          vector_store_identifier: The ID or name of the vector store

          name: New name for the store

          description: New description

          is_public: Whether the vector store can be accessed by anyone with valid login credentials

          expires_after: Represents an expiration policy for a store.

          metadata: Optional metadata key-value pairs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_identifier:
            raise ValueError(
                f"Expected a non-empty value for `vector_store_identifier` but received {vector_store_identifier!r}"
            )
        return self._put(
            f"/v1/vector_stores/{vector_store_identifier}",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "is_public": is_public,
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

    @typing_extensions.deprecated("deprecated")
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
    ) -> SyncCursor[VectorStore]:
        """
        DEPRECATED: Use GET /stores instead

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
            "/v1/vector_stores",
            page=SyncCursor[VectorStore],
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
                    vector_store_list_params.VectorStoreListParams,
                ),
            ),
            model=VectorStore,
        )

    @typing_extensions.deprecated("deprecated")
    def delete(
        self,
        vector_store_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStoreDeleteResponse:
        """
        DEPRECATED: Use DELETE /stores/{store_identifier} instead

        Args:
          vector_store_identifier: The ID or name of the vector store to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_identifier:
            raise ValueError(
                f"Expected a non-empty value for `vector_store_identifier` but received {vector_store_identifier!r}"
            )
        return self._delete(
            f"/v1/vector_stores/{vector_store_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreDeleteResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def question_answering(
        self,
        *,
        query: str | Omit = omit,
        vector_store_identifiers: SequenceNotStr[str],
        top_k: int | Omit = omit,
        filters: Optional[vector_store_question_answering_params.Filters] | Omit = omit,
        file_ids: Union[Iterable[object], SequenceNotStr[str], None] | Omit = omit,
        search_options: VectorStoreChunkSearchOptionsParam | Omit = omit,
        stream: bool | Omit = omit,
        qa_options: vector_store_question_answering_params.QaOptions | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStoreQuestionAnsweringResponse:
        """
        DEPRECATED: Use POST /stores/question-answering instead

        Args:
          query: Question to answer. If not provided, the question will be extracted from the
              passed messages.

          vector_store_identifiers: IDs or names of vector stores to search

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
            "/v1/vector_stores/question-answering",
            body=maybe_transform(
                {
                    "query": query,
                    "vector_store_identifiers": vector_store_identifiers,
                    "top_k": top_k,
                    "filters": filters,
                    "file_ids": file_ids,
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

    @typing_extensions.deprecated("deprecated")
    def search(
        self,
        *,
        query: str,
        vector_store_identifiers: SequenceNotStr[str],
        top_k: int | Omit = omit,
        filters: Optional[vector_store_search_params.Filters] | Omit = omit,
        file_ids: Union[Iterable[object], SequenceNotStr[str], None] | Omit = omit,
        search_options: VectorStoreChunkSearchOptionsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStoreSearchResponse:
        """
        DEPRECATED: Use POST /stores/search instead

        Args:
          query: Search query text

          vector_store_identifiers: IDs or names of vector stores to search

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
            "/v1/vector_stores/search",
            body=maybe_transform(
                {
                    "query": query,
                    "vector_store_identifiers": vector_store_identifiers,
                    "top_k": top_k,
                    "filters": filters,
                    "file_ids": file_ids,
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

    @typing_extensions.deprecated("deprecated")
    async def create(
        self,
        *,
        name: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        is_public: bool | Omit = omit,
        expires_after: Optional[ExpiresAfterParam] | Omit = omit,
        metadata: object | Omit = omit,
        file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStore:
        """
        DEPRECATED: Use POST /stores instead

        Args:
          name: Name for the new vector store

          description: Description of the vector store

          is_public: Whether the vector store can be accessed by anyone with valid login credentials

          expires_after: Represents an expiration policy for a store.

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
                    "is_public": is_public,
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

    @typing_extensions.deprecated("deprecated")
    async def retrieve(
        self,
        vector_store_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStore:
        """
        DEPRECATED: Use GET /stores/{store_identifier} instead

        Args:
          vector_store_identifier: The ID or name of the vector store

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_identifier:
            raise ValueError(
                f"Expected a non-empty value for `vector_store_identifier` but received {vector_store_identifier!r}"
            )
        return await self._get(
            f"/v1/vector_stores/{vector_store_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStore,
        )

    @typing_extensions.deprecated("deprecated")
    async def update(
        self,
        vector_store_identifier: str,
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
    ) -> VectorStore:
        """
        DEPRECATED: Use PUT /stores/{store_identifier} instead

        Args:
          vector_store_identifier: The ID or name of the vector store

          name: New name for the store

          description: New description

          is_public: Whether the vector store can be accessed by anyone with valid login credentials

          expires_after: Represents an expiration policy for a store.

          metadata: Optional metadata key-value pairs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_identifier:
            raise ValueError(
                f"Expected a non-empty value for `vector_store_identifier` but received {vector_store_identifier!r}"
            )
        return await self._put(
            f"/v1/vector_stores/{vector_store_identifier}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "is_public": is_public,
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

    @typing_extensions.deprecated("deprecated")
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
    ) -> AsyncPaginator[VectorStore, AsyncCursor[VectorStore]]:
        """
        DEPRECATED: Use GET /stores instead

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
            "/v1/vector_stores",
            page=AsyncCursor[VectorStore],
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
                    vector_store_list_params.VectorStoreListParams,
                ),
            ),
            model=VectorStore,
        )

    @typing_extensions.deprecated("deprecated")
    async def delete(
        self,
        vector_store_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStoreDeleteResponse:
        """
        DEPRECATED: Use DELETE /stores/{store_identifier} instead

        Args:
          vector_store_identifier: The ID or name of the vector store to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_identifier:
            raise ValueError(
                f"Expected a non-empty value for `vector_store_identifier` but received {vector_store_identifier!r}"
            )
        return await self._delete(
            f"/v1/vector_stores/{vector_store_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreDeleteResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def question_answering(
        self,
        *,
        query: str | Omit = omit,
        vector_store_identifiers: SequenceNotStr[str],
        top_k: int | Omit = omit,
        filters: Optional[vector_store_question_answering_params.Filters] | Omit = omit,
        file_ids: Union[Iterable[object], SequenceNotStr[str], None] | Omit = omit,
        search_options: VectorStoreChunkSearchOptionsParam | Omit = omit,
        stream: bool | Omit = omit,
        qa_options: vector_store_question_answering_params.QaOptions | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStoreQuestionAnsweringResponse:
        """
        DEPRECATED: Use POST /stores/question-answering instead

        Args:
          query: Question to answer. If not provided, the question will be extracted from the
              passed messages.

          vector_store_identifiers: IDs or names of vector stores to search

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
            "/v1/vector_stores/question-answering",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "vector_store_identifiers": vector_store_identifiers,
                    "top_k": top_k,
                    "filters": filters,
                    "file_ids": file_ids,
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

    @typing_extensions.deprecated("deprecated")
    async def search(
        self,
        *,
        query: str,
        vector_store_identifiers: SequenceNotStr[str],
        top_k: int | Omit = omit,
        filters: Optional[vector_store_search_params.Filters] | Omit = omit,
        file_ids: Union[Iterable[object], SequenceNotStr[str], None] | Omit = omit,
        search_options: VectorStoreChunkSearchOptionsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStoreSearchResponse:
        """
        DEPRECATED: Use POST /stores/search instead

        Args:
          query: Search query text

          vector_store_identifiers: IDs or names of vector stores to search

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
            "/v1/vector_stores/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "vector_store_identifiers": vector_store_identifiers,
                    "top_k": top_k,
                    "filters": filters,
                    "file_ids": file_ids,
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

        self.create = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                vector_stores.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                vector_stores.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                vector_stores.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                vector_stores.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                vector_stores.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.question_answering = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                vector_stores.question_answering,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                vector_stores.search,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._vector_stores.files)


class AsyncVectorStoresResourceWithRawResponse:
    def __init__(self, vector_stores: AsyncVectorStoresResource) -> None:
        self._vector_stores = vector_stores

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                vector_stores.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                vector_stores.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                vector_stores.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                vector_stores.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                vector_stores.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.question_answering = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                vector_stores.question_answering,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                vector_stores.search,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._vector_stores.files)


class VectorStoresResourceWithStreamingResponse:
    def __init__(self, vector_stores: VectorStoresResource) -> None:
        self._vector_stores = vector_stores

        self.create = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                vector_stores.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                vector_stores.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                vector_stores.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                vector_stores.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                vector_stores.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.question_answering = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                vector_stores.question_answering,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                vector_stores.search,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._vector_stores.files)


class AsyncVectorStoresResourceWithStreamingResponse:
    def __init__(self, vector_stores: AsyncVectorStoresResource) -> None:
        self._vector_stores = vector_stores

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                vector_stores.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                vector_stores.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                vector_stores.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                vector_stores.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                vector_stores.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.question_answering = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                vector_stores.question_answering,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                vector_stores.search,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._vector_stores.files)
