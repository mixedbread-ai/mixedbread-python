# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .file_object import FileObject

__all__ = ["FileListResponse", "Pagination"]


class Pagination(BaseModel):
    total: int

    after: Optional[str] = None
    """The cursor after which to paginate"""

    limit: Optional[int] = None
    """The maximum number of items to return"""


class FileListResponse(BaseModel):
    data: List[FileObject]

    pagination: Pagination
