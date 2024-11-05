# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["FileListResponse", "Data", "Pagination"]


class Data(BaseModel):
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


class Pagination(BaseModel):
    after: Optional[int] = None

    limit: Optional[int] = None

    total: Optional[int] = None


class FileListResponse(BaseModel):
    data: List[Data]

    pagination: Pagination
