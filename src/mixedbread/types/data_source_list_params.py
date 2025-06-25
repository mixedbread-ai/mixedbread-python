# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["DataSourceListParams"]


class DataSourceListParams(TypedDict, total=False):
    limit: int
    """Maximum number of items to return per page"""

    cursor: Optional[str]
    """Cursor for pagination (base64 encoded cursor)"""

    include_total: bool
    """Whether to include the total number of items"""
