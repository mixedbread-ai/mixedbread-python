# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["VectorStoreSearchParams", "Pagination", "SearchOptions"]


class VectorStoreSearchParams(TypedDict, total=False):
    query: Required[str]
    """Search query text"""

    vector_store_ids: Required[List[str]]
    """IDs of vector stores to search"""

    pagination: Pagination
    """Pagination options"""

    search_options: SearchOptions
    """Search configuration options"""


class Pagination(TypedDict, total=False):
    limit: int
    """Maximum number of items to return per page"""

    offset: int
    """Offset of the first item to return"""


class SearchOptions(TypedDict, total=False):
    return_chunks: bool
    """Whether to return matching text chunks"""

    return_metadata: bool
    """Whether to return file metadata"""

    rewrite_query: bool
    """Whether to rewrite the query"""

    score_threshold: float
    """Minimum similarity score threshold"""
