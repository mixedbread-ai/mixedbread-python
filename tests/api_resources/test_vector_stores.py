# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixedbread import Mixedbread, AsyncMixedbread
from tests.utils import assert_matches_type
from mixedbread.types import (
    VectorStore,
    SearchResponse,
    VectorStoreListResponse,
    VectorStoreDeleteResponse,
)
from mixedbread._utils import parse_datetime

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
            description="description",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            metadata={},
            name="name",
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
            "vector_store_id",
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Mixedbread) -> None:
        response = client.vector_stores.with_raw_response.retrieve(
            "vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = response.parse()
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Mixedbread) -> None:
        with client.vector_stores.with_streaming_response.retrieve(
            "vector_store_id",
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
            vector_store_id="vector_store_id",
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Mixedbread) -> None:
        vector_store = client.vector_stores.update(
            vector_store_id="vector_store_id",
            description="description",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            metadata={},
            name="name",
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Mixedbread) -> None:
        response = client.vector_stores.with_raw_response.update(
            vector_store_id="vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = response.parse()
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Mixedbread) -> None:
        with client.vector_stores.with_streaming_response.update(
            vector_store_id="vector_store_id",
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
        assert_matches_type(VectorStoreListResponse, vector_store, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Mixedbread) -> None:
        vector_store = client.vector_stores.list(
            after=0,
            limit=0,
        )
        assert_matches_type(VectorStoreListResponse, vector_store, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Mixedbread) -> None:
        response = client.vector_stores.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = response.parse()
        assert_matches_type(VectorStoreListResponse, vector_store, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Mixedbread) -> None:
        with client.vector_stores.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = response.parse()
            assert_matches_type(VectorStoreListResponse, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Mixedbread) -> None:
        vector_store = client.vector_stores.delete(
            "vector_store_id",
        )
        assert_matches_type(VectorStoreDeleteResponse, vector_store, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Mixedbread) -> None:
        response = client.vector_stores.with_raw_response.delete(
            "vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = response.parse()
        assert_matches_type(VectorStoreDeleteResponse, vector_store, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Mixedbread) -> None:
        with client.vector_stores.with_streaming_response.delete(
            "vector_store_id",
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
    def test_method_search(self, client: Mixedbread) -> None:
        vector_store = client.vector_stores.search(
            query="query",
            vector_store_ids=["string", "string", "string"],
        )
        assert_matches_type(SearchResponse, vector_store, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Mixedbread) -> None:
        vector_store = client.vector_stores.search(
            query="query",
            vector_store_ids=["string", "string", "string"],
            after=0,
            filter={
                "and": {
                    "and": {},
                    "not": [
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                    ],
                    "or": [
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                    ],
                },
                "not": {
                    "and": [
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                    ],
                    "not": {},
                    "or": [
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                    ],
                },
                "or": {
                    "and": [
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                    ],
                    "not": [
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                    ],
                    "or": {},
                },
            },
            limit=0,
            options={
                "min_score": 0,
                "return_chunks": True,
                "return_metadata": True,
            },
        )
        assert_matches_type(SearchResponse, vector_store, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Mixedbread) -> None:
        response = client.vector_stores.with_raw_response.search(
            query="query",
            vector_store_ids=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = response.parse()
        assert_matches_type(SearchResponse, vector_store, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Mixedbread) -> None:
        with client.vector_stores.with_streaming_response.search(
            query="query",
            vector_store_ids=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = response.parse()
            assert_matches_type(SearchResponse, vector_store, path=["response"])

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
            description="description",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            metadata={},
            name="name",
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
            "vector_store_id",
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.vector_stores.with_raw_response.retrieve(
            "vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = await response.parse()
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMixedbread) -> None:
        async with async_client.vector_stores.with_streaming_response.retrieve(
            "vector_store_id",
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
            vector_store_id="vector_store_id",
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMixedbread) -> None:
        vector_store = await async_client.vector_stores.update(
            vector_store_id="vector_store_id",
            description="description",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            metadata={},
            name="name",
        )
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.vector_stores.with_raw_response.update(
            vector_store_id="vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = await response.parse()
        assert_matches_type(VectorStore, vector_store, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMixedbread) -> None:
        async with async_client.vector_stores.with_streaming_response.update(
            vector_store_id="vector_store_id",
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
        assert_matches_type(VectorStoreListResponse, vector_store, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMixedbread) -> None:
        vector_store = await async_client.vector_stores.list(
            after=0,
            limit=0,
        )
        assert_matches_type(VectorStoreListResponse, vector_store, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.vector_stores.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = await response.parse()
        assert_matches_type(VectorStoreListResponse, vector_store, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMixedbread) -> None:
        async with async_client.vector_stores.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = await response.parse()
            assert_matches_type(VectorStoreListResponse, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncMixedbread) -> None:
        vector_store = await async_client.vector_stores.delete(
            "vector_store_id",
        )
        assert_matches_type(VectorStoreDeleteResponse, vector_store, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.vector_stores.with_raw_response.delete(
            "vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = await response.parse()
        assert_matches_type(VectorStoreDeleteResponse, vector_store, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMixedbread) -> None:
        async with async_client.vector_stores.with_streaming_response.delete(
            "vector_store_id",
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
    async def test_method_search(self, async_client: AsyncMixedbread) -> None:
        vector_store = await async_client.vector_stores.search(
            query="query",
            vector_store_ids=["string", "string", "string"],
        )
        assert_matches_type(SearchResponse, vector_store, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncMixedbread) -> None:
        vector_store = await async_client.vector_stores.search(
            query="query",
            vector_store_ids=["string", "string", "string"],
            after=0,
            filter={
                "and": {
                    "and": {},
                    "not": [
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                    ],
                    "or": [
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                    ],
                },
                "not": {
                    "and": [
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                    ],
                    "not": {},
                    "or": [
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                    ],
                },
                "or": {
                    "and": [
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                    ],
                    "not": [
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                        {
                            "key": "price",
                            "operator": "eq",
                            "value": {},
                        },
                    ],
                    "or": {},
                },
            },
            limit=0,
            options={
                "min_score": 0,
                "return_chunks": True,
                "return_metadata": True,
            },
        )
        assert_matches_type(SearchResponse, vector_store, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.vector_stores.with_raw_response.search(
            query="query",
            vector_store_ids=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vector_store = await response.parse()
        assert_matches_type(SearchResponse, vector_store, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncMixedbread) -> None:
        async with async_client.vector_stores.with_streaming_response.search(
            query="query",
            vector_store_ids=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vector_store = await response.parse()
            assert_matches_type(SearchResponse, vector_store, path=["response"])

        assert cast(Any, response.is_closed) is True
