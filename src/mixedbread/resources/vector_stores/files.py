# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import functools

import httpx

from ...lib import polling
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.vector_stores import file_list_params, file_create_params
from ...types.vector_stores.vector_store_file import VectorStoreFile
from ...types.vector_stores.file_list_response import FileListResponse
from ...types.vector_stores.vector_store_file_deleted import VectorStoreFileDeleted

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return FilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#with_streaming_response
        """
        return FilesResourceWithStreamingResponse(self)

    def create(
        self,
        vector_store_id: str,
        *,
        file_id: str,
        metadata: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreFile:
        """
        Upload a new file to a vector store for indexing.

        Args: vector_store_id: The ID of the vector store to upload to file: The file to
        upload and index

        Returns: VectorStoreFile: Details of the uploaded and indexed file

        Args:
          vector_store_id: The ID of the vector store

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return self._post(
            f"/v1/vector_stores/{vector_store_id}/files",
            body=maybe_transform(
                {
                    "file_id": file_id,
                    "metadata": metadata,
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
        vector_store_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreFile:
        """
        Get details of a specific file in a vector store.

        Args: vector_store_id: The ID of the vector store file_id: The ID of the file

        Returns: VectorStoreFile: Details of the vector store file

        Args:
          vector_store_id: The ID of the vector store

          file_id: The ID of the file

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._get(
            f"/v1/vector_stores/{vector_store_id}/files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreFile,
        )

    def list(
        self,
        vector_store_id: str,
        *,
        after: int | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileListResponse:
        """
        List files indexed in a vector store with pagination.

        Args: vector_store_id: The ID of the vector store pagination: Pagination
        parameters

        Returns: VectorStoreFileListResponse: Paginated list of vector store files

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
            f"/v1/vector_stores/{vector_store_id}/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            cast_to=FileListResponse,
        )

    def delete(
        self,
        file_id: str,
        *,
        vector_store_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreFileDeleted:
        """
        Delete a file from a vector store.

        Args: vector_store_id: The ID of the vector store file_id: The ID of the file to
        delete

        Returns: VectorStoreFileDeleted: The deleted file

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._delete(
            f"/v1/vector_stores/{vector_store_id}/files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreFileDeleted,
        )

    def poll(
        self,
        file_id: str,
        *,
        vector_store_id: str,
        poll_interval_ms: int | NotGiven = NOT_GIVEN,
        poll_timeout_ms: float | NotGiven = NOT_GIVEN,
    ) -> VectorStoreFileObject:
        """
        Poll for a file's status until it reaches a terminal state.

        Args:
            file_id: The ID of the file to poll
            vector_store_id: The ID of the vector store
            poll_interval_ms: The interval between polls in milliseconds
            poll_timeout_ms: The maximum time to poll for in milliseconds

        Returns:
            The file object once it reaches a terminal state
        """
        polling_interval_ms = poll_interval_ms or 500
        polling_timeout_ms = poll_timeout_ms or None

        return polling.poll(
            fn=functools.partial(self.retrieve, file_id, vector_store_id=vector_store_id),
            condition=lambda res: res.status == "successful" or res.status == "failed",
            interval_seconds=polling_interval_ms / 1000,
            timeout_seconds=polling_timeout_ms / 1000 if polling_timeout_ms else None,
        )

    def create_and_poll(
        self,
        file_id: str,
        *,
        vector_store_id: str,
        metadata: object,
        poll_interval_ms: int | NotGiven = NOT_GIVEN,
        poll_timeout_ms: float | NotGiven = NOT_GIVEN,
    ) -> VectorStoreFileObject:
        """
        Attach a file to the given vector store and wait for it to be processed.

        Args:
            file_id: The ID of the file to poll
            vector_store_id: The ID of the vector store
            metadata: The metadata to attach to the file
            poll_interval_ms: The interval between polls in milliseconds
            poll_timeout_ms: The maximum time to poll for in milliseconds
        Returns:
            The file object once it reaches a terminal state
        """
        self.create(vector_store_id=vector_store_id, file_id=file_id, metadata=metadata)

        return self.poll(
            file_id,
            vector_store_id=vector_store_id,
            poll_interval_ms=poll_interval_ms,
            poll_timeout_ms=poll_timeout_ms,
        )

    def upload(
        self,
        *,
        vector_store_id: str,
        file: FileTypes,
        metadata: object,
    ) -> VectorStoreFileObject:
        """Upload a file to the `files` API and then attach it to the given vector store.

        Note the file will be asynchronously processed (you can use the alternative
        polling helper method to wait for processing to complete).
        """
        file_obj = self._client.files.create(file=file)
        return self.create(vector_store_id=vector_store_id, file_id=file_obj.id, metadata=metadata)

    def upload_and_poll(
        self,
        *,
        vector_store_id: str,
        file: FileTypes,
        metadata: object,
        poll_interval_ms: int | NotGiven = NOT_GIVEN,
    ) -> VectorStoreFileObject:
        """Add a file to a vector store and poll until processing is complete."""
        file_obj = self._client.files.create(file=file)

        return self.create_and_poll(
            vector_store_id=vector_store_id,
            file_id=file_obj.id,
            metadata=metadata,
            poll_interval_ms=poll_interval_ms,
        )


class AsyncFilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#with_streaming_response
        """
        return AsyncFilesResourceWithStreamingResponse(self)

    async def create(
        self,
        vector_store_id: str,
        *,
        file_id: str,
        metadata: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreFile:
        """
        Upload a new file to a vector store for indexing.

        Args: vector_store_id: The ID of the vector store to upload to file: The file to
        upload and index

        Returns: VectorStoreFile: Details of the uploaded and indexed file

        Args:
          vector_store_id: The ID of the vector store

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        return await self._post(
            f"/v1/vector_stores/{vector_store_id}/files",
            body=await async_maybe_transform(
                {
                    "file_id": file_id,
                    "metadata": metadata,
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
        vector_store_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreFile:
        """
        Get details of a specific file in a vector store.

        Args: vector_store_id: The ID of the vector store file_id: The ID of the file

        Returns: VectorStoreFile: Details of the vector store file

        Args:
          vector_store_id: The ID of the vector store

          file_id: The ID of the file

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._get(
            f"/v1/vector_stores/{vector_store_id}/files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreFile,
        )

    async def list(
        self,
        vector_store_id: str,
        *,
        after: int | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileListResponse:
        """
        List files indexed in a vector store with pagination.

        Args: vector_store_id: The ID of the vector store pagination: Pagination
        parameters

        Returns: VectorStoreFileListResponse: Paginated list of vector store files

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
            f"/v1/vector_stores/{vector_store_id}/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            cast_to=FileListResponse,
        )

    async def delete(
        self,
        file_id: str,
        *,
        vector_store_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorStoreFileDeleted:
        """
        Delete a file from a vector store.

        Args: vector_store_id: The ID of the vector store file_id: The ID of the file to
        delete

        Returns: VectorStoreFileDeleted: The deleted file

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vector_store_id:
            raise ValueError(f"Expected a non-empty value for `vector_store_id` but received {vector_store_id!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._delete(
            f"/v1/vector_stores/{vector_store_id}/files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VectorStoreFileDeleted,
        )

    async def poll(
        self,
        file_id: str,
        *,
        vector_store_id: str,
        poll_interval_ms: int | NotGiven = NOT_GIVEN,
        poll_timeout_ms: float | NotGiven = NOT_GIVEN,
    ) -> VectorStoreFileObject:
        """
        Poll for a file's status until it reaches a terminal state.

        Args:
            file_id: The ID of the file to poll
            vector_store_id: The ID of the vector store
            poll_interval_ms: The interval between polls in milliseconds
            poll_timeout_ms: The maximum time to poll for in milliseconds

        Returns:
            The file object once it reaches a terminal state
        """
        polling_interval_ms = poll_interval_ms or 500
        polling_timeout_ms = poll_timeout_ms or None

        return await polling.poll_async(
            fn=functools.partial(self.retrieve, file_id, vector_store_id=vector_store_id),
            condition=lambda res: res.status == "successful" or res.status == "failed",
            interval_seconds=polling_interval_ms / 1000,
            timeout_seconds=polling_timeout_ms / 1000 if polling_timeout_ms else None,
        )

    async def create_and_poll(
        self,
        file_id: str,
        *,
        vector_store_id: str,
        metadata: object,
        poll_interval_ms: int | NotGiven = NOT_GIVEN,
        poll_timeout_ms: float | NotGiven = NOT_GIVEN,
    ) -> VectorStoreFileObject:
        """
        Attach a file to the given vector store and wait for it to be processed.

        Args:
            file_id: The ID of the file to poll
            vector_store_id: The ID of the vector store
            metadata: The metadata to attach to the file
            poll_interval_ms: The interval between polls in milliseconds
            poll_timeout_ms: The maximum time to poll for in milliseconds
        Returns:
            The file object once it reaches a terminal state
        """
        await self.create(vector_store_id=vector_store_id, file_id=file_id, metadata=metadata)

        return await self.poll(
            file_id,
            vector_store_id=vector_store_id,
            poll_interval_ms=poll_interval_ms,
            poll_timeout_ms=poll_timeout_ms,
        )

    async def upload(
        self,
        *,
        vector_store_id: str,
        file: FileTypes,
        metadata: object,
    ) -> VectorStoreFileObject:
        """Upload a file to the `files` API and then attach it to the given vector store.

        Note the file will be asynchronously processed (you can use the alternative
        polling helper method to wait for processing to complete).
        """
        file_obj = await self._client.files.create(file=file)
        return await self.create(vector_store_id=vector_store_id, file_id=file_obj.id, metadata=metadata)

    async def upload_and_poll(
        self,
        *,
        vector_store_id: str,
        file: FileTypes,
        metadata: object,
        poll_interval_ms: int | NotGiven = NOT_GIVEN,
    ) -> VectorStoreFileObject:
        """Add a file to a vector store and poll until processing is complete."""
        file_obj = await self._client.files.create(file=file)

        return await self.create_and_poll(
            vector_store_id=vector_store_id,
            file_id=file_obj.id,
            metadata=metadata,
            poll_interval_ms=poll_interval_ms,
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
