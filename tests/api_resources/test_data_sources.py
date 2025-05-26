# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixedbread import Mixedbread, AsyncMixedbread
from tests.utils import assert_matches_type
from mixedbread.types import (
    DataSourceListResponse,
    DataSourceCreateResponse,
    DataSourceDeleteResponse,
    DataSourceUpdateResponse,
    DataSourceRetrieveResponse,
)
from mixedbread._utils import parse_datetime
from mixedbread.pagination import SyncLimitOffset, AsyncLimitOffset

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDataSources:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Mixedbread) -> None:
        data_source = client.data_sources.create(
            type="notion",
            name="name",
        )
        assert_matches_type(DataSourceCreateResponse, data_source, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Mixedbread) -> None:
        data_source = client.data_sources.create(
            type="notion",
            name="name",
            metadata={},
            auth_params={
                "type": "oauth2",
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "client_id": "client_id",
                "client_secret": "client_secret",
                "redirect_uri": "redirect_uri",
                "scope": "scope",
                "access_token": "access_token",
                "refresh_token": "refresh_token",
                "token_type": "token_type",
                "expires_on": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(DataSourceCreateResponse, data_source, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Mixedbread) -> None:
        response = client.data_sources.with_raw_response.create(
            type="notion",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(DataSourceCreateResponse, data_source, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Mixedbread) -> None:
        with client.data_sources.with_streaming_response.create(
            type="notion",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = response.parse()
            assert_matches_type(DataSourceCreateResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Mixedbread) -> None:
        data_source = client.data_sources.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DataSourceRetrieveResponse, data_source, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Mixedbread) -> None:
        response = client.data_sources.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(DataSourceRetrieveResponse, data_source, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Mixedbread) -> None:
        with client.data_sources.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = response.parse()
            assert_matches_type(DataSourceRetrieveResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
            client.data_sources.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Mixedbread) -> None:
        data_source = client.data_sources.update(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DataSourceUpdateResponse, data_source, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Mixedbread) -> None:
        data_source = client.data_sources.update(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            metadata={},
            auth_params={
                "type": "oauth2",
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "client_id": "client_id",
                "client_secret": "client_secret",
                "redirect_uri": "redirect_uri",
                "scope": "scope",
                "access_token": "access_token",
                "refresh_token": "refresh_token",
                "token_type": "token_type",
                "expires_on": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(DataSourceUpdateResponse, data_source, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Mixedbread) -> None:
        response = client.data_sources.with_raw_response.update(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(DataSourceUpdateResponse, data_source, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Mixedbread) -> None:
        with client.data_sources.with_streaming_response.update(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = response.parse()
            assert_matches_type(DataSourceUpdateResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
            client.data_sources.with_raw_response.update(
                data_source_id="",
            )

    @parametrize
    def test_method_list(self, client: Mixedbread) -> None:
        data_source = client.data_sources.list()
        assert_matches_type(SyncLimitOffset[DataSourceListResponse], data_source, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Mixedbread) -> None:
        data_source = client.data_sources.list(
            limit=1000,
            offset=0,
        )
        assert_matches_type(SyncLimitOffset[DataSourceListResponse], data_source, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Mixedbread) -> None:
        response = client.data_sources.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(SyncLimitOffset[DataSourceListResponse], data_source, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Mixedbread) -> None:
        with client.data_sources.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = response.parse()
            assert_matches_type(SyncLimitOffset[DataSourceListResponse], data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Mixedbread) -> None:
        data_source = client.data_sources.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DataSourceDeleteResponse, data_source, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Mixedbread) -> None:
        response = client.data_sources.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = response.parse()
        assert_matches_type(DataSourceDeleteResponse, data_source, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Mixedbread) -> None:
        with client.data_sources.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = response.parse()
            assert_matches_type(DataSourceDeleteResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
            client.data_sources.with_raw_response.delete(
                "",
            )


class TestAsyncDataSources:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMixedbread) -> None:
        data_source = await async_client.data_sources.create(
            type="notion",
            name="name",
        )
        assert_matches_type(DataSourceCreateResponse, data_source, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMixedbread) -> None:
        data_source = await async_client.data_sources.create(
            type="notion",
            name="name",
            metadata={},
            auth_params={
                "type": "oauth2",
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "client_id": "client_id",
                "client_secret": "client_secret",
                "redirect_uri": "redirect_uri",
                "scope": "scope",
                "access_token": "access_token",
                "refresh_token": "refresh_token",
                "token_type": "token_type",
                "expires_on": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(DataSourceCreateResponse, data_source, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.data_sources.with_raw_response.create(
            type="notion",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(DataSourceCreateResponse, data_source, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMixedbread) -> None:
        async with async_client.data_sources.with_streaming_response.create(
            type="notion",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = await response.parse()
            assert_matches_type(DataSourceCreateResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMixedbread) -> None:
        data_source = await async_client.data_sources.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DataSourceRetrieveResponse, data_source, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.data_sources.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(DataSourceRetrieveResponse, data_source, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMixedbread) -> None:
        async with async_client.data_sources.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = await response.parse()
            assert_matches_type(DataSourceRetrieveResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
            await async_client.data_sources.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncMixedbread) -> None:
        data_source = await async_client.data_sources.update(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DataSourceUpdateResponse, data_source, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMixedbread) -> None:
        data_source = await async_client.data_sources.update(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            metadata={},
            auth_params={
                "type": "oauth2",
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "client_id": "client_id",
                "client_secret": "client_secret",
                "redirect_uri": "redirect_uri",
                "scope": "scope",
                "access_token": "access_token",
                "refresh_token": "refresh_token",
                "token_type": "token_type",
                "expires_on": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(DataSourceUpdateResponse, data_source, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.data_sources.with_raw_response.update(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(DataSourceUpdateResponse, data_source, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMixedbread) -> None:
        async with async_client.data_sources.with_streaming_response.update(
            data_source_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = await response.parse()
            assert_matches_type(DataSourceUpdateResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
            await async_client.data_sources.with_raw_response.update(
                data_source_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncMixedbread) -> None:
        data_source = await async_client.data_sources.list()
        assert_matches_type(AsyncLimitOffset[DataSourceListResponse], data_source, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMixedbread) -> None:
        data_source = await async_client.data_sources.list(
            limit=1000,
            offset=0,
        )
        assert_matches_type(AsyncLimitOffset[DataSourceListResponse], data_source, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.data_sources.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(AsyncLimitOffset[DataSourceListResponse], data_source, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMixedbread) -> None:
        async with async_client.data_sources.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = await response.parse()
            assert_matches_type(AsyncLimitOffset[DataSourceListResponse], data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncMixedbread) -> None:
        data_source = await async_client.data_sources.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DataSourceDeleteResponse, data_source, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.data_sources.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_source = await response.parse()
        assert_matches_type(DataSourceDeleteResponse, data_source, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMixedbread) -> None:
        async with async_client.data_sources.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_source = await response.parse()
            assert_matches_type(DataSourceDeleteResponse, data_source, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_source_id` but received ''"):
            await async_client.data_sources.with_raw_response.delete(
                "",
            )
