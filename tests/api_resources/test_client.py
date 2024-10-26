# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixedbread import Mixedbread, AsyncMixedbread
from tests.utils import assert_matches_type
from mixedbread.types import BaseStatusCheckResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClient:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_base_status_check(self, client: Mixedbread) -> None:
        client_ = client.base_status_check()
        assert_matches_type(BaseStatusCheckResponse, client_, path=["response"])

    @parametrize
    def test_raw_response_base_status_check(self, client: Mixedbread) -> None:
        response = client.with_raw_response.base_status_check()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(BaseStatusCheckResponse, client_, path=["response"])

    @parametrize
    def test_streaming_response_base_status_check(self, client: Mixedbread) -> None:
        with client.with_streaming_response.base_status_check() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(BaseStatusCheckResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClient:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_base_status_check(self, async_client: AsyncMixedbread) -> None:
        client = await async_client.base_status_check()
        assert_matches_type(BaseStatusCheckResponse, client, path=["response"])

    @parametrize
    async def test_raw_response_base_status_check(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.with_raw_response.base_status_check()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(BaseStatusCheckResponse, client, path=["response"])

    @parametrize
    async def test_streaming_response_base_status_check(self, async_client: AsyncMixedbread) -> None:
        async with async_client.with_streaming_response.base_status_check() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(BaseStatusCheckResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True
