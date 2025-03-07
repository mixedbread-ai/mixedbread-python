# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VectorStoreChunkSearchOptionsParam"]


class VectorStoreChunkSearchOptionsParam(TypedDict, total=False):
    score_threshold: float
    """Minimum similarity score threshold"""

    rewrite_query: bool
    """Whether to rewrite the query"""

    return_metadata: bool
    """Whether to return file metadata"""
