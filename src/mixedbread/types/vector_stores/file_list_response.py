# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .vector_store_file import VectorStoreFile

__all__ = ["FileListResponse", "Pagination"]


class Pagination(BaseModel):
    limit: Optional[int] = None
    """Maximum number of items to return per page"""

    offset: Optional[int] = None
    """Offset of the first item to return"""

    total: Optional[int] = None
    """Total number of items available"""


class FileListResponse(BaseModel):
    data: List[VectorStoreFile]
    """The list of vector store files"""

    pagination: Pagination
    """Pagination model that includes total count of items."""

    object: Optional[Literal["list"]] = None
    """The object type of the response"""
