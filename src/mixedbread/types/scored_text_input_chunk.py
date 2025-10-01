# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ScoredTextInputChunk"]


class ScoredTextInputChunk(BaseModel):
    chunk_index: int
    """position of the chunk in a file"""

    mime_type: Optional[str] = None
    """mime type of the chunk"""

    generated_metadata: Optional[Dict[str, object]] = None
    """metadata of the chunk"""

    model: Optional[str] = None
    """model used for this chunk"""

    score: float
    """score of the chunk"""

    file_id: str
    """file id"""

    filename: str
    """filename"""

    store_id: str
    """store id"""

    metadata: Optional[object] = None
    """file metadata"""

    type: Optional[Literal["text"]] = None
    """Input type identifier"""

    offset: Optional[int] = None
    """The offset of the text in the file relative to the start of the file."""

    text: str
    """Text content to process"""
