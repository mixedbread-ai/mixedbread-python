# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["VectorStoreCreateParams", "ExpiresAfter"]


class VectorStoreCreateParams(TypedDict, total=False):
    description: Optional[str]
    """Description of the vector store"""

    expires_after: Optional[ExpiresAfter]
    """Represents an expiration policy for a vector store."""

    file_ids: Optional[List[str]]
    """Optional list of file IDs"""

    metadata: Optional[object]
    """Optional metadata key-value pairs"""

    name: Optional[str]
    """Name for the new vector store"""


class ExpiresAfter(TypedDict, total=False):
    anchor: Literal["last_used_at"]
    """Anchor date for the expiration policy"""

    days: int
    """Number of days after which the vector store expires"""
