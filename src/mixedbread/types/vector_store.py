# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .expires_after import ExpiresAfter

__all__ = ["VectorStore", "FileCounts"]


class FileCounts(BaseModel):
    pending: Optional[int] = None
    """Number of files waiting to be processed"""

    in_progress: Optional[int] = None
    """Number of files currently being processed"""

    cancelled: Optional[int] = None
    """Number of files whose processing was cancelled"""

    completed: Optional[int] = None
    """Number of successfully processed files"""

    failed: Optional[int] = None
    """Number of files that failed processing"""

    total: Optional[int] = None
    """Total number of files"""


class VectorStore(BaseModel):
    id: str
    """Unique identifier for the vector store"""

    name: str
    """Name of the vector store"""

    description: Optional[str] = None
    """Detailed description of the vector store's purpose and contents"""

    is_public: Optional[bool] = None
    """Whether the vector store can be accessed by anyone with valid login credentials"""

    metadata: Optional[object] = None
    """Additional metadata associated with the vector store"""

    file_counts: Optional[FileCounts] = None
    """Counts of files in different states"""

    expires_after: Optional[ExpiresAfter] = None
    """Represents an expiration policy for a store."""

    status: Optional[Literal["expired", "in_progress", "completed"]] = None
    """Processing status of the vector store"""

    created_at: datetime
    """Timestamp when the vector store was created"""

    updated_at: datetime
    """Timestamp when the vector store was last updated"""

    last_active_at: Optional[datetime] = None
    """Timestamp when the vector store was last used"""

    usage_bytes: Optional[int] = None
    """Total storage usage in bytes"""

    expires_at: Optional[datetime] = None
    """Optional expiration timestamp for the vector store"""

    object: Optional[Literal["vector_store"]] = None
    """Type of the object"""
