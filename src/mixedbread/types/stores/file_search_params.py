# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..shared_params.search_filter_condition import SearchFilterCondition

__all__ = [
    "FileSearchParams",
    "Filters",
    "FiltersUnionMember2",
    "SearchOptions",
    "SearchOptionsRerank",
    "SearchOptionsRerankRerankConfig",
    "SearchOptionsAgentic",
    "SearchOptionsAgenticAgenticSearchConfig",
]


class FileSearchParams(TypedDict, total=False):
    query: Required[str]
    """Search query text"""

    store_identifiers: Required[SequenceNotStr[str]]
    """IDs or names of stores to search"""

    top_k: int
    """Number of results to return"""

    filters: Optional[Filters]
    """Optional filter conditions"""

    file_ids: Union[Iterable[object], SequenceNotStr[str], None]
    """Optional list of file IDs to filter chunks by (inclusion filter)"""

    search_options: SearchOptions
    """Search configuration options"""


FiltersUnionMember2: TypeAlias = Union["SearchFilter", SearchFilterCondition]

Filters: TypeAlias = Union["SearchFilter", SearchFilterCondition, Iterable[FiltersUnionMember2]]


class SearchOptionsRerankRerankConfig(TypedDict, total=False):
    """Represents a reranking configuration."""

    model: str
    """The name of the reranking model"""

    with_metadata: Union[bool, SequenceNotStr[str]]
    """Whether to include metadata in the reranked results"""

    top_k: Optional[int]
    """Maximum number of results to return after reranking.

    If None, returns all reranked results.
    """


SearchOptionsRerank: TypeAlias = Union[bool, SearchOptionsRerankRerankConfig]


class SearchOptionsAgenticAgenticSearchConfig(TypedDict, total=False):
    """Configuration for agentic multi-query search."""

    max_rounds: int
    """Maximum number of search rounds"""

    queries_per_round: int
    """Maximum queries per round"""

    results_per_query: int
    """Results to fetch per query"""


SearchOptionsAgentic: TypeAlias = Union[bool, SearchOptionsAgenticAgenticSearchConfig]


class SearchOptions(TypedDict, total=False):
    """Search configuration options"""

    score_threshold: float
    """Minimum similarity score threshold"""

    rewrite_query: bool
    """Whether to rewrite the query.

    Ignored when agentic is enabled (the agent handles query decomposition).
    """

    rerank: Optional[SearchOptionsRerank]
    """Whether to rerank results and optional reranking configuration.

    Ignored when agentic is enabled (the agent handles ranking).
    """

    agentic: Optional[SearchOptionsAgentic]
    """
    Whether to use agentic multi-query search with automatic query decomposition and
    ranking. When enabled, rewrite_query and rerank options are ignored.
    """

    return_metadata: bool
    """Whether to return file metadata"""

    return_chunks: bool
    """Whether to return matching text chunks"""

    chunks_per_file: int
    """Number of chunks to return for each file"""

    apply_search_rules: bool
    """Whether to apply search rules"""


from ..shared_params.search_filter import SearchFilter
