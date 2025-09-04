# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Iterable, Optional
from typing_extensions import TypeAlias, TypedDict, TypeAliasType

from ..._compat import PYDANTIC_V1
from .search_filter_condition import SearchFilterCondition

__all__ = ["SearchFilter", "All", "Any", "NoneType"]

if TYPE_CHECKING or not PYDANTIC_V1:
    All = TypeAliasType("All", Union["SearchFilter", SearchFilterCondition])
else:
    All: TypeAlias = Union["SearchFilter", SearchFilterCondition]

if TYPE_CHECKING or not PYDANTIC_V1:
    Any = TypeAliasType("Any", Union["SearchFilter", SearchFilterCondition])
else:
    Any: TypeAlias = Union["SearchFilter", SearchFilterCondition]

if TYPE_CHECKING or not PYDANTIC_V1:
    NoneType = TypeAliasType("NoneType", Union["SearchFilter", SearchFilterCondition])
else:
    NoneType: TypeAlias = Union["SearchFilter", SearchFilterCondition]


class SearchFilter(TypedDict, total=False):
    all: Optional[Iterable[All]]
    """List of conditions or filters to be ANDed together"""

    any: Optional[Iterable[Any]]
    """List of conditions or filters to be ORed together"""

    none: Optional[Iterable[NoneType]]
    """List of conditions or filters to be NOTed"""
