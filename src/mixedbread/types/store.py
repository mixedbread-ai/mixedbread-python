# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .expires_after import ExpiresAfter

__all__ = ["Store", "Config", "ConfigContextualization", "ConfigContextualizationContextualizationConfig", "FileCounts"]


class ConfigContextualizationContextualizationConfig(BaseModel):
    with_metadata: Union[bool, List[str], None] = None
    """Include all metadata or specific fields in the contextualization.

    Supports dot notation for nested fields (e.g., 'author.name'). When True, all
    metadata is included (flattened). When a list, only specified fields are
    included.
    """


ConfigContextualization: TypeAlias = Union[bool, ConfigContextualizationContextualizationConfig, None]


class Config(BaseModel):
    contextualization: Optional[ConfigContextualization] = None
    """Contextualize files with metadata"""


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


class Store(BaseModel):
    id: str
    """Unique identifier for the store"""

    name: str
    """Name of the store"""

    description: Optional[str] = None
    """Detailed description of the store's purpose and contents"""

    is_public: Optional[bool] = None
    """Whether the store can be accessed by anyone with valid login credentials"""

    metadata: Optional[object] = None
    """Additional metadata associated with the store"""

    config: Optional[Config] = None
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

    expires_at: Optional[datetime] = None
    """Optional expiration timestamp for the store"""

    object: Optional[Literal["store"]] = None
    """Type of the object"""
