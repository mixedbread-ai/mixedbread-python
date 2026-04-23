# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import TypeAlias, TypedDict

from .rerank_config_param import RerankConfigParam
from .agentic_search_config_param import AgenticSearchConfigParam

__all__ = ["StoreChunkSearchOptionsParam", "Rerank", "Agentic"]

Rerank: TypeAlias = Union[bool, RerankConfigParam]

Agentic: TypeAlias = Union[bool, AgenticSearchConfigParam]


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
