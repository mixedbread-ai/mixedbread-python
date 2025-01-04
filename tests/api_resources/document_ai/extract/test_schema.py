# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixedbread import Mixedbread, AsyncMixedbread
from tests.utils import assert_matches_type
from mixedbread.types.document_ai.extract import (
    CreatedJsonSchema,
    EnhancedJsonSchema,
    ValidatedJsonSchema,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSchema:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Mixedbread) -> None:
        schema = client.document_ai.extract.schema.create(
            description="description",
        )
        assert_matches_type(CreatedJsonSchema, schema, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Mixedbread) -> None:
        response = client.document_ai.extract.schema.with_raw_response.create(
            description="description",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(CreatedJsonSchema, schema, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Mixedbread) -> None:
        with client.document_ai.extract.schema.with_streaming_response.create(
            description="description",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(CreatedJsonSchema, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_enhance(self, client: Mixedbread) -> None:
        schema = client.document_ai.extract.schema.enhance(
            json_schema={},
        )
        assert_matches_type(EnhancedJsonSchema, schema, path=["response"])

    @parametrize
    def test_raw_response_enhance(self, client: Mixedbread) -> None:
        response = client.document_ai.extract.schema.with_raw_response.enhance(
            json_schema={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(EnhancedJsonSchema, schema, path=["response"])

    @parametrize
    def test_streaming_response_enhance(self, client: Mixedbread) -> None:
        with client.document_ai.extract.schema.with_streaming_response.enhance(
            json_schema={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(EnhancedJsonSchema, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_validate(self, client: Mixedbread) -> None:
        schema = client.document_ai.extract.schema.validate(
            json_schema={},
        )
        assert_matches_type(ValidatedJsonSchema, schema, path=["response"])

    @parametrize
    def test_raw_response_validate(self, client: Mixedbread) -> None:
        response = client.document_ai.extract.schema.with_raw_response.validate(
            json_schema={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(ValidatedJsonSchema, schema, path=["response"])

    @parametrize
    def test_streaming_response_validate(self, client: Mixedbread) -> None:
        with client.document_ai.extract.schema.with_streaming_response.validate(
            json_schema={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(ValidatedJsonSchema, schema, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSchema:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMixedbread) -> None:
        schema = await async_client.document_ai.extract.schema.create(
            description="description",
        )
        assert_matches_type(CreatedJsonSchema, schema, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.document_ai.extract.schema.with_raw_response.create(
            description="description",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(CreatedJsonSchema, schema, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMixedbread) -> None:
        async with async_client.document_ai.extract.schema.with_streaming_response.create(
            description="description",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(CreatedJsonSchema, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_enhance(self, async_client: AsyncMixedbread) -> None:
        schema = await async_client.document_ai.extract.schema.enhance(
            json_schema={},
        )
        assert_matches_type(EnhancedJsonSchema, schema, path=["response"])

    @parametrize
    async def test_raw_response_enhance(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.document_ai.extract.schema.with_raw_response.enhance(
            json_schema={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(EnhancedJsonSchema, schema, path=["response"])

    @parametrize
    async def test_streaming_response_enhance(self, async_client: AsyncMixedbread) -> None:
        async with async_client.document_ai.extract.schema.with_streaming_response.enhance(
            json_schema={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(EnhancedJsonSchema, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_validate(self, async_client: AsyncMixedbread) -> None:
        schema = await async_client.document_ai.extract.schema.validate(
            json_schema={},
        )
        assert_matches_type(ValidatedJsonSchema, schema, path=["response"])

    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.document_ai.extract.schema.with_raw_response.validate(
            json_schema={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(ValidatedJsonSchema, schema, path=["response"])

    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncMixedbread) -> None:
        async with async_client.document_ai.extract.schema.with_streaming_response.validate(
            json_schema={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(ValidatedJsonSchema, schema, path=["response"])

        assert cast(Any, response.is_closed) is True
