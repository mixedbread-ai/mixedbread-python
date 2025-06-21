# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixedbread import Mixedbread, AsyncMixedbread
from tests.utils import assert_matches_type
from mixedbread.types import (
    InfoResponse,
    RerankResponse,
    EmbeddingCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClient:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_embed(self, client: Mixedbread) -> None:
        client_ = client.embed(
            model="mixedbread-ai/mxbai-embed-large-v1",
            input="x",
        )
        assert_matches_type(EmbeddingCreateResponse, client_, path=["response"])

    @parametrize
    def test_method_embed_with_all_params(self, client: Mixedbread) -> None:
        client_ = client.embed(
            model="mixedbread-ai/mxbai-embed-large-v1",
            input="x",
            dimensions=768,
            prompt="Provide a detailed summary of the following text.",
            normalized=True,
            encoding_format="float",
        )
        assert_matches_type(EmbeddingCreateResponse, client_, path=["response"])

    @parametrize
    def test_raw_response_embed(self, client: Mixedbread) -> None:
        response = client.with_raw_response.embed(
            model="mixedbread-ai/mxbai-embed-large-v1",
            input="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(EmbeddingCreateResponse, client_, path=["response"])

    @parametrize
    def test_streaming_response_embed(self, client: Mixedbread) -> None:
        with client.with_streaming_response.embed(
            model="mixedbread-ai/mxbai-embed-large-v1",
            input="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(EmbeddingCreateResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_info(self, client: Mixedbread) -> None:
        client_ = client.info()
        assert_matches_type(InfoResponse, client_, path=["response"])

    @parametrize
    def test_raw_response_info(self, client: Mixedbread) -> None:
        response = client.with_raw_response.info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(InfoResponse, client_, path=["response"])

    @parametrize
    def test_streaming_response_info(self, client: Mixedbread) -> None:
        with client.with_streaming_response.info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(InfoResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_rerank(self, client: Mixedbread) -> None:
        client_ = client.rerank(
            query="What are the key features of the Mixedbread embedding model?",
            input=["Document 1", "Document 2"],
        )
        assert_matches_type(RerankResponse, client_, path=["response"])

    @parametrize
    def test_method_rerank_with_all_params(self, client: Mixedbread) -> None:
        client_ = client.rerank(
            model="mixedbread-ai/mxbai-rerank-large-v2",
            query="What are the key features of the Mixedbread embedding model?",
            input=["Document 1", "Document 2"],
            rank_fields=["content", "title"],
            top_k=10,
            return_input=False,
            rewrite_query=False,
        )
        assert_matches_type(RerankResponse, client_, path=["response"])

    @parametrize
    def test_raw_response_rerank(self, client: Mixedbread) -> None:
        response = client.with_raw_response.rerank(
            query="What are the key features of the Mixedbread embedding model?",
            input=["Document 1", "Document 2"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(RerankResponse, client_, path=["response"])

    @parametrize
    def test_streaming_response_rerank(self, client: Mixedbread) -> None:
        with client.with_streaming_response.rerank(
            query="What are the key features of the Mixedbread embedding model?",
            input=["Document 1", "Document 2"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(RerankResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClient:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_embed(self, async_client: AsyncMixedbread) -> None:
        client = await async_client.embed(
            model="mixedbread-ai/mxbai-embed-large-v1",
            input="x",
        )
        assert_matches_type(EmbeddingCreateResponse, client, path=["response"])

    @parametrize
    async def test_method_embed_with_all_params(self, async_client: AsyncMixedbread) -> None:
        client = await async_client.embed(
            model="mixedbread-ai/mxbai-embed-large-v1",
            input="x",
            dimensions=768,
            prompt="Provide a detailed summary of the following text.",
            normalized=True,
            encoding_format="float",
        )
        assert_matches_type(EmbeddingCreateResponse, client, path=["response"])

    @parametrize
    async def test_raw_response_embed(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.with_raw_response.embed(
            model="mixedbread-ai/mxbai-embed-large-v1",
            input="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(EmbeddingCreateResponse, client, path=["response"])

    @parametrize
    async def test_streaming_response_embed(self, async_client: AsyncMixedbread) -> None:
        async with async_client.with_streaming_response.embed(
            model="mixedbread-ai/mxbai-embed-large-v1",
            input="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(EmbeddingCreateResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_info(self, async_client: AsyncMixedbread) -> None:
        client = await async_client.info()
        assert_matches_type(InfoResponse, client, path=["response"])

    @parametrize
    async def test_raw_response_info(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.with_raw_response.info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(InfoResponse, client, path=["response"])

    @parametrize
    async def test_streaming_response_info(self, async_client: AsyncMixedbread) -> None:
        async with async_client.with_streaming_response.info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(InfoResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_rerank(self, async_client: AsyncMixedbread) -> None:
        client = await async_client.rerank(
            query="What are the key features of the Mixedbread embedding model?",
            input=["Document 1", "Document 2"],
        )
        assert_matches_type(RerankResponse, client, path=["response"])

    @parametrize
    async def test_method_rerank_with_all_params(self, async_client: AsyncMixedbread) -> None:
        client = await async_client.rerank(
            model="mixedbread-ai/mxbai-rerank-large-v2",
            query="What are the key features of the Mixedbread embedding model?",
            input=["Document 1", "Document 2"],
            rank_fields=["content", "title"],
            top_k=10,
            return_input=False,
            rewrite_query=False,
        )
        assert_matches_type(RerankResponse, client, path=["response"])

    @parametrize
    async def test_raw_response_rerank(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.with_raw_response.rerank(
            query="What are the key features of the Mixedbread embedding model?",
            input=["Document 1", "Document 2"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(RerankResponse, client, path=["response"])

    @parametrize
    async def test_streaming_response_rerank(self, async_client: AsyncMixedbread) -> None:
        async with async_client.with_streaming_response.rerank(
            query="What are the key features of the Mixedbread embedding model?",
            input=["Document 1", "Document 2"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(RerankResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True
