# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RerankingCreateResponse", "Data", "Usage"]


class Data(BaseModel):
    index: int
    """The index of the document."""

    input: Optional[object] = None
    """The input document."""

    score: float
    """The score of the document."""

    object: Optional[Literal["list", "embedding", "embedding_dict", "text_document", "file"]] = None
    """The object type."""


class Usage(BaseModel):
    prompt_tokens: int
    """The number of tokens used for the prompt"""

    total_tokens: int
    """The total number of tokens used"""

    completion_tokens: Optional[int] = None
    """The number of tokens used for the completion"""


class RerankingCreateResponse(BaseModel):
    data: List[Data]
    """The ranked documents."""

    model: str
    """The model used"""

    return_input: bool
    """Whether to return the documents."""

    top_k: int
    """The number of documents to return."""

    usage: Usage
    """The usage of the model"""

    object: Optional[Literal["list", "embedding", "embedding_dict", "text_document", "file"]] = None
    """The object type of the response"""
