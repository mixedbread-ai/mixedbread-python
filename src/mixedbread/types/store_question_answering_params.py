# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .store_chunk_search_options_param import StoreChunkSearchOptionsParam
from .shared_params.search_filter_condition import SearchFilterCondition

__all__ = ["StoreQuestionAnsweringParams", "Filters", "FiltersUnionMember2", "QaOptions"]


class StoreQuestionAnsweringParams(TypedDict, total=False):
    query: str
    """Question to answer.

    If not provided, the question will be extracted from the passed messages.
    """

    store_identifiers: Required[SequenceNotStr[str]]
    """IDs or names of stores to search"""

    top_k: int
    """Number of results to return"""

    filters: Optional[Filters]
    """Optional filter conditions"""

    file_ids: Union[Iterable[object], SequenceNotStr[str], None]
    """Optional list of file IDs to filter chunks by (inclusion filter)"""

    search_options: StoreChunkSearchOptionsParam
    """Search configuration options"""

    stream: bool
    """Whether to stream the answer"""

    qa_options: QaOptions
    """Question answering configuration options"""


FiltersUnionMember2: TypeAlias = Union["SearchFilter", SearchFilterCondition]

Filters: TypeAlias = Union["SearchFilter", SearchFilterCondition, Iterable[FiltersUnionMember2]]


class QaOptions(TypedDict, total=False):
    """Question answering configuration options"""

    cite: bool
    """Whether to use citations"""

    multimodal: bool
    """Whether to use multimodal context"""


from .shared_params.search_filter import SearchFilter
