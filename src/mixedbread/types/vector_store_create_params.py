# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

from .expires_after_param import ExpiresAfterParam

__all__ = ["VectorStoreCreateParams"]


class VectorStoreCreateParams(TypedDict, total=False):
    description: Optional[str]
    """Description of the vector store"""

    expires_after: Optional[ExpiresAfterParam]
    """Represents an expiration policy for a vector store."""

    file_ids: Optional[List[str]]
    """Optional list of file IDs"""

    metadata: object
    """Optional metadata key-value pairs"""

    name: Optional[str]
    """Name for the new vector store"""
