# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .embedding import Embedding

__all__ = ["EmbeddingCreateResponse", "Usage", "DataUnionMember1", "DataUnionMember1Embedding"]


class Usage(BaseModel):
    prompt_tokens: int
    """The number of tokens used for the prompt"""

    total_tokens: int
    """The total number of tokens used"""

    completion_tokens: Optional[int] = None
    """The number of tokens used for the completion"""


class DataUnionMember1Embedding(BaseModel):
    float: Optional[List[builtins.float]] = None

    int8: Optional[List[int]] = None

    uint8: Optional[List[int]] = None

    binary: Optional[List[int]] = None

    ubinary: Optional[List[int]] = None

    base64: Optional[str] = None


class DataUnionMember1(BaseModel):
    embedding: DataUnionMember1Embedding
    """
    The encoded embedding data by encoding format.Returned, if more than one
    encoding format is used.
    """

    index: int
    """The index of the embedding."""

    object: Optional[Literal["embedding_dict"]] = None
    """The object type of the embedding."""


class EmbeddingCreateResponse(BaseModel):
    usage: Usage
    """The usage of the model"""

    model: str
    """The model used"""

    data: Union[List[Embedding], List[DataUnionMember1]]
    """The created embeddings."""

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

    normalized: bool
    """Whether the embeddings are normalized."""

    encoding_format: Union[
        Literal["float", "float16", "base64", "binary", "ubinary", "int8", "uint8"],
        List[Literal["float", "float16", "base64", "binary", "ubinary", "int8", "uint8"]],
    ]
    """The encoding formats of the embeddings."""

    dimensions: Optional[int] = None
    """The number of dimensions used for the embeddings."""
