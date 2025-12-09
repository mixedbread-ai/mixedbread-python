# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["StoreDeleteResponse"]


class StoreDeleteResponse(BaseModel):
    """Response model for store deletion."""

    id: str
    """ID of the deleted store"""

    deleted: bool
    """Whether the deletion was successful"""

    object: Optional[Literal["store"]] = None
    """Type of the deleted object"""
