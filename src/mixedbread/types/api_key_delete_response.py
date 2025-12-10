# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["APIKeyDeleteResponse"]


class APIKeyDeleteResponse(BaseModel):
    """Response model for deleting an API key."""

    id: str
    """The ID of the deleted API key"""

    deleted: bool
    """Whether the API key was deleted"""

    object: Optional[Literal["api_key"]] = None
    """The type of the object deleted"""
