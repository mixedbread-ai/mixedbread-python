# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .file_object import FileObject

__all__ = ["FileListResponse", "Pagination"]


class Pagination(BaseModel):
    limit: Optional[int] = None
    """Maximum number of items to return per page"""

    offset: Optional[int] = None
    """Cursor from which to start returning items"""

    total: Optional[int] = None
    """Total number of items available"""


class FileListResponse(BaseModel):
    data: List[FileObject]

    pagination: Pagination
    """Pagination model that includes total count of items."""

    object: Optional[Literal["list"]] = None
    """The object type of the response"""
