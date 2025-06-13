# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import TypeAlias, TypedDict

__all__ = ["VectorStoreChunkSearchOptionsParam", "Rerank", "RerankRerankConfig"]


class RerankRerankConfig(TypedDict, total=False):
    model: str
    """The name of the reranking model"""

    with_metadata: Union[bool, List[str]]
    """Whether to include metadata in the reranked results"""

    top_k: Optional[int]
    """Maximum number of results to return after reranking.

    If None, returns all reranked results.
    """


Rerank: TypeAlias = Union[bool, RerankRerankConfig]


class VectorStoreChunkSearchOptionsParam(TypedDict, total=False):
    score_threshold: float
    """Minimum similarity score threshold"""

    rewrite_query: bool
    """Whether to rewrite the query"""

    rerank: Optional[Rerank]
    """Whether to rerank results and optional reranking configuration"""

    return_metadata: bool
    """Whether to return file metadata"""
