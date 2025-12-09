# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["FileObject"]


class FileObject(BaseModel):
    """A model representing a file object in the system.

    This model contains metadata about files stored in the system, including
    identifiers, size information, and timestamps.
    """

    id: str
    """Unique identifier for the file"""

    filename: str
    """Name of the file including extension"""

    bytes: int
    """Size of the file in bytes"""

    mime_type: str
    """MIME type of the file"""

    version: int
    """Version of the file"""

    created_at: datetime
    """Timestamp when the file was created"""

    updated_at: datetime
    """Timestamp when the file was last updated"""
