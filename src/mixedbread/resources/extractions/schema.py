# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.extractions import schema_create_params, schema_enhance_params, schema_validate_params
from ...types.extractions.created_json_schema import CreatedJsonSchema
from ...types.extractions.enhanced_json_schema import EnhancedJsonSchema
from ...types.extractions.validated_json_schema import ValidatedJsonSchema

__all__ = ["SchemaResource", "AsyncSchemaResource"]


class SchemaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SchemaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return SchemaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchemaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return SchemaResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreatedJsonSchema:
        """
        Create a schema with the provided parameters.

        Args: params: The parameters for creating a schema.

        Returns: The created schema.

        Args:
          description: Description of the data to extract

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/extractions/schema",
            body=maybe_transform({"description": description}, schema_create_params.SchemaCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatedJsonSchema,
        )

    def enhance(
        self,
        *,
        json_schema: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnhancedJsonSchema:
        """
        Enhance a schema by enriching the descriptions to aid extraction.

        Args: params: The parameters for enhancing a schema.

        Returns: The enhanced schema.

        Args:
          json_schema: The JSON schema to enhance

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/extractions/schema/enhance",
            body=maybe_transform({"json_schema": json_schema}, schema_enhance_params.SchemaEnhanceParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnhancedJsonSchema,
        )

    def validate(
        self,
        *,
        json_schema: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ValidatedJsonSchema:
        """
        Validate a schema.

        Args: params: The parameters for validating a schema.

        Returns: The validation result.

        Args:
          json_schema: The JSON schema to validate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/extractions/schema/validate",
            body=maybe_transform({"json_schema": json_schema}, schema_validate_params.SchemaValidateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ValidatedJsonSchema,
        )


class AsyncSchemaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSchemaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSchemaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchemaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return AsyncSchemaResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreatedJsonSchema:
        """
        Create a schema with the provided parameters.

        Args: params: The parameters for creating a schema.

        Returns: The created schema.

        Args:
          description: Description of the data to extract

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/extractions/schema",
            body=await async_maybe_transform({"description": description}, schema_create_params.SchemaCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatedJsonSchema,
        )

    async def enhance(
        self,
        *,
        json_schema: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnhancedJsonSchema:
        """
        Enhance a schema by enriching the descriptions to aid extraction.

        Args: params: The parameters for enhancing a schema.

        Returns: The enhanced schema.

        Args:
          json_schema: The JSON schema to enhance

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/extractions/schema/enhance",
            body=await async_maybe_transform({"json_schema": json_schema}, schema_enhance_params.SchemaEnhanceParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnhancedJsonSchema,
        )

    async def validate(
        self,
        *,
        json_schema: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ValidatedJsonSchema:
        """
        Validate a schema.

        Args: params: The parameters for validating a schema.

        Returns: The validation result.

        Args:
          json_schema: The JSON schema to validate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/extractions/schema/validate",
            body=await async_maybe_transform({"json_schema": json_schema}, schema_validate_params.SchemaValidateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ValidatedJsonSchema,
        )


class SchemaResourceWithRawResponse:
    def __init__(self, schema: SchemaResource) -> None:
        self._schema = schema

        self.create = to_raw_response_wrapper(
            schema.create,
        )
        self.enhance = to_raw_response_wrapper(
            schema.enhance,
        )
        self.validate = to_raw_response_wrapper(
            schema.validate,
        )


class AsyncSchemaResourceWithRawResponse:
    def __init__(self, schema: AsyncSchemaResource) -> None:
        self._schema = schema

        self.create = async_to_raw_response_wrapper(
            schema.create,
        )
        self.enhance = async_to_raw_response_wrapper(
            schema.enhance,
        )
        self.validate = async_to_raw_response_wrapper(
            schema.validate,
        )


class SchemaResourceWithStreamingResponse:
    def __init__(self, schema: SchemaResource) -> None:
        self._schema = schema

        self.create = to_streamed_response_wrapper(
            schema.create,
        )
        self.enhance = to_streamed_response_wrapper(
            schema.enhance,
        )
        self.validate = to_streamed_response_wrapper(
            schema.validate,
        )


class AsyncSchemaResourceWithStreamingResponse:
    def __init__(self, schema: AsyncSchemaResource) -> None:
        self._schema = schema

        self.create = async_to_streamed_response_wrapper(
            schema.create,
        )
        self.enhance = async_to_streamed_response_wrapper(
            schema.enhance,
        )
        self.validate = async_to_streamed_response_wrapper(
            schema.validate,
        )
