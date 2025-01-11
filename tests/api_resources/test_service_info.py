# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixedbread import Mixedbread, AsyncMixedbread
from tests.utils import assert_matches_type
from mixedbread.types import InfoResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServiceInfo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Mixedbread) -> None:
        service_info = client.service_info.retrieve()
        assert_matches_type(InfoResponse, service_info, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Mixedbread) -> None:
        response = client.service_info.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_info = response.parse()
        assert_matches_type(InfoResponse, service_info, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Mixedbread) -> None:
        with client.service_info.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_info = response.parse()
            assert_matches_type(InfoResponse, service_info, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncServiceInfo:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMixedbread) -> None:
        service_info = await async_client.service_info.retrieve()
        assert_matches_type(InfoResponse, service_info, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.service_info.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_info = await response.parse()
        assert_matches_type(InfoResponse, service_info, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMixedbread) -> None:
        async with async_client.service_info.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_info = await response.parse()
            assert_matches_type(InfoResponse, service_info, path=["response"])

        assert cast(Any, response.is_closed) is True
