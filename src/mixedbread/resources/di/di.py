# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .parse import (
    ParseResource,
    AsyncParseResource,
    ParseResourceWithRawResponse,
    AsyncParseResourceWithRawResponse,
    ParseResourceWithStreamingResponse,
    AsyncParseResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["DiResource", "AsyncDiResource"]


class DiResource(SyncAPIResource):
    @cached_property
    def parse(self) -> ParseResource:
        return ParseResource(self._client)

    @cached_property
    def with_raw_response(self) -> DiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return DiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#with_streaming_response
        """
        return DiResourceWithStreamingResponse(self)


class AsyncDiResource(AsyncAPIResource):
    @cached_property
    def parse(self) -> AsyncParseResource:
        return AsyncParseResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#with_streaming_response
        """
        return AsyncDiResourceWithStreamingResponse(self)


class DiResourceWithRawResponse:
    def __init__(self, di: DiResource) -> None:
        self._di = di

    @cached_property
    def parse(self) -> ParseResourceWithRawResponse:
        return ParseResourceWithRawResponse(self._di.parse)


class AsyncDiResourceWithRawResponse:
    def __init__(self, di: AsyncDiResource) -> None:
        self._di = di

    @cached_property
    def parse(self) -> AsyncParseResourceWithRawResponse:
        return AsyncParseResourceWithRawResponse(self._di.parse)


class DiResourceWithStreamingResponse:
    def __init__(self, di: DiResource) -> None:
        self._di = di

    @cached_property
    def parse(self) -> ParseResourceWithStreamingResponse:
        return ParseResourceWithStreamingResponse(self._di.parse)


class AsyncDiResourceWithStreamingResponse:
    def __init__(self, di: AsyncDiResource) -> None:
        self._di = di

    @cached_property
    def parse(self) -> AsyncParseResourceWithStreamingResponse:
        return AsyncParseResourceWithStreamingResponse(self._di.parse)
