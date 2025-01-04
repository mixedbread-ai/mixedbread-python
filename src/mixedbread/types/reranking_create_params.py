# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["RerankingCreateParams"]


class RerankingCreateParams(TypedDict, total=False):
    input: Required[object]

    query: Required[str]
    """The query to rerank the documents."""

    model: str
    """The model to use for reranking documents."""

    rank_fields: Optional[List[str]]
    """The fields of the documents to rank."""

    return_input: bool
    """Whether to return the documents."""

    top_k: int
    """The number of documents to return."""
