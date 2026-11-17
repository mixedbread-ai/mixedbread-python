# File generated from our OpenAPI spec by sdkgen. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .shared_params.search_filter import SearchFilter
from .store_chunk_search_options_param import StoreChunkSearchOptionsParam
from .shared_params.search_filter_condition import SearchFilterCondition

__all__ = ["StoreQuestionAnsweringParams", "Filters", "FiltersUnionMember2", "QaOptions"]

FiltersUnionMember2: TypeAlias = Union[SearchFilter, SearchFilterCondition]

Filters: TypeAlias = Union[SearchFilter, SearchFilterCondition, Iterable[FiltersUnionMember2]]


class QaOptions(TypedDict, total=False):
    """Question answering configuration options"""

    cite: bool
    """Whether to use citations"""

    multimodal: bool
    """Whether to use multimodal context"""


class StoreQuestionAnsweringParams(TypedDict, total=False):
    store_identifiers: Required[SequenceNotStr[str]]
    """IDs or names of stores"""

    filters: Optional[Filters]
    """Optional filter conditions"""

    file_ids: Union[Iterable[object], SequenceNotStr[str], None]
    """Optional list of file IDs to filter chunks by (inclusion filter)"""

    query: str
    """Question to answer.

    If not provided, the question will be extracted from the passed messages.
    """

    top_k: Optional[int]
    """Maximum number of results to return.

    When omitted or null, agentic search returns all chunks selected by the agent
    without a final-result cap; non-agentic search returns up to 10. Required when
    strict_top_k is true.
    """

    search_options: StoreChunkSearchOptionsParam
    """Search configuration options"""

    stream: bool
    """
    Internal: when set, the response is a server-sent event stream of the retrieved
    chunks, live trace events, and finally the answer. Used by the Mixedbread
    playground; not part of the documented public API.
    """

    instructions: Optional[str]
    """
    Additional custom instructions (followed only when not in conflict with existing
    rules)
    """

    qa_options: QaOptions
    """Question answering configuration options"""
