# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .shared_params.search_filter_condition import SearchFilterCondition

__all__ = ["VectorStoreQuestionAnsweringParams", "Filters", "FiltersUnionMember2", "SearchOptions", "QaOptions"]


class VectorStoreQuestionAnsweringParams(TypedDict, total=False):
    query: str
    """Question to answer.

    If not provided, the question will be extracted from the passed messages.
    """

    vector_store_ids: Required[List[str]]
    """IDs of vector stores to search"""

    top_k: int
    """Number of results to return"""

    filters: Optional[Filters]
    """Optional filter conditions"""

    search_options: SearchOptions
    """Search configuration options"""

    stream: bool
    """Whether to stream the answer"""

    qa_options: QaOptions
    """Question answering configuration options"""


FiltersUnionMember2: TypeAlias = Union["SearchFilter", SearchFilterCondition]

Filters: TypeAlias = Union["SearchFilter", SearchFilterCondition, Iterable[FiltersUnionMember2]]


class SearchOptions(TypedDict, total=False):
    score_threshold: float
    """Minimum similarity score threshold"""

    rewrite_query: bool
    """Whether to rewrite the query"""

    return_metadata: bool
    """Whether to return file metadata"""


class QaOptions(TypedDict, total=False):
    cite: bool
    """Whether to use citations"""

    multimodal: bool
    """Whether to use multimodal context"""


from .shared_params.search_filter import SearchFilter
