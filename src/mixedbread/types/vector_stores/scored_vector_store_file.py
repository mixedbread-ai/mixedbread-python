# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..scored_vector_store_chunk import ScoredVectorStoreChunk

__all__ = ["ScoredVectorStoreFile"]


class ScoredVectorStoreFile(BaseModel):
    id: str
    """file id"""

    created_at: datetime
    """Timestamp of vector store file creation"""

    score: float
    """score of the file"""

    usage_bytes: int
    """usage in bytes"""

    vector_store_id: str
    """vector store id"""

    version: int
    """version of the file"""

    chunks: Optional[List[ScoredVectorStoreChunk]] = None
    """chunks"""

    last_error: Optional[object] = None
    """last error"""

    metadata: Optional[object] = None
    """metadata"""

    status: Optional[Literal["in_progress", "completed", "failed", "cancelled"]] = None
    """status of the file"""
