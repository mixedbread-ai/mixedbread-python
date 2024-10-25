# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["ServiceStatusRerankParams", "Query", "QueryTextInput"]


class ServiceStatusRerankParams(TypedDict, total=False):
    input: Required[Union[List[str], Iterable[object]]]
    """The text input documents to rerank."""

    query: Required[Query]
    """The query to rerank the documents."""

    model: str
    """The model to use for reranking documents."""

    rank_fields: Optional[List[str]]
    """The fields of the documents to rank."""

    return_input: bool
    """Whether to return the documents."""

    top_k: int
    """The number of documents to return."""


class QueryTextInput(TypedDict, total=False):
    text: Required[str]
    """The text to be processed"""


Query: TypeAlias = Union[QueryTextInput, str]
