# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["VectorStoreListParams"]


class VectorStoreListParams(TypedDict, total=False):
    limit: int
    """Maximum number of items to return per page"""

    offset: int
    """Offset of the first item to return"""

    q: Optional[str]
    """Search query for fuzzy matching over name and description fields"""
