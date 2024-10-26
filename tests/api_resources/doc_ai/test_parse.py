# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixedbread import Mixedbread, AsyncMixedbread
from tests.utils import assert_matches_type
from mixedbread.types.doc_ai import ParseResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestParse:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_job(self, client: Mixedbread) -> None:
        parse = client.doc_ai.parse.create_job(
            file=b"raw file contents",
        )
        assert_matches_type(ParseResponse, parse, path=["response"])

    @parametrize
    def test_raw_response_create_job(self, client: Mixedbread) -> None:
        response = client.doc_ai.parse.with_raw_response.create_job(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = response.parse()
        assert_matches_type(ParseResponse, parse, path=["response"])

    @parametrize
    def test_streaming_response_create_job(self, client: Mixedbread) -> None:
        with client.doc_ai.parse.with_streaming_response.create_job(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = response.parse()
            assert_matches_type(ParseResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_job(self, client: Mixedbread) -> None:
        parse = client.doc_ai.parse.retrieve_job(
            "job_id",
        )
        assert_matches_type(ParseResponse, parse, path=["response"])

    @parametrize
    def test_raw_response_retrieve_job(self, client: Mixedbread) -> None:
        response = client.doc_ai.parse.with_raw_response.retrieve_job(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = response.parse()
        assert_matches_type(ParseResponse, parse, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_job(self, client: Mixedbread) -> None:
        with client.doc_ai.parse.with_streaming_response.retrieve_job(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = response.parse()
            assert_matches_type(ParseResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_job(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.doc_ai.parse.with_raw_response.retrieve_job(
                "",
            )


class TestAsyncParse:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_job(self, async_client: AsyncMixedbread) -> None:
        parse = await async_client.doc_ai.parse.create_job(
            file=b"raw file contents",
        )
        assert_matches_type(ParseResponse, parse, path=["response"])

    @parametrize
    async def test_raw_response_create_job(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.doc_ai.parse.with_raw_response.create_job(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = await response.parse()
        assert_matches_type(ParseResponse, parse, path=["response"])

    @parametrize
    async def test_streaming_response_create_job(self, async_client: AsyncMixedbread) -> None:
        async with async_client.doc_ai.parse.with_streaming_response.create_job(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = await response.parse()
            assert_matches_type(ParseResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_job(self, async_client: AsyncMixedbread) -> None:
        parse = await async_client.doc_ai.parse.retrieve_job(
            "job_id",
        )
        assert_matches_type(ParseResponse, parse, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_job(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.doc_ai.parse.with_raw_response.retrieve_job(
            "job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = await response.parse()
        assert_matches_type(ParseResponse, parse, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_job(self, async_client: AsyncMixedbread) -> None:
        async with async_client.doc_ai.parse.with_streaming_response.retrieve_job(
            "job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = await response.parse()
            assert_matches_type(ParseResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_job(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.doc_ai.parse.with_raw_response.retrieve_job(
                "",
            )
