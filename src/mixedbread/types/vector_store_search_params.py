# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "VectorStoreSearchParams",
    "Filters",
    "FiltersFilter",
    "FiltersFilterAll",
    "FiltersFilterAllCondition",
    "FiltersFilterAny",
    "FiltersFilterAnyCondition",
    "FiltersFilterNone",
    "FiltersFilterNoneCondition",
    "FiltersCondition",
    "FiltersUnionMember2",
    "FiltersUnionMember2Filter",
    "FiltersUnionMember2FilterAll",
    "FiltersUnionMember2FilterAllCondition",
    "FiltersUnionMember2FilterAny",
    "FiltersUnionMember2FilterAnyCondition",
    "FiltersUnionMember2FilterNone",
    "FiltersUnionMember2FilterNoneCondition",
    "FiltersUnionMember2Condition",
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


class FiltersFilterAllCondition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FiltersFilterAll: TypeAlias = Union[FiltersFilterAllCondition, object]


class FiltersFilterAnyCondition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FiltersFilterAny: TypeAlias = Union[FiltersFilterAnyCondition, object]


class FiltersFilterNoneCondition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FiltersFilterNone: TypeAlias = Union[FiltersFilterNoneCondition, object]


class FiltersFilter(TypedDict, total=False):
    all: Optional[Iterable[FiltersFilterAll]]
    """List of conditions or filters to be ANDed together"""

    any: Optional[Iterable[FiltersFilterAny]]
    """List of conditions or filters to be ORed together"""

    none: Optional[Iterable[FiltersFilterNone]]
    """List of conditions or filters to be NOTed"""


class FiltersCondition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


class FiltersUnionMember2FilterAllCondition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FiltersUnionMember2FilterAll: TypeAlias = Union[FiltersUnionMember2FilterAllCondition, object]


class FiltersUnionMember2FilterAnyCondition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FiltersUnionMember2FilterAny: TypeAlias = Union[FiltersUnionMember2FilterAnyCondition, object]


class FiltersUnionMember2FilterNoneCondition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FiltersUnionMember2FilterNone: TypeAlias = Union[FiltersUnionMember2FilterNoneCondition, object]


class FiltersUnionMember2Filter(TypedDict, total=False):
    all: Optional[Iterable[FiltersUnionMember2FilterAll]]
    """List of conditions or filters to be ANDed together"""

    any: Optional[Iterable[FiltersUnionMember2FilterAny]]
    """List of conditions or filters to be ORed together"""

    none: Optional[Iterable[FiltersUnionMember2FilterNone]]
    """List of conditions or filters to be NOTed"""


class FiltersUnionMember2Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FiltersUnionMember2: TypeAlias = Union[FiltersUnionMember2Filter, FiltersUnionMember2Condition]

Filters: TypeAlias = Union[FiltersFilter, FiltersCondition, Iterable[FiltersUnionMember2]]


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
