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

__all__ = ["DocumentIntelligenceResource", "AsyncDocumentIntelligenceResource"]


class DocumentIntelligenceResource(SyncAPIResource):
    @cached_property
    def parse(self) -> ParseResource:
        return ParseResource(self._client)

    @cached_property
    def with_raw_response(self) -> DocumentIntelligenceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return DocumentIntelligenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocumentIntelligenceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#with_streaming_response
        """
        return DocumentIntelligenceResourceWithStreamingResponse(self)


class AsyncDocumentIntelligenceResource(AsyncAPIResource):
    @cached_property
    def parse(self) -> AsyncParseResource:
        return AsyncParseResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDocumentIntelligenceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDocumentIntelligenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocumentIntelligenceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#with_streaming_response
        """
        return AsyncDocumentIntelligenceResourceWithStreamingResponse(self)


class DocumentIntelligenceResourceWithRawResponse:
    def __init__(self, document_intelligence: DocumentIntelligenceResource) -> None:
        self._document_intelligence = document_intelligence

    @cached_property
    def parse(self) -> ParseResourceWithRawResponse:
        return ParseResourceWithRawResponse(self._document_intelligence.parse)


class AsyncDocumentIntelligenceResourceWithRawResponse:
    def __init__(self, document_intelligence: AsyncDocumentIntelligenceResource) -> None:
        self._document_intelligence = document_intelligence

    @cached_property
    def parse(self) -> AsyncParseResourceWithRawResponse:
        return AsyncParseResourceWithRawResponse(self._document_intelligence.parse)


class DocumentIntelligenceResourceWithStreamingResponse:
    def __init__(self, document_intelligence: DocumentIntelligenceResource) -> None:
        self._document_intelligence = document_intelligence

    @cached_property
    def parse(self) -> ParseResourceWithStreamingResponse:
        return ParseResourceWithStreamingResponse(self._document_intelligence.parse)


class AsyncDocumentIntelligenceResourceWithStreamingResponse:
    def __init__(self, document_intelligence: AsyncDocumentIntelligenceResource) -> None:
        self._document_intelligence = document_intelligence

    @cached_property
    def parse(self) -> AsyncParseResourceWithStreamingResponse:
        return AsyncParseResourceWithStreamingResponse(self._document_intelligence.parse)
