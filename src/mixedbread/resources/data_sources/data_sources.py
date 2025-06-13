# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import overload

import httpx

from ...types import DataSourceType, data_source_list_params, data_source_create_params, data_source_update_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .connectors import (
    ConnectorsResource,
    AsyncConnectorsResource,
    ConnectorsResourceWithRawResponse,
    AsyncConnectorsResourceWithRawResponse,
    ConnectorsResourceWithStreamingResponse,
    AsyncConnectorsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncLimitOffset, AsyncLimitOffset
from ..._base_client import AsyncPaginator, make_request_options
from ...types.data_source import DataSource
from ...types.data_source_type import DataSourceType
from ...types.data_source_delete_response import DataSourceDeleteResponse

__all__ = ["DataSourcesResource", "AsyncDataSourcesResource"]


class DataSourcesResource(SyncAPIResource):
    @cached_property
    def connectors(self) -> ConnectorsResource:
        return ConnectorsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DataSourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return DataSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataSourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return DataSourcesResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        type: DataSourceType | NotGiven = NOT_GIVEN,
        name: str,
        metadata: object | NotGiven = NOT_GIVEN,
        auth_params: Optional[data_source_create_params.NotionDataSourceCreateOrUpdateParamsAuthParams]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSource:
        """
        Create a new data source.

        Args: params: The data source to create.

        Returns: The created data source.

        Args:
          type: The type of data source to create

          name: The name of the data source

          metadata: The metadata of the data source

          auth_params: The authentication parameters of the data source. Notion supports OAuth2 and API
              key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        type: DataSourceType | NotGiven = NOT_GIVEN,
        name: str,
        metadata: object | NotGiven = NOT_GIVEN,
        auth_params: Optional[data_source_create_params.LinearDataSourceCreateOrUpdateParamsAuthParams]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSource:
        """
        Create a new data source.

        Args: params: The data source to create.

        Returns: The created data source.

        Args:
          type: The type of data source to create

          name: The name of the data source

          metadata: The metadata of the data source

          auth_params: Base class for OAuth2 create or update parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["name"])
    def create(
        self,
        *,
        type: DataSourceType | NotGiven = NOT_GIVEN,
        name: str,
        metadata: object | NotGiven = NOT_GIVEN,
        auth_params: Optional[data_source_create_params.NotionDataSourceCreateOrUpdateParamsAuthParams]
        | Optional[data_source_create_params.LinearDataSourceCreateOrUpdateParamsAuthParams]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSource:
        return self._post(
            "/v1/data_sources/",
            body=maybe_transform(
                {
                    "type": type,
                    "name": name,
                    "metadata": metadata,
                    "auth_params": auth_params,
                },
                data_source_create_params.DataSourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSource,
        )

    def retrieve(
        self,
        data_source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSource:
        """
        Get a data source by ID.

        Args: data_source_id: The ID of the data source to fetch.

        Returns: The data source.

        Args:
          data_source_id: The ID of the data source to fetch

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        return self._get(
            f"/v1/data_sources/{data_source_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSource,
        )

    @overload
    def update(
        self,
        data_source_id: str,
        *,
        type: DataSourceType | NotGiven = NOT_GIVEN,
        name: str,
        metadata: object | NotGiven = NOT_GIVEN,
        auth_params: Optional[data_source_update_params.NotionDataSourceCreateOrUpdateParamsAuthParams]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSource:
        """Update a data source.

        Args: data_source_id: The ID of the data source to update.

        params: The data
        source to update.

        Returns: The updated data source.

        Args:
          data_source_id: The ID of the data source to update

          type: The type of data source to create

          name: The name of the data source

          metadata: The metadata of the data source

          auth_params: The authentication parameters of the data source. Notion supports OAuth2 and API
              key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        data_source_id: str,
        *,
        type: DataSourceType | NotGiven = NOT_GIVEN,
        name: str,
        metadata: object | NotGiven = NOT_GIVEN,
        auth_params: Optional[data_source_update_params.LinearDataSourceCreateOrUpdateParamsAuthParams]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSource:
        """Update a data source.

        Args: data_source_id: The ID of the data source to update.

        params: The data
        source to update.

        Returns: The updated data source.

        Args:
          data_source_id: The ID of the data source to update

          type: The type of data source to create

          name: The name of the data source

          metadata: The metadata of the data source

          auth_params: Base class for OAuth2 create or update parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["name"])
    def update(
        self,
        data_source_id: str,
        *,
        type: DataSourceType | NotGiven = NOT_GIVEN,
        name: str,
        metadata: object | NotGiven = NOT_GIVEN,
        auth_params: Optional[data_source_update_params.NotionDataSourceCreateOrUpdateParamsAuthParams]
        | Optional[data_source_update_params.LinearDataSourceCreateOrUpdateParamsAuthParams]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSource:
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        return self._put(
            f"/v1/data_sources/{data_source_id}",
            body=maybe_transform(
                {
                    "type": type,
                    "name": name,
                    "metadata": metadata,
                    "auth_params": auth_params,
                },
                data_source_update_params.DataSourceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSource,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncLimitOffset[DataSource]:
        """
        Get all data sources.

        Returns: The list of data sources.

        Args:
          limit: Maximum number of items to return per page

          offset: Offset of the first item to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/data_sources/",
            page=SyncLimitOffset[DataSource],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    data_source_list_params.DataSourceListParams,
                ),
            ),
            model=DataSource,
        )

    def delete(
        self,
        data_source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSourceDeleteResponse:
        """
        Delete a data source.

        Args: data_source_id: The ID of the data source to delete.

        Args:
          data_source_id: The ID of the data source to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        return self._delete(
            f"/v1/data_sources/{data_source_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSourceDeleteResponse,
        )


class AsyncDataSourcesResource(AsyncAPIResource):
    @cached_property
    def connectors(self) -> AsyncConnectorsResource:
        return AsyncConnectorsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDataSourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDataSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataSourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return AsyncDataSourcesResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        type: DataSourceType | NotGiven = NOT_GIVEN,
        name: str,
        metadata: object | NotGiven = NOT_GIVEN,
        auth_params: Optional[data_source_create_params.NotionDataSourceCreateOrUpdateParamsAuthParams]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSource:
        """
        Create a new data source.

        Args: params: The data source to create.

        Returns: The created data source.

        Args:
          type: The type of data source to create

          name: The name of the data source

          metadata: The metadata of the data source

          auth_params: The authentication parameters of the data source. Notion supports OAuth2 and API
              key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        type: DataSourceType | NotGiven = NOT_GIVEN,
        name: str,
        metadata: object | NotGiven = NOT_GIVEN,
        auth_params: Optional[data_source_create_params.LinearDataSourceCreateOrUpdateParamsAuthParams]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSource:
        """
        Create a new data source.

        Args: params: The data source to create.

        Returns: The created data source.

        Args:
          type: The type of data source to create

          name: The name of the data source

          metadata: The metadata of the data source

          auth_params: Base class for OAuth2 create or update parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["name"])
    async def create(
        self,
        *,
        type: DataSourceType | NotGiven = NOT_GIVEN,
        name: str,
        metadata: object | NotGiven = NOT_GIVEN,
        auth_params: Optional[data_source_create_params.NotionDataSourceCreateOrUpdateParamsAuthParams]
        | Optional[data_source_create_params.LinearDataSourceCreateOrUpdateParamsAuthParams]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSource:
        return await self._post(
            "/v1/data_sources/",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "name": name,
                    "metadata": metadata,
                    "auth_params": auth_params,
                },
                data_source_create_params.DataSourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSource,
        )

    async def retrieve(
        self,
        data_source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSource:
        """
        Get a data source by ID.

        Args: data_source_id: The ID of the data source to fetch.

        Returns: The data source.

        Args:
          data_source_id: The ID of the data source to fetch

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        return await self._get(
            f"/v1/data_sources/{data_source_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSource,
        )

    @overload
    async def update(
        self,
        data_source_id: str,
        *,
        type: DataSourceType | NotGiven = NOT_GIVEN,
        name: str,
        metadata: object | NotGiven = NOT_GIVEN,
        auth_params: Optional[data_source_update_params.NotionDataSourceCreateOrUpdateParamsAuthParams]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSource:
        """Update a data source.

        Args: data_source_id: The ID of the data source to update.

        params: The data
        source to update.

        Returns: The updated data source.

        Args:
          data_source_id: The ID of the data source to update

          type: The type of data source to create

          name: The name of the data source

          metadata: The metadata of the data source

          auth_params: The authentication parameters of the data source. Notion supports OAuth2 and API
              key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        data_source_id: str,
        *,
        type: DataSourceType | NotGiven = NOT_GIVEN,
        name: str,
        metadata: object | NotGiven = NOT_GIVEN,
        auth_params: Optional[data_source_update_params.LinearDataSourceCreateOrUpdateParamsAuthParams]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSource:
        """Update a data source.

        Args: data_source_id: The ID of the data source to update.

        params: The data
        source to update.

        Returns: The updated data source.

        Args:
          data_source_id: The ID of the data source to update

          type: The type of data source to create

          name: The name of the data source

          metadata: The metadata of the data source

          auth_params: Base class for OAuth2 create or update parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["name"])
    async def update(
        self,
        data_source_id: str,
        *,
        type: DataSourceType | NotGiven = NOT_GIVEN,
        name: str,
        metadata: object | NotGiven = NOT_GIVEN,
        auth_params: Optional[data_source_update_params.NotionDataSourceCreateOrUpdateParamsAuthParams]
        | Optional[data_source_update_params.LinearDataSourceCreateOrUpdateParamsAuthParams]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSource:
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        return await self._put(
            f"/v1/data_sources/{data_source_id}",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "name": name,
                    "metadata": metadata,
                    "auth_params": auth_params,
                },
                data_source_update_params.DataSourceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSource,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[DataSource, AsyncLimitOffset[DataSource]]:
        """
        Get all data sources.

        Returns: The list of data sources.

        Args:
          limit: Maximum number of items to return per page

          offset: Offset of the first item to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/data_sources/",
            page=AsyncLimitOffset[DataSource],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    data_source_list_params.DataSourceListParams,
                ),
            ),
            model=DataSource,
        )

    async def delete(
        self,
        data_source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataSourceDeleteResponse:
        """
        Delete a data source.

        Args: data_source_id: The ID of the data source to delete.

        Args:
          data_source_id: The ID of the data source to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        return await self._delete(
            f"/v1/data_sources/{data_source_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSourceDeleteResponse,
        )


class DataSourcesResourceWithRawResponse:
    def __init__(self, data_sources: DataSourcesResource) -> None:
        self._data_sources = data_sources

        self.create = to_raw_response_wrapper(
            data_sources.create,
        )
        self.retrieve = to_raw_response_wrapper(
            data_sources.retrieve,
        )
        self.update = to_raw_response_wrapper(
            data_sources.update,
        )
        self.list = to_raw_response_wrapper(
            data_sources.list,
        )
        self.delete = to_raw_response_wrapper(
            data_sources.delete,
        )

    @cached_property
    def connectors(self) -> ConnectorsResourceWithRawResponse:
        return ConnectorsResourceWithRawResponse(self._data_sources.connectors)


class AsyncDataSourcesResourceWithRawResponse:
    def __init__(self, data_sources: AsyncDataSourcesResource) -> None:
        self._data_sources = data_sources

        self.create = async_to_raw_response_wrapper(
            data_sources.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            data_sources.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            data_sources.update,
        )
        self.list = async_to_raw_response_wrapper(
            data_sources.list,
        )
        self.delete = async_to_raw_response_wrapper(
            data_sources.delete,
        )

    @cached_property
    def connectors(self) -> AsyncConnectorsResourceWithRawResponse:
        return AsyncConnectorsResourceWithRawResponse(self._data_sources.connectors)


class DataSourcesResourceWithStreamingResponse:
    def __init__(self, data_sources: DataSourcesResource) -> None:
        self._data_sources = data_sources

        self.create = to_streamed_response_wrapper(
            data_sources.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            data_sources.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            data_sources.update,
        )
        self.list = to_streamed_response_wrapper(
            data_sources.list,
        )
        self.delete = to_streamed_response_wrapper(
            data_sources.delete,
        )

    @cached_property
    def connectors(self) -> ConnectorsResourceWithStreamingResponse:
        return ConnectorsResourceWithStreamingResponse(self._data_sources.connectors)


class AsyncDataSourcesResourceWithStreamingResponse:
    def __init__(self, data_sources: AsyncDataSourcesResource) -> None:
        self._data_sources = data_sources

        self.create = async_to_streamed_response_wrapper(
            data_sources.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            data_sources.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            data_sources.update,
        )
        self.list = async_to_streamed_response_wrapper(
            data_sources.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            data_sources.delete,
        )

    @cached_property
    def connectors(self) -> AsyncConnectorsResourceWithStreamingResponse:
        return AsyncConnectorsResourceWithStreamingResponse(self._data_sources.connectors)
