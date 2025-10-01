# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ExpiresAfter"]


class ExpiresAfter(BaseModel):
    anchor: Optional[Literal["last_active_at"]] = None
    """Anchor date for the expiration policy"""

    days: Optional[int] = None
    """Number of days after which the store expires"""
