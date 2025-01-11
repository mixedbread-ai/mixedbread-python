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
from .schema import (
    SchemaResource,
    AsyncSchemaResource,
    SchemaResourceWithRawResponse,
    AsyncSchemaResourceWithRawResponse,
    SchemaResourceWithStreamingResponse,
    AsyncSchemaResourceWithStreamingResponse,
)
from .content import (
    ContentResource,
    AsyncContentResource,
    ContentResourceWithRawResponse,
    AsyncContentResourceWithRawResponse,
    ContentResourceWithStreamingResponse,
    AsyncContentResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ExtractionsResource", "AsyncExtractionsResource"]


class ExtractionsResource(SyncAPIResource):
    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def schema(self) -> SchemaResource:
        return SchemaResource(self._client)

    @cached_property
    def content(self) -> ContentResource:
        return ContentResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExtractionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return ExtractionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtractionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#with_streaming_response
        """
        return ExtractionsResourceWithStreamingResponse(self)


class AsyncExtractionsResource(AsyncAPIResource):
    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def schema(self) -> AsyncSchemaResource:
        return AsyncSchemaResource(self._client)

    @cached_property
    def content(self) -> AsyncContentResource:
        return AsyncContentResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExtractionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExtractionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtractionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/mixedbread-python#with_streaming_response
        """
        return AsyncExtractionsResourceWithStreamingResponse(self)


class ExtractionsResourceWithRawResponse:
    def __init__(self, extractions: ExtractionsResource) -> None:
        self._extractions = extractions

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._extractions.jobs)

    @cached_property
    def schema(self) -> SchemaResourceWithRawResponse:
        return SchemaResourceWithRawResponse(self._extractions.schema)

    @cached_property
    def content(self) -> ContentResourceWithRawResponse:
        return ContentResourceWithRawResponse(self._extractions.content)


class AsyncExtractionsResourceWithRawResponse:
    def __init__(self, extractions: AsyncExtractionsResource) -> None:
        self._extractions = extractions

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._extractions.jobs)

    @cached_property
    def schema(self) -> AsyncSchemaResourceWithRawResponse:
        return AsyncSchemaResourceWithRawResponse(self._extractions.schema)

    @cached_property
    def content(self) -> AsyncContentResourceWithRawResponse:
        return AsyncContentResourceWithRawResponse(self._extractions.content)


class ExtractionsResourceWithStreamingResponse:
    def __init__(self, extractions: ExtractionsResource) -> None:
        self._extractions = extractions

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._extractions.jobs)

    @cached_property
    def schema(self) -> SchemaResourceWithStreamingResponse:
        return SchemaResourceWithStreamingResponse(self._extractions.schema)

    @cached_property
    def content(self) -> ContentResourceWithStreamingResponse:
        return ContentResourceWithStreamingResponse(self._extractions.content)


class AsyncExtractionsResourceWithStreamingResponse:
    def __init__(self, extractions: AsyncExtractionsResource) -> None:
        self._extractions = extractions

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._extractions.jobs)

    @cached_property
    def schema(self) -> AsyncSchemaResourceWithStreamingResponse:
        return AsyncSchemaResourceWithStreamingResponse(self._extractions.schema)

    @cached_property
    def content(self) -> AsyncContentResourceWithStreamingResponse:
        return AsyncContentResourceWithStreamingResponse(self._extractions.content)
