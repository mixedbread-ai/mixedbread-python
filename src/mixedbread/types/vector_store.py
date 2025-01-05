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
