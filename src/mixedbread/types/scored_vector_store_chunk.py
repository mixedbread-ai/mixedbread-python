# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["ScoredVectorStoreChunk", "Value", "ValueImageURLInput", "ValueImageURLInputImage", "ValueTextInput"]


class ValueImageURLInputImage(BaseModel):
    url: str
    """The image URL. Can be either a URL or a Data URI."""


class ValueImageURLInput(BaseModel):
    type: Optional[Literal["image_url"]] = None
    """Input type identifier"""

    image: ValueImageURLInputImage
    """The image input specification."""


class ValueTextInput(BaseModel):
    type: Optional[Literal["text"]] = None
    """Input type identifier"""

    text: str
    """Text content to process"""


Value: TypeAlias = Union[str, ValueImageURLInput, ValueTextInput, Dict[str, object], None]


class ScoredVectorStoreChunk(BaseModel):
    position: int
    """position of the chunk in a file"""

    value: Optional[Value] = None
    """value of the chunk"""

    content: Optional[str] = None
    """content of the chunk"""

    score: float
    """score of the chunk"""

    file_id: str
    """file id"""

    filename: str
    """filename"""

    vector_store_id: str
    """vector store id"""

    metadata: Optional[object] = None
    """file metadata"""
