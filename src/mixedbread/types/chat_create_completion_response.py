# File generated from our OpenAPI spec by sdkgen. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "ChatCreateCompletionResponse",
    "Choice",
    "ChoiceMessage",
    "ChoiceMessageToolCall",
    "ChoiceMessageToolCallFunction",
    "ChoiceMessageAnnotation",
    "Usage",
    "UsagePromptTokensDetails",
    "UsageCompletionTokensDetails",
    "HostedToolCall",
    "HostedToolCallSearchCorpusCallItem",
    "HostedToolCallSearchCorpusCallItemMetadataFilter",
    "HostedToolCallSearchCorpusCallItemError",
    "HostedToolCallGrepCallItem",
    "HostedToolCallGrepCallItemMetadataFilter",
    "HostedToolCallGrepCallItemError",
    "HostedToolCallFilterChunksCallItem",
    "HostedToolCallFilterChunksCallItemMetadataFilter",
    "HostedToolCallFilterChunksCallItemError",
    "HostedToolCallInspectMetadataCallItem",
    "HostedToolCallInspectMetadataCallItemError",
    "HostedToolCallGetChunksCallItem",
    "HostedToolCallGetChunksCallItemError",
    "HostedToolCallStoreSearchCallItem",
    "HostedToolCallStoreSearchCallItemMetadataFilter",
    "HostedToolCallStoreSearchCallItemError",
    "HostedToolCallStoreGrepCallItem",
    "HostedToolCallStoreGrepCallItemMetadataFilter",
    "HostedToolCallStoreGrepCallItemError",
    "HostedToolCallStoreListChunksCallItem",
    "HostedToolCallStoreListChunksCallItemMetadataFilter",
    "HostedToolCallStoreListChunksCallItemError",
    "HostedToolCallMetadataFacetsCallItem",
    "HostedToolCallMetadataFacetsCallItemError",
    "HostedToolCallListStoresCallItem",
    "HostedToolCallListStoresCallItemStore",
    "HostedToolCallListStoresCallItemError",
    "ContextManagement",
    "ContextManagementAppliedEdit",
    "ContextManagementAppliedEditAppliedPruneContextEdit",
    "ContextManagementAppliedEditAppliedTruncateToolResultEdit",
    "ToolTicket",
    "Transcript",
    "TranscriptSystemMessage",
    "TranscriptSystemMessageContentUnionMember1",
    "TranscriptDeveloperMessage",
    "TranscriptDeveloperMessageContentUnionMember1",
    "TranscriptUserMessage",
    "TranscriptUserMessageContentUnionMember1",
    "TranscriptAssistantMessageOutput",
    "TranscriptAssistantMessageOutputContentUnionMember1",
    "TranscriptAssistantMessageOutputToolCall",
    "TranscriptAssistantMessageOutputToolCallFunction",
    "TranscriptAssistantMessageOutputAnnotation",
    "TranscriptToolMessage",
    "TranscriptToolMessageContentUnionMember1",
]


class ChoiceMessageToolCallFunction(BaseModel):
    name: str

    arguments: str


class ChoiceMessageToolCall(BaseModel):
    """One function tool call of an assistant message."""

    id: str

    type: Optional[Literal["function"]] = None

    function: ChoiceMessageToolCallFunction


class ChoiceMessageAnnotation(BaseModel):
    """The OpenAI ``file_citation`` annotation, plus the chunk it points at.

    ``chunk_id`` is the same ``file_id:chunk_index`` reference every hosted result
    carries, and ``store_id`` the store whose index holds the chunk; the cited text
    and score are on the included tool results.
    """

    type: Optional[Literal["file_citation"]] = None

    file_id: str

    filename: str

    index: int

    chunk_id: str

    store_id: str


class ChoiceMessage(BaseModel):
    """The assistant message of one completion choice."""

    role: Optional[Literal["assistant"]] = None

    content: Optional[str] = None

    refusal: Optional[str] = None

    tool_calls: Optional[List[ChoiceMessageToolCall]] = None

    reasoning_content: Optional[str] = None

    annotations: Optional[List[ChoiceMessageAnnotation]] = None


class Choice(BaseModel):
    index: Optional[int] = None

    message: ChoiceMessage
    """The assistant message of one completion choice."""

    finish_reason: Optional[Literal["stop", "tool_calls", "length"]] = None

    logprobs: Optional[object] = None


class UsagePromptTokensDetails(BaseModel):
    """Breakdown of the prompt tokens, as in the OpenAI usage object."""

    cached_tokens: Optional[int] = None
    """Prompt tokens served from the cache; part of prompt_tokens, not extra"""


class UsageCompletionTokensDetails(BaseModel):
    """Breakdown of the completion tokens, as in the OpenAI usage object."""

    reasoning_tokens: Optional[int] = None
    """Tokens of the hosted loop's narration; part of completion_tokens, not extra"""


class Usage(BaseModel):
    prompt_tokens: Optional[int] = None

    completion_tokens: Optional[int] = None

    total_tokens: Optional[int] = None

    prompt_tokens_details: Optional[UsagePromptTokensDetails] = None
    """Breakdown of the prompt tokens, as in the OpenAI usage object."""

    completion_tokens_details: Optional[UsageCompletionTokensDetails] = None
    """Breakdown of the completion tokens, as in the OpenAI usage object."""


class HostedToolCallSearchCorpusCallItemMetadataFilter(BaseModel):
    """One metadata filter condition the model may attach to a hosted tool call."""

    key: str
    """Metadata field key"""

    operator: Literal[
        "eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "contains", "starts_with", "not_like", "regex"
    ]
    """Comparison operator"""

    value: Union[str, int, float, bool, List[Union[str, int, float, bool]], None] = None
    """Value to compare against. Use a list for `in`/`not_in`."""


class HostedToolCallSearchCorpusCallItemError(BaseModel):
    """Machine-readable reason a hosted tool call failed (Mixedbread extension)."""

    code: Literal["permission_denied", "invalid_arguments", "server_error"]

    message: str


class HostedToolCallSearchCorpusCallItem(BaseModel):
    """
    Server-side hosted tool executions of this completion (Mixedbread extension);
    chunk results ride along only for requested include keys, e.g.
    search_corpus_call.results
    """

    type: Optional[Literal["search_corpus_call"]] = None

    id: str

    status: Optional[Literal["in_progress", "completed", "failed"]] = None

    queries: Optional[List[str]] = None

    metadata_filters: Optional[List[HostedToolCallSearchCorpusCallItemMetadataFilter]] = None

    filter_mode: Optional[Literal["all", "any"]] = None

    store: Optional[str] = None

    results: Optional[List[Dict[str, object]]] = None

    error: Optional[HostedToolCallSearchCorpusCallItemError] = None
    """Machine-readable reason a hosted tool call failed (Mixedbread extension)."""


class HostedToolCallGrepCallItemMetadataFilter(BaseModel):
    """One metadata filter condition the model may attach to a hosted tool call."""

    key: str
    """Metadata field key"""

    operator: Literal[
        "eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "contains", "starts_with", "not_like", "regex"
    ]
    """Comparison operator"""

    value: Union[str, int, float, bool, List[Union[str, int, float, bool]], None] = None
    """Value to compare against. Use a list for `in`/`not_in`."""


class HostedToolCallGrepCallItemError(BaseModel):
    """Machine-readable reason a hosted tool call failed (Mixedbread extension)."""

    code: Literal["permission_denied", "invalid_arguments", "server_error"]

    message: str


class HostedToolCallGrepCallItem(BaseModel):
    """
    Server-side hosted tool executions of this completion (Mixedbread extension);
    chunk results ride along only for requested include keys, e.g.
    search_corpus_call.results
    """

    type: Optional[Literal["grep_call"]] = None

    id: str

    status: Optional[Literal["in_progress", "completed", "failed"]] = None

    pattern: Optional[str] = None

    targets: Optional[List[Literal["text", "generated"]]] = None

    case_sensitive: Optional[bool] = None

    metadata_filters: Optional[List[HostedToolCallGrepCallItemMetadataFilter]] = None

    filter_mode: Optional[Literal["all", "any"]] = None

    store: Optional[str] = None

    results: Optional[List[Dict[str, object]]] = None

    error: Optional[HostedToolCallGrepCallItemError] = None
    """Machine-readable reason a hosted tool call failed (Mixedbread extension)."""


class HostedToolCallFilterChunksCallItemMetadataFilter(BaseModel):
    """One metadata filter condition the model may attach to a hosted tool call."""

    key: str
    """Metadata field key"""

    operator: Literal[
        "eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "contains", "starts_with", "not_like", "regex"
    ]
    """Comparison operator"""

    value: Union[str, int, float, bool, List[Union[str, int, float, bool]], None] = None
    """Value to compare against. Use a list for `in`/`not_in`."""


class HostedToolCallFilterChunksCallItemError(BaseModel):
    """Machine-readable reason a hosted tool call failed (Mixedbread extension)."""

    code: Literal["permission_denied", "invalid_arguments", "server_error"]

    message: str


class HostedToolCallFilterChunksCallItem(BaseModel):
    """
    Server-side hosted tool executions of this completion (Mixedbread extension);
    chunk results ride along only for requested include keys, e.g.
    search_corpus_call.results
    """

    type: Optional[Literal["filter_chunks_call"]] = None

    id: str

    status: Optional[Literal["in_progress", "completed", "failed"]] = None

    metadata_filters: Optional[List[HostedToolCallFilterChunksCallItemMetadataFilter]] = None

    filter_mode: Optional[Literal["all", "any"]] = None

    rank_by: Optional[str] = None

    direction: Optional[Literal["asc", "desc"]] = None

    store: Optional[str] = None

    results: Optional[List[Dict[str, object]]] = None

    error: Optional[HostedToolCallFilterChunksCallItemError] = None
    """Machine-readable reason a hosted tool call failed (Mixedbread extension)."""


class HostedToolCallInspectMetadataCallItemError(BaseModel):
    """Machine-readable reason a hosted tool call failed (Mixedbread extension)."""

    code: Literal["permission_denied", "invalid_arguments", "server_error"]

    message: str


class HostedToolCallInspectMetadataCallItem(BaseModel):
    """
    Server-side hosted tool executions of this completion (Mixedbread extension);
    chunk results ride along only for requested include keys, e.g.
    search_corpus_call.results
    """

    type: Optional[Literal["inspect_metadata_call"]] = None

    id: str

    status: Optional[Literal["in_progress", "completed", "failed"]] = None

    store: Optional[str] = None

    facets: Optional[Dict[str, object]] = None

    error: Optional[HostedToolCallInspectMetadataCallItemError] = None
    """Machine-readable reason a hosted tool call failed (Mixedbread extension)."""


class HostedToolCallGetChunksCallItemError(BaseModel):
    """Machine-readable reason a hosted tool call failed (Mixedbread extension)."""

    code: Literal["permission_denied", "invalid_arguments", "server_error"]

    message: str


class HostedToolCallGetChunksCallItem(BaseModel):
    """
    Server-side hosted tool executions of this completion (Mixedbread extension);
    chunk results ride along only for requested include keys, e.g.
    search_corpus_call.results
    """

    type: Optional[Literal["get_chunks_call"]] = None

    id: str

    status: Optional[Literal["in_progress", "completed", "failed"]] = None

    chunk_ids: Optional[List[str]] = None

    results: Optional[List[Dict[str, object]]] = None

    error: Optional[HostedToolCallGetChunksCallItemError] = None
    """Machine-readable reason a hosted tool call failed (Mixedbread extension)."""


class HostedToolCallStoreSearchCallItemMetadataFilter(BaseModel):
    """One metadata filter condition the model may attach to a hosted tool call."""

    key: str
    """Metadata field key"""

    operator: Literal[
        "eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "contains", "starts_with", "not_like", "regex"
    ]
    """Comparison operator"""

    value: Union[str, int, float, bool, List[Union[str, int, float, bool]], None] = None
    """Value to compare against. Use a list for `in`/`not_in`."""


class HostedToolCallStoreSearchCallItemError(BaseModel):
    """Machine-readable reason a hosted tool call failed (Mixedbread extension)."""

    code: Literal["permission_denied", "invalid_arguments", "server_error"]

    message: str


class HostedToolCallStoreSearchCallItem(BaseModel):
    """
    Server-side hosted tool executions of this completion (Mixedbread extension);
    chunk results ride along only for requested include keys, e.g.
    search_corpus_call.results
    """

    type: Optional[Literal["store_search_call"]] = None

    id: str

    status: Optional[Literal["in_progress", "completed", "failed"]] = None

    queries: Optional[List[str]] = None

    metadata_filters: Optional[List[HostedToolCallStoreSearchCallItemMetadataFilter]] = None

    filter_mode: Optional[Literal["all", "any"]] = None

    store: Optional[str] = None

    results: Optional[List[Dict[str, object]]] = None

    error: Optional[HostedToolCallStoreSearchCallItemError] = None
    """Machine-readable reason a hosted tool call failed (Mixedbread extension)."""


class HostedToolCallStoreGrepCallItemMetadataFilter(BaseModel):
    """One metadata filter condition the model may attach to a hosted tool call."""

    key: str
    """Metadata field key"""

    operator: Literal[
        "eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "contains", "starts_with", "not_like", "regex"
    ]
    """Comparison operator"""

    value: Union[str, int, float, bool, List[Union[str, int, float, bool]], None] = None
    """Value to compare against. Use a list for `in`/`not_in`."""


class HostedToolCallStoreGrepCallItemError(BaseModel):
    """Machine-readable reason a hosted tool call failed (Mixedbread extension)."""

    code: Literal["permission_denied", "invalid_arguments", "server_error"]

    message: str


class HostedToolCallStoreGrepCallItem(BaseModel):
    """
    Server-side hosted tool executions of this completion (Mixedbread extension);
    chunk results ride along only for requested include keys, e.g.
    search_corpus_call.results
    """

    type: Optional[Literal["store_grep_call"]] = None

    id: str

    status: Optional[Literal["in_progress", "completed", "failed"]] = None

    pattern: Optional[str] = None

    targets: Optional[List[Literal["text", "generated"]]] = None

    case_sensitive: Optional[bool] = None

    metadata_filters: Optional[List[HostedToolCallStoreGrepCallItemMetadataFilter]] = None

    filter_mode: Optional[Literal["all", "any"]] = None

    store: Optional[str] = None

    results: Optional[List[Dict[str, object]]] = None

    error: Optional[HostedToolCallStoreGrepCallItemError] = None
    """Machine-readable reason a hosted tool call failed (Mixedbread extension)."""


class HostedToolCallStoreListChunksCallItemMetadataFilter(BaseModel):
    """One metadata filter condition the model may attach to a hosted tool call."""

    key: str
    """Metadata field key"""

    operator: Literal[
        "eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "contains", "starts_with", "not_like", "regex"
    ]
    """Comparison operator"""

    value: Union[str, int, float, bool, List[Union[str, int, float, bool]], None] = None
    """Value to compare against. Use a list for `in`/`not_in`."""


class HostedToolCallStoreListChunksCallItemError(BaseModel):
    """Machine-readable reason a hosted tool call failed (Mixedbread extension)."""

    code: Literal["permission_denied", "invalid_arguments", "server_error"]

    message: str


class HostedToolCallStoreListChunksCallItem(BaseModel):
    """
    Server-side hosted tool executions of this completion (Mixedbread extension);
    chunk results ride along only for requested include keys, e.g.
    search_corpus_call.results
    """

    type: Optional[Literal["store_list_chunks_call"]] = None

    id: str

    status: Optional[Literal["in_progress", "completed", "failed"]] = None

    metadata_filters: Optional[List[HostedToolCallStoreListChunksCallItemMetadataFilter]] = None

    filter_mode: Optional[Literal["all", "any"]] = None

    rank_by: Optional[str] = None

    direction: Optional[Literal["asc", "desc"]] = None

    store: Optional[str] = None

    results: Optional[List[Dict[str, object]]] = None

    error: Optional[HostedToolCallStoreListChunksCallItemError] = None
    """Machine-readable reason a hosted tool call failed (Mixedbread extension)."""


class HostedToolCallMetadataFacetsCallItemError(BaseModel):
    """Machine-readable reason a hosted tool call failed (Mixedbread extension)."""

    code: Literal["permission_denied", "invalid_arguments", "server_error"]

    message: str


class HostedToolCallMetadataFacetsCallItem(BaseModel):
    """
    Server-side hosted tool executions of this completion (Mixedbread extension);
    chunk results ride along only for requested include keys, e.g.
    search_corpus_call.results
    """

    type: Optional[Literal["store_metadata_facets_call"]] = None

    id: str

    status: Optional[Literal["in_progress", "completed", "failed"]] = None

    store: Optional[str] = None

    facets: Optional[Dict[str, object]] = None

    error: Optional[HostedToolCallMetadataFacetsCallItemError] = None
    """Machine-readable reason a hosted tool call failed (Mixedbread extension)."""


class HostedToolCallListStoresCallItemStore(BaseModel):
    """One store entry returned by the hosted list stores tool."""

    name: str

    description: Optional[str] = None

    connectors: Optional[List[str]] = None
    """Providers of the connectors ingesting into this store, e.g. slack or notion"""


class HostedToolCallListStoresCallItemError(BaseModel):
    """Machine-readable reason a hosted tool call failed (Mixedbread extension)."""

    code: Literal["permission_denied", "invalid_arguments", "server_error"]

    message: str


class HostedToolCallListStoresCallItem(BaseModel):
    """
    Server-side hosted tool executions of this completion (Mixedbread extension);
    chunk results ride along only for requested include keys, e.g.
    search_corpus_call.results
    """

    type: Optional[Literal["list_stores_call"]] = None

    id: str

    status: Optional[Literal["in_progress", "completed", "failed"]] = None

    cursor: Optional[str] = None

    stores: Optional[List[HostedToolCallListStoresCallItemStore]] = None

    has_more: Optional[bool] = None

    next_cursor: Optional[str] = None

    error: Optional[HostedToolCallListStoresCallItemError] = None
    """Machine-readable reason a hosted tool call failed (Mixedbread extension)."""


HostedToolCall: TypeAlias = Annotated[
    Union[
        HostedToolCallSearchCorpusCallItem,
        HostedToolCallGrepCallItem,
        HostedToolCallFilterChunksCallItem,
        HostedToolCallInspectMetadataCallItem,
        HostedToolCallGetChunksCallItem,
        HostedToolCallStoreSearchCallItem,
        HostedToolCallStoreGrepCallItem,
        HostedToolCallStoreListChunksCallItem,
        HostedToolCallMetadataFacetsCallItem,
        HostedToolCallListStoresCallItem,
    ],
    PropertyInfo(discriminator="type"),
]


class ContextManagementAppliedEditAppliedPruneContextEdit(BaseModel):
    """Aggregate of the model's prune_context calls in one request."""

    type: Optional[Literal["prune_context"]] = None

    calls: int
    """Number of prune_context calls the model made in this request"""

    cleared_input_tokens: int
    """Input tokens cleared from the model's context"""


class ContextManagementAppliedEditAppliedTruncateToolResultEdit(BaseModel):
    """One caller tool result shortened by the server's context-overflow recovery."""

    type: Optional[Literal["truncate_tool_result"]] = None

    tool_call_id: str
    """ID of the tool call whose result was shortened"""

    cleared_input_tokens: int
    """Input tokens cleared from the model's context"""


ContextManagementAppliedEdit: TypeAlias = Annotated[
    Union[
        ContextManagementAppliedEditAppliedPruneContextEdit, ContextManagementAppliedEditAppliedTruncateToolResultEdit
    ],
    PropertyInfo(discriminator="type"),
]


class ContextManagement(BaseModel):
    """Context edits applied while serving one request (Mixedbread extension).

    Only ever emitted non-empty: a request whose context was never edited carries no
    `context_management` object at all.
    """

    applied_edits: List[ContextManagementAppliedEdit]


class ToolTicket(BaseModel):
    """One short-lived ticket per client-executed tool call (Mixedbread extension).

    Send the matching ticket as the X-Mxbai-Tool-Ticket header on the store search
    or grep you run for that call, and it bills at the discounted agent rate. Each
    ticket redeems once.
    """

    tool_call_id: str
    """ID of the tool call in `choices[].message.tool_calls` this covers"""

    ticket: str
    """Opaque token to send as the X-Mxbai-Tool-Ticket header"""

    expires_at: int
    """Unix timestamp after which the ticket no longer redeems"""


class TranscriptSystemMessageContentUnionMember1(BaseModel):
    type: Optional[Literal["text"]] = None

    text: str


class TranscriptSystemMessage(BaseModel):
    """Complete stored conversation transcript when requested through include"""

    role: Literal["system"]

    content: Union[str, List[TranscriptSystemMessageContentUnionMember1]]


class TranscriptDeveloperMessageContentUnionMember1(BaseModel):
    type: Optional[Literal["text"]] = None

    text: str


class TranscriptDeveloperMessage(BaseModel):
    """Complete stored conversation transcript when requested through include"""

    role: Literal["developer"]

    content: Union[str, List[TranscriptDeveloperMessageContentUnionMember1]]


class TranscriptUserMessageContentUnionMember1(BaseModel):
    type: Optional[Literal["text"]] = None

    text: str


class TranscriptUserMessage(BaseModel):
    """Complete stored conversation transcript when requested through include"""

    role: Literal["user"]

    content: Union[str, List[TranscriptUserMessageContentUnionMember1]]


class TranscriptAssistantMessageOutputContentUnionMember1(BaseModel):
    type: Optional[Literal["text"]] = None

    text: str


class TranscriptAssistantMessageOutputToolCallFunction(BaseModel):
    name: str

    arguments: str


class TranscriptAssistantMessageOutputToolCall(BaseModel):
    """One function tool call of an assistant message."""

    id: str

    type: Optional[Literal["function"]] = None

    function: TranscriptAssistantMessageOutputToolCallFunction


class TranscriptAssistantMessageOutputAnnotation(BaseModel):
    """The OpenAI ``file_citation`` annotation, plus the chunk it points at.

    ``chunk_id`` is the same ``file_id:chunk_index`` reference every hosted result
    carries, and ``store_id`` the store whose index holds the chunk; the cited text
    and score are on the included tool results.
    """

    type: Optional[Literal["file_citation"]] = None

    file_id: str

    filename: str

    index: int

    chunk_id: str

    store_id: str


class TranscriptAssistantMessageOutput(BaseModel):
    """Complete stored conversation transcript when requested through include"""

    role: Literal["assistant"]

    content: Union[str, List[TranscriptAssistantMessageOutputContentUnionMember1], None] = None

    tool_calls: Optional[List[TranscriptAssistantMessageOutputToolCall]] = None

    reasoning_content: Optional[str] = None

    annotations: Optional[List[TranscriptAssistantMessageOutputAnnotation]] = None


class TranscriptToolMessageContentUnionMember1(BaseModel):
    type: Optional[Literal["text"]] = None

    text: str


class TranscriptToolMessage(BaseModel):
    """Complete stored conversation transcript when requested through include"""

    role: Literal["tool"]

    content: Union[str, List[TranscriptToolMessageContentUnionMember1]]

    tool_call_id: str


Transcript: TypeAlias = Annotated[
    Union[
        TranscriptSystemMessage,
        TranscriptDeveloperMessage,
        TranscriptUserMessage,
        TranscriptAssistantMessageOutput,
        TranscriptToolMessage,
    ],
    PropertyInfo(discriminator="role"),
]


class ChatCreateCompletionResponse(BaseModel):
    """A chat completion object, as returned by the API and persisted for retrieval."""

    id: str

    object: Optional[Literal["chat.completion"]] = None

    created: int

    model: str

    choices: List[Choice]

    usage: Optional[Usage] = None

    metadata: Optional[Dict[str, str]] = None

    title: Optional[str] = None
    """
    Short display title of the conversation this completion belongs to (Mixedbread
    extension)
    """

    hosted_tool_calls: Optional[List[HostedToolCall]] = None
    """
    Server-side hosted tool executions of this completion (Mixedbread extension);
    chunk results ride along only for requested include keys, e.g.
    search_corpus_call.results
    """

    context_management: Optional[ContextManagement] = None
    """Context edits applied while serving one request (Mixedbread extension).

    Only ever emitted non-empty: a request whose context was never edited carries no
    `context_management` object at all.
    """

    tool_tickets: Optional[List[ToolTicket]] = None
    """One short-lived ticket per client-executed tool call (Mixedbread extension).

    Send the matching ticket as the X-Mxbai-Tool-Ticket header on the store search
    or grep you run for that call, and it bills at the discounted agent rate. Each
    ticket redeems once.
    """

    transcript: Optional[List[Transcript]] = None
    """Complete stored conversation transcript when requested through include"""
