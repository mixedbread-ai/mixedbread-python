# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Embedding"]


class Embedding(BaseModel):
    embedding: Union[List[float], List[int], str]
    """The encoded embedding."""

    index: int
    """The index of the embedding."""

    object: Literal["embedding"]
    """The object type of the embedding."""
