# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MultiEncodingEmbedding", "Embedding"]


class Embedding(BaseModel):
    """
    The encoded embedding data by encoding format.Returned, if more than one encoding format is used.
    """

    float: Optional[List[builtins.float]] = None

    int8: Optional[List[int]] = None

    uint8: Optional[List[int]] = None

    binary: Optional[List[int]] = None

    ubinary: Optional[List[int]] = None

    base64: Optional[str] = None


class MultiEncodingEmbedding(BaseModel):
    embedding: Embedding
    """
    The encoded embedding data by encoding format.Returned, if more than one
    encoding format is used.
    """

    index: int
    """The index of the embedding."""

    object: Optional[Literal["embedding_dict"]] = None
    """The object type of the embedding."""
