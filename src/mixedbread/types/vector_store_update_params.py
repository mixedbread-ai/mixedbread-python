# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["VectorStoreUpdateParams", "ExpiresAfter"]


class VectorStoreUpdateParams(TypedDict, total=False):
    name: Optional[str]
    """New name for the vector store"""

    description: Optional[str]
    """New description"""

    expires_after: Optional[ExpiresAfter]
    """Represents an expiration policy for a vector store."""

    metadata: object
    """Optional metadata key-value pairs"""


class ExpiresAfter(TypedDict, total=False):
    anchor: Literal["last_active_at"]
    """Anchor date for the expiration policy"""

    days: int
    """Number of days after which the vector store expires"""
