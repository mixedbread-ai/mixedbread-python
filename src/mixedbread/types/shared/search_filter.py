# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel
from .search_filter_condition import SearchFilterCondition

__all__ = ["SearchFilter", "All", "Any", "NoneType"]

All: TypeAlias = Union["SearchFilter", SearchFilterCondition]

Any: TypeAlias = Union["SearchFilter", SearchFilterCondition]

NoneType: TypeAlias = Union["SearchFilter", SearchFilterCondition]


class SearchFilter(BaseModel):
    all: Optional[List[All]] = None
    """List of conditions or filters to be ANDed together"""

    any: Optional[List[Any]] = None
    """List of conditions or filters to be ORed together"""

    none: Optional[List[NoneType]] = None
    """List of conditions or filters to be NOTed"""


if PYDANTIC_V2:
    SearchFilter.model_rebuild()
else:
    SearchFilter.update_forward_refs()  # type: ignore
