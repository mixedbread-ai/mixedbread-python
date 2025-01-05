# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ParseResource", "AsyncParseResource"]


class ParseResource(SyncAPIResource):
    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ParseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return ParseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ParseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return ParseResourceWithStreamingResponse(self)


class AsyncParseResource(AsyncAPIResource):
    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncParseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return AsyncParseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncParseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return AsyncParseResourceWithStreamingResponse(self)


class ParseResourceWithRawResponse:
    def __init__(self, parse: ParseResource) -> None:
        self._parse = parse

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._parse.jobs)


class AsyncParseResourceWithRawResponse:
    def __init__(self, parse: AsyncParseResource) -> None:
        self._parse = parse

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._parse.jobs)


class ParseResourceWithStreamingResponse:
    def __init__(self, parse: ParseResource) -> None:
        self._parse = parse

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._parse.jobs)


class AsyncParseResourceWithStreamingResponse:
    def __init__(self, parse: AsyncParseResource) -> None:
        self._parse = parse

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._parse.jobs)
