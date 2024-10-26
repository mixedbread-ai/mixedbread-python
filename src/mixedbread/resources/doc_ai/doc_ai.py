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

__all__ = ["DocAIResource", "AsyncDocAIResource"]


class DocAIResource(SyncAPIResource):
    @cached_property
    def parse(self) -> ParseResource:
        return ParseResource(self._client)

    @cached_property
    def with_raw_response(self) -> DocAIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return DocAIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocAIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#with_streaming_response
        """
        return DocAIResourceWithStreamingResponse(self)


class AsyncDocAIResource(AsyncAPIResource):
    @cached_property
    def parse(self) -> AsyncParseResource:
        return AsyncParseResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDocAIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDocAIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocAIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#with_streaming_response
        """
        return AsyncDocAIResourceWithStreamingResponse(self)


class DocAIResourceWithRawResponse:
    def __init__(self, doc_ai: DocAIResource) -> None:
        self._doc_ai = doc_ai

    @cached_property
    def parse(self) -> ParseResourceWithRawResponse:
        return ParseResourceWithRawResponse(self._doc_ai.parse)


class AsyncDocAIResourceWithRawResponse:
    def __init__(self, doc_ai: AsyncDocAIResource) -> None:
        self._doc_ai = doc_ai

    @cached_property
    def parse(self) -> AsyncParseResourceWithRawResponse:
        return AsyncParseResourceWithRawResponse(self._doc_ai.parse)


class DocAIResourceWithStreamingResponse:
    def __init__(self, doc_ai: DocAIResource) -> None:
        self._doc_ai = doc_ai

    @cached_property
    def parse(self) -> ParseResourceWithStreamingResponse:
        return ParseResourceWithStreamingResponse(self._doc_ai.parse)


class AsyncDocAIResourceWithStreamingResponse:
    def __init__(self, doc_ai: AsyncDocAIResource) -> None:
        self._doc_ai = doc_ai

    @cached_property
    def parse(self) -> AsyncParseResourceWithStreamingResponse:
        return AsyncParseResourceWithStreamingResponse(self._doc_ai.parse)
