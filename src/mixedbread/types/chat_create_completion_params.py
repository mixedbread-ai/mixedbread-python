# File generated from our OpenAPI spec by sdkgen. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .shared_params.search_filter import SearchFilter
from .shared_params.search_filter_condition import SearchFilterCondition

__all__ = [
    "ChatCreateCompletionParams",
    "Message",
    "MessageSystemMessage",
    "MessageSystemMessageContentUnionMember1",
    "MessageDeveloperMessage",
    "MessageDeveloperMessageContentUnionMember1",
    "MessageUserMessage",
    "MessageUserMessageContentUnionMember1",
    "MessageAssistantMessageInput",
    "MessageAssistantMessageInputContentUnionMember1",
    "MessageAssistantMessageInputToolCall",
    "MessageAssistantMessageInputToolCallFunction",
    "MessageAssistantMessageInputAnnotation",
    "MessageToolMessage",
    "MessageToolMessageContentUnionMember1",
    "Tool",
    "ToolSearchCorpusTool",
    "ToolSearchCorpusToolFilters",
    "ToolSearchCorpusToolFiltersUnionMember2",
    "ToolGrepTool",
    "ToolGrepToolFilters",
    "ToolGrepToolFiltersUnionMember2",
    "ToolFilterChunksTool",
    "ToolFilterChunksToolFilters",
    "ToolFilterChunksToolFiltersUnionMember2",
    "ToolInspectMetadataTool",
    "ToolInspectMetadataToolFilters",
    "ToolInspectMetadataToolFiltersUnionMember2",
    "ToolGetChunksTool",
    "ToolStoreSearchTool",
    "ToolStoreSearchToolFilters",
    "ToolStoreSearchToolFiltersUnionMember2",
    "ToolStoreGrepTool",
    "ToolStoreGrepToolFilters",
    "ToolStoreGrepToolFiltersUnionMember2",
    "ToolStoreListChunksTool",
    "ToolStoreListChunksToolFilters",
    "ToolStoreListChunksToolFiltersUnionMember2",
    "ToolMetadataFacetsTool",
    "ToolMetadataFacetsToolFilters",
    "ToolMetadataFacetsToolFiltersUnionMember2",
    "ToolListStoresTool",
    "ToolFunctionTool",
    "ToolFunctionToolFunction",
    "ToolChoice",
    "ToolChoiceToolChoiceFunction",
    "ToolChoiceToolChoiceFunctionFunction",
    "ToolChoiceToolChoiceSearchCorpus",
    "ToolChoiceToolChoiceGrep",
    "ToolChoiceToolChoiceFilterChunks",
    "ToolChoiceToolChoiceInspectMetadata",
    "ToolChoiceToolChoiceListStores",
    "ToolChoiceToolChoiceStoreSearch",
    "ToolChoiceToolChoiceStoreGrep",
    "ToolChoiceToolChoiceStoreListChunks",
    "ToolChoiceToolChoiceMetadataFacets",
    "PreviousMessage",
    "PreviousMessageSystemMessage",
    "PreviousMessageSystemMessageContentUnionMember1",
    "PreviousMessageDeveloperMessage",
    "PreviousMessageDeveloperMessageContentUnionMember1",
    "PreviousMessageUserMessage",
    "PreviousMessageUserMessageContentUnionMember1",
    "PreviousMessageAssistantMessageInput",
    "PreviousMessageAssistantMessageInputContentUnionMember1",
    "PreviousMessageAssistantMessageInputToolCall",
    "PreviousMessageAssistantMessageInputToolCallFunction",
    "PreviousMessageAssistantMessageInputAnnotation",
    "PreviousMessageToolMessage",
    "PreviousMessageToolMessageContentUnionMember1",
    "ContextManagement",
    "ContextManagementEdit",
]


class MessageSystemMessageContentUnionMember1(TypedDict, total=False):
    type: Literal["text"]

    text: Required[str]


class MessageSystemMessage(TypedDict, total=False):
    """The conversation, or its new suffix when continuing a stored completion"""

    role: Required[Literal["system"]]

    content: Required[Union[str, Iterable[MessageSystemMessageContentUnionMember1]]]


class MessageDeveloperMessageContentUnionMember1(TypedDict, total=False):
    type: Literal["text"]

    text: Required[str]


class MessageDeveloperMessage(TypedDict, total=False):
    """The conversation, or its new suffix when continuing a stored completion"""

    role: Required[Literal["developer"]]

    content: Required[Union[str, Iterable[MessageDeveloperMessageContentUnionMember1]]]


class MessageUserMessageContentUnionMember1(TypedDict, total=False):
    type: Literal["text"]

    text: Required[str]


class MessageUserMessage(TypedDict, total=False):
    """The conversation, or its new suffix when continuing a stored completion"""

    role: Required[Literal["user"]]

    content: Required[Union[str, Iterable[MessageUserMessageContentUnionMember1]]]


class MessageAssistantMessageInputContentUnionMember1(TypedDict, total=False):
    type: Literal["text"]

    text: Required[str]


class MessageAssistantMessageInputToolCallFunction(TypedDict, total=False):
    name: Required[str]

    arguments: Required[str]


class MessageAssistantMessageInputToolCall(TypedDict, total=False):
    """One function tool call of an assistant message."""

    id: Required[str]

    type: Literal["function"]

    function: Required[MessageAssistantMessageInputToolCallFunction]


class MessageAssistantMessageInputAnnotation(TypedDict, total=False):
    """The OpenAI ``file_citation`` annotation, plus the chunk it points at.

    ``chunk_id`` is the same ``file_id:chunk_index`` reference every hosted result
    carries, and ``store_id`` the store whose index holds the chunk; the cited text
    and score are on the included tool results.
    """

    type: Literal["file_citation"]

    file_id: Required[str]

    filename: Required[str]

    index: Required[int]

    chunk_id: Required[str]

    store_id: Required[str]


class MessageAssistantMessageInput(TypedDict, total=False):
    """The conversation, or its new suffix when continuing a stored completion"""

    role: Required[Literal["assistant"]]

    content: Union[str, Iterable[MessageAssistantMessageInputContentUnionMember1], None]

    tool_calls: Iterable[MessageAssistantMessageInputToolCall]

    reasoning_content: Optional[str]

    annotations: Iterable[MessageAssistantMessageInputAnnotation]


class MessageToolMessageContentUnionMember1(TypedDict, total=False):
    type: Literal["text"]

    text: Required[str]


class MessageToolMessage(TypedDict, total=False):
    """The conversation, or its new suffix when continuing a stored completion"""

    role: Required[Literal["tool"]]

    content: Required[Union[str, Iterable[MessageToolMessageContentUnionMember1]]]

    tool_call_id: Required[str]


Message: TypeAlias = Union[
    MessageSystemMessage, MessageDeveloperMessage, MessageUserMessage, MessageAssistantMessageInput, MessageToolMessage
]

ToolSearchCorpusToolFiltersUnionMember2: TypeAlias = Union[SearchFilter, SearchFilterCondition]

ToolSearchCorpusToolFilters: TypeAlias = Union[
    SearchFilter, SearchFilterCondition, Iterable[ToolSearchCorpusToolFiltersUnionMember2]
]


class ToolSearchCorpusTool(TypedDict, total=False):
    """
    Tools the model may call; the hosted tools are opt-in and run server-side for
    the completions that declare them
    """

    store_identifiers: Optional[SequenceNotStr[str]]
    """
    IDs or names of the stores the tool runs against; omit to let the model pick a
    store per call (requires the list_stores tool)
    """

    type: Literal["search_corpus"]

    filters: Optional[ToolSearchCorpusToolFilters]
    """Optional filter conditions applied to every search"""

    score_threshold: float
    """Minimum similarity score threshold"""

    citations: bool
    """
    Have the model cite its evidence inline; the answer ships with the markers
    removed and an annotations list of file_citation entries pointing at the cited
    chunks
    """


ToolGrepToolFiltersUnionMember2: TypeAlias = Union[SearchFilter, SearchFilterCondition]

ToolGrepToolFilters: TypeAlias = Union[SearchFilter, SearchFilterCondition, Iterable[ToolGrepToolFiltersUnionMember2]]


class ToolGrepTool(TypedDict, total=False):
    """
    Tools the model may call; the hosted tools are opt-in and run server-side for
    the completions that declare them
    """

    store_identifiers: Optional[SequenceNotStr[str]]
    """
    IDs or names of the stores the tool runs against; omit to let the model pick a
    store per call (requires the list_stores tool)
    """

    type: Literal["grep"]

    filters: Optional[ToolGrepToolFilters]
    """Optional filter conditions applied to every grep"""

    citations: bool
    """
    Have the model cite its evidence inline; the answer ships with the markers
    removed and an annotations list of file_citation entries pointing at the cited
    chunks
    """


ToolFilterChunksToolFiltersUnionMember2: TypeAlias = Union[SearchFilter, SearchFilterCondition]

ToolFilterChunksToolFilters: TypeAlias = Union[
    SearchFilter, SearchFilterCondition, Iterable[ToolFilterChunksToolFiltersUnionMember2]
]


class ToolFilterChunksTool(TypedDict, total=False):
    """
    Tools the model may call; the hosted tools are opt-in and run server-side for
    the completions that declare them
    """

    store_identifiers: Optional[SequenceNotStr[str]]
    """
    IDs or names of the stores the tool runs against; omit to let the model pick a
    store per call (requires the list_stores tool)
    """

    type: Literal["filter_chunks"]

    filters: Optional[ToolFilterChunksToolFilters]
    """Optional filter conditions applied to every listing"""

    citations: bool
    """
    Have the model cite its evidence inline; the answer ships with the markers
    removed and an annotations list of file_citation entries pointing at the cited
    chunks
    """


ToolInspectMetadataToolFiltersUnionMember2: TypeAlias = Union[SearchFilter, SearchFilterCondition]

ToolInspectMetadataToolFilters: TypeAlias = Union[
    SearchFilter, SearchFilterCondition, Iterable[ToolInspectMetadataToolFiltersUnionMember2]
]


class ToolInspectMetadataTool(TypedDict, total=False):
    """
    Tools the model may call; the hosted tools are opt-in and run server-side for
    the completions that declare them
    """

    store_identifiers: Optional[SequenceNotStr[str]]
    """
    IDs or names of the stores the tool runs against; omit to let the model pick a
    store per call (requires the list_stores tool)
    """

    type: Literal["inspect_metadata"]

    filters: Optional[ToolInspectMetadataToolFilters]
    """Optional filter conditions restricting the files the facets are computed over"""


class ToolGetChunksTool(TypedDict, total=False):
    """
    Tools the model may call; the hosted tools are opt-in and run server-side for
    the completions that declare them
    """

    store_identifiers: Optional[SequenceNotStr[str]]
    """
    IDs or names of the stores the tool runs against; omit to let the model pick a
    store per call (requires the list_stores tool)
    """

    type: Literal["get_chunks"]


ToolStoreSearchToolFiltersUnionMember2: TypeAlias = Union[SearchFilter, SearchFilterCondition]

ToolStoreSearchToolFilters: TypeAlias = Union[
    SearchFilter, SearchFilterCondition, Iterable[ToolStoreSearchToolFiltersUnionMember2]
]


class ToolStoreSearchTool(TypedDict, total=False):
    """
    Tools the model may call; the hosted tools are opt-in and run server-side for
    the completions that declare them
    """

    store_identifiers: Optional[SequenceNotStr[str]]
    """
    IDs or names of the stores the tool runs against; omit to let the model pick a
    store per call (requires the list_stores tool)
    """

    type: Literal["store_search"]

    filters: Optional[ToolStoreSearchToolFilters]
    """Optional filter conditions applied to every search"""

    score_threshold: float
    """Minimum similarity score threshold"""

    citations: bool
    """
    Have the model cite its evidence inline; the answer ships with the markers
    removed and an annotations list of file_citation entries pointing at the cited
    chunks
    """


ToolStoreGrepToolFiltersUnionMember2: TypeAlias = Union[SearchFilter, SearchFilterCondition]

ToolStoreGrepToolFilters: TypeAlias = Union[
    SearchFilter, SearchFilterCondition, Iterable[ToolStoreGrepToolFiltersUnionMember2]
]


class ToolStoreGrepTool(TypedDict, total=False):
    """
    Tools the model may call; the hosted tools are opt-in and run server-side for
    the completions that declare them
    """

    store_identifiers: Optional[SequenceNotStr[str]]
    """
    IDs or names of the stores the tool runs against; omit to let the model pick a
    store per call (requires the list_stores tool)
    """

    type: Literal["store_grep"]

    filters: Optional[ToolStoreGrepToolFilters]
    """Optional filter conditions applied to every grep"""

    citations: bool
    """
    Have the model cite its evidence inline; the answer ships with the markers
    removed and an annotations list of file_citation entries pointing at the cited
    chunks
    """


ToolStoreListChunksToolFiltersUnionMember2: TypeAlias = Union[SearchFilter, SearchFilterCondition]

ToolStoreListChunksToolFilters: TypeAlias = Union[
    SearchFilter, SearchFilterCondition, Iterable[ToolStoreListChunksToolFiltersUnionMember2]
]


class ToolStoreListChunksTool(TypedDict, total=False):
    """
    Tools the model may call; the hosted tools are opt-in and run server-side for
    the completions that declare them
    """

    store_identifiers: Optional[SequenceNotStr[str]]
    """
    IDs or names of the stores the tool runs against; omit to let the model pick a
    store per call (requires the list_stores tool)
    """

    type: Literal["store_list_chunks"]

    filters: Optional[ToolStoreListChunksToolFilters]
    """Optional filter conditions applied to every listing"""

    citations: bool
    """
    Have the model cite its evidence inline; the answer ships with the markers
    removed and an annotations list of file_citation entries pointing at the cited
    chunks
    """


ToolMetadataFacetsToolFiltersUnionMember2: TypeAlias = Union[SearchFilter, SearchFilterCondition]

ToolMetadataFacetsToolFilters: TypeAlias = Union[
    SearchFilter, SearchFilterCondition, Iterable[ToolMetadataFacetsToolFiltersUnionMember2]
]


class ToolMetadataFacetsTool(TypedDict, total=False):
    """
    Tools the model may call; the hosted tools are opt-in and run server-side for
    the completions that declare them
    """

    store_identifiers: Optional[SequenceNotStr[str]]
    """
    IDs or names of the stores the tool runs against; omit to let the model pick a
    store per call (requires the list_stores tool)
    """

    type: Literal["store_metadata_facets"]

    filters: Optional[ToolMetadataFacetsToolFilters]
    """Optional filter conditions restricting the files the facets are computed over"""


class ToolListStoresTool(TypedDict, total=False):
    """
    Tools the model may call; the hosted tools are opt-in and run server-side for
    the completions that declare them
    """

    type: Literal["list_stores"]

    limit: int
    """Number of stores returned per listing call"""


class ToolFunctionToolFunction(TypedDict, total=False):
    """
    Definition of a client-executed function tool, as in the OpenAI Chat Completions
    API.

    Any name is usable; hosted tool names are only reserved against the requests
    that declare that hosted tool (checked at the params level).
    """

    name: Required[str]

    description: Optional[str]

    parameters: Optional[Dict[str, object]]

    strict: Optional[bool]


class ToolFunctionTool(TypedDict, total=False):
    """
    Tools the model may call; the hosted tools are opt-in and run server-side for
    the completions that declare them
    """

    type: Literal["function"]

    function: Required[ToolFunctionToolFunction]
    """
    Definition of a client-executed function tool, as in the OpenAI Chat Completions
    API.

    Any name is usable; hosted tool names are only reserved against the requests
    that declare that hosted tool (checked at the params level).
    """


Tool: TypeAlias = Union[
    ToolSearchCorpusTool,
    ToolGrepTool,
    ToolFilterChunksTool,
    ToolInspectMetadataTool,
    ToolGetChunksTool,
    ToolStoreSearchTool,
    ToolStoreGrepTool,
    ToolStoreListChunksTool,
    ToolMetadataFacetsTool,
    ToolListStoresTool,
    ToolFunctionTool,
]


class ToolChoiceToolChoiceFunctionFunction(TypedDict, total=False):
    name: Required[str]


class ToolChoiceToolChoiceFunction(TypedDict, total=False):
    """Force a call to a specific function tool, as in the OpenAI Chat Completions API."""

    type: Literal["function"]

    function: Required[ToolChoiceToolChoiceFunctionFunction]


class ToolChoiceToolChoiceSearchCorpus(TypedDict, total=False):
    """Force a call to the hosted search tool (Mixedbread extension)."""

    type: Literal["search_corpus"]


class ToolChoiceToolChoiceGrep(TypedDict, total=False):
    """Force a call to the hosted grep tool (Mixedbread extension)."""

    type: Literal["grep"]


class ToolChoiceToolChoiceFilterChunks(TypedDict, total=False):
    """Force a call to the hosted chunk-listing tool (Mixedbread extension)."""

    type: Literal["filter_chunks"]


class ToolChoiceToolChoiceInspectMetadata(TypedDict, total=False):
    """Force a call to the hosted metadata-overview tool (Mixedbread extension)."""

    type: Literal["inspect_metadata"]


class ToolChoiceToolChoiceListStores(TypedDict, total=False):
    """Force a call to the hosted list stores tool (Mixedbread extension)."""

    type: Literal["list_stores"]


class ToolChoiceToolChoiceStoreSearch(TypedDict, total=False):
    """Deprecated alias of the `search_corpus` tool choice."""

    type: Literal["store_search"]


class ToolChoiceToolChoiceStoreGrep(TypedDict, total=False):
    """Deprecated alias of the `grep` tool choice."""

    type: Literal["store_grep"]


class ToolChoiceToolChoiceStoreListChunks(TypedDict, total=False):
    """Deprecated alias of the `filter_chunks` tool choice."""

    type: Literal["store_list_chunks"]


class ToolChoiceToolChoiceMetadataFacets(TypedDict, total=False):
    """Deprecated alias of the `inspect_metadata` tool choice."""

    type: Literal["store_metadata_facets"]


ToolChoice: TypeAlias = Union[
    Literal["auto", "none", "required"],
    ToolChoiceToolChoiceFunction,
    ToolChoiceToolChoiceSearchCorpus,
    ToolChoiceToolChoiceGrep,
    ToolChoiceToolChoiceFilterChunks,
    ToolChoiceToolChoiceInspectMetadata,
    ToolChoiceToolChoiceListStores,
    ToolChoiceToolChoiceStoreSearch,
    ToolChoiceToolChoiceStoreGrep,
    ToolChoiceToolChoiceStoreListChunks,
    ToolChoiceToolChoiceMetadataFacets,
]


class PreviousMessageSystemMessageContentUnionMember1(TypedDict, total=False):
    type: Literal["text"]

    text: Required[str]


class PreviousMessageSystemMessage(TypedDict, total=False):
    """Deprecated.

    Replacement for the previous completion's stored model context after client-side
    pruning. Send the full edited history in `messages` without
    `previous_completion_id` instead; the request is honored exactly as sent
    """

    role: Required[Literal["system"]]

    content: Required[Union[str, Iterable[PreviousMessageSystemMessageContentUnionMember1]]]


class PreviousMessageDeveloperMessageContentUnionMember1(TypedDict, total=False):
    type: Literal["text"]

    text: Required[str]


class PreviousMessageDeveloperMessage(TypedDict, total=False):
    """Deprecated.

    Replacement for the previous completion's stored model context after client-side
    pruning. Send the full edited history in `messages` without
    `previous_completion_id` instead; the request is honored exactly as sent
    """

    role: Required[Literal["developer"]]

    content: Required[Union[str, Iterable[PreviousMessageDeveloperMessageContentUnionMember1]]]


class PreviousMessageUserMessageContentUnionMember1(TypedDict, total=False):
    type: Literal["text"]

    text: Required[str]


class PreviousMessageUserMessage(TypedDict, total=False):
    """Deprecated.

    Replacement for the previous completion's stored model context after client-side
    pruning. Send the full edited history in `messages` without
    `previous_completion_id` instead; the request is honored exactly as sent
    """

    role: Required[Literal["user"]]

    content: Required[Union[str, Iterable[PreviousMessageUserMessageContentUnionMember1]]]


class PreviousMessageAssistantMessageInputContentUnionMember1(TypedDict, total=False):
    type: Literal["text"]

    text: Required[str]


class PreviousMessageAssistantMessageInputToolCallFunction(TypedDict, total=False):
    name: Required[str]

    arguments: Required[str]


class PreviousMessageAssistantMessageInputToolCall(TypedDict, total=False):
    """One function tool call of an assistant message."""

    id: Required[str]

    type: Literal["function"]

    function: Required[PreviousMessageAssistantMessageInputToolCallFunction]


class PreviousMessageAssistantMessageInputAnnotation(TypedDict, total=False):
    """The OpenAI ``file_citation`` annotation, plus the chunk it points at.

    ``chunk_id`` is the same ``file_id:chunk_index`` reference every hosted result
    carries, and ``store_id`` the store whose index holds the chunk; the cited text
    and score are on the included tool results.
    """

    type: Literal["file_citation"]

    file_id: Required[str]

    filename: Required[str]

    index: Required[int]

    chunk_id: Required[str]

    store_id: Required[str]


class PreviousMessageAssistantMessageInput(TypedDict, total=False):
    """Deprecated.

    Replacement for the previous completion's stored model context after client-side
    pruning. Send the full edited history in `messages` without
    `previous_completion_id` instead; the request is honored exactly as sent
    """

    role: Required[Literal["assistant"]]

    content: Union[str, Iterable[PreviousMessageAssistantMessageInputContentUnionMember1], None]

    tool_calls: Iterable[PreviousMessageAssistantMessageInputToolCall]

    reasoning_content: Optional[str]

    annotations: Iterable[PreviousMessageAssistantMessageInputAnnotation]


class PreviousMessageToolMessageContentUnionMember1(TypedDict, total=False):
    type: Literal["text"]

    text: Required[str]


class PreviousMessageToolMessage(TypedDict, total=False):
    """Deprecated.

    Replacement for the previous completion's stored model context after client-side
    pruning. Send the full edited history in `messages` without
    `previous_completion_id` instead; the request is honored exactly as sent
    """

    role: Required[Literal["tool"]]

    content: Required[Union[str, Iterable[PreviousMessageToolMessageContentUnionMember1]]]

    tool_call_id: Required[str]


PreviousMessage: TypeAlias = Union[
    PreviousMessageSystemMessage,
    PreviousMessageDeveloperMessage,
    PreviousMessageUserMessage,
    PreviousMessageAssistantMessageInput,
    PreviousMessageToolMessage,
]


class ContextManagementEdit(TypedDict, total=False):
    """The context edits enabled for this completion"""

    type: Literal["prune_context"]


class ContextManagement(TypedDict, total=False):
    """Opt-in context editing for one completion (Mixedbread extension)."""

    edits: Required[Iterable[ContextManagementEdit]]
    """The context edits enabled for this completion"""


class ChatCreateCompletionParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """The conversation, or its new suffix when continuing a stored completion"""

    model: str
    """Public model ID. Defaults to toast-1"""

    tools: Iterable[Tool]
    """
    Tools the model may call; the hosted tools are opt-in and run server-side for
    the completions that declare them
    """

    tool_choice: ToolChoice

    store: bool
    """Whether to persist this completion for later retrieval"""

    previous_completion_id: Optional[str]
    """ID of a stored completion this one continues (Mixedbread extension).

    Groups turns into a conversation for listing and deletion, and always restores
    the previous completion's full model context, including hosted tool calls and
    results
    """

    previous_messages: Optional[Iterable[PreviousMessage]]
    """Deprecated.

    Replacement for the previous completion's stored model context after client-side
    pruning. Send the full edited history in `messages` without
    `previous_completion_id` instead; the request is honored exactly as sent
    """

    terminal_tool_name: Optional[str]
    """Deprecated and ignored.

    The stored transcript is never rewritten around a terminal tool call; the
    completion ends with the model's plain-text answer
    """

    stream: bool
    """Stream the completion as server-sent events"""

    temperature: Optional[float]

    top_p: Optional[float]

    max_completion_tokens: Optional[int]

    max_tokens: Optional[int]
    """Deprecated alias of max_completion_tokens, honored when it is absent"""

    max_tool_calls: Optional[int]
    """
    Maximum number of server-handled tool calls (store tools and prune_context)
    executed for this completion; ignored when none are declared
    """

    context_management: Optional[ContextManagement]
    """Opt-in context editing for one completion (Mixedbread extension)."""

    parallel_tool_calls: bool
    """
    Whether the model may call multiple tools in one turn; when false, at most one
    is honored
    """

    metadata: Optional[Dict[str, str]]

    include: Optional[SequenceNotStr[str]]
    """Extra fields to include, e.g.

    search_corpus_call.results; unsupported values are ignored
    """
