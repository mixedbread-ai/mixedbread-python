# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixedbread import Mixedbread, AsyncMixedbread
from tests.utils import assert_matches_type
from mixedbread.types import InfoResponse, ServiceStatusRerankResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServiceStatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Mixedbread) -> None:
        service_status = client.service_status.retrieve()
        assert_matches_type(InfoResponse, service_status, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Mixedbread) -> None:
        response = client.service_status.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_status = response.parse()
        assert_matches_type(InfoResponse, service_status, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Mixedbread) -> None:
        with client.service_status.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_status = response.parse()
            assert_matches_type(InfoResponse, service_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_rerank(self, client: Mixedbread) -> None:
        service_status = client.service_status.rerank(
            input=["Document 1", "Document 2"],
            query="What is mixedbread ai?",
        )
        assert_matches_type(ServiceStatusRerankResponse, service_status, path=["response"])

    @parametrize
    def test_method_rerank_with_all_params(self, client: Mixedbread) -> None:
        service_status = client.service_status.rerank(
            input=["Document 1", "Document 2"],
            query="What is mixedbread ai?",
            model="mixedbread-ai/mxbai-rerank-large-v1",
            rank_fields=["field1", "field2"],
            return_input=False,
            top_k=10,
        )
        assert_matches_type(ServiceStatusRerankResponse, service_status, path=["response"])

    @parametrize
    def test_raw_response_rerank(self, client: Mixedbread) -> None:
        response = client.service_status.with_raw_response.rerank(
            input=["Document 1", "Document 2"],
            query="What is mixedbread ai?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_status = response.parse()
        assert_matches_type(ServiceStatusRerankResponse, service_status, path=["response"])

    @parametrize
    def test_streaming_response_rerank(self, client: Mixedbread) -> None:
        with client.service_status.with_streaming_response.rerank(
            input=["Document 1", "Document 2"],
            query="What is mixedbread ai?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_status = response.parse()
            assert_matches_type(ServiceStatusRerankResponse, service_status, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncServiceStatus:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMixedbread) -> None:
        service_status = await async_client.service_status.retrieve()
        assert_matches_type(InfoResponse, service_status, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.service_status.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_status = await response.parse()
        assert_matches_type(InfoResponse, service_status, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMixedbread) -> None:
        async with async_client.service_status.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_status = await response.parse()
            assert_matches_type(InfoResponse, service_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_rerank(self, async_client: AsyncMixedbread) -> None:
        service_status = await async_client.service_status.rerank(
            input=["Document 1", "Document 2"],
            query="What is mixedbread ai?",
        )
        assert_matches_type(ServiceStatusRerankResponse, service_status, path=["response"])

    @parametrize
    async def test_method_rerank_with_all_params(self, async_client: AsyncMixedbread) -> None:
        service_status = await async_client.service_status.rerank(
            input=["Document 1", "Document 2"],
            query="What is mixedbread ai?",
            model="mixedbread-ai/mxbai-rerank-large-v1",
            rank_fields=["field1", "field2"],
            return_input=False,
            top_k=10,
        )
        assert_matches_type(ServiceStatusRerankResponse, service_status, path=["response"])

    @parametrize
    async def test_raw_response_rerank(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.service_status.with_raw_response.rerank(
            input=["Document 1", "Document 2"],
            query="What is mixedbread ai?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service_status = await response.parse()
        assert_matches_type(ServiceStatusRerankResponse, service_status, path=["response"])

    @parametrize
    async def test_streaming_response_rerank(self, async_client: AsyncMixedbread) -> None:
        async with async_client.service_status.with_streaming_response.rerank(
            input=["Document 1", "Document 2"],
            query="What is mixedbread ai?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service_status = await response.parse()
            assert_matches_type(ServiceStatusRerankResponse, service_status, path=["response"])

        assert cast(Any, response.is_closed) is True
