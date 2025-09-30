# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursor, AsyncCursor
from ..._base_client import AsyncPaginator, make_request_options
from ...types.data_sources import connector_list_params, connector_create_params, connector_update_params
from ...types.data_sources.data_source_connector import DataSourceConnector
from ...types.data_sources.connector_delete_response import ConnectorDeleteResponse

__all__ = ["ConnectorsResource", "AsyncConnectorsResource"]


class ConnectorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return ConnectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return ConnectorsResourceWithStreamingResponse(self)

    def create(
        self,
        data_source_id: str,
        *,
        store_id: str,
        name: str | Omit = omit,
        trigger_sync: bool | Omit = omit,
        metadata: object | Omit = omit,
        polling_interval: Union[int, str, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSourceConnector:
        """
        Create a new connector.

        Args: data_source_id: The ID of the data source to create a connector for.
        params: The connector to create.

        Returns: The created connector.

        Args:
          data_source_id: The ID of the data source to create a connector for

          store_id: The ID of the store

          name: The name of the connector

          trigger_sync: Whether the connector should be synced after creation

          metadata: The metadata of the connector

          polling_interval: Polling interval for the connector. Defaults to 30 minutes if not specified. Can
              be provided as:

              - int: Number of seconds (e.g., 1800 for 30 minutes)
              - str: Duration string (e.g., '30m', '1h', '2d') or ISO 8601 format (e.g.,
                'PT30M', 'P1D') Valid range: 15 seconds to 30 days

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        return self._post(
            f"/v1/data_sources/{data_source_id}/connectors",
            body=maybe_transform(
                {
                    "store_id": store_id,
                    "name": name,
                    "trigger_sync": trigger_sync,
                    "metadata": metadata,
                    "polling_interval": polling_interval,
                },
                connector_create_params.ConnectorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSourceConnector,
        )

    def retrieve(
        self,
        connector_id: str,
        *,
        data_source_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSourceConnector:
        """
        Get a connector by ID.

        Args: data_source_id: The ID of the data source to get a connector for.
        connector_id: The ID of the connector to get.

        Returns: The connector.

        Args:
          data_source_id: The ID of the data source to get a connector for

          connector_id: The ID of the connector to get

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return self._get(
            f"/v1/data_sources/{data_source_id}/connectors/{connector_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSourceConnector,
        )

    def update(
        self,
        connector_id: str,
        *,
        data_source_id: str,
        name: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        trigger_sync: Optional[bool] | Omit = omit,
        polling_interval: Union[int, str, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSourceConnector:
        """
        Update a connector.

        Args: data_source_id: The ID of the data source to update a connector for.
        connector_id: The ID of the connector to update. params: The connector to
        update.

        Returns: The updated connector.

        Args:
          data_source_id: The ID of the data source to update a connector for

          connector_id: The ID of the connector to update

          name: The name of the connector

          metadata: The metadata of the connector

          trigger_sync: Whether the connector should be synced after update

          polling_interval: Polling interval for the connector. Defaults to 30 minutes if not specified. Can
              be provided as:

              - int: Number of seconds (e.g., 1800 for 30 minutes)
              - str: Duration string (e.g., '30m', '1h', '2d') or ISO 8601 format (e.g.,
                'PT30M', 'P1D') Valid range: 15 seconds to 30 days

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return self._put(
            f"/v1/data_sources/{data_source_id}/connectors/{connector_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "metadata": metadata,
                    "trigger_sync": trigger_sync,
                    "polling_interval": polling_interval,
                },
                connector_update_params.ConnectorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSourceConnector,
        )

    def list(
        self,
        data_source_id: str,
        *,
        limit: int | Omit = omit,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        include_total: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[DataSourceConnector]:
        """
        Get all connectors for a data source.

        Args: data_source_id: The ID of the data source to get connectors for.
        pagination: The pagination options.

        Returns: The list of connectors.

        Args:
          data_source_id: The ID of the data source to get connectors for

          limit: Maximum number of items to return per page (1-100)

          after: Cursor for forward pagination - get items after this position. Use last_cursor
              from previous response.

          before: Cursor for backward pagination - get items before this position. Use
              first_cursor from previous response.

          include_total: Whether to include total count in response (expensive operation)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        return self._get_api_list(
            f"/v1/data_sources/{data_source_id}/connectors",
            page=SyncCursor[DataSourceConnector],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "after": after,
                        "before": before,
                        "include_total": include_total,
                    },
                    connector_list_params.ConnectorListParams,
                ),
            ),
            model=DataSourceConnector,
        )

    def delete(
        self,
        connector_id: str,
        *,
        data_source_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorDeleteResponse:
        """
        Delete a connector.

        Args: data_source_id: The ID of the data source to delete a connector for.
        connector_id: The ID of the connector to delete.

        Returns: The deleted connector.

        Args:
          data_source_id: The ID of the data source to delete a connector for

          connector_id: The ID of the connector to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return self._delete(
            f"/v1/data_sources/{data_source_id}/connectors/{connector_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorDeleteResponse,
        )


class AsyncConnectorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return AsyncConnectorsResourceWithStreamingResponse(self)

    async def create(
        self,
        data_source_id: str,
        *,
        store_id: str,
        name: str | Omit = omit,
        trigger_sync: bool | Omit = omit,
        metadata: object | Omit = omit,
        polling_interval: Union[int, str, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSourceConnector:
        """
        Create a new connector.

        Args: data_source_id: The ID of the data source to create a connector for.
        params: The connector to create.

        Returns: The created connector.

        Args:
          data_source_id: The ID of the data source to create a connector for

          store_id: The ID of the store

          name: The name of the connector

          trigger_sync: Whether the connector should be synced after creation

          metadata: The metadata of the connector

          polling_interval: Polling interval for the connector. Defaults to 30 minutes if not specified. Can
              be provided as:

              - int: Number of seconds (e.g., 1800 for 30 minutes)
              - str: Duration string (e.g., '30m', '1h', '2d') or ISO 8601 format (e.g.,
                'PT30M', 'P1D') Valid range: 15 seconds to 30 days

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        return await self._post(
            f"/v1/data_sources/{data_source_id}/connectors",
            body=await async_maybe_transform(
                {
                    "store_id": store_id,
                    "name": name,
                    "trigger_sync": trigger_sync,
                    "metadata": metadata,
                    "polling_interval": polling_interval,
                },
                connector_create_params.ConnectorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSourceConnector,
        )

    async def retrieve(
        self,
        connector_id: str,
        *,
        data_source_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSourceConnector:
        """
        Get a connector by ID.

        Args: data_source_id: The ID of the data source to get a connector for.
        connector_id: The ID of the connector to get.

        Returns: The connector.

        Args:
          data_source_id: The ID of the data source to get a connector for

          connector_id: The ID of the connector to get

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return await self._get(
            f"/v1/data_sources/{data_source_id}/connectors/{connector_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSourceConnector,
        )

    async def update(
        self,
        connector_id: str,
        *,
        data_source_id: str,
        name: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, object]] | Omit = omit,
        trigger_sync: Optional[bool] | Omit = omit,
        polling_interval: Union[int, str, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSourceConnector:
        """
        Update a connector.

        Args: data_source_id: The ID of the data source to update a connector for.
        connector_id: The ID of the connector to update. params: The connector to
        update.

        Returns: The updated connector.

        Args:
          data_source_id: The ID of the data source to update a connector for

          connector_id: The ID of the connector to update

          name: The name of the connector

          metadata: The metadata of the connector

          trigger_sync: Whether the connector should be synced after update

          polling_interval: Polling interval for the connector. Defaults to 30 minutes if not specified. Can
              be provided as:

              - int: Number of seconds (e.g., 1800 for 30 minutes)
              - str: Duration string (e.g., '30m', '1h', '2d') or ISO 8601 format (e.g.,
                'PT30M', 'P1D') Valid range: 15 seconds to 30 days

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return await self._put(
            f"/v1/data_sources/{data_source_id}/connectors/{connector_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "metadata": metadata,
                    "trigger_sync": trigger_sync,
                    "polling_interval": polling_interval,
                },
                connector_update_params.ConnectorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSourceConnector,
        )

    def list(
        self,
        data_source_id: str,
        *,
        limit: int | Omit = omit,
        after: Optional[str] | Omit = omit,
        before: Optional[str] | Omit = omit,
        include_total: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DataSourceConnector, AsyncCursor[DataSourceConnector]]:
        """
        Get all connectors for a data source.

        Args: data_source_id: The ID of the data source to get connectors for.
        pagination: The pagination options.

        Returns: The list of connectors.

        Args:
          data_source_id: The ID of the data source to get connectors for

          limit: Maximum number of items to return per page (1-100)

          after: Cursor for forward pagination - get items after this position. Use last_cursor
              from previous response.

          before: Cursor for backward pagination - get items before this position. Use
              first_cursor from previous response.

          include_total: Whether to include total count in response (expensive operation)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        return self._get_api_list(
            f"/v1/data_sources/{data_source_id}/connectors",
            page=AsyncCursor[DataSourceConnector],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "after": after,
                        "before": before,
                        "include_total": include_total,
                    },
                    connector_list_params.ConnectorListParams,
                ),
            ),
            model=DataSourceConnector,
        )

    async def delete(
        self,
        connector_id: str,
        *,
        data_source_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectorDeleteResponse:
        """
        Delete a connector.

        Args: data_source_id: The ID of the data source to delete a connector for.
        connector_id: The ID of the connector to delete.

        Returns: The deleted connector.

        Args:
          data_source_id: The ID of the data source to delete a connector for

          connector_id: The ID of the connector to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        if not connector_id:
            raise ValueError(f"Expected a non-empty value for `connector_id` but received {connector_id!r}")
        return await self._delete(
            f"/v1/data_sources/{data_source_id}/connectors/{connector_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectorDeleteResponse,
        )


class ConnectorsResourceWithRawResponse:
    def __init__(self, connectors: ConnectorsResource) -> None:
        self._connectors = connectors

        self.create = to_raw_response_wrapper(
            connectors.create,
        )
        self.retrieve = to_raw_response_wrapper(
            connectors.retrieve,
        )
        self.update = to_raw_response_wrapper(
            connectors.update,
        )
        self.list = to_raw_response_wrapper(
            connectors.list,
        )
        self.delete = to_raw_response_wrapper(
            connectors.delete,
        )


class AsyncConnectorsResourceWithRawResponse:
    def __init__(self, connectors: AsyncConnectorsResource) -> None:
        self._connectors = connectors

        self.create = async_to_raw_response_wrapper(
            connectors.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            connectors.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            connectors.update,
        )
        self.list = async_to_raw_response_wrapper(
            connectors.list,
        )
        self.delete = async_to_raw_response_wrapper(
            connectors.delete,
        )


class ConnectorsResourceWithStreamingResponse:
    def __init__(self, connectors: ConnectorsResource) -> None:
        self._connectors = connectors

        self.create = to_streamed_response_wrapper(
            connectors.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            connectors.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            connectors.update,
        )
        self.list = to_streamed_response_wrapper(
            connectors.list,
        )
        self.delete = to_streamed_response_wrapper(
            connectors.delete,
        )


class AsyncConnectorsResourceWithStreamingResponse:
    def __init__(self, connectors: AsyncConnectorsResource) -> None:
        self._connectors = connectors

        self.create = async_to_streamed_response_wrapper(
            connectors.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            connectors.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            connectors.update,
        )
        self.list = async_to_streamed_response_wrapper(
            connectors.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            connectors.delete,
        )
