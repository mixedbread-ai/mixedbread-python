# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixedbread import Mixedbread, AsyncMixedbread
from tests.utils import assert_matches_type
from mixedbread.types import BaseStatusResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBase:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_status(self, client: Mixedbread) -> None:
        base = client.base.status()
        assert_matches_type(BaseStatusResponse, base, path=["response"])

    @parametrize
    def test_raw_response_status(self, client: Mixedbread) -> None:
        response = client.base.with_raw_response.status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        base = response.parse()
        assert_matches_type(BaseStatusResponse, base, path=["response"])

    @parametrize
    def test_streaming_response_status(self, client: Mixedbread) -> None:
        with client.base.with_streaming_response.status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            base = response.parse()
            assert_matches_type(BaseStatusResponse, base, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBase:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_status(self, async_client: AsyncMixedbread) -> None:
        base = await async_client.base.status()
        assert_matches_type(BaseStatusResponse, base, path=["response"])

    @parametrize
    async def test_raw_response_status(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.base.with_raw_response.status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        base = await response.parse()
        assert_matches_type(BaseStatusResponse, base, path=["response"])

    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncMixedbread) -> None:
        async with async_client.base.with_streaming_response.status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            base = await response.parse()
            assert_matches_type(BaseStatusResponse, base, path=["response"])

        assert cast(Any, response.is_closed) is True
