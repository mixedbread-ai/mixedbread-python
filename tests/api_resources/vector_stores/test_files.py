# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixedbread import Mixedbread, AsyncMixedbread
from tests.utils import assert_matches_type
from mixedbread.types.vector_stores import (
    VectorStoreFileObject,
    VectorStoreFileDeleted,
    VectorStoreFileListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Mixedbread) -> None:
        file = client.vector_stores.files.create(
            vector_store_id="vector_store_id",
            file_id="file_id",
            metadata={},
        )
        assert_matches_type(VectorStoreFileObject, file, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Mixedbread) -> None:
        response = client.vector_stores.files.with_raw_response.create(
            vector_store_id="vector_store_id",
            file_id="file_id",
            metadata={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(VectorStoreFileObject, file, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Mixedbread) -> None:
        with client.vector_stores.files.with_streaming_response.create(
            vector_store_id="vector_store_id",
            file_id="file_id",
            metadata={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(VectorStoreFileObject, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.vector_stores.files.with_raw_response.create(
                vector_store_id="",
                file_id="file_id",
                metadata={},
            )

    @parametrize
    def test_method_retrieve(self, client: Mixedbread) -> None:
        file = client.vector_stores.files.retrieve(
            file_id="file_id",
            vector_store_id="vector_store_id",
        )
        assert_matches_type(VectorStoreFileObject, file, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Mixedbread) -> None:
        response = client.vector_stores.files.with_raw_response.retrieve(
            file_id="file_id",
            vector_store_id="vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(VectorStoreFileObject, file, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Mixedbread) -> None:
        with client.vector_stores.files.with_streaming_response.retrieve(
            file_id="file_id",
            vector_store_id="vector_store_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(VectorStoreFileObject, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.vector_stores.files.with_raw_response.retrieve(
                file_id="file_id",
                vector_store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.vector_stores.files.with_raw_response.retrieve(
                file_id="",
                vector_store_id="vector_store_id",
            )

    @parametrize
    def test_method_list(self, client: Mixedbread) -> None:
        file = client.vector_stores.files.list(
            vector_store_id="vector_store_id",
        )
        assert_matches_type(VectorStoreFileListResponse, file, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Mixedbread) -> None:
        file = client.vector_stores.files.list(
            vector_store_id="vector_store_id",
            after=0,
            limit=0,
        )
        assert_matches_type(VectorStoreFileListResponse, file, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Mixedbread) -> None:
        response = client.vector_stores.files.with_raw_response.list(
            vector_store_id="vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(VectorStoreFileListResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Mixedbread) -> None:
        with client.vector_stores.files.with_streaming_response.list(
            vector_store_id="vector_store_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(VectorStoreFileListResponse, file, path=["response"])

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
            file_id="file_id",
            vector_store_id="vector_store_id",
        )
        assert_matches_type(VectorStoreFileDeleted, file, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Mixedbread) -> None:
        response = client.vector_stores.files.with_raw_response.delete(
            file_id="file_id",
            vector_store_id="vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(VectorStoreFileDeleted, file, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Mixedbread) -> None:
        with client.vector_stores.files.with_streaming_response.delete(
            file_id="file_id",
            vector_store_id="vector_store_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(VectorStoreFileDeleted, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            client.vector_stores.files.with_raw_response.delete(
                file_id="file_id",
                vector_store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.vector_stores.files.with_raw_response.delete(
                file_id="",
                vector_store_id="vector_store_id",
            )


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMixedbread) -> None:
        file = await async_client.vector_stores.files.create(
            vector_store_id="vector_store_id",
            file_id="file_id",
            metadata={},
        )
        assert_matches_type(VectorStoreFileObject, file, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.vector_stores.files.with_raw_response.create(
            vector_store_id="vector_store_id",
            file_id="file_id",
            metadata={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(VectorStoreFileObject, file, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMixedbread) -> None:
        async with async_client.vector_stores.files.with_streaming_response.create(
            vector_store_id="vector_store_id",
            file_id="file_id",
            metadata={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(VectorStoreFileObject, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.vector_stores.files.with_raw_response.create(
                vector_store_id="",
                file_id="file_id",
                metadata={},
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMixedbread) -> None:
        file = await async_client.vector_stores.files.retrieve(
            file_id="file_id",
            vector_store_id="vector_store_id",
        )
        assert_matches_type(VectorStoreFileObject, file, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.vector_stores.files.with_raw_response.retrieve(
            file_id="file_id",
            vector_store_id="vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(VectorStoreFileObject, file, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMixedbread) -> None:
        async with async_client.vector_stores.files.with_streaming_response.retrieve(
            file_id="file_id",
            vector_store_id="vector_store_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(VectorStoreFileObject, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.vector_stores.files.with_raw_response.retrieve(
                file_id="file_id",
                vector_store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.vector_stores.files.with_raw_response.retrieve(
                file_id="",
                vector_store_id="vector_store_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncMixedbread) -> None:
        file = await async_client.vector_stores.files.list(
            vector_store_id="vector_store_id",
        )
        assert_matches_type(VectorStoreFileListResponse, file, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMixedbread) -> None:
        file = await async_client.vector_stores.files.list(
            vector_store_id="vector_store_id",
            after=0,
            limit=0,
        )
        assert_matches_type(VectorStoreFileListResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.vector_stores.files.with_raw_response.list(
            vector_store_id="vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(VectorStoreFileListResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMixedbread) -> None:
        async with async_client.vector_stores.files.with_streaming_response.list(
            vector_store_id="vector_store_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(VectorStoreFileListResponse, file, path=["response"])

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
            file_id="file_id",
            vector_store_id="vector_store_id",
        )
        assert_matches_type(VectorStoreFileDeleted, file, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.vector_stores.files.with_raw_response.delete(
            file_id="file_id",
            vector_store_id="vector_store_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(VectorStoreFileDeleted, file, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMixedbread) -> None:
        async with async_client.vector_stores.files.with_streaming_response.delete(
            file_id="file_id",
            vector_store_id="vector_store_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(VectorStoreFileDeleted, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vector_store_id` but received ''"):
            await async_client.vector_stores.files.with_raw_response.delete(
                file_id="file_id",
                vector_store_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.vector_stores.files.with_raw_response.delete(
                file_id="",
                vector_store_id="vector_store_id",
            )
