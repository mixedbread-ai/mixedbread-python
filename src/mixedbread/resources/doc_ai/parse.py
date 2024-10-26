# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from ..._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
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
from ...types.doc_ai import parse_create_job_params
from ...types.doc_ai.parse_response import ParseResponse

__all__ = ["ParseResource", "AsyncParseResource"]


class ParseResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ParseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return ParseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ParseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#with_streaming_response
        """
        return ParseResourceWithStreamingResponse(self)

    def create_job(
        self,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParseResponse:
        """
        Start a parse job for the provided file.

        Args: file: The file to parse information from. state: The application state.

        Returns: ParseResponse: The response containing the created job information.

        Args:
          file: The file to parse information from

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/document-intelligence/parse",
            body=maybe_transform(body, parse_create_job_params.ParseCreateJobParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParseResponse,
        )

    def retrieve_job(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParseResponse:
        """
        Get detailed information about a specific parse job.

        Args: job_id: The ID of the parse job. state: The application state.

        Returns: ParseResponse: Detailed information about the parse job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/v1/document-intelligence/parse/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParseResponse,
        )


class AsyncParseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncParseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return AsyncParseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncParseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#with_streaming_response
        """
        return AsyncParseResourceWithStreamingResponse(self)

    async def create_job(
        self,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParseResponse:
        """
        Start a parse job for the provided file.

        Args: file: The file to parse information from. state: The application state.

        Returns: ParseResponse: The response containing the created job information.

        Args:
          file: The file to parse information from

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/document-intelligence/parse",
            body=await async_maybe_transform(body, parse_create_job_params.ParseCreateJobParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParseResponse,
        )

    async def retrieve_job(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParseResponse:
        """
        Get detailed information about a specific parse job.

        Args: job_id: The ID of the parse job. state: The application state.

        Returns: ParseResponse: Detailed information about the parse job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/v1/document-intelligence/parse/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParseResponse,
        )


class ParseResourceWithRawResponse:
    def __init__(self, parse: ParseResource) -> None:
        self._parse = parse

        self.create_job = to_raw_response_wrapper(
            parse.create_job,
        )
        self.retrieve_job = to_raw_response_wrapper(
            parse.retrieve_job,
        )


class AsyncParseResourceWithRawResponse:
    def __init__(self, parse: AsyncParseResource) -> None:
        self._parse = parse

        self.create_job = async_to_raw_response_wrapper(
            parse.create_job,
        )
        self.retrieve_job = async_to_raw_response_wrapper(
            parse.retrieve_job,
        )


class ParseResourceWithStreamingResponse:
    def __init__(self, parse: ParseResource) -> None:
        self._parse = parse

        self.create_job = to_streamed_response_wrapper(
            parse.create_job,
        )
        self.retrieve_job = to_streamed_response_wrapper(
            parse.retrieve_job,
        )


class AsyncParseResourceWithStreamingResponse:
    def __init__(self, parse: AsyncParseResource) -> None:
        self._parse = parse

        self.create_job = async_to_streamed_response_wrapper(
            parse.create_job,
        )
        self.retrieve_job = async_to_streamed_response_wrapper(
            parse.retrieve_job,
        )
