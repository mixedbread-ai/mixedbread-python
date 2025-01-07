# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .expires_after_param import ExpiresAfterParam

__all__ = ["VectorStoreUpdateParams"]


class VectorStoreUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """New description"""

    expires_after: Optional[ExpiresAfterParam]
    """Represents an expiration policy for a vector store."""

    metadata: object
    """Optional metadata key-value pairs"""

    name: Optional[str]
    """New name for the vector store"""
