# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .chunk import Chunk
from ..._models import BaseModel
from .element_type import ElementType
from .return_format import ReturnFormat
from .chunking_strategy import ChunkingStrategy

__all__ = ["DocumentParserResult"]


class DocumentParserResult(BaseModel):
    """Result of document parsing operation."""

    chunking_strategy: ChunkingStrategy
    """The strategy used for chunking the document"""

    return_format: ReturnFormat
    """The format of the returned content"""

    element_types: List[ElementType]
    """The types of elements extracted"""

    chunks: List[Chunk]
    """List of extracted chunks from the document"""

    page_sizes: Optional[List[List[object]]] = None
    """List of (width, height) tuples for each page"""
