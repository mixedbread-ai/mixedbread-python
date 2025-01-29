# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixedbread import Mixedbread, AsyncMixedbread
from tests.utils import assert_matches_type
from mixedbread.pagination import SyncLimitOffset, AsyncLimitOffset
from mixedbread.types.vector_stores import (
    VectorStoreFile,
    FileDeleteResponse,
    FileSearchResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Mixedbread) -> None:
        file = client.vector_stores.files.create(
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Mixedbread) -> None:
        file = client.vector_stores.files.create(
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={},
            experimental={"parsing_strategy": "fast"},
        )
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Mixedbread) -> None:
        response = client.vector_stores.files.with_raw_response.create(
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Mixedbread) -> None:
        with client.vector_stores.files.with_streaming_response.create(
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(VectorStoreFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.vector_stores.files.with_raw_response.create(
                vector_store_id="",
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_retrieve(self, client: Mixedbread) -> None:
        file = client.vector_stores.files.retrieve(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Mixedbread) -> None:
        response = client.vector_stores.files.with_raw_response.retrieve(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Mixedbread) -> None:
        with client.vector_stores.files.with_streaming_response.retrieve(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(VectorStoreFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.vector_stores.files.with_raw_response.retrieve(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                vector_store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.vector_stores.files.with_raw_response.retrieve(
                file_id="",
                vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_list(self, client: Mixedbread) -> None:
        file = client.vector_stores.files.list(
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncLimitOffset[VectorStoreFile], file, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Mixedbread) -> None:
        file = client.vector_stores.files.list(
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1000,
            offset=0,
        )
        assert_matches_type(SyncLimitOffset[VectorStoreFile], file, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Mixedbread) -> None:
        response = client.vector_stores.files.with_raw_response.list(
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(SyncLimitOffset[VectorStoreFile], file, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Mixedbread) -> None:
        with client.vector_stores.files.with_streaming_response.list(
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(SyncLimitOffset[VectorStoreFile], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.vector_stores.files.with_raw_response.list(
                vector_store_id="",
            )

    @parametrize
    def test_method_delete(self, client: Mixedbread) -> None:
        file = client.vector_stores.files.delete(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Mixedbread) -> None:
        response = client.vector_stores.files.with_raw_response.delete(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Mixedbread) -> None:
        with client.vector_stores.files.with_streaming_response.delete(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileDeleteResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.vector_stores.files.with_raw_response.delete(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                vector_store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.vector_stores.files.with_raw_response.delete(
                file_id="",
                vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_search(self, client: Mixedbread) -> None:
        file = client.vector_stores.files.search(
            query="how to configure SSL",
            vector_store_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(FileSearchResponse, file, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Mixedbread) -> None:
        file = client.vector_stores.files.search(
            query="how to configure SSL",
            vector_store_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            top_k=1,
            filters={
                "all": [
                    {
                        "key": "price",
                        "value": "100",
                        "operator": "eq",
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
                        "operator": "eq",
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
                        "operator": "eq",
                    },
                    {
                        "key": "color",
                        "value": "red",
                        "operator": "eq",
                    },
                ],
            },
            search_options={
                "return_metadata": True,
                "return_chunks": True,
                "score_threshold": 0,
                "rewrite_query": True,
            },
        )
        assert_matches_type(FileSearchResponse, file, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Mixedbread) -> None:
        response = client.vector_stores.files.with_raw_response.search(
            query="how to configure SSL",
            vector_store_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileSearchResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Mixedbread) -> None:
        with client.vector_stores.files.with_streaming_response.search(
            query="how to configure SSL",
            vector_store_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileSearchResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMixedbread) -> None:
        file = await async_client.vector_stores.files.create(
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMixedbread) -> None:
        file = await async_client.vector_stores.files.create(
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={},
            experimental={"parsing_strategy": "fast"},
        )
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.vector_stores.files.with_raw_response.create(
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMixedbread) -> None:
        async with async_client.vector_stores.files.with_streaming_response.create(
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(VectorStoreFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.vector_stores.files.with_raw_response.create(
                vector_store_id="",
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMixedbread) -> None:
        file = await async_client.vector_stores.files.retrieve(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.vector_stores.files.with_raw_response.retrieve(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(VectorStoreFile, file, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMixedbread) -> None:
        async with async_client.vector_stores.files.with_streaming_response.retrieve(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(VectorStoreFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.vector_stores.files.with_raw_response.retrieve(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                vector_store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.vector_stores.files.with_raw_response.retrieve(
                file_id="",
                vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncMixedbread) -> None:
        file = await async_client.vector_stores.files.list(
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncLimitOffset[VectorStoreFile], file, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMixedbread) -> None:
        file = await async_client.vector_stores.files.list(
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1000,
            offset=0,
        )
        assert_matches_type(AsyncLimitOffset[VectorStoreFile], file, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.vector_stores.files.with_raw_response.list(
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(AsyncLimitOffset[VectorStoreFile], file, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMixedbread) -> None:
        async with async_client.vector_stores.files.with_streaming_response.list(
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(AsyncLimitOffset[VectorStoreFile], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.vector_stores.files.with_raw_response.list(
                vector_store_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncMixedbread) -> None:
        file = await async_client.vector_stores.files.delete(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.vector_stores.files.with_raw_response.delete(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMixedbread) -> None:
        async with async_client.vector_stores.files.with_streaming_response.delete(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileDeleteResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.vector_stores.files.with_raw_response.delete(
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                vector_store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.vector_stores.files.with_raw_response.delete(
                file_id="",
                vector_store_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_search(self, async_client: AsyncMixedbread) -> None:
        file = await async_client.vector_stores.files.search(
            query="how to configure SSL",
            vector_store_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(FileSearchResponse, file, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncMixedbread) -> None:
        file = await async_client.vector_stores.files.search(
            query="how to configure SSL",
            vector_store_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            top_k=1,
            filters={
                "all": [
                    {
                        "key": "price",
                        "value": "100",
                        "operator": "eq",
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
                        "operator": "eq",
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
                        "operator": "eq",
                    },
                    {
                        "key": "color",
                        "value": "red",
                        "operator": "eq",
                    },
                ],
            },
            search_options={
                "return_metadata": True,
                "return_chunks": True,
                "score_threshold": 0,
                "rewrite_query": True,
            },
        )
        assert_matches_type(FileSearchResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.vector_stores.files.with_raw_response.search(
            query="how to configure SSL",
            vector_store_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileSearchResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncMixedbread) -> None:
        async with async_client.vector_stores.files.with_streaming_response.search(
            query="how to configure SSL",
            vector_store_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileSearchResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True
