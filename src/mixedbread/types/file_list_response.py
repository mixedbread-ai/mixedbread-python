# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FileListResponse", "Data", "Pagination"]


class Data(BaseModel):
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


class Pagination(BaseModel):
    limit: Optional[int] = None
    """Maximum number of items to return per page"""

    offset: Optional[int] = None
    """Offset of the first item to return"""

    total: Optional[int] = None
    """Total number of items available"""


class FileListResponse(BaseModel):
    data: List[Data]
    """The list of files"""

    pagination: Pagination
    """Pagination model that includes total count of items."""

    object: Optional[Literal["list"]] = None
    """The object type of the response"""
