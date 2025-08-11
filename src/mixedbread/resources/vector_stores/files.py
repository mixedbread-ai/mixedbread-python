# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import functools
from typing import Any, List, Union, Iterable, Optional

import httpx

from ...lib import polling
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
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
from ...types.vector_stores import file_create_params, file_search_params, file_retrieve_params
from ...types.vector_stores.vector_store_file import VectorStoreFile
from ...types.vector_stores.file_delete_response import FileDeleteResponse
from ...types.vector_stores.file_search_response import FileSearchResponse

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
        file_id: str,
        metadata: object | NotGiven = NOT_GIVEN,
        experimental: file_create_params.Experimental | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreFile:
        """
        Upload a new file to a vector store for indexing.

        Args: vector_store_identifier: The ID or name of the vector store to upload to
        file: The file to upload and index

        Returns: VectorStoreFile: Details of the uploaded and indexed file

        Args:
          vector_store_identifier: The ID or name of the vector store

          file_id: ID of the file to add

          metadata: Optional metadata for the file

          experimental: Strategy for adding the file

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
                    "file_id": file_id,
                    "metadata": metadata,
                    "experimental": experimental,
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
        return_chunks: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        vector_store_identifiers: Optional[List[str]] | NotGiven = NOT_GIVEN,
        vector_store_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        filters: Optional[file_search_params.Filters] | NotGiven = NOT_GIVEN,
        file_ids: Union[Iterable[object], List[str], None] | NotGiven = NOT_GIVEN,
        search_options: file_search_params.SearchOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
                    "vector_store_ids": vector_store_ids,
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

    def poll(
        self,
        file_id: str,
        *,
        vector_store_identifier: str,
        poll_interval_ms: int | NotGiven = NOT_GIVEN,
        poll_timeout_ms: float | NotGiven = NOT_GIVEN,
        **kwargs: Any,
    ) -> VectorStoreFile:
        """
        Poll for a file's status until it reaches a terminal state.
        Args:
            file_id: The ID of the file to poll
            vector_store_identifier: The ID of the vector store
            poll_interval_ms: The interval between polls in milliseconds
            poll_timeout_ms: The maximum time to poll for in milliseconds
        Returns:
            The file object once it reaches a terminal state
        """
        polling_interval_ms = poll_interval_ms or 500
        polling_timeout_ms = poll_timeout_ms or None
        return polling.poll(
            fn=functools.partial(self.retrieve, file_id, vector_store_identifier=vector_store_identifier, **kwargs),
            condition=lambda res: res.status == "completed" or res.status == "failed" or res.status == "cancelled",
            interval_seconds=polling_interval_ms / 1000,
            timeout_seconds=polling_timeout_ms / 1000 if polling_timeout_ms else None,
        )

    def create_and_poll(
        self,
        file_id: str,
        *,
        vector_store_identifier: str,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        experimental: file_create_params.Experimental | NotGiven = NOT_GIVEN,
        poll_interval_ms: int | NotGiven = NOT_GIVEN,
        poll_timeout_ms: float | NotGiven = NOT_GIVEN,
        **kwargs: Any,
    ) -> VectorStoreFile:
        """
        Attach a file to the given vector store and wait for it to be processed.
        Args:
            file_id: The ID of the file to poll
            vector_store_identifier: The ID of the vector store
            metadata: The metadata to attach to the file
            poll_interval_ms: The interval between polls in milliseconds
            poll_timeout_ms: The maximum time to poll for in milliseconds
        Returns:
            The file object once it reaches a terminal state
        """
        self.create(
            vector_store_identifier=vector_store_identifier, file_id=file_id, metadata=metadata, experimental=experimental, **kwargs
        )
        return self.poll(
            file_id,
            vector_store_identifier=vector_store_identifier,
            poll_interval_ms=poll_interval_ms,
            poll_timeout_ms=poll_timeout_ms,
            **kwargs,
        )

    def upload(
        self,
        *,
        vector_store_identifier: str,
        file: FileTypes,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        experimental: file_create_params.Experimental | NotGiven = NOT_GIVEN,
        **kwargs: Any,
    ) -> VectorStoreFile:
        """Upload a file to the `files` API and then attach it to the given vector store.
        Note the file will be asynchronously processed (you can use the alternative
        polling helper method to wait for processing to complete).
        """
        file_obj = self._client.files.create(file=file, **kwargs)
        return self.create(
            vector_store_identifier=vector_store_identifier,
            file_id=file_obj.id,
            metadata=metadata,
            experimental=experimental,
            **kwargs,
        )

    def upload_and_poll(
        self,
        *,
        vector_store_identifier: str,
        file: FileTypes,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        experimental: file_create_params.Experimental | NotGiven = NOT_GIVEN,
        poll_interval_ms: int | NotGiven = NOT_GIVEN,
        poll_timeout_ms: float | NotGiven = NOT_GIVEN,
        **kwargs: Any,
    ) -> VectorStoreFile:
        """Add a file to a vector store and poll until processing is complete."""
        file_obj = self._client.files.create(file=file, **kwargs)
        return self.create_and_poll(
            vector_store_identifier=vector_store_identifier,
            file_id=file_obj.id,
            metadata=metadata,
            experimental=experimental,
            poll_interval_ms=poll_interval_ms,
            poll_timeout_ms=poll_timeout_ms,
            **kwargs,
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
        file_id: str,
        metadata: object | NotGiven = NOT_GIVEN,
        experimental: file_create_params.Experimental | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreFile:
        """
        Upload a new file to a vector store for indexing.

        Args: vector_store_identifier: The ID or name of the vector store to upload to
        file: The file to upload and index

        Returns: VectorStoreFile: Details of the uploaded and indexed file

        Args:
          vector_store_identifier: The ID or name of the vector store

          file_id: ID of the file to add

          metadata: Optional metadata for the file

          experimental: Strategy for adding the file

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
                    "file_id": file_id,
                    "metadata": metadata,
                    "experimental": experimental,
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
        return_chunks: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        vector_store_identifiers: Optional[List[str]] | NotGiven = NOT_GIVEN,
        vector_store_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        filters: Optional[file_search_params.Filters] | NotGiven = NOT_GIVEN,
        file_ids: Union[Iterable[object], List[str], None] | NotGiven = NOT_GIVEN,
        search_options: file_search_params.SearchOptions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
                    "vector_store_ids": vector_store_ids,
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

    async def poll(
        self,
        file_id: str,
        *,
        vector_store_identifier: str,
        poll_interval_ms: int | NotGiven = NOT_GIVEN,
        poll_timeout_ms: float | NotGiven = NOT_GIVEN,
        **kwargs: Any,
    ) -> VectorStoreFile:
        """
        Poll for a file's status until it reaches a terminal state.
        Args:
            file_id: The ID of the file to poll
            vector_store_identifier: The ID of the vector store
            poll_interval_ms: The interval between polls in milliseconds
            poll_timeout_ms: The maximum time to poll for in milliseconds
        Returns:
            The file object once it reaches a terminal state
        """
        polling_interval_ms = poll_interval_ms or 500
        polling_timeout_ms = poll_timeout_ms or None
        return await polling.poll_async(
            fn=functools.partial(self.retrieve, file_id, vector_store_identifier=vector_store_identifier, **kwargs),
            condition=lambda res: res.status == "completed" or res.status == "failed" or res.status == "cancelled",
            interval_seconds=polling_interval_ms / 1000,
            timeout_seconds=polling_timeout_ms / 1000 if polling_timeout_ms else None,
        )

    async def create_and_poll(
        self,
        file_id: str,
        *,
        vector_store_identifier: str,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        experimental: file_create_params.Experimental | NotGiven = NOT_GIVEN,
        poll_interval_ms: int | NotGiven = NOT_GIVEN,
        poll_timeout_ms: float | NotGiven = NOT_GIVEN,
        **kwargs: Any,
    ) -> VectorStoreFile:
        """
        Attach a file to the given vector store and wait for it to be processed.
        Args:
            file_id: The ID of the file to poll
            vector_store_identifier: The ID of the vector store
            metadata: The metadata to attach to the file
            poll_interval_ms: The interval between polls in milliseconds
            poll_timeout_ms: The maximum time to poll for in milliseconds
        Returns:
            The file object once it reaches a terminal state
        """
        await self.create(
            vector_store_identifier=vector_store_identifier,
            file_id=file_id,
            metadata=metadata,
            experimental=experimental,
            **kwargs,
        )
        return await self.poll(
            file_id,
            vector_store_identifier=vector_store_identifier,
            poll_interval_ms=poll_interval_ms,
            poll_timeout_ms=poll_timeout_ms,
            **kwargs,
        )

    async def upload(
        self,
        *,
        vector_store_identifier: str,
        file: FileTypes,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        experimental: file_create_params.Experimental | NotGiven = NOT_GIVEN,
        **kwargs: Any,
    ) -> VectorStoreFile:
        """Upload a file to the `files` API and then attach it to the given vector store.
        Note the file will be asynchronously processed (you can use the alternative
        polling helper method to wait for processing to complete).
        """
        file_obj = await self._client.files.create(file=file, **kwargs)
        return await self.create(
            vector_store_identifier=vector_store_identifier,
            file_id=file_obj.id,
            metadata=metadata,
            experimental=experimental,
            **kwargs,
        )

    async def upload_and_poll(
        self,
        *,
        vector_store_identifier: str,
        file: FileTypes,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        experimental: file_create_params.Experimental | NotGiven = NOT_GIVEN,
        poll_interval_ms: int | NotGiven = NOT_GIVEN,
        poll_timeout_ms: float | NotGiven = NOT_GIVEN,
        **kwargs: Any,
    ) -> VectorStoreFile:
        """Add a file to a vector store and poll until processing is complete."""
        file_obj = await self._client.files.create(file=file, **kwargs)
        return await self.create_and_poll(
            vector_store_identifier=vector_store_identifier,
            file_id=file_obj.id,
            metadata=metadata,
            experimental=experimental,
            poll_interval_ms=poll_interval_ms,
            poll_timeout_ms=poll_timeout_ms,
            **kwargs,
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
        self.delete = async_to_streamed_response_wrapper(
            files.delete,
        )
        self.search = async_to_streamed_response_wrapper(
            files.search,
        )
