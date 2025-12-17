# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixedbread import Mixedbread, AsyncMixedbread
from tests.utils import assert_matches_type
from mixedbread.types.stores import (
    StoreFile,
    FileListResponse,
    FileDeleteResponse,
    FileSearchResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Mixedbread) -> None:
        file = client.stores.files.create(
            store_identifier="store_identifier",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(StoreFile, file, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Mixedbread) -> None:
        file = client.stores.files.create(
            store_identifier="store_identifier",
            metadata={},
            config={"parsing_strategy": "fast"},
            external_id="external_id",
            overwrite=False,
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            experimental={"parsing_strategy": "fast"},
        )
        assert_matches_type(StoreFile, file, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Mixedbread) -> None:
        response = client.stores.files.with_raw_response.create(
            store_identifier="store_identifier",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(StoreFile, file, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Mixedbread) -> None:
        with client.stores.files.with_streaming_response.create(
            store_identifier="store_identifier",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(StoreFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `store_identifier` but received ''"):
            client.stores.files.with_raw_response.create(
                store_identifier="",
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_retrieve(self, client: Mixedbread) -> None:
        file = client.stores.files.retrieve(
            file_identifier="file_identifier",
            store_identifier="store_identifier",
        )
        assert_matches_type(StoreFile, file, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Mixedbread) -> None:
        file = client.stores.files.retrieve(
            file_identifier="file_identifier",
            store_identifier="store_identifier",
            return_chunks=True,
        )
        assert_matches_type(StoreFile, file, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Mixedbread) -> None:
        response = client.stores.files.with_raw_response.retrieve(
            file_identifier="file_identifier",
            store_identifier="store_identifier",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(StoreFile, file, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Mixedbread) -> None:
        with client.stores.files.with_streaming_response.retrieve(
            file_identifier="file_identifier",
            store_identifier="store_identifier",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(StoreFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `store_identifier` but received ''"):
            client.stores.files.with_raw_response.retrieve(
                file_identifier="file_identifier",
                store_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_identifier` but received ''"):
            client.stores.files.with_raw_response.retrieve(
                file_identifier="",
                store_identifier="store_identifier",
            )

    @parametrize
    def test_method_update(self, client: Mixedbread) -> None:
        file = client.stores.files.update(
            file_identifier="file_identifier",
            store_identifier="store_identifier",
        )
        assert_matches_type(StoreFile, file, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Mixedbread) -> None:
        file = client.stores.files.update(
            file_identifier="file_identifier",
            store_identifier="store_identifier",
            metadata={"foo": "bar"},
        )
        assert_matches_type(StoreFile, file, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Mixedbread) -> None:
        response = client.stores.files.with_raw_response.update(
            file_identifier="file_identifier",
            store_identifier="store_identifier",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(StoreFile, file, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Mixedbread) -> None:
        with client.stores.files.with_streaming_response.update(
            file_identifier="file_identifier",
            store_identifier="store_identifier",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(StoreFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `store_identifier` but received ''"):
            client.stores.files.with_raw_response.update(
                file_identifier="file_identifier",
                store_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_identifier` but received ''"):
            client.stores.files.with_raw_response.update(
                file_identifier="",
                store_identifier="store_identifier",
            )

    @parametrize
    def test_method_list(self, client: Mixedbread) -> None:
        file = client.stores.files.list(
            store_identifier="store_identifier",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Mixedbread) -> None:
        file = client.stores.files.list(
            store_identifier="store_identifier",
            limit=10,
            after="eyJjcmVhdGVkX2F0IjoiMjAyNC0xMi0zMVQyMzo1OTo1OS4wMDBaIiwiaWQiOiJhYmMxMjMifQ==",
            before="eyJjcmVhdGVkX2F0IjoiMjAyNC0xMi0zMVQyMzo1OTo1OS4wMDBaIiwiaWQiOiJhYmMxMjMifQ==",
            include_total=False,
            statuses=["pending"],
            metadata_filter={
                "all": [{}, {}],
                "any": [{}, {}],
                "none": [{}, {}],
            },
            q="x",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Mixedbread) -> None:
        response = client.stores.files.with_raw_response.list(
            store_identifier="store_identifier",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Mixedbread) -> None:
        with client.stores.files.with_streaming_response.list(
            store_identifier="store_identifier",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `store_identifier` but received ''"):
            client.stores.files.with_raw_response.list(
                store_identifier="",
            )

    @parametrize
    def test_method_delete(self, client: Mixedbread) -> None:
        file = client.stores.files.delete(
            file_identifier="file_identifier",
            store_identifier="store_identifier",
        )
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Mixedbread) -> None:
        response = client.stores.files.with_raw_response.delete(
            file_identifier="file_identifier",
            store_identifier="store_identifier",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Mixedbread) -> None:
        with client.stores.files.with_streaming_response.delete(
            file_identifier="file_identifier",
            store_identifier="store_identifier",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileDeleteResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `store_identifier` but received ''"):
            client.stores.files.with_raw_response.delete(
                file_identifier="file_identifier",
                store_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_identifier` but received ''"):
            client.stores.files.with_raw_response.delete(
                file_identifier="",
                store_identifier="store_identifier",
            )

    @parametrize
    def test_method_search(self, client: Mixedbread) -> None:
        file = client.stores.files.search(
            query="how to configure SSL",
            store_identifiers=["string"],
        )
        assert_matches_type(FileSearchResponse, file, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Mixedbread) -> None:
        file = client.stores.files.search(
            query="how to configure SSL",
            store_identifiers=["string"],
            top_k=1,
            filters={
                "all": [{}, {}],
                "any": [{}, {}],
                "none": [{}, {}],
            },
            file_ids=["123e4567-e89b-12d3-a456-426614174000", "123e4567-e89b-12d3-a456-426614174001"],
            search_options={
                "score_threshold": 0,
                "rewrite_query": True,
                "rerank": True,
                "return_metadata": True,
                "return_chunks": True,
                "chunks_per_file": 0,
                "apply_search_rules": True,
            },
        )
        assert_matches_type(FileSearchResponse, file, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Mixedbread) -> None:
        response = client.stores.files.with_raw_response.search(
            query="how to configure SSL",
            store_identifiers=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileSearchResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Mixedbread) -> None:
        with client.stores.files.with_streaming_response.search(
            query="how to configure SSL",
            store_identifiers=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileSearchResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncMixedbread) -> None:
        file = await async_client.stores.files.create(
            store_identifier="store_identifier",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(StoreFile, file, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMixedbread) -> None:
        file = await async_client.stores.files.create(
            store_identifier="store_identifier",
            metadata={},
            config={"parsing_strategy": "fast"},
            external_id="external_id",
            overwrite=False,
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            experimental={"parsing_strategy": "fast"},
        )
        assert_matches_type(StoreFile, file, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.stores.files.with_raw_response.create(
            store_identifier="store_identifier",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(StoreFile, file, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMixedbread) -> None:
        async with async_client.stores.files.with_streaming_response.create(
            store_identifier="store_identifier",
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(StoreFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `store_identifier` but received ''"):
            await async_client.stores.files.with_raw_response.create(
                store_identifier="",
                file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMixedbread) -> None:
        file = await async_client.stores.files.retrieve(
            file_identifier="file_identifier",
            store_identifier="store_identifier",
        )
        assert_matches_type(StoreFile, file, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMixedbread) -> None:
        file = await async_client.stores.files.retrieve(
            file_identifier="file_identifier",
            store_identifier="store_identifier",
            return_chunks=True,
        )
        assert_matches_type(StoreFile, file, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.stores.files.with_raw_response.retrieve(
            file_identifier="file_identifier",
            store_identifier="store_identifier",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(StoreFile, file, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMixedbread) -> None:
        async with async_client.stores.files.with_streaming_response.retrieve(
            file_identifier="file_identifier",
            store_identifier="store_identifier",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(StoreFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `store_identifier` but received ''"):
            await async_client.stores.files.with_raw_response.retrieve(
                file_identifier="file_identifier",
                store_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_identifier` but received ''"):
            await async_client.stores.files.with_raw_response.retrieve(
                file_identifier="",
                store_identifier="store_identifier",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncMixedbread) -> None:
        file = await async_client.stores.files.update(
            file_identifier="file_identifier",
            store_identifier="store_identifier",
        )
        assert_matches_type(StoreFile, file, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMixedbread) -> None:
        file = await async_client.stores.files.update(
            file_identifier="file_identifier",
            store_identifier="store_identifier",
            metadata={"foo": "bar"},
        )
        assert_matches_type(StoreFile, file, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.stores.files.with_raw_response.update(
            file_identifier="file_identifier",
            store_identifier="store_identifier",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(StoreFile, file, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMixedbread) -> None:
        async with async_client.stores.files.with_streaming_response.update(
            file_identifier="file_identifier",
            store_identifier="store_identifier",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(StoreFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `store_identifier` but received ''"):
            await async_client.stores.files.with_raw_response.update(
                file_identifier="file_identifier",
                store_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_identifier` but received ''"):
            await async_client.stores.files.with_raw_response.update(
                file_identifier="",
                store_identifier="store_identifier",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncMixedbread) -> None:
        file = await async_client.stores.files.list(
            store_identifier="store_identifier",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMixedbread) -> None:
        file = await async_client.stores.files.list(
            store_identifier="store_identifier",
            limit=10,
            after="eyJjcmVhdGVkX2F0IjoiMjAyNC0xMi0zMVQyMzo1OTo1OS4wMDBaIiwiaWQiOiJhYmMxMjMifQ==",
            before="eyJjcmVhdGVkX2F0IjoiMjAyNC0xMi0zMVQyMzo1OTo1OS4wMDBaIiwiaWQiOiJhYmMxMjMifQ==",
            include_total=False,
            statuses=["pending"],
            metadata_filter={
                "all": [{}, {}],
                "any": [{}, {}],
                "none": [{}, {}],
            },
            q="x",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.stores.files.with_raw_response.list(
            store_identifier="store_identifier",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMixedbread) -> None:
        async with async_client.stores.files.with_streaming_response.list(
            store_identifier="store_identifier",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `store_identifier` but received ''"):
            await async_client.stores.files.with_raw_response.list(
                store_identifier="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncMixedbread) -> None:
        file = await async_client.stores.files.delete(
            file_identifier="file_identifier",
            store_identifier="store_identifier",
        )
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.stores.files.with_raw_response.delete(
            file_identifier="file_identifier",
            store_identifier="store_identifier",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMixedbread) -> None:
        async with async_client.stores.files.with_streaming_response.delete(
            file_identifier="file_identifier",
            store_identifier="store_identifier",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileDeleteResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `store_identifier` but received ''"):
            await async_client.stores.files.with_raw_response.delete(
                file_identifier="file_identifier",
                store_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_identifier` but received ''"):
            await async_client.stores.files.with_raw_response.delete(
                file_identifier="",
                store_identifier="store_identifier",
            )

    @parametrize
    async def test_method_search(self, async_client: AsyncMixedbread) -> None:
        file = await async_client.stores.files.search(
            query="how to configure SSL",
            store_identifiers=["string"],
        )
        assert_matches_type(FileSearchResponse, file, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncMixedbread) -> None:
        file = await async_client.stores.files.search(
            query="how to configure SSL",
            store_identifiers=["string"],
            top_k=1,
            filters={
                "all": [{}, {}],
                "any": [{}, {}],
                "none": [{}, {}],
            },
            file_ids=["123e4567-e89b-12d3-a456-426614174000", "123e4567-e89b-12d3-a456-426614174001"],
            search_options={
                "score_threshold": 0,
                "rewrite_query": True,
                "rerank": True,
                "return_metadata": True,
                "return_chunks": True,
                "chunks_per_file": 0,
                "apply_search_rules": True,
            },
        )
        assert_matches_type(FileSearchResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.stores.files.with_raw_response.search(
            query="how to configure SSL",
            store_identifiers=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileSearchResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncMixedbread) -> None:
        async with async_client.stores.files.with_streaming_response.search(
            query="how to configure SSL",
            store_identifiers=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileSearchResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True
