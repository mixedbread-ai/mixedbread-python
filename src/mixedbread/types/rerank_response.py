# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.usage import Usage

__all__ = ["RerankResponse", "Data"]


class Data(BaseModel):
    index: int
    """The index of the document."""

    score: float
    """The score of the document."""

    input: Optional[object] = None
    """The input document."""

    object: Optional[Literal["rank_result"]] = None
    """The object type."""


class RerankResponse(BaseModel):
    usage: Usage
    """The usage of the model"""

    model: str
    """The model used"""

    data: List[Data]
    """The ranked documents."""

    object: Optional[
        Literal[
            "list",
            "parsing_job",
            "job",
            "embedding",
            "embedding_dict",
            "rank_result",
            "file",
            "vector_store",
            "vector_store.file",
            "api_key",
        ]
    ] = None
    """The object type of the response"""

    top_k: int
    """The number of documents to return."""

    return_input: bool
    """Whether to return the documents."""
