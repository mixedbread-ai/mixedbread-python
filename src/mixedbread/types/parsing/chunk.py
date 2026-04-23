# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .chunk_element import ChunkElement

__all__ = ["Chunk"]


class Chunk(BaseModel):
    """A chunk of text extracted from a document page."""

    content: Optional[str] = None
    """The full content of the chunk"""

    content_to_embed: str
    """The content of the chunk to embed"""

    elements: List[ChunkElement]
    """List of elements contained in this chunk"""
