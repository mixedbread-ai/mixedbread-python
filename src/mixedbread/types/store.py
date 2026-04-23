# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .file_counts import FileCounts
from .store_config import StoreConfig
from .expires_after import ExpiresAfter

__all__ = ["Store"]


class Store(BaseModel):
    """Model representing a store with its metadata and timestamps."""

    id: str
    """Unique identifier for the store"""

    name: str
    """Name of the store"""

    description: Optional[str] = None
    """Detailed description of the store's purpose and contents"""

    is_public: Optional[bool] = None
    """Whether the store can be accessed by anyone with valid login credentials"""

    license: Optional[str] = None
    """License for public stores"""

    metadata: Optional[object] = None
    """Additional metadata associated with the store"""

    config: Optional[StoreConfig] = None
    """Configuration for a store."""

    file_counts: Optional[FileCounts] = None
    """Counts of files in different states"""

    expires_after: Optional[ExpiresAfter] = None
    """Represents an expiration policy for a store."""

    status: Optional[Literal["expired", "in_progress", "completed"]] = None
    """Processing status of the store"""

    created_at: datetime
    """Timestamp when the store was created"""

    updated_at: datetime
    """Timestamp when the store was last updated"""

    last_active_at: Optional[datetime] = None
    """Timestamp when the store was last used"""

    usage_bytes: Optional[int] = None
    """Total storage usage in bytes"""

    usage_tokens: Optional[int] = None
    """Total storage usage in tokens"""

    expires_at: Optional[datetime] = None
    """Optional expiration timestamp for the store"""

    object: Optional[Literal["store"]] = None
    """Type of the object"""
