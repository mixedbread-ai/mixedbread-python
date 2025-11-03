# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import functools
from typing import Any, List, Union, Iterable, Optional

import httpx

from ...lib import polling
from ..._types import Body, FileTypes, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.stores import file_list_params, file_create_params, file_search_params
from ...types.stores.store_file import StoreFile
from ...types.stores.store_file_status import StoreFileStatus
from ...types.stores.file_list_response import FileListResponse
from ...types.stores.file_delete_response import FileDeleteResponse
from ...types.stores.file_search_response import FileSearchResponse

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
        store_identifier: str,
        *,
        metadata: object | Omit = omit,
        config: file_create_params.Config | Omit = omit,
        external_id: Optional[str] | Omit = omit,
        overwrite: bool | Omit = omit,
        file_id: str,
        experimental: Optional[file_create_params.Experimental] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoreFile:
        """Upload a file to a store.

        Args: store_identifier: The ID or name of the store.

        file_add_params: The file
        to add to the store.

        Returns: VectorStoreFile: The uploaded file details.

        Args:
          store_identifier: The ID or name of the store

          metadata: Optional metadata for the file

          config: Configuration for adding the file

          external_id: External identifier for this file in the store

          overwrite: If true, overwrite an existing file with the same external_id

          file_id: ID of the file to add

          experimental: Configuration for a file.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not store_identifier:
            raise ValueError(f"Expected a non-empty value for `store_identifier` but received {store_identifier!r}")
        return self._post(
            f"/v1/stores/{store_identifier}/files",
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "config": config,
                    "external_id": external_id,
                    "overwrite": overwrite,
                    "file_id": file_id,
                    "experimental": experimental,
                },
                file_create_params.FileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoreFile,
        )

    def list(
        self,
        store_identifier: str,
        *,
        limit: int | Omit = omit,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        include_total: bool | Omit = omit,
        statuses: Optional[List[StoreFileStatus]] | Omit = omit,
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
          store_identifier: The ID or name of the store

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
        if not store_identifier:
            raise ValueError(f"Expected a non-empty value for `store_identifier` but received {store_identifier!r}")
        return self._post(
            f"/v1/stores/{store_identifier}/files/list",
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
        store_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileDeleteResponse:
        """Delete a file from a store.

        Args: store_identifier: The ID or name of the store.

        file_id: The ID or name of
        the file to delete.

        Returns: VectorStoreFileDeleted: The deleted file details.

        Args:
          store_identifier: The ID or name of the store

          file_id: The ID or name of the file to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not store_identifier:
            raise ValueError(f"Expected a non-empty value for `store_identifier` but received {store_identifier!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._delete(
            f"/v1/stores/{store_identifier}/files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileDeleteResponse,
        )

    def search(
        self,
        *,
        query: str,
        store_identifiers: SequenceNotStr[str],
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
        Search for files within a store based on semantic similarity.

        Args: store_identifier: The ID or name of the store to search within
        search_params: Search configuration including query text, pagination, and
        filters

        Returns: StoreFileSearchResponse: List of matching files with relevance scores

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
            "/v1/stores/files/search",
            body=maybe_transform(
                {
                    "query": query,
                    "store_identifiers": store_identifiers,
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
        store_identifier: str,
        poll_interval_ms: int | NotGiven = not_given,
        poll_timeout_ms: float | NotGiven = not_given,
        **kwargs: Any,
    ) -> StoreFile:
        """
        Poll for a file's status until it reaches a terminal state.
        Args:
            file_id: The ID of the file to poll
            store_identifier: The ID of the store
            poll_interval_ms: The interval between polls in milliseconds
            poll_timeout_ms: The maximum time to poll for in milliseconds
        Returns:
            The file object once it reaches a terminal state
        """
        polling_interval_ms = poll_interval_ms or 500
        polling_timeout_ms = poll_timeout_ms or None
        return polling.poll(
            fn=functools.partial(self.retrieve, file_id, store_identifier=store_identifier, **kwargs),
            condition=lambda res: res.status == "completed" or res.status == "failed" or res.status == "cancelled",
            interval_seconds=polling_interval_ms / 1000,
            timeout_seconds=polling_timeout_ms / 1000 if polling_timeout_ms else None,
        )

    def create_and_poll(
        self,
        file_id: str,
        *,
        store_identifier: str,
        metadata: Optional[object] | NotGiven = not_given,
        experimental: file_create_params.Experimental | Omit = omit,
        poll_interval_ms: int | NotGiven = not_given,
        poll_timeout_ms: float | NotGiven = not_given,
        **kwargs: Any,
    ) -> StoreFile:
        """
        Attach a file to the given store and wait for it to be processed.
        Args:
            file_id: The ID of the file to poll
            store_identifier: The ID of the store
            metadata: The metadata to attach to the file
            poll_interval_ms: The interval between polls in milliseconds
            poll_timeout_ms: The maximum time to poll for in milliseconds
        Returns:
            The file object once it reaches a terminal state
        """
        self.create(
            store_identifier=store_identifier, file_id=file_id, metadata=metadata, experimental=experimental, **kwargs
        )
        return self.poll(
            file_id,
            store_identifier=store_identifier,
            poll_interval_ms=poll_interval_ms,
            poll_timeout_ms=poll_timeout_ms,
            **kwargs,
        )

    def upload(
        self,
        *,
        store_identifier: str,
        file: FileTypes,
        metadata: Optional[object] | Omit = omit,
        experimental: file_create_params.Experimental | Omit = omit,
        **kwargs: Any,
    ) -> StoreFile:
        """Upload a file to the `files` API and then attach it to the given store.
        Note the file will be asynchronously processed (you can use the alternative
        polling helper method to wait for processing to complete).
        """
        file_obj = self._client.files.create(file=file, **kwargs)
        return self.create(
            store_identifier=store_identifier,
            file_id=file_obj.id,
            metadata=metadata,
            experimental=experimental,
            **kwargs,
        )

    def upload_and_poll(
        self,
        *,
        store_identifier: str,
        file: FileTypes,
        metadata: Optional[object] | NotGiven = not_given,
        experimental: file_create_params.Experimental | Omit = omit,
        poll_interval_ms: int | NotGiven = not_given,
        poll_timeout_ms: float | NotGiven = not_given,
        **kwargs: Any,
    ) -> StoreFile:
        """Add a file to a store and poll until processing is complete."""
        file_obj = self._client.files.create(file=file, **kwargs)
        return self.create_and_poll(
            store_identifier=store_identifier,
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
        store_identifier: str,
        *,
        metadata: object | Omit = omit,
        config: file_create_params.Config | Omit = omit,
        external_id: Optional[str] | Omit = omit,
        overwrite: bool | Omit = omit,
        file_id: str,
        experimental: Optional[file_create_params.Experimental] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoreFile:
        """Upload a file to a store.

        Args: store_identifier: The ID or name of the store.

        file_add_params: The file
        to add to the store.

        Returns: VectorStoreFile: The uploaded file details.

        Args:
          store_identifier: The ID or name of the store

          metadata: Optional metadata for the file

          config: Configuration for adding the file

          external_id: External identifier for this file in the store

          overwrite: If true, overwrite an existing file with the same external_id

          file_id: ID of the file to add

          experimental: Configuration for a file.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not store_identifier:
            raise ValueError(f"Expected a non-empty value for `store_identifier` but received {store_identifier!r}")
        return await self._post(
            f"/v1/stores/{store_identifier}/files",
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "config": config,
                    "external_id": external_id,
                    "overwrite": overwrite,
                    "file_id": file_id,
                    "experimental": experimental,
                },
                file_create_params.FileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoreFile,
        )

    async def list(
        self,
        store_identifier: str,
        *,
        limit: int | Omit = omit,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        include_total: bool | Omit = omit,
        statuses: Optional[List[StoreFileStatus]] | Omit = omit,
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
          store_identifier: The ID or name of the store

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
        if not store_identifier:
            raise ValueError(f"Expected a non-empty value for `store_identifier` but received {store_identifier!r}")
        return await self._post(
            f"/v1/stores/{store_identifier}/files/list",
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
        store_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileDeleteResponse:
        """Delete a file from a store.

        Args: store_identifier: The ID or name of the store.

        file_id: The ID or name of
        the file to delete.

        Returns: VectorStoreFileDeleted: The deleted file details.

        Args:
          store_identifier: The ID or name of the store

          file_id: The ID or name of the file to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not store_identifier:
            raise ValueError(f"Expected a non-empty value for `store_identifier` but received {store_identifier!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._delete(
            f"/v1/stores/{store_identifier}/files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileDeleteResponse,
        )

    async def search(
        self,
        *,
        query: str,
        store_identifiers: SequenceNotStr[str],
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
        Search for files within a store based on semantic similarity.

        Args: store_identifier: The ID or name of the store to search within
        search_params: Search configuration including query text, pagination, and
        filters

        Returns: StoreFileSearchResponse: List of matching files with relevance scores

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
            "/v1/stores/files/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "store_identifiers": store_identifiers,
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
        store_identifier: str,
        poll_interval_ms: int | NotGiven = not_given,
        poll_timeout_ms: float | NotGiven = not_given,
        **kwargs: Any,
    ) -> StoreFile:
        """
        Poll for a file's status until it reaches a terminal state.
        Args:
            file_id: The ID of the file to poll
            store_identifier: The ID of the store
            poll_interval_ms: The interval between polls in milliseconds
            poll_timeout_ms: The maximum time to poll for in milliseconds
        Returns:
            The file object once it reaches a terminal state
        """
        polling_interval_ms = poll_interval_ms or 500
        polling_timeout_ms = poll_timeout_ms or None
        return await polling.poll_async(
            fn=functools.partial(self.retrieve, file_id, store_identifier=store_identifier, **kwargs),
            condition=lambda res: res.status == "completed" or res.status == "failed" or res.status == "cancelled",
            interval_seconds=polling_interval_ms / 1000,
            timeout_seconds=polling_timeout_ms / 1000 if polling_timeout_ms else None,
        )

    async def create_and_poll(
        self,
        file_id: str,
        *,
        store_identifier: str,
        metadata: Optional[object] | NotGiven = not_given,
        experimental: file_create_params.Experimental | Omit = omit,
        poll_interval_ms: int | NotGiven = not_given,
        poll_timeout_ms: float | NotGiven = not_given,
        **kwargs: Any,
    ) -> StoreFile:
        """
        Attach a file to the given vector store and wait for it to be processed.
        Args:
            file_id: The ID of the file to poll
            store_identifier: The ID of the store
            metadata: The metadata to attach to the file
            poll_interval_ms: The interval between polls in milliseconds
            poll_timeout_ms: The maximum time to poll for in milliseconds
        Returns:
            The file object once it reaches a terminal state
        """
        await self.create(
            store_identifier=store_identifier,
            file_id=file_id,
            metadata=metadata,
            experimental=experimental,
            **kwargs,
        )
        return await self.poll(
            file_id,
            store_identifier=store_identifier,
            poll_interval_ms=poll_interval_ms,
            poll_timeout_ms=poll_timeout_ms,
            **kwargs,
        )

    async def upload(
        self,
        *,
        store_identifier: str,
        file: FileTypes,
        metadata: Optional[object] | NotGiven = not_given,
        experimental: file_create_params.Experimental | Omit = omit,
        **kwargs: Any,
    ) -> StoreFile:
        """Upload a file to the `files` API and then attach it to the given vector store.
        Note the file will be asynchronously processed (you can use the alternative
        polling helper method to wait for processing to complete).
        """
        file_obj = await self._client.files.create(file=file, **kwargs)
        return await self.create(
            store_identifier=store_identifier,
            file_id=file_obj.id,
            metadata=metadata,
            experimental=experimental,
            **kwargs,
        )

    async def upload_and_poll(
        self,
        *,
        store_identifier: str,
        file: FileTypes,
        metadata: Optional[object] | NotGiven = not_given,
        experimental: file_create_params.Experimental | Omit = omit,
        poll_interval_ms: int | NotGiven = not_given,
        poll_timeout_ms: float | NotGiven = not_given,
        **kwargs: Any,
    ) -> StoreFile:
        """Add a file to a store and poll until processing is complete."""
        file_obj = await self._client.files.create(file=file, **kwargs)
        return await self.create_and_poll(
            store_identifier=store_identifier,
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
        self.list = async_to_streamed_response_wrapper(
            files.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            files.delete,
        )
        self.search = async_to_streamed_response_wrapper(
            files.search,
        )
