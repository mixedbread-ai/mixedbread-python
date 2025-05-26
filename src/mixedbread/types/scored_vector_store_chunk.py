# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel
from .extractions.text_input import TextInput
from .extractions.image_url_input import ImageURLInput

__all__ = ["ScoredVectorStoreChunk", "Value"]

Value: TypeAlias = Union[str, ImageURLInput, TextInput, Dict[str, object], None]


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
