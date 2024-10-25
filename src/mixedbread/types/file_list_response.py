# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["FileListResponse", "Data", "Pagination"]


class Data(BaseModel):
    mime_type: str

    name: str

    size: int

    user_id: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    updated_at: Optional[datetime] = None


class Pagination(BaseModel):
    total: int

    limit: Optional[int] = None

    offset: Optional[int] = None


class FileListResponse(BaseModel):
    data: List[Data]

    pagination: Pagination
