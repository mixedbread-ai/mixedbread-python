# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .embedding import Embedding
from .multi_encoding_embedding import MultiEncodingEmbedding

__all__ = ["Em", "Usage"]


class Usage(BaseModel):
    prompt_tokens: int
    """The number of tokens used for the prompt"""

    total_tokens: int
    """The total number of tokens used"""

    completion_tokens: Optional[int] = None
    """The number of tokens used for the completion"""


class Em(BaseModel):
    usage: Usage
    """The usage of the model"""

    model: str
    """The model used"""

    data: Union[List[Embedding], List[MultiEncodingEmbedding]]
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
