# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["VectorStoreQuestionAnsweringParams", "QaOptions", "SearchOptions"]


class VectorStoreQuestionAnsweringParams(TypedDict, total=False):
    vector_store_ids: Required[List[str]]
    """IDs of vector stores to search"""

    qa_options: QaOptions
    """Question answering configuration options"""

    query: str
    """Question to answer.

    If not provided, the question will be extracted from the passed messages.
    """

    search_options: SearchOptions
    """Search configuration options"""

    stream: bool
    """Whether to stream the answer"""

    top_k: int
    """Number of results to return"""


class QaOptions(TypedDict, total=False):
    cite: bool
    """Whether to use citations"""


class SearchOptions(TypedDict, total=False):
    return_chunks: bool
    """Whether to return matching text chunks"""

    return_metadata: bool
    """Whether to return file metadata"""

    rewrite_query: bool
    """Whether to rewrite the query"""

    score_threshold: float
    """Minimum similarity score threshold"""
