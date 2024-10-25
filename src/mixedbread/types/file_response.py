# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["FileResponse", "Data", "DataStoredFile", "DataErrorAsValue"]


class DataStoredFile(BaseModel):
    mime_type: str

    name: str

    size: int

    user_id: str

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    updated_at: Optional[datetime] = None


class DataErrorAsValue(BaseModel):
    detail: Optional[object] = None
    """Additional error details"""

    detail_str: Optional[str] = None
    """String representation of additional error details"""

    message: Optional[str] = None
    """The error message"""


Data: TypeAlias = Union[DataStoredFile, DataErrorAsValue]


class FileResponse(BaseModel):
    data: List[Data]
