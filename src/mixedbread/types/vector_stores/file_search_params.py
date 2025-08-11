# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .rerank_config_param import RerankConfigParam
from ..shared_params.search_filter_condition import SearchFilterCondition

__all__ = [
    "FileSearchParams",
    "Filters",
    "FiltersMxbaiOmniCoreVectorStoreModelsSearchFilter1",
    "FiltersMxbaiOmniCoreVectorStoreModelsSearchFilter1All",
    "FiltersMxbaiOmniCoreVectorStoreModelsSearchFilter1Any",
    "FiltersMxbaiOmniCoreVectorStoreModelsSearchFilter1None",
    "FiltersUnionMember2",
    "FiltersUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter1",
    "FiltersUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter1All",
    "FiltersUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter1Any",
    "FiltersUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter1None",
    "SearchOptions",
    "SearchOptionsRerank",
]


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


FiltersMxbaiOmniCoreVectorStoreModelsSearchFilter1All: TypeAlias = Union[SearchFilterCondition, object]

FiltersMxbaiOmniCoreVectorStoreModelsSearchFilter1Any: TypeAlias = Union[SearchFilterCondition, object]

FiltersMxbaiOmniCoreVectorStoreModelsSearchFilter1None: TypeAlias = Union[SearchFilterCondition, object]


class FiltersMxbaiOmniCoreVectorStoreModelsSearchFilter1(TypedDict, total=False):
    all: Optional[Iterable[FiltersMxbaiOmniCoreVectorStoreModelsSearchFilter1All]]
    """List of conditions or filters to be ANDed together"""

    any: Optional[Iterable[FiltersMxbaiOmniCoreVectorStoreModelsSearchFilter1Any]]
    """List of conditions or filters to be ORed together"""

    none: Optional[Iterable[FiltersMxbaiOmniCoreVectorStoreModelsSearchFilter1None]]
    """List of conditions or filters to be NOTed"""


FiltersUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter1All: TypeAlias = Union[SearchFilterCondition, object]

FiltersUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter1Any: TypeAlias = Union[SearchFilterCondition, object]

FiltersUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter1None: TypeAlias = Union[SearchFilterCondition, object]


class FiltersUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter1(TypedDict, total=False):
    all: Optional[Iterable[FiltersUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter1All]]
    """List of conditions or filters to be ANDed together"""

    any: Optional[Iterable[FiltersUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter1Any]]
    """List of conditions or filters to be ORed together"""

    none: Optional[Iterable[FiltersUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter1None]]
    """List of conditions or filters to be NOTed"""


FiltersUnionMember2: TypeAlias = Union[
    FiltersUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter1, SearchFilterCondition
]

Filters: TypeAlias = Union[
    FiltersMxbaiOmniCoreVectorStoreModelsSearchFilter1, SearchFilterCondition, Iterable[FiltersUnionMember2]
]

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
