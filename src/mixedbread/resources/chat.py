# File generated from our OpenAPI spec by sdkgen. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from ..types import chat_create_completion_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.chat_create_completion_response import ChatCreateCompletionResponse

__all__ = ["ChatResource", "AsyncChatResource"]


class ChatResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return ChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return ChatResourceWithStreamingResponse(self)

    def create_completion(
        self,
        *,
        messages: Iterable[chat_create_completion_params.Message],
        model: str | Omit = omit,
        tools: Iterable[chat_create_completion_params.Tool] | Omit = omit,
        tool_choice: chat_create_completion_params.ToolChoice | Omit = omit,
        response_format: Optional[chat_create_completion_params.ResponseFormat] | Omit = omit,
        store: bool | Omit = omit,
        previous_completion_id: Optional[str] | Omit = omit,
        previous_messages: Optional[Iterable[chat_create_completion_params.PreviousMessage]] | Omit = omit,
        terminal_tool_name: Optional[str] | Omit = omit,
        stream: bool | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        max_completion_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        context_management: Optional[chat_create_completion_params.ContextManagement] | Omit = omit,
        parallel_tool_calls: bool | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        include: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCreateCompletionResponse:
        """
        Create a chat completion, optionally grounded in the caller's stores.

        Supports the OpenAI Chat Completions API subset: a message list, function tools,
        streaming via server-sent events, and persistence via `store`. A request without
        hosted tools is one generation over exactly what was sent: no instructions,
        tools, or turns are added. The `previous_completion_id` groups stored turns into
        a conversation and restores the full model context; callers normally send only
        the new suffix. (`previous_messages` and `terminal_tool_name` are deprecated:
        resend the full edited history in `messages` instead.) Retrieval is opt-in:
        declare the hosted store tools (`store_search`, `store_grep`,
        `store_list_chunks`, `store_metadata_facets`, `list_stores`) in `tools` to let
        the model search, grep, filter, and read the caller's stores server-side, scoped
        by each declaration. Those executions are reported in the `hosted_tool_calls`
        extension field (and as extra streaming chunks), with chunk results included
        only for the requested `include` keys. A model call to a caller-declared
        function tool ends the completion with `tool_calls` on the choice message
        (finish_reason `tool_calls`); execute the functions and continue the
        conversation by appending the assistant message and the matching `tool` messages
        to the next request.

        Args:
          messages: The conversation, or its new suffix when continuing a stored completion

          model: Public model ID. Defaults to toast-1

          tools: Tools the model may call; the hosted tools are opt-in and run server-side for
              the completions that declare them

          response_format: The shape of the answer: plain text, any JSON object, or JSON matching a schema.
              A JSON answer is grammar-constrained on the final generation; tool calls are
              unaffected

          store: Whether to persist this completion for later retrieval

          previous_completion_id: ID of a stored completion this one continues (Mixedbread extension). Groups
              turns into a conversation for listing and deletion, and always restores the
              previous completion's full model context, including hosted tool calls and
              results

          previous_messages: Deprecated. Replacement for the previous completion's stored model context after
              client-side pruning. Send the full edited history in `messages` without
              `previous_completion_id` instead; the request is honored exactly as sent

          terminal_tool_name: Deprecated and ignored. The stored transcript is never rewritten around a
              terminal tool call; the completion ends with the model's plain-text answer

          stream: Stream the completion as server-sent events

          max_tokens: Deprecated alias of max_completion_tokens, honored when it is absent

          max_tool_calls: Maximum number of server-handled tool calls (store tools and prune_context)
              executed for this completion; ignored when none are declared

          context_management: Opt-in context editing for one completion (Mixedbread extension).

          parallel_tool_calls: Whether the model may call multiple tools in one turn; when false, at most one
              is honored

          include: Extra fields to include, e.g. search_corpus_call.results; unsupported values are
              ignored

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/chat/completions",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "tools": tools,
                    "tool_choice": tool_choice,
                    "response_format": response_format,
                    "store": store,
                    "previous_completion_id": previous_completion_id,
                    "previous_messages": previous_messages,
                    "terminal_tool_name": terminal_tool_name,
                    "stream": stream,
                    "temperature": temperature,
                    "top_p": top_p,
                    "max_completion_tokens": max_completion_tokens,
                    "max_tokens": max_tokens,
                    "max_tool_calls": max_tool_calls,
                    "context_management": context_management,
                    "parallel_tool_calls": parallel_tool_calls,
                    "metadata": metadata,
                    "include": include,
                },
                chat_create_completion_params.ChatCreateCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCreateCompletionResponse,
        )


class AsyncChatResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mixedbread-ai/mixedbread-python#with_streaming_response
        """
        return AsyncChatResourceWithStreamingResponse(self)

    async def create_completion(
        self,
        *,
        messages: Iterable[chat_create_completion_params.Message],
        model: str | Omit = omit,
        tools: Iterable[chat_create_completion_params.Tool] | Omit = omit,
        tool_choice: chat_create_completion_params.ToolChoice | Omit = omit,
        response_format: Optional[chat_create_completion_params.ResponseFormat] | Omit = omit,
        store: bool | Omit = omit,
        previous_completion_id: Optional[str] | Omit = omit,
        previous_messages: Optional[Iterable[chat_create_completion_params.PreviousMessage]] | Omit = omit,
        terminal_tool_name: Optional[str] | Omit = omit,
        stream: bool | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        max_completion_tokens: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        max_tool_calls: Optional[int] | Omit = omit,
        context_management: Optional[chat_create_completion_params.ContextManagement] | Omit = omit,
        parallel_tool_calls: bool | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        include: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCreateCompletionResponse:
        """
        Create a chat completion, optionally grounded in the caller's stores.

        Supports the OpenAI Chat Completions API subset: a message list, function tools,
        streaming via server-sent events, and persistence via `store`. A request without
        hosted tools is one generation over exactly what was sent: no instructions,
        tools, or turns are added. The `previous_completion_id` groups stored turns into
        a conversation and restores the full model context; callers normally send only
        the new suffix. (`previous_messages` and `terminal_tool_name` are deprecated:
        resend the full edited history in `messages` instead.) Retrieval is opt-in:
        declare the hosted store tools (`store_search`, `store_grep`,
        `store_list_chunks`, `store_metadata_facets`, `list_stores`) in `tools` to let
        the model search, grep, filter, and read the caller's stores server-side, scoped
        by each declaration. Those executions are reported in the `hosted_tool_calls`
        extension field (and as extra streaming chunks), with chunk results included
        only for the requested `include` keys. A model call to a caller-declared
        function tool ends the completion with `tool_calls` on the choice message
        (finish_reason `tool_calls`); execute the functions and continue the
        conversation by appending the assistant message and the matching `tool` messages
        to the next request.

        Args:
          messages: The conversation, or its new suffix when continuing a stored completion

          model: Public model ID. Defaults to toast-1

          tools: Tools the model may call; the hosted tools are opt-in and run server-side for
              the completions that declare them

          response_format: The shape of the answer: plain text, any JSON object, or JSON matching a schema.
              A JSON answer is grammar-constrained on the final generation; tool calls are
              unaffected

          store: Whether to persist this completion for later retrieval

          previous_completion_id: ID of a stored completion this one continues (Mixedbread extension). Groups
              turns into a conversation for listing and deletion, and always restores the
              previous completion's full model context, including hosted tool calls and
              results

          previous_messages: Deprecated. Replacement for the previous completion's stored model context after
              client-side pruning. Send the full edited history in `messages` without
              `previous_completion_id` instead; the request is honored exactly as sent

          terminal_tool_name: Deprecated and ignored. The stored transcript is never rewritten around a
              terminal tool call; the completion ends with the model's plain-text answer

          stream: Stream the completion as server-sent events

          max_tokens: Deprecated alias of max_completion_tokens, honored when it is absent

          max_tool_calls: Maximum number of server-handled tool calls (store tools and prune_context)
              executed for this completion; ignored when none are declared

          context_management: Opt-in context editing for one completion (Mixedbread extension).

          parallel_tool_calls: Whether the model may call multiple tools in one turn; when false, at most one
              is honored

          include: Extra fields to include, e.g. search_corpus_call.results; unsupported values are
              ignored

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/chat/completions",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "tools": tools,
                    "tool_choice": tool_choice,
                    "response_format": response_format,
                    "store": store,
                    "previous_completion_id": previous_completion_id,
                    "previous_messages": previous_messages,
                    "terminal_tool_name": terminal_tool_name,
                    "stream": stream,
                    "temperature": temperature,
                    "top_p": top_p,
                    "max_completion_tokens": max_completion_tokens,
                    "max_tokens": max_tokens,
                    "max_tool_calls": max_tool_calls,
                    "context_management": context_management,
                    "parallel_tool_calls": parallel_tool_calls,
                    "metadata": metadata,
                    "include": include,
                },
                chat_create_completion_params.ChatCreateCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCreateCompletionResponse,
        )


class ChatResourceWithRawResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.create_completion = to_raw_response_wrapper(
            chat.create_completion,
        )


class AsyncChatResourceWithRawResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.create_completion = async_to_raw_response_wrapper(
            chat.create_completion,
        )


class ChatResourceWithStreamingResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.create_completion = to_streamed_response_wrapper(
            chat.create_completion,
        )


class AsyncChatResourceWithStreamingResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.create_completion = async_to_streamed_response_wrapper(
            chat.create_completion,
        )
