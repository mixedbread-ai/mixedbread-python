# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PaginationWithTotal"]


class PaginationWithTotal(BaseModel):
    """Pagination model that includes total count of items."""

    limit: Optional[int] = None
    """Maximum number of items to return per page"""

    offset: Optional[int] = None
    """Offset of the first item to return"""

    total: Optional[int] = None
    """Total number of items available"""
