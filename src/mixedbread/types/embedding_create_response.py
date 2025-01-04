# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EmbeddingCreateResponse", "DataUnionMember0", "DataUnionMember1", "DataUnionMember1Embedding", "Usage"]


class DataUnionMember0(BaseModel):
    embedding: Union[List[float], List[int], str]
    """The encoded embedding."""

    index: int
    """The index of the embedding."""

    object: Literal["embedding"]
    """The object type of the embedding."""


class DataUnionMember1Embedding(BaseModel):
    base64: Optional[List[str]] = None

    binary: Optional[List[int]] = None

    float: Optional[List[builtins.float]] = None

    int8: Optional[List[int]] = None

    ubinary: Optional[List[int]] = None

    uint8: Optional[List[int]] = None


class DataUnionMember1(BaseModel):
    embedding: DataUnionMember1Embedding
    """
    The encoded embedding data by encoding format.Returned, if more than one
    encoding format is used.
    """

    index: int
    """The index of the embedding."""

    object: Literal["embedding_dict"]
    """The object type of the embedding."""


class Usage(BaseModel):
    prompt_tokens: int
    """The number of tokens used for the prompt"""

    total_tokens: int
    """The total number of tokens used"""

    completion_tokens: Optional[int] = None
    """The number of tokens used for the completion"""


class EmbeddingCreateResponse(BaseModel):
    data: Union[List[DataUnionMember0], List[DataUnionMember1]]
    """The created embeddings."""

    dimensions: Optional[int] = None
    """The number of dimensions used for the embeddings."""

    encoding_format: Union[
        Literal["float", "float16", "base64", "binary", "ubinary", "int8", "uint8"],
        List[Literal["float", "float16", "base64", "binary", "ubinary", "int8", "uint8"]],
    ]
    """The encoding format of the embeddings."""

    model: str
    """The model used"""

    normalized: bool
    """Whether the embeddings are normalized."""

    usage: Usage
    """The usage of the model"""

    object: Optional[
        Literal[
            "list",
            "job",
            "embedding",
            "embedding_dict",
            "text_document",
            "file",
            "vector_store",
            "vector_store.file",
            "api_key",
        ]
    ] = None
    """The object type of the response"""
