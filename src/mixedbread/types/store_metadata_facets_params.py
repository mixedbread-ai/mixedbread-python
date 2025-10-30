# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import TypeAlias, TypedDict

from .._types import SequenceNotStr
from .shared_params.search_filter_condition import SearchFilterCondition

__all__ = ["StoreMetadataFacetsParams", "Filters", "FiltersUnionMember2"]


class StoreMetadataFacetsParams(TypedDict, total=False):
    filters: Optional[Filters]
    """Optional filter conditions"""

    facets: Optional[SequenceNotStr[str]]
    """Optional list of facets to return. Use dot for nested fields."""


FiltersUnionMember2: TypeAlias = Union["SearchFilter", SearchFilterCondition]

Filters: TypeAlias = Union["SearchFilter", SearchFilterCondition, Iterable[FiltersUnionMember2]]

from .shared_params.search_filter import SearchFilter
