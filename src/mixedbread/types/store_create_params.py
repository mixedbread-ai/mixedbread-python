# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr
from .expires_after_param import ExpiresAfterParam

__all__ = ["StoreCreateParams"]


class StoreCreateParams(TypedDict, total=False):
    name: Optional[str]
    """Name for the new store"""

    description: Optional[str]
    """Description of the store"""

    is_public: bool
    """Whether the store can be accessed by anyone with valid login credentials"""

    expires_after: Optional[ExpiresAfterParam]
    """Represents an expiration policy for a store."""

    metadata: object
    """Optional metadata key-value pairs"""

    file_ids: Optional[SequenceNotStr[str]]
    """Optional list of file IDs"""
