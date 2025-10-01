# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ScoredImageURLInputChunk", "ImageURL"]


class ImageURL(BaseModel):
    url: str
    """The image URL. Can be either a URL or a Data URI."""

    format: Optional[str] = None
    """The image format/mimetype"""


class ScoredImageURLInputChunk(BaseModel):
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

    type: Optional[Literal["image_url"]] = None
    """Input type identifier"""

    ocr_text: Optional[str] = None
    """ocr text of the image"""

    summary: Optional[str] = None
    """summary of the image"""

    image_url: ImageURL
    """The image input specification."""
