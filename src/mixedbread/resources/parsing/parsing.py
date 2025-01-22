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
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ParsingResource", "AsyncParsingResource"]


class ParsingResource(SyncAPIResource):
    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ParsingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return ParsingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ParsingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return ParsingResourceWithStreamingResponse(self)


class AsyncParsingResource(AsyncAPIResource):
    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncParsingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return AsyncParsingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncParsingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return AsyncParsingResourceWithStreamingResponse(self)


class ParsingResourceWithRawResponse:
    def __init__(self, parsing: ParsingResource) -> None:
        self._parsing = parsing

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._parsing.jobs)


class AsyncParsingResourceWithRawResponse:
    def __init__(self, parsing: AsyncParsingResource) -> None:
        self._parsing = parsing

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._parsing.jobs)


class ParsingResourceWithStreamingResponse:
    def __init__(self, parsing: ParsingResource) -> None:
        self._parsing = parsing

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._parsing.jobs)


class AsyncParsingResourceWithStreamingResponse:
    def __init__(self, parsing: AsyncParsingResource) -> None:
        self._parsing = parsing

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._parsing.jobs)
