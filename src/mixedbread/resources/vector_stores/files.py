# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional

import httpx

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
from ..._base_client import make_request_options
from ...types.vector_stores import file_list_params, file_create_params, file_search_params, file_retrieve_params
from ...types.vector_stores.vector_store_file import VectorStoreFile
from ...types.vector_stores.file_list_response import FileListResponse
from ...types.vector_stores.file_delete_response import FileDeleteResponse
from ...types.vector_stores.file_search_response import FileSearchResponse
from ...types.vector_stores.vector_store_file_status import VectorStoreFileStatus

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return FilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return FilesResourceWithStreamingResponse(self)

    def create(
        self,
        vector_store_identifier: str,
        *,
        metadata: object | Omit = omit,
        experimental: file_create_params.Experimental | Omit = omit,
        file_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStoreFile:
        """
        Add an already uploaded file to a vector store.

        Args: vector_store_identifier: The ID or name of the vector store to add the
        file to file: The file to add and index

        Returns: VectorStoreFile: Details of the added and indexed file

        Args:
          vector_store_identifier: The ID or name of the vector store

          metadata: Optional metadata for the file

          experimental: Strategy for adding the file

          file_id: ID of the file to add

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_identifier:
            raise ValueError(
                f"Expected a non-empty value for `vector_store_identifier` but received {vector_store_identifier!r}"
            )
        return self._post(
            f"/v1/vector_stores/{vector_store_identifier}/files",
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "experimental": experimental,
                    "file_id": file_id,
                },
                file_create_params.FileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreFile,
        )

    def retrieve(
        self,
        file_id: str,
        *,
        vector_store_identifier: str,
        return_chunks: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStoreFile:
        """
        Get details of a specific file in a vector store.

        Args: vector_store_identifier: The ID or name of the vector store file_id: The
        ID of the file

        Returns: VectorStoreFile: Details of the vector store file

        Args:
          vector_store_identifier: The ID or name of the vector store

          file_id: The ID of the file

          return_chunks: Whether to return the chunks for the file

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_identifier:
            raise ValueError(
                f"Expected a non-empty value for `vector_store_identifier` but received {vector_store_identifier!r}"
            )
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._get(
            f"/v1/vector_stores/{vector_store_identifier}/files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"return_chunks": return_chunks}, file_retrieve_params.FileRetrieveParams),
            ),
            cast_to=VectorStoreFile,
        )

    def list(
        self,
        vector_store_identifier: str,
        *,
        limit: int | Omit = omit,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        include_total: bool | Omit = omit,
        statuses: Optional[List[VectorStoreFileStatus]] | Omit = omit,
        metadata_filter: Optional[file_list_params.MetadataFilter] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileListResponse:
        """
        List files indexed in a vector store with pagination and metadata filter.

        Args: vector_store_identifier: The ID or name of the vector store pagination:
        Pagination parameters and metadata filter

        Returns: VectorStoreFileListResponse: Paginated list of vector store files

        Args:
          vector_store_identifier: The ID or name of the vector store

          limit: Maximum number of items to return per page (1-100)

          after: Cursor for forward pagination - get items after this position. Use last_cursor
              from previous response.

          before: Cursor for backward pagination - get items before this position. Use
              first_cursor from previous response.

          include_total: Whether to include total count in response (expensive operation)

          statuses: Status to filter by

          metadata_filter: Metadata filter to apply to the query

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_identifier:
            raise ValueError(
                f"Expected a non-empty value for `vector_store_identifier` but received {vector_store_identifier!r}"
            )
        return self._post(
            f"/v1/vector_stores/{vector_store_identifier}/files/list",
            body=maybe_transform(
                {
                    "limit": limit,
                    "after": after,
                    "before": before,
                    "include_total": include_total,
                    "statuses": statuses,
                    "metadata_filter": metadata_filter,
                },
                file_list_params.FileListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileListResponse,
        )

    def delete(
        self,
        file_id: str,
        *,
        vector_store_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileDeleteResponse:
        """
        Delete a file from a vector store.

        Args: vector_store_identifier: The ID or name of the vector store file_id: The
        ID of the file to delete

        Returns: VectorStoreFileDeleted: The deleted file

        Args:
          vector_store_identifier: The ID or name of the vector store

          file_id: The ID of the file to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_identifier:
            raise ValueError(
                f"Expected a non-empty value for `vector_store_identifier` but received {vector_store_identifier!r}"
            )
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._delete(
            f"/v1/vector_stores/{vector_store_identifier}/files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileDeleteResponse,
        )

    def search(
        self,
        *,
        query: str,
        vector_store_identifiers: SequenceNotStr[str],
        top_k: int | Omit = omit,
        filters: Optional[file_search_params.Filters] | Omit = omit,
        file_ids: Union[Iterable[object], SequenceNotStr[str], None] | Omit = omit,
        search_options: file_search_params.SearchOptions | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileSearchResponse:
        """
        Perform semantic search across complete vector store files.

        This endpoint searches through vector store files using semantic similarity
        matching. Unlike chunk search, it returns complete matching files rather than
        individual chunks. Supports complex search queries with filters and returns
        relevance-scored results.

        Args: search_params: Search configuration including: - query text or
        embeddings - metadata filters - pagination parameters - sorting preferences
        \\__state: API state dependency \\__ctx: Service context dependency

        Returns: VectorStoreSearchFileResponse containing: - List of matched files with
        relevance scores - Pagination details including total result count

        Raises: HTTPException (400): If search parameters are invalid HTTPException
        (404): If no vector stores are found to search

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
            "/v1/vector_stores/files/search",
            body=maybe_transform(
                {
                    "query": query,
                    "vector_store_identifiers": vector_store_identifiers,
                    "top_k": top_k,
                    "filters": filters,
                    "file_ids": file_ids,
                    "search_options": search_options,
                },
                file_search_params.FileSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileSearchResponse,
        )


class AsyncFilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return AsyncFilesResourceWithStreamingResponse(self)

    async def create(
        self,
        vector_store_identifier: str,
        *,
        metadata: object | Omit = omit,
        experimental: file_create_params.Experimental | Omit = omit,
        file_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStoreFile:
        """
        Add an already uploaded file to a vector store.

        Args: vector_store_identifier: The ID or name of the vector store to add the
        file to file: The file to add and index

        Returns: VectorStoreFile: Details of the added and indexed file

        Args:
          vector_store_identifier: The ID or name of the vector store

          metadata: Optional metadata for the file

          experimental: Strategy for adding the file

          file_id: ID of the file to add

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_identifier:
            raise ValueError(
                f"Expected a non-empty value for `vector_store_identifier` but received {vector_store_identifier!r}"
            )
        return await self._post(
            f"/v1/vector_stores/{vector_store_identifier}/files",
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "experimental": experimental,
                    "file_id": file_id,
                },
                file_create_params.FileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreFile,
        )

    async def retrieve(
        self,
        file_id: str,
        *,
        vector_store_identifier: str,
        return_chunks: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VectorStoreFile:
        """
        Get details of a specific file in a vector store.

        Args: vector_store_identifier: The ID or name of the vector store file_id: The
        ID of the file

        Returns: VectorStoreFile: Details of the vector store file

        Args:
          vector_store_identifier: The ID or name of the vector store

          file_id: The ID of the file

          return_chunks: Whether to return the chunks for the file

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_identifier:
            raise ValueError(
                f"Expected a non-empty value for `vector_store_identifier` but received {vector_store_identifier!r}"
            )
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._get(
            f"/v1/vector_stores/{vector_store_identifier}/files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"return_chunks": return_chunks}, file_retrieve_params.FileRetrieveParams
                ),
            ),
            cast_to=VectorStoreFile,
        )

    async def list(
        self,
        vector_store_identifier: str,
        *,
        limit: int | Omit = omit,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        include_total: bool | Omit = omit,
        statuses: Optional[List[VectorStoreFileStatus]] | Omit = omit,
        metadata_filter: Optional[file_list_params.MetadataFilter] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileListResponse:
        """
        List files indexed in a vector store with pagination and metadata filter.

        Args: vector_store_identifier: The ID or name of the vector store pagination:
        Pagination parameters and metadata filter

        Returns: VectorStoreFileListResponse: Paginated list of vector store files

        Args:
          vector_store_identifier: The ID or name of the vector store

          limit: Maximum number of items to return per page (1-100)

          after: Cursor for forward pagination - get items after this position. Use last_cursor
              from previous response.

          before: Cursor for backward pagination - get items before this position. Use
              first_cursor from previous response.

          include_total: Whether to include total count in response (expensive operation)

          statuses: Status to filter by

          metadata_filter: Metadata filter to apply to the query

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_identifier:
            raise ValueError(
                f"Expected a non-empty value for `vector_store_identifier` but received {vector_store_identifier!r}"
            )
        return await self._post(
            f"/v1/vector_stores/{vector_store_identifier}/files/list",
            body=await async_maybe_transform(
                {
                    "limit": limit,
                    "after": after,
                    "before": before,
                    "include_total": include_total,
                    "statuses": statuses,
                    "metadata_filter": metadata_filter,
                },
                file_list_params.FileListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileListResponse,
        )

    async def delete(
        self,
        file_id: str,
        *,
        vector_store_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileDeleteResponse:
        """
        Delete a file from a vector store.

        Args: vector_store_identifier: The ID or name of the vector store file_id: The
        ID of the file to delete

        Returns: VectorStoreFileDeleted: The deleted file

        Args:
          vector_store_identifier: The ID or name of the vector store

          file_id: The ID of the file to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_identifier:
            raise ValueError(
                f"Expected a non-empty value for `vector_store_identifier` but received {vector_store_identifier!r}"
            )
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._delete(
            f"/v1/vector_stores/{vector_store_identifier}/files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileDeleteResponse,
        )

    async def search(
        self,
        *,
        query: str,
        vector_store_identifiers: SequenceNotStr[str],
        top_k: int | Omit = omit,
        filters: Optional[file_search_params.Filters] | Omit = omit,
        file_ids: Union[Iterable[object], SequenceNotStr[str], None] | Omit = omit,
        search_options: file_search_params.SearchOptions | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileSearchResponse:
        """
        Perform semantic search across complete vector store files.

        This endpoint searches through vector store files using semantic similarity
        matching. Unlike chunk search, it returns complete matching files rather than
        individual chunks. Supports complex search queries with filters and returns
        relevance-scored results.

        Args: search_params: Search configuration including: - query text or
        embeddings - metadata filters - pagination parameters - sorting preferences
        \\__state: API state dependency \\__ctx: Service context dependency

        Returns: VectorStoreSearchFileResponse containing: - List of matched files with
        relevance scores - Pagination details including total result count

        Raises: HTTPException (400): If search parameters are invalid HTTPException
        (404): If no vector stores are found to search

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
            "/v1/vector_stores/files/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "vector_store_identifiers": vector_store_identifiers,
                    "top_k": top_k,
                    "filters": filters,
                    "file_ids": file_ids,
                    "search_options": search_options,
                },
                file_search_params.FileSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileSearchResponse,
        )


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.create = to_raw_response_wrapper(
            files.create,
        )
        self.retrieve = to_raw_response_wrapper(
            files.retrieve,
        )
        self.list = to_raw_response_wrapper(
            files.list,
        )
        self.delete = to_raw_response_wrapper(
            files.delete,
        )
        self.search = to_raw_response_wrapper(
            files.search,
        )


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.create = async_to_raw_response_wrapper(
            files.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            files.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            files.list,
        )
        self.delete = async_to_raw_response_wrapper(
            files.delete,
        )
        self.search = async_to_raw_response_wrapper(
            files.search,
        )


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.create = to_streamed_response_wrapper(
            files.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            files.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            files.list,
        )
        self.delete = to_streamed_response_wrapper(
            files.delete,
        )
        self.search = to_streamed_response_wrapper(
            files.search,
        )


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.create = async_to_streamed_response_wrapper(
            files.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            files.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            files.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            files.delete,
        )
        self.search = async_to_streamed_response_wrapper(
            files.search,
        )
