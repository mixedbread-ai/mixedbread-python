# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixedbread import Mixedbread, AsyncMixedbread
from tests.utils import assert_matches_type
from mixedbread.types import EmbeddingCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmbeddings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Mixedbread) -> None:
        embedding = client.embeddings.create(
            model="mixedbread-ai/mxbai-embed-large-v1",
            input="x",
        )
        assert_matches_type(EmbeddingCreateResponse, embedding, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Mixedbread) -> None:
        embedding = client.embeddings.create(
            model="mixedbread-ai/mxbai-embed-large-v1",
            input="x",
            dimensions=768,
            prompt="Provide a detailed summary of the following text.",
            normalized=True,
            encoding_format="float",
        )
        assert_matches_type(EmbeddingCreateResponse, embedding, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Mixedbread) -> None:
        response = client.embeddings.with_raw_response.create(
            model="mixedbread-ai/mxbai-embed-large-v1",
            input="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = response.parse()
        assert_matches_type(EmbeddingCreateResponse, embedding, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Mixedbread) -> None:
        with client.embeddings.with_streaming_response.create(
            model="mixedbread-ai/mxbai-embed-large-v1",
            input="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = response.parse()
            assert_matches_type(EmbeddingCreateResponse, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmbeddings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMixedbread) -> None:
        embedding = await async_client.embeddings.create(
            model="mixedbread-ai/mxbai-embed-large-v1",
            input="x",
        )
        assert_matches_type(EmbeddingCreateResponse, embedding, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMixedbread) -> None:
        embedding = await async_client.embeddings.create(
            model="mixedbread-ai/mxbai-embed-large-v1",
            input="x",
            dimensions=768,
            prompt="Provide a detailed summary of the following text.",
            normalized=True,
            encoding_format="float",
        )
        assert_matches_type(EmbeddingCreateResponse, embedding, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.embeddings.with_raw_response.create(
            model="mixedbread-ai/mxbai-embed-large-v1",
            input="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        embedding = await response.parse()
        assert_matches_type(EmbeddingCreateResponse, embedding, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMixedbread) -> None:
        async with async_client.embeddings.with_streaming_response.create(
            model="mixedbread-ai/mxbai-embed-large-v1",
            input="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            embedding = await response.parse()
            assert_matches_type(EmbeddingCreateResponse, embedding, path=["response"])

        assert cast(Any, response.is_closed) is True
