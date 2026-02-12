# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = ["StoreChunkSearchOptionsParam", "Rerank", "RerankRerankConfig", "Agentic", "AgenticAgenticSearchConfig"]


class RerankRerankConfig(TypedDict, total=False):
    """Represents a reranking configuration."""

    model: str
    """The name of the reranking model"""

    with_metadata: Union[bool, SequenceNotStr[str]]
    """Whether to include metadata in the reranked results"""

    top_k: Optional[int]
    """Maximum number of results to return after reranking.

    If None, returns all reranked results.
    """


Rerank: TypeAlias = Union[bool, RerankRerankConfig]


class AgenticAgenticSearchConfig(TypedDict, total=False):
    """Configuration for agentic multi-query search."""

    max_rounds: int
    """Maximum number of search rounds"""

    queries_per_round: int
    """Maximum queries per round"""

    results_per_query: int
    """Results to fetch per query"""


Agentic: TypeAlias = Union[bool, AgenticAgenticSearchConfig]


class StoreChunkSearchOptionsParam(TypedDict, total=False):
    """Options for configuring store chunk searches."""

    score_threshold: float
    """Minimum similarity score threshold"""

    rewrite_query: bool
    """Whether to rewrite the query.

    Ignored when agentic is enabled (the agent handles query decomposition).
    """

    rerank: Optional[Rerank]
    """Whether to rerank results and optional reranking configuration.

    Ignored when agentic is enabled (the agent handles ranking).
    """

    agentic: Optional[Agentic]
    """
    Whether to use agentic multi-query search with automatic query decomposition and
    ranking. When enabled, rewrite_query and rerank options are ignored.
    """

    return_metadata: bool
    """Whether to return file metadata"""

    apply_search_rules: bool
    """Whether to apply search rules"""
