# File generated from our OpenAPI spec by sdkgen. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixedbread import Mixedbread, AsyncMixedbread
from tests.utils import assert_matches_type
from mixedbread.types.stores import StoreFileBatch

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFileBatches:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Mixedbread) -> None:
        file_batch = client.stores.file_batches.create(
            store_identifier="store_identifier",
            files=[
                {
                    "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "external_id": "external_id",
                    "metadata": {},
                    "config": {"parsing_strategy": "fast"},
                }
            ],
        )
        assert_matches_type(StoreFileBatch, file_batch, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Mixedbread) -> None:
        response = client.stores.file_batches.with_raw_response.create(
            store_identifier="store_identifier",
            files=[
                {
                    "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "external_id": "external_id",
                    "metadata": {},
                    "config": {"parsing_strategy": "fast"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_batch = response.parse()
        assert_matches_type(StoreFileBatch, file_batch, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Mixedbread) -> None:
        with client.stores.file_batches.with_streaming_response.create(
            store_identifier="store_identifier",
            files=[
                {
                    "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "external_id": "external_id",
                    "metadata": {},
                    "config": {"parsing_strategy": "fast"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_batch = response.parse()
            assert_matches_type(StoreFileBatch, file_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `store_identifier` but received ''"):
            client.stores.file_batches.with_raw_response.create(
                store_identifier="",
                files=[
                    {
                        "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "external_id": "external_id",
                        "metadata": {},
                        "config": {"parsing_strategy": "fast"},
                    }
                ],
            )


class TestAsyncFileBatches:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncMixedbread) -> None:
        file_batch = await async_client.stores.file_batches.create(
            store_identifier="store_identifier",
            files=[
                {
                    "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "external_id": "external_id",
                    "metadata": {},
                    "config": {"parsing_strategy": "fast"},
                }
            ],
        )
        assert_matches_type(StoreFileBatch, file_batch, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.stores.file_batches.with_raw_response.create(
            store_identifier="store_identifier",
            files=[
                {
                    "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "external_id": "external_id",
                    "metadata": {},
                    "config": {"parsing_strategy": "fast"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_batch = await response.parse()
        assert_matches_type(StoreFileBatch, file_batch, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMixedbread) -> None:
        async with async_client.stores.file_batches.with_streaming_response.create(
            store_identifier="store_identifier",
            files=[
                {
                    "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "external_id": "external_id",
                    "metadata": {},
                    "config": {"parsing_strategy": "fast"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_batch = await response.parse()
            assert_matches_type(StoreFileBatch, file_batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `store_identifier` but received ''"):
            await async_client.stores.file_batches.with_raw_response.create(
                store_identifier="",
                files=[
                    {
                        "file_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "external_id": "external_id",
                        "metadata": {},
                        "config": {"parsing_strategy": "fast"},
                    }
                ],
            )
