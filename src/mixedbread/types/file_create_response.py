# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["FileCreateResponse"]


class FileCreateResponse(BaseModel):
    id: str
    """Unique identifier for the record"""

    created_at: datetime
    """Timestamp of record creation"""

    mime_type: str
    """MIME type of the file"""

    name: str
    """Name of the file"""

    size: int
    """Size of the file in bytes"""

    updated_at: datetime
    """Timestamp of last record update"""

    version: int
    """Version of the file"""
