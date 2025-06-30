# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["DataSourceListParams"]


class DataSourceListParams(TypedDict, total=False):
    limit: int
    """Maximum number of items to return per page (1-100)"""

    after: Optional[str]
    """Cursor for forward pagination - get items after this position.

    Use last_cursor from previous response.
    """

    before: Optional[str]
    """Cursor for backward pagination - get items before this position.

    Use first_cursor from previous response.
    """

    include_total: bool
    """Whether to include total count in response (expensive operation)"""
