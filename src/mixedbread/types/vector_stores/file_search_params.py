# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["FileSearchParams", "SearchOptions"]


class FileSearchParams(TypedDict, total=False):
    query: Required[str]
    """Search query text"""

    vector_store_ids: Required[List[str]]
    """IDs of vector stores to search"""

    search_options: SearchOptions
    """Search configuration options"""

    top_k: int
    """Number of results to return"""


class SearchOptions(TypedDict, total=False):
    return_chunks: bool
    """Whether to return matching text chunks"""

    return_metadata: bool
    """Whether to return file metadata"""

    rewrite_query: bool
    """Whether to rewrite the query"""

    score_threshold: float
    """Minimum similarity score threshold"""
