# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .shared_params.search_filter_condition import SearchFilterCondition

__all__ = ["VectorStoreSearchParams", "Filters", "FiltersUnionMember2", "SearchOptions"]


class VectorStoreSearchParams(TypedDict, total=False):
    query: Required[str]
    """Search query text"""

    vector_store_ids: Required[List[str]]
    """IDs of vector stores to search"""

    top_k: int
    """Number of results to return"""

    filters: Optional[Filters]
    """Optional filter conditions"""

    search_options: SearchOptions
    """Search configuration options"""


FiltersUnionMember2: TypeAlias = Union["SearchFilter", SearchFilterCondition]

Filters: TypeAlias = Union["SearchFilter", SearchFilterCondition, Iterable[FiltersUnionMember2]]


class SearchOptions(TypedDict, total=False):
    score_threshold: float
    """Minimum similarity score threshold"""

    rewrite_query: bool
    """Whether to rewrite the query"""

    return_metadata: bool
    """Whether to return file metadata"""


from .shared_params.search_filter import SearchFilter
