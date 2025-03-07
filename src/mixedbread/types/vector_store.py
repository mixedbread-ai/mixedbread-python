# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .file_counts import FileCounts
from .expires_after import ExpiresAfter

__all__ = ["VectorStore"]


class VectorStore(BaseModel):
    id: str
    """Unique identifier for the vector store"""

    name: str
    """Name of the vector store"""

    description: Optional[str] = None
    """Detailed description of the vector store's purpose and contents"""

    metadata: Optional[object] = None
    """Additional metadata associated with the vector store"""

    file_counts: Optional[FileCounts] = None
    """Counts of files in different states"""

    expires_after: Optional[ExpiresAfter] = None
    """Represents an expiration policy for a vector store."""

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
