# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["FileObject"]


class FileObject(BaseModel):
    mime_type: str
    """MIME type of the file"""

    name: str
    """Name of the file"""

    size: int
    """Size of the file in bytes"""

    id: Optional[str] = None
    """Unique identifier for the record"""

    created_at: Optional[datetime] = None
    """Timestamp of record creation"""

    updated_at: Optional[datetime] = None
    """Timestamp of last record update"""
