# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .rerank_config_param import RerankConfigParam
from ..shared_params.search_filter_condition import SearchFilterCondition

__all__ = ["FileSearchParams", "Filters", "FiltersUnionMember2", "SearchOptions", "SearchOptionsRerank"]


class FileSearchParams(TypedDict, total=False):
    query: Required[str]
    """Search query text"""

    vector_store_identifiers: Optional[List[str]]
    """IDs or names of vector stores to search"""

    vector_store_ids: Optional[List[str]]

    top_k: int
    """Number of results to return"""

    filters: Optional[Filters]
    """Optional filter conditions"""

    file_ids: Union[Iterable[object], List[str], None]
    """Optional list of file IDs to filter chunks by (inclusion filter)"""

    search_options: SearchOptions
    """Search configuration options"""


FiltersUnionMember2: TypeAlias = Union["SearchFilter", SearchFilterCondition]

Filters: TypeAlias = Union["SearchFilter", SearchFilterCondition, Iterable[FiltersUnionMember2]]

SearchOptionsRerank: TypeAlias = Union[bool, RerankConfigParam]


class SearchOptions(TypedDict, total=False):
    score_threshold: float
    """Minimum similarity score threshold"""

    rewrite_query: bool
    """Whether to rewrite the query"""

    rerank: Optional[SearchOptionsRerank]
    """Whether to rerank results and optional reranking configuration"""

    return_metadata: bool
    """Whether to return file metadata"""

    return_chunks: bool
    """Whether to return matching text chunks"""

    chunks_per_file: int
    """Number of chunks to return for each file"""

    apply_search_rules: bool
    """Whether to apply search rules"""


from ..shared_params.search_filter import SearchFilter
