# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, Optional
from typing_extensions import TypeAlias, TypeAliasType

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel
from .search_filter_condition import SearchFilterCondition

__all__ = ["SearchFilter", "All", "Any", "NoneType"]

if TYPE_CHECKING or PYDANTIC_V2:
    All = TypeAliasType("All", Union["SearchFilter", SearchFilterCondition])
else:
    All: TypeAlias = Union["SearchFilter", SearchFilterCondition]

if TYPE_CHECKING or PYDANTIC_V2:
    Any = TypeAliasType("Any", Union["SearchFilter", SearchFilterCondition])
else:
    Any: TypeAlias = Union["SearchFilter", SearchFilterCondition]

if TYPE_CHECKING or PYDANTIC_V2:
    NoneType = TypeAliasType("NoneType", Union["SearchFilter", SearchFilterCondition])
else:
    NoneType: TypeAlias = Union["SearchFilter", SearchFilterCondition]


class SearchFilter(BaseModel):
    all: Optional[List[All]] = None
    """List of conditions or filters to be ANDed together"""

    any: Optional[List[Any]] = None
    """List of conditions or filters to be ORed together"""

    none: Optional[List[NoneType]] = None
    """List of conditions or filters to be NOTed"""
