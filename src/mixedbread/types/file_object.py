# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["FileObject"]


class FileObject(BaseModel):
    mime_type: str

    name: str

    size: int

    user_id: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    updated_at: Optional[datetime] = None
