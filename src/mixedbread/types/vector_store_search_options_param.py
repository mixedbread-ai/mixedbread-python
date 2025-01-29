# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VectorStoreSearchOptionsParam"]


class VectorStoreSearchOptionsParam(TypedDict, total=False):
    return_metadata: bool
    """Whether to return file metadata"""

    return_chunks: bool
    """Whether to return matching text chunks"""

    score_threshold: float
    """Minimum similarity score threshold"""

    rewrite_query: bool
    """Whether to rewrite the query"""
