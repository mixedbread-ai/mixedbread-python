# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import TypeAlias, TypedDict

from .search_filter_condition import SearchFilterCondition

__all__ = ["SearchFilter", "All", "Any", "NoneType"]

All: TypeAlias = Union["SearchFilter", SearchFilterCondition]

Any: TypeAlias = Union["SearchFilter", SearchFilterCondition]

NoneType: TypeAlias = Union["SearchFilter", SearchFilterCondition]


class SearchFilter(TypedDict, total=False):
    all: Optional[Iterable[All]]
    """List of conditions or filters to be ANDed together"""

    any: Optional[Iterable[Any]]
    """List of conditions or filters to be ORed together"""

    none: Optional[Iterable[NoneType]]
    """List of conditions or filters to be NOTed"""
