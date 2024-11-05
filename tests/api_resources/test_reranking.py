# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixedbread import Mixedbread, AsyncMixedbread
from tests.utils import assert_matches_type
from mixedbread.types import RerankingCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReranking:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Mixedbread) -> None:
        reranking = client.reranking.create(
            input={},
            query="What is mixedbread ai?",
        )
        assert_matches_type(RerankingCreateResponse, reranking, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Mixedbread) -> None:
        reranking = client.reranking.create(
            input={},
            query="What is mixedbread ai?",
            model="mixedbread-ai/mxbai-rerank-large-v1",
            rank_fields=["field1", "field2"],
            return_input=False,
            top_k=10,
        )
        assert_matches_type(RerankingCreateResponse, reranking, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Mixedbread) -> None:
        response = client.reranking.with_raw_response.create(
            input={},
            query="What is mixedbread ai?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reranking = response.parse()
        assert_matches_type(RerankingCreateResponse, reranking, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Mixedbread) -> None:
        with client.reranking.with_streaming_response.create(
            input={},
            query="What is mixedbread ai?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reranking = response.parse()
            assert_matches_type(RerankingCreateResponse, reranking, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReranking:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMixedbread) -> None:
        reranking = await async_client.reranking.create(
            input={},
            query="What is mixedbread ai?",
        )
        assert_matches_type(RerankingCreateResponse, reranking, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMixedbread) -> None:
        reranking = await async_client.reranking.create(
            input={},
            query="What is mixedbread ai?",
            model="mixedbread-ai/mxbai-rerank-large-v1",
            rank_fields=["field1", "field2"],
            return_input=False,
            top_k=10,
        )
        assert_matches_type(RerankingCreateResponse, reranking, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.reranking.with_raw_response.create(
            input={},
            query="What is mixedbread ai?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reranking = await response.parse()
        assert_matches_type(RerankingCreateResponse, reranking, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMixedbread) -> None:
        async with async_client.reranking.with_streaming_response.create(
            input={},
            query="What is mixedbread ai?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reranking = await response.parse()
            assert_matches_type(RerankingCreateResponse, reranking, path=["response"])

        assert cast(Any, response.is_closed) is True
