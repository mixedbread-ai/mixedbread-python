# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["APIKeyCreated"]


class APIKeyCreated(BaseModel):
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

    value: str
    """The value of the API key"""
