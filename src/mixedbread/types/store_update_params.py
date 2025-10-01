# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .expires_after_param import ExpiresAfterParam

__all__ = ["StoreUpdateParams"]


class StoreUpdateParams(TypedDict, total=False):
    name: Optional[str]
    """New name for the store"""

    description: Optional[str]
    """New description"""

    is_public: Optional[bool]
    """Whether the store can be accessed by anyone with valid login credentials"""

    expires_after: Optional[ExpiresAfterParam]
    """Represents an expiration policy for a store."""

    metadata: object
    """Optional metadata key-value pairs"""
