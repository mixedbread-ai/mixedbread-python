# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.files import upload_create_params, upload_complete_params
from ..._base_client import make_request_options
from ...types.file_object import FileObject
from ...types.files.upload_list_response import UploadListResponse
from ...types.files.upload_abort_response import UploadAbortResponse
from ...types.files.upload_create_response import UploadCreateResponse
from ...types.files.upload_retrieve_response import UploadRetrieveResponse
from ...types.files.multipart_upload_part_param import MultipartUploadPartParam

__all__ = ["UploadsResource", "AsyncUploadsResource"]


class UploadsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return UploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return UploadsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        filename: str,
        file_size: int,
        mime_type: str,
        part_count: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadCreateResponse:
        """
        Initiate a multipart upload and receive presigned URLs for uploading parts
        directly to storage.

        Args:
          filename: Name of the file including extension

          file_size: Total size of the file in bytes

          mime_type: MIME type of the file

          part_count: Number of parts to split the upload into

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/files/uploads",
            body=maybe_transform(
                {
                    "filename": filename,
                    "file_size": file_size,
                    "mime_type": mime_type,
                    "part_count": part_count,
                },
                upload_create_params.UploadCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadCreateResponse,
        )

    def retrieve(
        self,
        upload_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadRetrieveResponse:
        """
        Get a multipart upload's details with fresh presigned URLs for any parts not yet
        uploaded.

        Args:
          upload_id: The ID of the multipart upload

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upload_id:
            raise ValueError(f"Expected a non-empty value for `upload_id` but received {upload_id!r}")
        return self._get(
            path_template("/v1/files/uploads/{upload_id}", upload_id=upload_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadRetrieveResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadListResponse:
        """List all in-progress multipart uploads for the authenticated organization."""
        return self._get(
            "/v1/files/uploads",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadListResponse,
        )

    def abort(
        self,
        upload_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadAbortResponse:
        """
        Abort a multipart upload and clean up any uploaded parts.

        Args:
          upload_id: The ID of the multipart upload to abort

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upload_id:
            raise ValueError(f"Expected a non-empty value for `upload_id` but received {upload_id!r}")
        return self._post(
            path_template("/v1/files/uploads/{upload_id}/abort", upload_id=upload_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadAbortResponse,
        )

    def complete(
        self,
        upload_id: str,
        *,
        parts: Iterable[MultipartUploadPartParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileObject:
        """Complete a multipart upload after all parts have been uploaded.

        Creates the file
        object and returns it.

        Args:
          upload_id: The ID of the multipart upload

          parts: List of completed parts with their ETags

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upload_id:
            raise ValueError(f"Expected a non-empty value for `upload_id` but received {upload_id!r}")
        return self._post(
            path_template("/v1/files/uploads/{upload_id}/complete", upload_id=upload_id),
            body=maybe_transform({"parts": parts}, upload_complete_params.UploadCompleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileObject,
        )


class AsyncUploadsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return AsyncUploadsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        filename: str,
        file_size: int,
        mime_type: str,
        part_count: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadCreateResponse:
        """
        Initiate a multipart upload and receive presigned URLs for uploading parts
        directly to storage.

        Args:
          filename: Name of the file including extension

          file_size: Total size of the file in bytes

          mime_type: MIME type of the file

          part_count: Number of parts to split the upload into

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/files/uploads",
            body=await async_maybe_transform(
                {
                    "filename": filename,
                    "file_size": file_size,
                    "mime_type": mime_type,
                    "part_count": part_count,
                },
                upload_create_params.UploadCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadCreateResponse,
        )

    async def retrieve(
        self,
        upload_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadRetrieveResponse:
        """
        Get a multipart upload's details with fresh presigned URLs for any parts not yet
        uploaded.

        Args:
          upload_id: The ID of the multipart upload

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upload_id:
            raise ValueError(f"Expected a non-empty value for `upload_id` but received {upload_id!r}")
        return await self._get(
            path_template("/v1/files/uploads/{upload_id}", upload_id=upload_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadRetrieveResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadListResponse:
        """List all in-progress multipart uploads for the authenticated organization."""
        return await self._get(
            "/v1/files/uploads",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadListResponse,
        )

    async def abort(
        self,
        upload_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadAbortResponse:
        """
        Abort a multipart upload and clean up any uploaded parts.

        Args:
          upload_id: The ID of the multipart upload to abort

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upload_id:
            raise ValueError(f"Expected a non-empty value for `upload_id` but received {upload_id!r}")
        return await self._post(
            path_template("/v1/files/uploads/{upload_id}/abort", upload_id=upload_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadAbortResponse,
        )

    async def complete(
        self,
        upload_id: str,
        *,
        parts: Iterable[MultipartUploadPartParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileObject:
        """Complete a multipart upload after all parts have been uploaded.

        Creates the file
        object and returns it.

        Args:
          upload_id: The ID of the multipart upload

          parts: List of completed parts with their ETags

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upload_id:
            raise ValueError(f"Expected a non-empty value for `upload_id` but received {upload_id!r}")
        return await self._post(
            path_template("/v1/files/uploads/{upload_id}/complete", upload_id=upload_id),
            body=await async_maybe_transform({"parts": parts}, upload_complete_params.UploadCompleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileObject,
        )


class UploadsResourceWithRawResponse:
    def __init__(self, uploads: UploadsResource) -> None:
        self._uploads = uploads

        self.create = to_raw_response_wrapper(
            uploads.create,
        )
        self.retrieve = to_raw_response_wrapper(
            uploads.retrieve,
        )
        self.list = to_raw_response_wrapper(
            uploads.list,
        )
        self.abort = to_raw_response_wrapper(
            uploads.abort,
        )
        self.complete = to_raw_response_wrapper(
            uploads.complete,
        )


class AsyncUploadsResourceWithRawResponse:
    def __init__(self, uploads: AsyncUploadsResource) -> None:
        self._uploads = uploads

        self.create = async_to_raw_response_wrapper(
            uploads.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            uploads.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            uploads.list,
        )
        self.abort = async_to_raw_response_wrapper(
            uploads.abort,
        )
        self.complete = async_to_raw_response_wrapper(
            uploads.complete,
        )


class UploadsResourceWithStreamingResponse:
    def __init__(self, uploads: UploadsResource) -> None:
        self._uploads = uploads

        self.create = to_streamed_response_wrapper(
            uploads.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            uploads.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            uploads.list,
        )
        self.abort = to_streamed_response_wrapper(
            uploads.abort,
        )
        self.complete = to_streamed_response_wrapper(
            uploads.complete,
        )


class AsyncUploadsResourceWithStreamingResponse:
    def __init__(self, uploads: AsyncUploadsResource) -> None:
        self._uploads = uploads

        self.create = async_to_streamed_response_wrapper(
            uploads.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            uploads.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            uploads.list,
        )
        self.abort = async_to_streamed_response_wrapper(
            uploads.abort,
        )
        self.complete = async_to_streamed_response_wrapper(
            uploads.complete,
        )
