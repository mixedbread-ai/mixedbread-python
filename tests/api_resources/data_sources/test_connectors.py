# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixedbread import Mixedbread, AsyncMixedbread
from tests.utils import assert_matches_type
from mixedbread.pagination import SyncLimitOffset, AsyncLimitOffset
from mixedbread.types.data_sources import (
    ConnectorListResponse,
    ConnectorCreateResponse,
    ConnectorDeleteResponse,
    ConnectorUpdateResponse,
    ConnectorRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnectors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Mixedbread) -> None:
        connector = client.data_sources.connectors.create(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector_store_id="vector_store_id",
        )
        assert_matches_type(ConnectorCreateResponse, connector, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Mixedbread) -> None:
        connector = client.data_sources.connectors.create(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector_store_id="vector_store_id",
            name="name",
            trigger_sync=True,
            metadata={},
            polling_interval="polling_interval",
        )
        assert_matches_type(ConnectorCreateResponse, connector, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Mixedbread) -> None:
        response = client.data_sources.connectors.with_raw_response.create(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector_store_id="vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = response.parse()
        assert_matches_type(ConnectorCreateResponse, connector, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Mixedbread) -> None:
        with client.data_sources.connectors.with_streaming_response.create(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector_store_id="vector_store_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = response.parse()
            assert_matches_type(ConnectorCreateResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
            client.data_sources.connectors.with_raw_response.create(
                data_source_id="",
                vector_store_id="vector_store_id",
            )

    @parametrize
    def test_method_retrieve(self, client: Mixedbread) -> None:
        connector = client.data_sources.connectors.retrieve(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectorRetrieveResponse, connector, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Mixedbread) -> None:
        response = client.data_sources.connectors.with_raw_response.retrieve(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = response.parse()
        assert_matches_type(ConnectorRetrieveResponse, connector, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Mixedbread) -> None:
        with client.data_sources.connectors.with_streaming_response.retrieve(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = response.parse()
            assert_matches_type(ConnectorRetrieveResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
            client.data_sources.connectors.with_raw_response.retrieve(
                connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                data_source_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            client.data_sources.connectors.with_raw_response.retrieve(
                connector_id="",
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_update(self, client: Mixedbread) -> None:
        connector = client.data_sources.connectors.update(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectorUpdateResponse, connector, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Mixedbread) -> None:
        connector = client.data_sources.connectors.update(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            metadata={"foo": "bar"},
            trigger_sync=True,
            polling_interval="polling_interval",
        )
        assert_matches_type(ConnectorUpdateResponse, connector, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Mixedbread) -> None:
        response = client.data_sources.connectors.with_raw_response.update(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = response.parse()
        assert_matches_type(ConnectorUpdateResponse, connector, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Mixedbread) -> None:
        with client.data_sources.connectors.with_streaming_response.update(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = response.parse()
            assert_matches_type(ConnectorUpdateResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
            client.data_sources.connectors.with_raw_response.update(
                connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                data_source_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            client.data_sources.connectors.with_raw_response.update(
                connector_id="",
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_list(self, client: Mixedbread) -> None:
        connector = client.data_sources.connectors.list(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncLimitOffset[ConnectorListResponse], connector, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Mixedbread) -> None:
        connector = client.data_sources.connectors.list(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1000,
            offset=0,
        )
        assert_matches_type(SyncLimitOffset[ConnectorListResponse], connector, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Mixedbread) -> None:
        response = client.data_sources.connectors.with_raw_response.list(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = response.parse()
        assert_matches_type(SyncLimitOffset[ConnectorListResponse], connector, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Mixedbread) -> None:
        with client.data_sources.connectors.with_streaming_response.list(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = response.parse()
            assert_matches_type(SyncLimitOffset[ConnectorListResponse], connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
            client.data_sources.connectors.with_raw_response.list(
                data_source_id="",
            )

    @parametrize
    def test_method_delete(self, client: Mixedbread) -> None:
        connector = client.data_sources.connectors.delete(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectorDeleteResponse, connector, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Mixedbread) -> None:
        response = client.data_sources.connectors.with_raw_response.delete(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = response.parse()
        assert_matches_type(ConnectorDeleteResponse, connector, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Mixedbread) -> None:
        with client.data_sources.connectors.with_streaming_response.delete(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = response.parse()
            assert_matches_type(ConnectorDeleteResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
            client.data_sources.connectors.with_raw_response.delete(
                connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                data_source_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            client.data_sources.connectors.with_raw_response.delete(
                connector_id="",
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncConnectors:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMixedbread) -> None:
        connector = await async_client.data_sources.connectors.create(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector_store_id="vector_store_id",
        )
        assert_matches_type(ConnectorCreateResponse, connector, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMixedbread) -> None:
        connector = await async_client.data_sources.connectors.create(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector_store_id="vector_store_id",
            name="name",
            trigger_sync=True,
            metadata={},
            polling_interval="polling_interval",
        )
        assert_matches_type(ConnectorCreateResponse, connector, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.data_sources.connectors.with_raw_response.create(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector_store_id="vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = await response.parse()
        assert_matches_type(ConnectorCreateResponse, connector, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMixedbread) -> None:
        async with async_client.data_sources.connectors.with_streaming_response.create(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector_store_id="vector_store_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = await response.parse()
            assert_matches_type(ConnectorCreateResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
            await async_client.data_sources.connectors.with_raw_response.create(
                data_source_id="",
                vector_store_id="vector_store_id",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMixedbread) -> None:
        connector = await async_client.data_sources.connectors.retrieve(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectorRetrieveResponse, connector, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.data_sources.connectors.with_raw_response.retrieve(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = await response.parse()
        assert_matches_type(ConnectorRetrieveResponse, connector, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMixedbread) -> None:
        async with async_client.data_sources.connectors.with_streaming_response.retrieve(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = await response.parse()
            assert_matches_type(ConnectorRetrieveResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
            await async_client.data_sources.connectors.with_raw_response.retrieve(
                connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                data_source_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            await async_client.data_sources.connectors.with_raw_response.retrieve(
                connector_id="",
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncMixedbread) -> None:
        connector = await async_client.data_sources.connectors.update(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectorUpdateResponse, connector, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMixedbread) -> None:
        connector = await async_client.data_sources.connectors.update(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            metadata={"foo": "bar"},
            trigger_sync=True,
            polling_interval="polling_interval",
        )
        assert_matches_type(ConnectorUpdateResponse, connector, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.data_sources.connectors.with_raw_response.update(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = await response.parse()
        assert_matches_type(ConnectorUpdateResponse, connector, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMixedbread) -> None:
        async with async_client.data_sources.connectors.with_streaming_response.update(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = await response.parse()
            assert_matches_type(ConnectorUpdateResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
            await async_client.data_sources.connectors.with_raw_response.update(
                connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                data_source_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            await async_client.data_sources.connectors.with_raw_response.update(
                connector_id="",
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncMixedbread) -> None:
        connector = await async_client.data_sources.connectors.list(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncLimitOffset[ConnectorListResponse], connector, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMixedbread) -> None:
        connector = await async_client.data_sources.connectors.list(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1000,
            offset=0,
        )
        assert_matches_type(AsyncLimitOffset[ConnectorListResponse], connector, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.data_sources.connectors.with_raw_response.list(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = await response.parse()
        assert_matches_type(AsyncLimitOffset[ConnectorListResponse], connector, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMixedbread) -> None:
        async with async_client.data_sources.connectors.with_streaming_response.list(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = await response.parse()
            assert_matches_type(AsyncLimitOffset[ConnectorListResponse], connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
            await async_client.data_sources.connectors.with_raw_response.list(
                data_source_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncMixedbread) -> None:
        connector = await async_client.data_sources.connectors.delete(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConnectorDeleteResponse, connector, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.data_sources.connectors.with_raw_response.delete(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = await response.parse()
        assert_matches_type(ConnectorDeleteResponse, connector, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMixedbread) -> None:
        async with async_client.data_sources.connectors.with_streaming_response.delete(
            connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = await response.parse()
            assert_matches_type(ConnectorDeleteResponse, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
            await async_client.data_sources.connectors.with_raw_response.delete(
                connector_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                data_source_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            await async_client.data_sources.connectors.with_raw_response.delete(
                connector_id="",
                data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
