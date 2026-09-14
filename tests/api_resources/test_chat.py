# File generated from our OpenAPI spec by sdkgen. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixedbread import Mixedbread, AsyncMixedbread
from tests.utils import assert_matches_type
from mixedbread.types import ChatCreateCompletionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_completion(self, client: Mixedbread) -> None:
        chat = client.chat.create_completion(
            messages=[
                {
                    "role": "system",
                    "content": "string",
                }
            ],
        )
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @parametrize
    def test_method_create_completion_with_all_params(self, client: Mixedbread) -> None:
        chat = client.chat.create_completion(
            messages=[
                {
                    "role": "system",
                    "content": "string",
                }
            ],
            model="model",
            tools=[
                {
                    "store_identifiers": ["string"],
                    "type": "search_corpus",
                    "filters": {
                        "all": [
                            {
                                "key": "price",
                                "operator": "gt",
                                "value": "100",
                            },
                            {
                                "key": "color",
                                "operator": "eq",
                                "value": "red",
                            },
                        ],
                        "any": [
                            {
                                "key": "price",
                                "operator": "gt",
                                "value": "100",
                            },
                            {
                                "key": "color",
                                "operator": "eq",
                                "value": "red",
                            },
                        ],
                        "none": [
                            {
                                "key": "price",
                                "operator": "gt",
                                "value": "100",
                            },
                            {
                                "key": "color",
                                "operator": "eq",
                                "value": "red",
                            },
                        ],
                    },
                    "score_threshold": 0,
                    "citations": True,
                }
            ],
            tool_choice="auto",
            response_format={"type": "text"},
            store=True,
            previous_completion_id="previous_completion_id",
            previous_messages=[
                {
                    "role": "system",
                    "content": "string",
                }
            ],
            terminal_tool_name="terminal_tool_name",
            stream=True,
            temperature=0,
            top_p=0,
            max_completion_tokens=16,
            max_tokens=16,
            max_tool_calls=1,
            context_management={"edits": [{"type": "prune_context"}]},
            parallel_tool_calls=True,
            metadata={"foo": "string"},
            include=["string"],
        )
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_create_completion(self, client: Mixedbread) -> None:
        response = client.chat.with_raw_response.create_completion(
            messages=[
                {
                    "role": "system",
                    "content": "string",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_create_completion(self, client: Mixedbread) -> None:
        with client.chat.with_streaming_response.create_completion(
            messages=[
                {
                    "role": "system",
                    "content": "string",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChat:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_completion(self, async_client: AsyncMixedbread) -> None:
        chat = await async_client.chat.create_completion(
            messages=[
                {
                    "role": "system",
                    "content": "string",
                }
            ],
        )
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @parametrize
    async def test_method_create_completion_with_all_params(self, async_client: AsyncMixedbread) -> None:
        chat = await async_client.chat.create_completion(
            messages=[
                {
                    "role": "system",
                    "content": "string",
                }
            ],
            model="model",
            tools=[
                {
                    "store_identifiers": ["string"],
                    "type": "search_corpus",
                    "filters": {
                        "all": [
                            {
                                "key": "price",
                                "operator": "gt",
                                "value": "100",
                            },
                            {
                                "key": "color",
                                "operator": "eq",
                                "value": "red",
                            },
                        ],
                        "any": [
                            {
                                "key": "price",
                                "operator": "gt",
                                "value": "100",
                            },
                            {
                                "key": "color",
                                "operator": "eq",
                                "value": "red",
                            },
                        ],
                        "none": [
                            {
                                "key": "price",
                                "operator": "gt",
                                "value": "100",
                            },
                            {
                                "key": "color",
                                "operator": "eq",
                                "value": "red",
                            },
                        ],
                    },
                    "score_threshold": 0,
                    "citations": True,
                }
            ],
            tool_choice="auto",
            response_format={"type": "text"},
            store=True,
            previous_completion_id="previous_completion_id",
            previous_messages=[
                {
                    "role": "system",
                    "content": "string",
                }
            ],
            terminal_tool_name="terminal_tool_name",
            stream=True,
            temperature=0,
            top_p=0,
            max_completion_tokens=16,
            max_tokens=16,
            max_tool_calls=1,
            context_management={"edits": [{"type": "prune_context"}]},
            parallel_tool_calls=True,
            metadata={"foo": "string"},
            include=["string"],
        )
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_create_completion(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.chat.with_raw_response.create_completion(
            messages=[
                {
                    "role": "system",
                    "content": "string",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_create_completion(self, async_client: AsyncMixedbread) -> None:
        async with async_client.chat.with_streaming_response.create_completion(
            messages=[
                {
                    "role": "system",
                    "content": "string",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True
