# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["ScoredVectorStoreChunk", "Value", "ValueImageURLInput", "ValueImageURLInputImage", "ValueTextInput"]


class ValueImageURLInputImage(BaseModel):
    url: str
    """The image URL. Can be either a URL or a Data URI."""


class ValueImageURLInput(BaseModel):
    image: ValueImageURLInputImage
    """The image input specification."""

    type: Optional[Literal["image_url"]] = None
    """Input type identifier"""


class ValueTextInput(BaseModel):
    text: str
    """Text content to process"""

    type: Optional[Literal["text"]] = None
    """Input type identifier"""


Value: TypeAlias = Union[str, ValueImageURLInput, ValueTextInput, Dict[str, object], None]


class ScoredVectorStoreChunk(BaseModel):
    file_id: str
    """file id"""

    position: int
    """position of the chunk in a file"""

    score: float
    """score of the chunk"""

    vector_store_id: str
    """vector store id"""

    content: Optional[str] = None
    """content of the chunk"""

    metadata: Optional[object] = None
    """file metadata"""

    value: Optional[Value] = None
    """value of the chunk"""
