# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .file_object import FileObject

__all__ = ["FileListResponse", "Pagination"]


class Pagination(BaseModel):
    next_cursor: Optional[str] = None
    """Cursor for the next page, null if no more pages"""

    prev_cursor: Optional[str] = None
    """Cursor for the previous page, null if no previous pages"""

    has_more: bool
    """Whether there are more items available"""

    has_prev: bool
    """Whether there are previous items available"""

    total: Optional[int] = None
    """Total number of items available"""


class FileListResponse(BaseModel):
    pagination: Pagination
    """Response model for cursor-based pagination."""

    object: Optional[Literal["list"]] = None
    """The object type of the response"""

    data: List[FileObject]
    """The list of files"""
