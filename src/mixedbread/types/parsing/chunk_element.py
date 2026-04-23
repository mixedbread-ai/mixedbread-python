# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .element_type import ElementType

__all__ = ["ChunkElement"]


class ChunkElement(BaseModel):
    """Represents an extracted element from a document with its content and metadata."""

    type: ElementType
    """The type of the extracted element"""

    confidence: float
    """The confidence score of the extraction"""

    bbox: List[object]
    """The bounding box coordinates [x1, y1, x2, y2]"""

    page: int
    """The page number where the element was found"""

    content: str
    """The extracted text content of the element"""

    summary: Optional[str] = None
    """A brief summary of the element's content"""

    image: Optional[str] = None
    """The base64-encoded image data for figure elements"""
