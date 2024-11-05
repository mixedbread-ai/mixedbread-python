# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VectorStoreCreateResponse", "FileCounts"]


class FileCounts(BaseModel):
    canceled: Optional[int] = None

    failed: Optional[int] = None

    in_progress: Optional[int] = None

    successful: Optional[int] = None

    total: Optional[int] = None


class VectorStoreCreateResponse(BaseModel):
    id: str

    created_at: datetime
    """Timestamp of vector store creation"""

    description: Optional[str] = None

    expires_at: Optional[datetime] = None
    """Timestamp of vector store expiration"""

    name: str

    status: Literal["expired", "active"]
    """The status of the vector store"""

    file_counts: Optional[FileCounts] = None

    metadata: Optional[object] = None
    """Set of key-value pairs that can be attached to an object."""

    usage_bytes: Optional[int] = None
