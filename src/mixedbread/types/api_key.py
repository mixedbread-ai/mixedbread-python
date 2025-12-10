# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["APIKey", "Scope"]


class Scope(BaseModel):
    method: Literal["read", "write", "delete", "list", "create"]

    resource_type: Optional[Literal["store"]] = None

    resource_id: Optional[str] = None


class APIKey(BaseModel):
    """Response model for an API key."""

    id: str
    """The ID of the API key"""

    name: str
    """The name of the API key"""

    redacted_value: str
    """The redacted value of the API key"""

    expires_at: Optional[datetime] = None
    """The expiration datetime of the API key"""

    created_at: datetime
    """The creation datetime of the API key"""

    updated_at: datetime
    """The last update datetime of the API key"""

    last_active_at: Optional[datetime] = None
    """The last active datetime of the API key"""

    object: Optional[Literal["api_key"]] = None
    """The type of the object"""

    scope: Optional[List[Scope]] = None
    """The scope of the API key"""
