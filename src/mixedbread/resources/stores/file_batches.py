# File generated from our OpenAPI spec by sdkgen. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.stores import file_batch_create_params
from ...lib.file_batches import FileBatchHelpers, AsyncFileBatchHelpers
from ...types.stores.store_file_batch import StoreFileBatch

__all__ = ["FileBatchesResource", "AsyncFileBatchesResource"]


class FileBatchesResourceBase(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FileBatchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return FileBatchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FileBatchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return FileBatchesResourceWithStreamingResponse(self)

    def create(
        self,
        store_identifier: str,
        *,
        files: Iterable[file_batch_create_params.File],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoreFileBatch:
        """Add already uploaded files to a store in one call, for backfills.

        Files are ingested with no latency guarantee.

        Each item takes one token from a
        rate limit of its own, at the same limits as file uploads. A file already in the
        store (same file ID or external ID) that is pending, in progress or completed is
        never replaced and comes back with `store_file_already_exists_error`; a failed
        or cancelled one is replaced, so resending a batch retries its failures. To
        update a file, use the single-file endpoint. Each item is checked on its own:
        one rejected item is reported in `data` without failing the others.

        Args:
          store_identifier: The ID or name of the store

          files: Files to add

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not store_identifier:
            raise ValueError(f"Expected a non-empty value for `store_identifier` but received {store_identifier!r}")
        return self._post(
            path_template("/v1/stores/{store_identifier}/file_batches", store_identifier=store_identifier),
            body=maybe_transform({"files": files}, file_batch_create_params.FileBatchCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoreFileBatch,
        )


class AsyncFileBatchesResourceBase(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFileBatchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFileBatchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFileBatchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return AsyncFileBatchesResourceWithStreamingResponse(self)

    async def create(
        self,
        store_identifier: str,
        *,
        files: Iterable[file_batch_create_params.File],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoreFileBatch:
        """Add already uploaded files to a store in one call, for backfills.

        Files are ingested with no latency guarantee.

        Each item takes one token from a
        rate limit of its own, at the same limits as file uploads. A file already in the
        store (same file ID or external ID) that is pending, in progress or completed is
        never replaced and comes back with `store_file_already_exists_error`; a failed
        or cancelled one is replaced, so resending a batch retries its failures. To
        update a file, use the single-file endpoint. Each item is checked on its own:
        one rejected item is reported in `data` without failing the others.

        Args:
          store_identifier: The ID or name of the store

          files: Files to add

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not store_identifier:
            raise ValueError(f"Expected a non-empty value for `store_identifier` but received {store_identifier!r}")
        return await self._post(
            path_template("/v1/stores/{store_identifier}/file_batches", store_identifier=store_identifier),
            body=await async_maybe_transform({"files": files}, file_batch_create_params.FileBatchCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoreFileBatch,
        )


class FileBatchesResource(FileBatchHelpers, FileBatchesResourceBase):
    pass


class AsyncFileBatchesResource(AsyncFileBatchHelpers, AsyncFileBatchesResourceBase):
    pass


class FileBatchesResourceWithRawResponse:
    def __init__(self, file_batches: FileBatchesResourceBase) -> None:
        self._file_batches = file_batches

        self.create = to_raw_response_wrapper(
            file_batches.create,
        )


class AsyncFileBatchesResourceWithRawResponse:
    def __init__(self, file_batches: AsyncFileBatchesResourceBase) -> None:
        self._file_batches = file_batches

        self.create = async_to_raw_response_wrapper(
            file_batches.create,
        )


class FileBatchesResourceWithStreamingResponse:
    def __init__(self, file_batches: FileBatchesResourceBase) -> None:
        self._file_batches = file_batches

        self.create = to_streamed_response_wrapper(
            file_batches.create,
        )


class AsyncFileBatchesResourceWithStreamingResponse:
    def __init__(self, file_batches: AsyncFileBatchesResourceBase) -> None:
        self._file_batches = file_batches

        self.create = async_to_streamed_response_wrapper(
            file_batches.create,
        )
