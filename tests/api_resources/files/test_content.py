# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from mixedbread import Mixedbread, AsyncMixedbread
from mixedbread._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: Mixedbread, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/files/file_id/content").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        content = client.files.content.retrieve(
            "file_id",
        )
        assert content.is_closed
        assert content.json() == {"foo": "bar"}
        assert cast(Any, content.is_closed) is True
        assert isinstance(content, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: Mixedbread, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/files/file_id/content").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        content = client.files.content.with_raw_response.retrieve(
            "file_id",
        )

        assert content.is_closed is True
        assert content.http_request.headers.get("X-Stainless-Lang") == "python"
        assert content.json() == {"foo": "bar"}
        assert isinstance(content, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: Mixedbread, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/files/file_id/content").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.files.content.with_streaming_response.retrieve(
            "file_id",
        ) as content:
            assert not content.is_closed
            assert content.http_request.headers.get("X-Stainless-Lang") == "python"

            assert content.json() == {"foo": "bar"}
            assert cast(Any, content.is_closed) is True
            assert isinstance(content, StreamedBinaryAPIResponse)

        assert cast(Any, content.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.content.with_raw_response.retrieve(
                "",
            )


class TestAsyncContent:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncMixedbread, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/files/file_id/content").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        content = await async_client.files.content.retrieve(
            "file_id",
        )
        assert content.is_closed
        assert await content.json() == {"foo": "bar"}
        assert cast(Any, content.is_closed) is True
        assert isinstance(content, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncMixedbread, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/files/file_id/content").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        content = await async_client.files.content.with_raw_response.retrieve(
            "file_id",
        )

        assert content.is_closed is True
        assert content.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await content.json() == {"foo": "bar"}
        assert isinstance(content, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncMixedbread, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/files/file_id/content").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.files.content.with_streaming_response.retrieve(
            "file_id",
        ) as content:
            assert not content.is_closed
            assert content.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await content.json() == {"foo": "bar"}
            assert cast(Any, content.is_closed) is True
            assert isinstance(content, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, content.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.content.with_raw_response.retrieve(
                "",
            )
