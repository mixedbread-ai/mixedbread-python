# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FileDeleted"]


class FileDeleted(BaseModel):
    id: str
    """The ID of the deleted file"""

    deleted: Optional[bool] = None
    """Whether the file was deleted"""

    object: Optional[Literal["file"]] = None
    """The type of the deleted object"""
