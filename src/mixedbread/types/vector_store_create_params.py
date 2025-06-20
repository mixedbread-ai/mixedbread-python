# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

from .expires_after_param import ExpiresAfterParam

__all__ = ["VectorStoreCreateParams"]


class VectorStoreCreateParams(TypedDict, total=False):
    name: Optional[str]
    """Name for the new vector store"""

    description: Optional[str]
    """Description of the vector store"""

    is_public: bool
    """Whether the vector store can be accessed by anyone with valid login credentials"""

    expires_after: Optional[ExpiresAfterParam]
    """Represents an expiration policy for a vector store."""

    metadata: object
    """Optional metadata key-value pairs"""

    file_ids: Optional[List[str]]
    """Optional list of file IDs"""
