# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import TypeAlias, TypedDict

from .vector_stores.rerank_config_param import RerankConfigParam

__all__ = ["VectorStoreChunkSearchOptionsParam", "Rerank"]

Rerank: TypeAlias = Union[bool, RerankConfigParam]


class VectorStoreChunkSearchOptionsParam(TypedDict, total=False):
    """Options for configuring vector store chunk searches."""

    score_threshold: float
    """Minimum similarity score threshold"""

    rewrite_query: bool
    """Whether to rewrite the query"""

    rerank: Optional[Rerank]
    """Whether to rerank results and optional reranking configuration"""

    return_metadata: bool
    """Whether to return file metadata"""

    apply_search_rules: bool
    """Whether to apply search rules"""
