# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ClientRerankParams"]


class ClientRerankParams(TypedDict, total=False):
    model: str
    """The model to use for reranking documents."""

    query: Required[str]
    """The query to rerank the documents."""

    input: Required[SequenceNotStr[Union[str, Iterable[object], object]]]
    """The input documents to rerank."""

    rank_fields: Optional[SequenceNotStr[str]]
    """The fields of the documents to rank."""

    top_k: int
    """The number of documents to return."""

    return_input: bool
    """Whether to return the documents."""

    rewrite_query: bool
    """Wether or not to rewrite the query before passing it to the reranking model"""
