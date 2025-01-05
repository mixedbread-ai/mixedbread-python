# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .scored_vector_store_chunk import ScoredVectorStoreChunk

__all__ = ["ScoredVectorStoreFile"]


class ScoredVectorStoreFile(BaseModel):
    id: str
    """Unique identifier for the file"""

    created_at: datetime
    """Timestamp of vector store file creation"""

    score: float
    """score of the file"""

    vector_store_id: str
    """ID of the containing vector store"""

    chunks: Optional[List[ScoredVectorStoreChunk]] = None
    """chunks"""

    errors: Optional[List[str]] = None
    """List of error messages if processing failed"""

    metadata: Optional[object] = None
    """Optional file metadata"""

    object: Optional[Literal["vector_store.file"]] = None
    """Type of the object"""

    status: Optional[Literal["none", "running", "canceled", "successful", "failed", "resumable", "pending"]] = None
    """Processing status of the file"""

    usage_bytes: Optional[int] = None
    """Storage usage in bytes"""

    version: Optional[int] = None
    """Version number of the file"""
