# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "VectorStoreSearchParams",
    "Filters",
    "FiltersSearchFilter",
    "FiltersSearchFilterAll",
    "FiltersSearchFilterAllSearchFilterCondition",
    "FiltersSearchFilterAny",
    "FiltersSearchFilterAnySearchFilterCondition",
    "FiltersSearchFilterNone",
    "FiltersSearchFilterNoneSearchFilterCondition",
    "FiltersSearchFilterCondition",
    "FiltersUnionMember2",
    "FiltersUnionMember2SearchFilter",
    "FiltersUnionMember2SearchFilterAll",
    "FiltersUnionMember2SearchFilterAllSearchFilterCondition",
    "FiltersUnionMember2SearchFilterAny",
    "FiltersUnionMember2SearchFilterAnySearchFilterCondition",
    "FiltersUnionMember2SearchFilterNone",
    "FiltersUnionMember2SearchFilterNoneSearchFilterCondition",
    "FiltersUnionMember2SearchFilterCondition",
    "Pagination",
    "SearchOptions",
]


class VectorStoreSearchParams(TypedDict, total=False):
    query: Required[str]
    """Search query text"""

    vector_store_ids: Required[List[str]]
    """IDs of vector stores to search"""

    filters: Optional[Filters]
    """Filter or condition"""

    pagination: Pagination
    """Pagination options"""

    search_options: SearchOptions
    """Search configuration options"""


class FiltersSearchFilterAllSearchFilterCondition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FiltersSearchFilterAll: TypeAlias = Union[FiltersSearchFilterAllSearchFilterCondition, object]


class FiltersSearchFilterAnySearchFilterCondition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FiltersSearchFilterAny: TypeAlias = Union[FiltersSearchFilterAnySearchFilterCondition, object]


class FiltersSearchFilterNoneSearchFilterCondition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FiltersSearchFilterNone: TypeAlias = Union[FiltersSearchFilterNoneSearchFilterCondition, object]


class FiltersSearchFilter(TypedDict, total=False):
    all: Optional[Iterable[FiltersSearchFilterAll]]
    """List of conditions or filters to be ANDed together"""

    any: Optional[Iterable[FiltersSearchFilterAny]]
    """List of conditions or filters to be ORed together"""

    none: Optional[Iterable[FiltersSearchFilterNone]]
    """List of conditions or filters to be NOTed"""


class FiltersSearchFilterCondition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


class FiltersUnionMember2SearchFilterAllSearchFilterCondition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FiltersUnionMember2SearchFilterAll: TypeAlias = Union[FiltersUnionMember2SearchFilterAllSearchFilterCondition, object]


class FiltersUnionMember2SearchFilterAnySearchFilterCondition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FiltersUnionMember2SearchFilterAny: TypeAlias = Union[FiltersUnionMember2SearchFilterAnySearchFilterCondition, object]


class FiltersUnionMember2SearchFilterNoneSearchFilterCondition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FiltersUnionMember2SearchFilterNone: TypeAlias = Union[FiltersUnionMember2SearchFilterNoneSearchFilterCondition, object]


class FiltersUnionMember2SearchFilter(TypedDict, total=False):
    all: Optional[Iterable[FiltersUnionMember2SearchFilterAll]]
    """List of conditions or filters to be ANDed together"""

    any: Optional[Iterable[FiltersUnionMember2SearchFilterAny]]
    """List of conditions or filters to be ORed together"""

    none: Optional[Iterable[FiltersUnionMember2SearchFilterNone]]
    """List of conditions or filters to be NOTed"""


class FiltersUnionMember2SearchFilterCondition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FiltersUnionMember2: TypeAlias = Union[FiltersUnionMember2SearchFilter, FiltersUnionMember2SearchFilterCondition]

Filters: TypeAlias = Union[FiltersSearchFilter, FiltersSearchFilterCondition, Iterable[FiltersUnionMember2]]


class Pagination(TypedDict, total=False):
    limit: int
    """Maximum number of items to return per page"""

    offset: int
    """Cursor from which to start returning items"""


class SearchOptions(TypedDict, total=False):
    return_chunks: bool
    """Whether to return matching text chunks"""

    return_metadata: bool
    """Whether to return file metadata"""

    rewrite_query: bool
    """Whether to rewrite the query"""

    score_threshold: float
    """Minimum similarity score threshold"""
