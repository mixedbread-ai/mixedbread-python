# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .file_object import FileObject

__all__ = ["FileListResponse", "Pagination"]


class Pagination(BaseModel):
    after: Optional[int] = None

    limit: Optional[int] = None

    total: Optional[int] = None


class FileListResponse(BaseModel):
    data: List[FileObject]

    pagination: Pagination
