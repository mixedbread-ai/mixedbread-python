# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from ..shared_params.search_filter_condition import SearchFilterCondition
from ..vector_store_file_search_options_param import VectorStoreFileSearchOptionsParam

__all__ = ["FileSearchParams", "Filters", "FiltersUnionMember2"]


class FileSearchParams(TypedDict, total=False):
    query: Required[str]
    """Search query text"""

    vector_store_ids: Required[List[str]]
    """IDs of vector stores to search"""

    top_k: int
    """Number of results to return"""

    filters: Optional[Filters]
    """Optional filter conditions"""

    search_options: VectorStoreFileSearchOptionsParam
    """Search configuration options"""


FiltersUnionMember2: TypeAlias = Union["SearchFilter", SearchFilterCondition]

Filters: TypeAlias = Union["SearchFilter", SearchFilterCondition, Iterable[FiltersUnionMember2]]

from ..shared_params.search_filter import SearchFilter
