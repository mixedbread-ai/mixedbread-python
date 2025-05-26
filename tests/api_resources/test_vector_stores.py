# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixedbread import Mixedbread, AsyncMixedbread
from tests.utils import assert_matches_type
from mixedbread.types import (
    VectorStore,
    VectorStoreDeleteResponse,
    VectorStoreSearchResponse,
    VectorStoreQuestionAnsweringResponse,
)
from mixedbread.pagination import SyncLimitOffset, AsyncLimitOffset

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVectorStores:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Mixedbread) -> None:
        vector_store = client.vector_stores.create()
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Mixedbread) -> None:
        vector_store = client.vector_stores.create(
            name="Technical Documentation",
            description="Contains technical specifications and guides",
            expires_after={
                "anchor": "last_active_at",
                "days": 0,
            },
            metadata={},
            file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Mixedbread) -> None:
        response = client.vector_stores.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = response.parse()
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Mixedbread) -> None:
        with client.vector_stores.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = response.parse()
            assert_matches_type(VectorStore, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Mixedbread) -> None:
        vector_store = client.vector_stores.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Mixedbread) -> None:
        response = client.vector_stores.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = response.parse()
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Mixedbread) -> None:
        with client.vector_stores.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = response.parse()
            assert_matches_type(VectorStore, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.vector_stores.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Mixedbread) -> None:
        vector_store = client.vector_stores.update(
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Mixedbread) -> None:
        vector_store = client.vector_stores.update(
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
            description="description",
            expires_after={
                "anchor": "last_active_at",
                "days": 0,
            },
            metadata={},
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Mixedbread) -> None:
        response = client.vector_stores.with_raw_response.update(
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = response.parse()
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Mixedbread) -> None:
        with client.vector_stores.with_streaming_response.update(
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = response.parse()
            assert_matches_type(VectorStore, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.vector_stores.with_raw_response.update(
                vector_store_id="",
            )

    @parametrize
    def test_method_list(self, client: Mixedbread) -> None:
        vector_store = client.vector_stores.list()
        assert_matches_type(SyncLimitOffset[VectorStore], vector_store, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Mixedbread) -> None:
        vector_store = client.vector_stores.list(
            limit=1000,
            offset=0,
        )
        assert_matches_type(SyncLimitOffset[VectorStore], vector_store, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Mixedbread) -> None:
        response = client.vector_stores.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = response.parse()
        assert_matches_type(SyncLimitOffset[VectorStore], vector_store, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Mixedbread) -> None:
        with client.vector_stores.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = response.parse()
            assert_matches_type(SyncLimitOffset[VectorStore], vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Mixedbread) -> None:
        vector_store = client.vector_stores.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VectorStoreDeleteResponse, vector_store, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Mixedbread) -> None:
        response = client.vector_stores.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = response.parse()
        assert_matches_type(VectorStoreDeleteResponse, vector_store, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Mixedbread) -> None:
        with client.vector_stores.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = response.parse()
            assert_matches_type(VectorStoreDeleteResponse, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.vector_stores.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_question_answering(self, client: Mixedbread) -> None:
        vector_store = client.vector_stores.question_answering(
            vector_store_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(VectorStoreQuestionAnsweringResponse, vector_store, path=["response"])

    @parametrize
    def test_method_question_answering_with_all_params(self, client: Mixedbread) -> None:
        vector_store = client.vector_stores.question_answering(
            query="x",
            vector_store_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            top_k=1,
            filters={
                "all": [
                    {
                        "key": "price",
                        "value": "100",
                        "operator": "gt",
                    },
                    {
                        "key": "color",
                        "value": "red",
                        "operator": "eq",
                    },
                ],
                "any": [
                    {
                        "key": "price",
                        "value": "100",
                        "operator": "gt",
                    },
                    {
                        "key": "color",
                        "value": "red",
                        "operator": "eq",
                    },
                ],
                "none": [
                    {
                        "key": "price",
                        "value": "100",
                        "operator": "gt",
                    },
                    {
                        "key": "color",
                        "value": "red",
                        "operator": "eq",
                    },
                ],
            },
            search_options={
                "score_threshold": 0,
                "rewrite_query": True,
                "return_metadata": True,
            },
            stream=True,
            qa_options={
                "cite": True,
                "multimodal": True,
            },
        )
        assert_matches_type(VectorStoreQuestionAnsweringResponse, vector_store, path=["response"])

    @parametrize
    def test_raw_response_question_answering(self, client: Mixedbread) -> None:
        response = client.vector_stores.with_raw_response.question_answering(
            vector_store_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = response.parse()
        assert_matches_type(VectorStoreQuestionAnsweringResponse, vector_store, path=["response"])

    @parametrize
    def test_streaming_response_question_answering(self, client: Mixedbread) -> None:
        with client.vector_stores.with_streaming_response.question_answering(
            vector_store_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = response.parse()
            assert_matches_type(VectorStoreQuestionAnsweringResponse, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search(self, client: Mixedbread) -> None:
        vector_store = client.vector_stores.search(
            query="how to configure SSL",
            vector_store_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(VectorStoreSearchResponse, vector_store, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Mixedbread) -> None:
        vector_store = client.vector_stores.search(
            query="how to configure SSL",
            vector_store_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            top_k=1,
            filters={
                "all": [
                    {
                        "key": "price",
                        "value": "100",
                        "operator": "gt",
                    },
                    {
                        "key": "color",
                        "value": "red",
                        "operator": "eq",
                    },
                ],
                "any": [
                    {
                        "key": "price",
                        "value": "100",
                        "operator": "gt",
                    },
                    {
                        "key": "color",
                        "value": "red",
                        "operator": "eq",
                    },
                ],
                "none": [
                    {
                        "key": "price",
                        "value": "100",
                        "operator": "gt",
                    },
                    {
                        "key": "color",
                        "value": "red",
                        "operator": "eq",
                    },
                ],
            },
            search_options={
                "score_threshold": 0,
                "rewrite_query": True,
                "return_metadata": True,
            },
        )
        assert_matches_type(VectorStoreSearchResponse, vector_store, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Mixedbread) -> None:
        response = client.vector_stores.with_raw_response.search(
            query="how to configure SSL",
            vector_store_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = response.parse()
        assert_matches_type(VectorStoreSearchResponse, vector_store, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Mixedbread) -> None:
        with client.vector_stores.with_streaming_response.search(
            query="how to configure SSL",
            vector_store_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = response.parse()
            assert_matches_type(VectorStoreSearchResponse, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVectorStores:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMixedbread) -> None:
        vector_store = await async_client.vector_stores.create()
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMixedbread) -> None:
        vector_store = await async_client.vector_stores.create(
            name="Technical Documentation",
            description="Contains technical specifications and guides",
            expires_after={
                "anchor": "last_active_at",
                "days": 0,
            },
            metadata={},
            file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.vector_stores.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = await response.parse()
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMixedbread) -> None:
        async with async_client.vector_stores.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = await response.parse()
            assert_matches_type(VectorStore, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMixedbread) -> None:
        vector_store = await async_client.vector_stores.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.vector_stores.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = await response.parse()
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMixedbread) -> None:
        async with async_client.vector_stores.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = await response.parse()
            assert_matches_type(VectorStore, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.vector_stores.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncMixedbread) -> None:
        vector_store = await async_client.vector_stores.update(
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMixedbread) -> None:
        vector_store = await async_client.vector_stores.update(
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
            description="description",
            expires_after={
                "anchor": "last_active_at",
                "days": 0,
            },
            metadata={},
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.vector_stores.with_raw_response.update(
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = await response.parse()
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMixedbread) -> None:
        async with async_client.vector_stores.with_streaming_response.update(
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = await response.parse()
            assert_matches_type(VectorStore, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.vector_stores.with_raw_response.update(
                vector_store_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncMixedbread) -> None:
        vector_store = await async_client.vector_stores.list()
        assert_matches_type(AsyncLimitOffset[VectorStore], vector_store, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMixedbread) -> None:
        vector_store = await async_client.vector_stores.list(
            limit=1000,
            offset=0,
        )
        assert_matches_type(AsyncLimitOffset[VectorStore], vector_store, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.vector_stores.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = await response.parse()
        assert_matches_type(AsyncLimitOffset[VectorStore], vector_store, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMixedbread) -> None:
        async with async_client.vector_stores.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = await response.parse()
            assert_matches_type(AsyncLimitOffset[VectorStore], vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncMixedbread) -> None:
        vector_store = await async_client.vector_stores.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VectorStoreDeleteResponse, vector_store, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.vector_stores.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = await response.parse()
        assert_matches_type(VectorStoreDeleteResponse, vector_store, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMixedbread) -> None:
        async with async_client.vector_stores.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = await response.parse()
            assert_matches_type(VectorStoreDeleteResponse, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.vector_stores.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_question_answering(self, async_client: AsyncMixedbread) -> None:
        vector_store = await async_client.vector_stores.question_answering(
            vector_store_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(VectorStoreQuestionAnsweringResponse, vector_store, path=["response"])

    @parametrize
    async def test_method_question_answering_with_all_params(self, async_client: AsyncMixedbread) -> None:
        vector_store = await async_client.vector_stores.question_answering(
            query="x",
            vector_store_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            top_k=1,
            filters={
                "all": [
                    {
                        "key": "price",
                        "value": "100",
                        "operator": "gt",
                    },
                    {
                        "key": "color",
                        "value": "red",
                        "operator": "eq",
                    },
                ],
                "any": [
                    {
                        "key": "price",
                        "value": "100",
                        "operator": "gt",
                    },
                    {
                        "key": "color",
                        "value": "red",
                        "operator": "eq",
                    },
                ],
                "none": [
                    {
                        "key": "price",
                        "value": "100",
                        "operator": "gt",
                    },
                    {
                        "key": "color",
                        "value": "red",
                        "operator": "eq",
                    },
                ],
            },
            search_options={
                "score_threshold": 0,
                "rewrite_query": True,
                "return_metadata": True,
            },
            stream=True,
            qa_options={
                "cite": True,
                "multimodal": True,
            },
        )
        assert_matches_type(VectorStoreQuestionAnsweringResponse, vector_store, path=["response"])

    @parametrize
    async def test_raw_response_question_answering(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.vector_stores.with_raw_response.question_answering(
            vector_store_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = await response.parse()
        assert_matches_type(VectorStoreQuestionAnsweringResponse, vector_store, path=["response"])

    @parametrize
    async def test_streaming_response_question_answering(self, async_client: AsyncMixedbread) -> None:
        async with async_client.vector_stores.with_streaming_response.question_answering(
            vector_store_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = await response.parse()
            assert_matches_type(VectorStoreQuestionAnsweringResponse, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search(self, async_client: AsyncMixedbread) -> None:
        vector_store = await async_client.vector_stores.search(
            query="how to configure SSL",
            vector_store_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(VectorStoreSearchResponse, vector_store, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncMixedbread) -> None:
        vector_store = await async_client.vector_stores.search(
            query="how to configure SSL",
            vector_store_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            top_k=1,
            filters={
                "all": [
                    {
                        "key": "price",
                        "value": "100",
                        "operator": "gt",
                    },
                    {
                        "key": "color",
                        "value": "red",
                        "operator": "eq",
                    },
                ],
                "any": [
                    {
                        "key": "price",
                        "value": "100",
                        "operator": "gt",
                    },
                    {
                        "key": "color",
                        "value": "red",
                        "operator": "eq",
                    },
                ],
                "none": [
                    {
                        "key": "price",
                        "value": "100",
                        "operator": "gt",
                    },
                    {
                        "key": "color",
                        "value": "red",
                        "operator": "eq",
                    },
                ],
            },
            search_options={
                "score_threshold": 0,
                "rewrite_query": True,
                "return_metadata": True,
            },
        )
        assert_matches_type(VectorStoreSearchResponse, vector_store, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.vector_stores.with_raw_response.search(
            query="how to configure SSL",
            vector_store_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = await response.parse()
        assert_matches_type(VectorStoreSearchResponse, vector_store, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncMixedbread) -> None:
        async with async_client.vector_stores.with_streaming_response.search(
            query="how to configure SSL",
            vector_store_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = await response.parse()
            assert_matches_type(VectorStoreSearchResponse, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True
