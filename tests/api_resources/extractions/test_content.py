# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixedbread import Mixedbread, AsyncMixedbread
from tests.utils import assert_matches_type
from mixedbread.types.extractions import ExtractionResult

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Mixedbread) -> None:
        content = client.extractions.content.create(
            content="string",
            json_schema={"foo": "bar"},
        )
        assert_matches_type(ExtractionResult, content, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Mixedbread) -> None:
        content = client.extractions.content.create(
            content="string",
            json_schema={"foo": "bar"},
            instructions="instructions",
        )
        assert_matches_type(ExtractionResult, content, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Mixedbread) -> None:
        response = client.extractions.content.with_raw_response.create(
            content="string",
            json_schema={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content = response.parse()
        assert_matches_type(ExtractionResult, content, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Mixedbread) -> None:
        with client.extractions.content.with_streaming_response.create(
            content="string",
            json_schema={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content = response.parse()
            assert_matches_type(ExtractionResult, content, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncContent:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMixedbread) -> None:
        content = await async_client.extractions.content.create(
            content="string",
            json_schema={"foo": "bar"},
        )
        assert_matches_type(ExtractionResult, content, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMixedbread) -> None:
        content = await async_client.extractions.content.create(
            content="string",
            json_schema={"foo": "bar"},
            instructions="instructions",
        )
        assert_matches_type(ExtractionResult, content, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.extractions.content.with_raw_response.create(
            content="string",
            json_schema={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content = await response.parse()
        assert_matches_type(ExtractionResult, content, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMixedbread) -> None:
        async with async_client.extractions.content.with_streaming_response.create(
            content="string",
            json_schema={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content = await response.parse()
            assert_matches_type(ExtractionResult, content, path=["response"])

        assert cast(Any, response.is_closed) is True
