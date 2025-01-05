# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["FileListResponse"]


class FileListResponse(BaseModel):
    id: str
    """Unique identifier for the file"""

    bytes: int
    """Size of the file in bytes"""

    created_at: datetime
    """Timestamp when the file was created"""

    filename: str
    """Name of the file including extension"""

    mime_type: str
    """MIME type of the file"""

    updated_at: datetime
    """Timestamp when the file was last updated"""

    version: int
    """Version of the file"""
