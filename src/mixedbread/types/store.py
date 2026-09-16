# File generated from our OpenAPI spec by sdkgen. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .file_counts import FileCounts
from .store_config import StoreConfig
from .expires_after import ExpiresAfter

__all__ = ["Store", "CopyState"]


class CopyState(BaseModel):
    """
    Progress of a store copy, present on both the source and the target while it
    runs.
    """

    role: Literal["source", "target"]
    """Whether this store is copied from or into"""

    status: Literal["in_progress", "failed"]
    """Progress of the copy"""

    peer_store_id: str
    """The other store of the copy"""

    started_at: datetime
    """When the copy was requested"""

    error: Optional[str] = None
    """Why the copy failed, when it did"""


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

    tags: Optional[List[str]] = None
    """Tags for organizing stores"""

    config: Optional[StoreConfig] = None
    """Configuration for a store."""

    bucket_id: Optional[str] = None
    """Customer bucket backing this store's storage; null = platform default"""

    file_counts: Optional[FileCounts] = None
    """Counts of files in different states"""

    expires_after: Optional[ExpiresAfter] = None
    """Represents an expiration policy for a store."""

    status: Optional[Literal["expired", "in_progress", "completed", "failed"]] = None
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

    copy_state: Optional[CopyState] = None
    """
    Progress of a store copy, present on both the source and the target while it
    runs.
    """

    object: Optional[Literal["store"]] = None
    """Type of the object"""
