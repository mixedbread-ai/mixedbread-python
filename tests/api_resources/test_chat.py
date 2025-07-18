# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixedbread import Mixedbread, AsyncMixedbread
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_completion(self, client: Mixedbread) -> None:
        chat = client.chat.create_completion()
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    def test_raw_response_create_completion(self, client: Mixedbread) -> None:
        response = client.chat.with_raw_response.create_completion()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    def test_streaming_response_create_completion(self, client: Mixedbread) -> None:
        with client.chat.with_streaming_response.create_completion() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChat:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_completion(self, async_client: AsyncMixedbread) -> None:
        chat = await async_client.chat.create_completion()
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    async def test_raw_response_create_completion(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.chat.with_raw_response.create_completion()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(object, chat, path=["response"])

    @parametrize
    async def test_streaming_response_create_completion(self, async_client: AsyncMixedbread) -> None:
        async with async_client.chat.with_streaming_response.create_completion() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(object, chat, path=["response"])

        assert cast(Any, response.is_closed) is True
