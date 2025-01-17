# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .vector_store_search_options_param import VectorStoreSearchOptionsParam
from .shared_params.search_filter_condition import SearchFilterCondition

__all__ = ["VectorStoreQuestionAnsweringParams", "Filters", "FiltersUnionMember2", "QaOptions"]


class VectorStoreQuestionAnsweringParams(TypedDict, total=False):
    vector_store_ids: Required[List[str]]
    """IDs of vector stores to search"""

    filters: Optional[Filters]
    """Optional filter conditions"""

    qa_options: QaOptions
    """Question answering configuration options"""

    query: str
    """Question to answer.

    If not provided, the question will be extracted from the passed messages.
    """

    search_options: VectorStoreSearchOptionsParam
    """Search configuration options"""

    stream: bool
    """Whether to stream the answer"""

    top_k: int
    """Number of results to return"""


FiltersUnionMember2: TypeAlias = Union["SearchFilter", SearchFilterCondition]

Filters: TypeAlias = Union["SearchFilter", SearchFilterCondition, Iterable[FiltersUnionMember2]]


class QaOptions(TypedDict, total=False):
    cite: bool
    """Whether to use citations"""


from .shared_params.search_filter import SearchFilter
