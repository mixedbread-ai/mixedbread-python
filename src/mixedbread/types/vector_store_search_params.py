# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "VectorStoreSearchParams",
    "Filter",
    "FilterFilter",
    "FilterFilterAndUnionMember0",
    "FilterFilterAndUnionMember0Condition",
    "FilterFilterNotUnionMember0",
    "FilterFilterNotUnionMember0Condition",
    "FilterFilterOrUnionMember0",
    "FilterFilterOrUnionMember0Condition",
    "FilterUnionMember1",
    "FilterUnionMember1Condition",
    "FilterUnionMember1Filter",
    "FilterUnionMember1FilterAndUnionMember0",
    "FilterUnionMember1FilterAndUnionMember0Condition",
    "FilterUnionMember1FilterNotUnionMember0",
    "FilterUnionMember1FilterNotUnionMember0Condition",
    "FilterUnionMember1FilterOrUnionMember0",
    "FilterUnionMember1FilterOrUnionMember0Condition",
    "Options",
]


class VectorStoreSearchParams(TypedDict, total=False):
    query: Required[str]

    vector_store_ids: Required[List[str]]

    after: int

    filter: Optional[Filter]
    """List of conditions or filters to be ANDed together"""

    limit: int

    options: Optional[Options]


class FilterFilterAndUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterFilterAndUnionMember0: TypeAlias = Union[FilterFilterAndUnionMember0Condition, object]


class FilterFilterNotUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterFilterNotUnionMember0: TypeAlias = Union[FilterFilterNotUnionMember0Condition, object]


class FilterFilterOrUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterFilterOrUnionMember0: TypeAlias = Union[FilterFilterOrUnionMember0Condition, object]


class FilterFilter(TypedDict, total=False):
    and_: Union[Iterable[FilterFilterAndUnionMember0], object]
    """List of conditions or filters to be ANDed together"""

    not_: Union[Iterable[FilterFilterNotUnionMember0], object]
    """List of conditions or filters to be NOTed"""

    or_: Union[Iterable[FilterFilterOrUnionMember0], object]
    """List of conditions or filters to be ORed together"""


class FilterUnionMember1Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


class FilterUnionMember1FilterAndUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterUnionMember1FilterAndUnionMember0: TypeAlias = Union[FilterUnionMember1FilterAndUnionMember0Condition, object]


class FilterUnionMember1FilterNotUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterUnionMember1FilterNotUnionMember0: TypeAlias = Union[FilterUnionMember1FilterNotUnionMember0Condition, object]


class FilterUnionMember1FilterOrUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterUnionMember1FilterOrUnionMember0: TypeAlias = Union[FilterUnionMember1FilterOrUnionMember0Condition, object]


class FilterUnionMember1Filter(TypedDict, total=False):
    and_: Union[Iterable[FilterUnionMember1FilterAndUnionMember0], object]
    """List of conditions or filters to be ANDed together"""

    not_: Union[Iterable[FilterUnionMember1FilterNotUnionMember0], object]
    """List of conditions or filters to be NOTed"""

    or_: Union[Iterable[FilterUnionMember1FilterOrUnionMember0], object]
    """List of conditions or filters to be ORed together"""


FilterUnionMember1: TypeAlias = Union[FilterUnionMember1Condition, FilterUnionMember1Filter]

Filter: TypeAlias = Union[FilterFilter, Iterable[FilterUnionMember1]]


class Options(TypedDict, total=False):
    min_score: float

    return_chunks: bool

    return_metadata: bool
