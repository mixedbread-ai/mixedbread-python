# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VectorStoreCreateResponse", "ExpiresAfter", "FileCounts"]


class ExpiresAfter(BaseModel):
    anchor: Optional[Literal["last_used_at"]] = None
    """Anchor date for the expiration policy"""

    days: Optional[int] = None
    """Number of days after which the vector store expires"""


class FileCounts(BaseModel):
    canceled: Optional[int] = None
    """Number of files whose processing was canceled"""

    failed: Optional[int] = None
    """Number of files that failed processing"""

    in_progress: Optional[int] = None
    """Number of files currently being processed"""

    successful: Optional[int] = None
    """Number of successfully processed files"""

    total: Optional[int] = None
    """Total number of files"""


class VectorStoreCreateResponse(BaseModel):
    id: str
    """Unique identifier for the vector store"""

    created_at: datetime
    """Timestamp when the vector store was created"""

    name: str
    """Name of the vector store"""

    updated_at: datetime
    """Timestamp when the vector store was last updated"""

    description: Optional[str] = None
    """Detailed description of the vector store's purpose and contents"""

    expires_after: Optional[ExpiresAfter] = None
    """Represents an expiration policy for a vector store."""

    expires_at: Optional[datetime] = None
    """Optional expiration timestamp for the vector store"""

    file_counts: Optional[FileCounts] = None
    """Counts of files in different states"""

    last_active_at: Optional[datetime] = None
    """Timestamp when the vector store was last used"""

    metadata: Optional[object] = None
    """Additional metadata associated with the vector store"""

    object: Optional[Literal["vector_store"]] = None
    """Type of the object"""
