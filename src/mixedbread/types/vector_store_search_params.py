# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "VectorStoreSearchParams",
    "Filter",
    "FilterFilter",
    "FilterFilterAnd",
    "FilterFilterAndFilter",
    "FilterFilterAndFilterNotUnionMember0",
    "FilterFilterAndFilterNotUnionMember0Condition",
    "FilterFilterAndFilterNotUnionMember0Filter",
    "FilterFilterAndFilterNotUnionMember0FilterOrUnionMember0",
    "FilterFilterAndFilterNotUnionMember0FilterOrUnionMember0Condition",
    "FilterFilterAndFilterOrUnionMember0",
    "FilterFilterAndFilterOrUnionMember0Condition",
    "FilterFilterAndFilterOrUnionMember0Filter",
    "FilterFilterAndFilterOrUnionMember0FilterNotUnionMember0",
    "FilterFilterAndFilterOrUnionMember0FilterNotUnionMember0Condition",
    "FilterFilterAndUnionMember1",
    "FilterFilterAndUnionMember1Condition",
    "FilterFilterAndUnionMember1Filter",
    "FilterFilterAndUnionMember1FilterNot",
    "FilterFilterAndUnionMember1FilterNotFilter",
    "FilterFilterAndUnionMember1FilterNotFilterOrUnionMember0",
    "FilterFilterAndUnionMember1FilterNotFilterOrUnionMember0Condition",
    "FilterFilterAndUnionMember1FilterNotUnionMember1",
    "FilterFilterAndUnionMember1FilterNotUnionMember1Condition",
    "FilterFilterAndUnionMember1FilterOr",
    "FilterFilterAndUnionMember1FilterOrFilter",
    "FilterFilterAndUnionMember1FilterOrFilterNotUnionMember0",
    "FilterFilterAndUnionMember1FilterOrFilterNotUnionMember0Condition",
    "FilterFilterAndUnionMember1FilterOrUnionMember1",
    "FilterFilterAndUnionMember1FilterOrUnionMember1Condition",
    "FilterFilterNot",
    "FilterFilterNotFilter",
    "FilterFilterNotFilterAndUnionMember0",
    "FilterFilterNotFilterAndUnionMember0Condition",
    "FilterFilterNotFilterAndUnionMember0Filter",
    "FilterFilterNotFilterAndUnionMember0FilterOrUnionMember0",
    "FilterFilterNotFilterAndUnionMember0FilterOrUnionMember0Condition",
    "FilterFilterNotFilterOrUnionMember0",
    "FilterFilterNotFilterOrUnionMember0Condition",
    "FilterFilterNotFilterOrUnionMember0Filter",
    "FilterFilterNotFilterOrUnionMember0FilterAndUnionMember0",
    "FilterFilterNotFilterOrUnionMember0FilterAndUnionMember0Condition",
    "FilterFilterNotUnionMember1",
    "FilterFilterNotUnionMember1Condition",
    "FilterFilterNotUnionMember1Filter",
    "FilterFilterNotUnionMember1FilterAnd",
    "FilterFilterNotUnionMember1FilterAndFilter",
    "FilterFilterNotUnionMember1FilterAndFilterOrUnionMember0",
    "FilterFilterNotUnionMember1FilterAndFilterOrUnionMember0Condition",
    "FilterFilterNotUnionMember1FilterAndUnionMember1",
    "FilterFilterNotUnionMember1FilterAndUnionMember1Condition",
    "FilterFilterNotUnionMember1FilterOr",
    "FilterFilterNotUnionMember1FilterOrFilter",
    "FilterFilterNotUnionMember1FilterOrFilterAndUnionMember0",
    "FilterFilterNotUnionMember1FilterOrFilterAndUnionMember0Condition",
    "FilterFilterNotUnionMember1FilterOrUnionMember1",
    "FilterFilterNotUnionMember1FilterOrUnionMember1Condition",
    "FilterFilterOr",
    "FilterFilterOrFilter",
    "FilterFilterOrFilterAndUnionMember0",
    "FilterFilterOrFilterAndUnionMember0Condition",
    "FilterFilterOrFilterAndUnionMember0Filter",
    "FilterFilterOrFilterAndUnionMember0FilterNotUnionMember0",
    "FilterFilterOrFilterAndUnionMember0FilterNotUnionMember0Condition",
    "FilterFilterOrFilterNotUnionMember0",
    "FilterFilterOrFilterNotUnionMember0Condition",
    "FilterFilterOrFilterNotUnionMember0Filter",
    "FilterFilterOrFilterNotUnionMember0FilterAndUnionMember0",
    "FilterFilterOrFilterNotUnionMember0FilterAndUnionMember0Condition",
    "FilterFilterOrUnionMember1",
    "FilterFilterOrUnionMember1Condition",
    "FilterFilterOrUnionMember1Filter",
    "FilterFilterOrUnionMember1FilterAnd",
    "FilterFilterOrUnionMember1FilterAndFilter",
    "FilterFilterOrUnionMember1FilterAndFilterNotUnionMember0",
    "FilterFilterOrUnionMember1FilterAndFilterNotUnionMember0Condition",
    "FilterFilterOrUnionMember1FilterAndUnionMember1",
    "FilterFilterOrUnionMember1FilterAndUnionMember1Condition",
    "FilterFilterOrUnionMember1FilterNot",
    "FilterFilterOrUnionMember1FilterNotFilter",
    "FilterFilterOrUnionMember1FilterNotFilterAndUnionMember0",
    "FilterFilterOrUnionMember1FilterNotFilterAndUnionMember0Condition",
    "FilterFilterOrUnionMember1FilterNotUnionMember1",
    "FilterFilterOrUnionMember1FilterNotUnionMember1Condition",
    "FilterUnionMember1",
    "FilterUnionMember1Condition",
    "FilterUnionMember1Filter",
    "FilterUnionMember1FilterAnd",
    "FilterUnionMember1FilterAndFilter",
    "FilterUnionMember1FilterAndFilterNotUnionMember0",
    "FilterUnionMember1FilterAndFilterNotUnionMember0Condition",
    "FilterUnionMember1FilterAndFilterNotUnionMember0Filter",
    "FilterUnionMember1FilterAndFilterNotUnionMember0FilterOrUnionMember0",
    "FilterUnionMember1FilterAndFilterNotUnionMember0FilterOrUnionMember0Condition",
    "FilterUnionMember1FilterAndFilterOrUnionMember0",
    "FilterUnionMember1FilterAndFilterOrUnionMember0Condition",
    "FilterUnionMember1FilterAndFilterOrUnionMember0Filter",
    "FilterUnionMember1FilterAndFilterOrUnionMember0FilterNotUnionMember0",
    "FilterUnionMember1FilterAndFilterOrUnionMember0FilterNotUnionMember0Condition",
    "FilterUnionMember1FilterAndUnionMember1",
    "FilterUnionMember1FilterAndUnionMember1Condition",
    "FilterUnionMember1FilterAndUnionMember1Filter",
    "FilterUnionMember1FilterAndUnionMember1FilterNot",
    "FilterUnionMember1FilterAndUnionMember1FilterNotFilter",
    "FilterUnionMember1FilterAndUnionMember1FilterNotFilterOrUnionMember0",
    "FilterUnionMember1FilterAndUnionMember1FilterNotFilterOrUnionMember0Condition",
    "FilterUnionMember1FilterAndUnionMember1FilterNotUnionMember1",
    "FilterUnionMember1FilterAndUnionMember1FilterNotUnionMember1Condition",
    "FilterUnionMember1FilterAndUnionMember1FilterOr",
    "FilterUnionMember1FilterAndUnionMember1FilterOrFilter",
    "FilterUnionMember1FilterAndUnionMember1FilterOrFilterNotUnionMember0",
    "FilterUnionMember1FilterAndUnionMember1FilterOrFilterNotUnionMember0Condition",
    "FilterUnionMember1FilterAndUnionMember1FilterOrUnionMember1",
    "FilterUnionMember1FilterAndUnionMember1FilterOrUnionMember1Condition",
    "FilterUnionMember1FilterNot",
    "FilterUnionMember1FilterNotFilter",
    "FilterUnionMember1FilterNotFilterAndUnionMember0",
    "FilterUnionMember1FilterNotFilterAndUnionMember0Condition",
    "FilterUnionMember1FilterNotFilterAndUnionMember0Filter",
    "FilterUnionMember1FilterNotFilterAndUnionMember0FilterOrUnionMember0",
    "FilterUnionMember1FilterNotFilterAndUnionMember0FilterOrUnionMember0Condition",
    "FilterUnionMember1FilterNotFilterOrUnionMember0",
    "FilterUnionMember1FilterNotFilterOrUnionMember0Condition",
    "FilterUnionMember1FilterNotFilterOrUnionMember0Filter",
    "FilterUnionMember1FilterNotFilterOrUnionMember0FilterAndUnionMember0",
    "FilterUnionMember1FilterNotFilterOrUnionMember0FilterAndUnionMember0Condition",
    "FilterUnionMember1FilterNotUnionMember1",
    "FilterUnionMember1FilterNotUnionMember1Condition",
    "FilterUnionMember1FilterNotUnionMember1Filter",
    "FilterUnionMember1FilterNotUnionMember1FilterAnd",
    "FilterUnionMember1FilterNotUnionMember1FilterAndFilter",
    "FilterUnionMember1FilterNotUnionMember1FilterAndFilterOrUnionMember0",
    "FilterUnionMember1FilterNotUnionMember1FilterAndFilterOrUnionMember0Condition",
    "FilterUnionMember1FilterNotUnionMember1FilterAndUnionMember1",
    "FilterUnionMember1FilterNotUnionMember1FilterAndUnionMember1Condition",
    "FilterUnionMember1FilterNotUnionMember1FilterOr",
    "FilterUnionMember1FilterNotUnionMember1FilterOrFilter",
    "FilterUnionMember1FilterNotUnionMember1FilterOrFilterAndUnionMember0",
    "FilterUnionMember1FilterNotUnionMember1FilterOrFilterAndUnionMember0Condition",
    "FilterUnionMember1FilterNotUnionMember1FilterOrUnionMember1",
    "FilterUnionMember1FilterNotUnionMember1FilterOrUnionMember1Condition",
    "FilterUnionMember1FilterOr",
    "FilterUnionMember1FilterOrFilter",
    "FilterUnionMember1FilterOrFilterAndUnionMember0",
    "FilterUnionMember1FilterOrFilterAndUnionMember0Condition",
    "FilterUnionMember1FilterOrFilterAndUnionMember0Filter",
    "FilterUnionMember1FilterOrFilterAndUnionMember0FilterNotUnionMember0",
    "FilterUnionMember1FilterOrFilterAndUnionMember0FilterNotUnionMember0Condition",
    "FilterUnionMember1FilterOrFilterNotUnionMember0",
    "FilterUnionMember1FilterOrFilterNotUnionMember0Condition",
    "FilterUnionMember1FilterOrFilterNotUnionMember0Filter",
    "FilterUnionMember1FilterOrFilterNotUnionMember0FilterAndUnionMember0",
    "FilterUnionMember1FilterOrFilterNotUnionMember0FilterAndUnionMember0Condition",
    "FilterUnionMember1FilterOrUnionMember1",
    "FilterUnionMember1FilterOrUnionMember1Condition",
    "FilterUnionMember1FilterOrUnionMember1Filter",
    "FilterUnionMember1FilterOrUnionMember1FilterAnd",
    "FilterUnionMember1FilterOrUnionMember1FilterAndFilter",
    "FilterUnionMember1FilterOrUnionMember1FilterAndFilterNotUnionMember0",
    "FilterUnionMember1FilterOrUnionMember1FilterAndFilterNotUnionMember0Condition",
    "FilterUnionMember1FilterOrUnionMember1FilterAndUnionMember1",
    "FilterUnionMember1FilterOrUnionMember1FilterAndUnionMember1Condition",
    "FilterUnionMember1FilterOrUnionMember1FilterNot",
    "FilterUnionMember1FilterOrUnionMember1FilterNotFilter",
    "FilterUnionMember1FilterOrUnionMember1FilterNotFilterAndUnionMember0",
    "FilterUnionMember1FilterOrUnionMember1FilterNotFilterAndUnionMember0Condition",
    "FilterUnionMember1FilterOrUnionMember1FilterNotUnionMember1",
    "FilterUnionMember1FilterOrUnionMember1FilterNotUnionMember1Condition",
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


class FilterFilterAndFilterNotUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


class FilterFilterAndFilterNotUnionMember0FilterOrUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterFilterAndFilterNotUnionMember0FilterOrUnionMember0: TypeAlias = Union[
    FilterFilterAndFilterNotUnionMember0FilterOrUnionMember0Condition, object
]


class FilterFilterAndFilterNotUnionMember0Filter(TypedDict, total=False):
    and_: object

    not_: object

    or_: Union[Iterable[FilterFilterAndFilterNotUnionMember0FilterOrUnionMember0], object]
    """List of conditions or filters to be ORed together"""


FilterFilterAndFilterNotUnionMember0: TypeAlias = Union[
    FilterFilterAndFilterNotUnionMember0Condition, FilterFilterAndFilterNotUnionMember0Filter
]


class FilterFilterAndFilterOrUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


class FilterFilterAndFilterOrUnionMember0FilterNotUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterFilterAndFilterOrUnionMember0FilterNotUnionMember0: TypeAlias = Union[
    FilterFilterAndFilterOrUnionMember0FilterNotUnionMember0Condition, object
]


class FilterFilterAndFilterOrUnionMember0Filter(TypedDict, total=False):
    and_: object

    not_: Union[Iterable[FilterFilterAndFilterOrUnionMember0FilterNotUnionMember0], object]
    """List of conditions or filters to be NOTed"""

    or_: object


FilterFilterAndFilterOrUnionMember0: TypeAlias = Union[
    FilterFilterAndFilterOrUnionMember0Condition, FilterFilterAndFilterOrUnionMember0Filter
]


class FilterFilterAndFilter(TypedDict, total=False):
    and_: object

    not_: Union[Iterable[FilterFilterAndFilterNotUnionMember0], object]
    """List of conditions or filters to be NOTed"""

    or_: Union[Iterable[FilterFilterAndFilterOrUnionMember0], object]
    """List of conditions or filters to be ORed together"""


class FilterFilterAndUnionMember1Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


class FilterFilterAndUnionMember1FilterNotFilterOrUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterFilterAndUnionMember1FilterNotFilterOrUnionMember0: TypeAlias = Union[
    FilterFilterAndUnionMember1FilterNotFilterOrUnionMember0Condition, object
]


class FilterFilterAndUnionMember1FilterNotFilter(TypedDict, total=False):
    and_: object

    not_: object

    or_: Union[Iterable[FilterFilterAndUnionMember1FilterNotFilterOrUnionMember0], object]
    """List of conditions or filters to be ORed together"""


class FilterFilterAndUnionMember1FilterNotUnionMember1Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterFilterAndUnionMember1FilterNotUnionMember1: TypeAlias = Union[
    FilterFilterAndUnionMember1FilterNotUnionMember1Condition, object
]

FilterFilterAndUnionMember1FilterNot: TypeAlias = Union[
    FilterFilterAndUnionMember1FilterNotFilter, Iterable[FilterFilterAndUnionMember1FilterNotUnionMember1]
]


class FilterFilterAndUnionMember1FilterOrFilterNotUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterFilterAndUnionMember1FilterOrFilterNotUnionMember0: TypeAlias = Union[
    FilterFilterAndUnionMember1FilterOrFilterNotUnionMember0Condition, object
]


class FilterFilterAndUnionMember1FilterOrFilter(TypedDict, total=False):
    and_: object

    not_: Union[Iterable[FilterFilterAndUnionMember1FilterOrFilterNotUnionMember0], object]
    """List of conditions or filters to be NOTed"""

    or_: object


class FilterFilterAndUnionMember1FilterOrUnionMember1Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterFilterAndUnionMember1FilterOrUnionMember1: TypeAlias = Union[
    FilterFilterAndUnionMember1FilterOrUnionMember1Condition, object
]

FilterFilterAndUnionMember1FilterOr: TypeAlias = Union[
    FilterFilterAndUnionMember1FilterOrFilter, Iterable[FilterFilterAndUnionMember1FilterOrUnionMember1]
]


class FilterFilterAndUnionMember1Filter(TypedDict, total=False):
    and_: object

    not_: FilterFilterAndUnionMember1FilterNot
    """List of conditions or filters to be NOTed"""

    or_: FilterFilterAndUnionMember1FilterOr
    """List of conditions or filters to be ORed together"""


FilterFilterAndUnionMember1: TypeAlias = Union[FilterFilterAndUnionMember1Condition, FilterFilterAndUnionMember1Filter]

FilterFilterAnd: TypeAlias = Union[FilterFilterAndFilter, Iterable[FilterFilterAndUnionMember1]]


class FilterFilterNotFilterAndUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


class FilterFilterNotFilterAndUnionMember0FilterOrUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterFilterNotFilterAndUnionMember0FilterOrUnionMember0: TypeAlias = Union[
    FilterFilterNotFilterAndUnionMember0FilterOrUnionMember0Condition, object
]


class FilterFilterNotFilterAndUnionMember0Filter(TypedDict, total=False):
    and_: object

    not_: object

    or_: Union[Iterable[FilterFilterNotFilterAndUnionMember0FilterOrUnionMember0], object]
    """List of conditions or filters to be ORed together"""


FilterFilterNotFilterAndUnionMember0: TypeAlias = Union[
    FilterFilterNotFilterAndUnionMember0Condition, FilterFilterNotFilterAndUnionMember0Filter
]


class FilterFilterNotFilterOrUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


class FilterFilterNotFilterOrUnionMember0FilterAndUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterFilterNotFilterOrUnionMember0FilterAndUnionMember0: TypeAlias = Union[
    FilterFilterNotFilterOrUnionMember0FilterAndUnionMember0Condition, object
]


class FilterFilterNotFilterOrUnionMember0Filter(TypedDict, total=False):
    and_: Union[Iterable[FilterFilterNotFilterOrUnionMember0FilterAndUnionMember0], object]
    """List of conditions or filters to be ANDed together"""

    not_: object

    or_: object


FilterFilterNotFilterOrUnionMember0: TypeAlias = Union[
    FilterFilterNotFilterOrUnionMember0Condition, FilterFilterNotFilterOrUnionMember0Filter
]


class FilterFilterNotFilter(TypedDict, total=False):
    and_: Union[Iterable[FilterFilterNotFilterAndUnionMember0], object]
    """List of conditions or filters to be ANDed together"""

    not_: object

    or_: Union[Iterable[FilterFilterNotFilterOrUnionMember0], object]
    """List of conditions or filters to be ORed together"""


class FilterFilterNotUnionMember1Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


class FilterFilterNotUnionMember1FilterAndFilterOrUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterFilterNotUnionMember1FilterAndFilterOrUnionMember0: TypeAlias = Union[
    FilterFilterNotUnionMember1FilterAndFilterOrUnionMember0Condition, object
]


class FilterFilterNotUnionMember1FilterAndFilter(TypedDict, total=False):
    and_: object

    not_: object

    or_: Union[Iterable[FilterFilterNotUnionMember1FilterAndFilterOrUnionMember0], object]
    """List of conditions or filters to be ORed together"""


class FilterFilterNotUnionMember1FilterAndUnionMember1Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterFilterNotUnionMember1FilterAndUnionMember1: TypeAlias = Union[
    FilterFilterNotUnionMember1FilterAndUnionMember1Condition, object
]

FilterFilterNotUnionMember1FilterAnd: TypeAlias = Union[
    FilterFilterNotUnionMember1FilterAndFilter, Iterable[FilterFilterNotUnionMember1FilterAndUnionMember1]
]


class FilterFilterNotUnionMember1FilterOrFilterAndUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterFilterNotUnionMember1FilterOrFilterAndUnionMember0: TypeAlias = Union[
    FilterFilterNotUnionMember1FilterOrFilterAndUnionMember0Condition, object
]


class FilterFilterNotUnionMember1FilterOrFilter(TypedDict, total=False):
    and_: Union[Iterable[FilterFilterNotUnionMember1FilterOrFilterAndUnionMember0], object]
    """List of conditions or filters to be ANDed together"""

    not_: object

    or_: object


class FilterFilterNotUnionMember1FilterOrUnionMember1Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterFilterNotUnionMember1FilterOrUnionMember1: TypeAlias = Union[
    FilterFilterNotUnionMember1FilterOrUnionMember1Condition, object
]

FilterFilterNotUnionMember1FilterOr: TypeAlias = Union[
    FilterFilterNotUnionMember1FilterOrFilter, Iterable[FilterFilterNotUnionMember1FilterOrUnionMember1]
]


class FilterFilterNotUnionMember1Filter(TypedDict, total=False):
    and_: FilterFilterNotUnionMember1FilterAnd
    """List of conditions or filters to be ANDed together"""

    not_: object

    or_: FilterFilterNotUnionMember1FilterOr
    """List of conditions or filters to be ORed together"""


FilterFilterNotUnionMember1: TypeAlias = Union[FilterFilterNotUnionMember1Condition, FilterFilterNotUnionMember1Filter]

FilterFilterNot: TypeAlias = Union[FilterFilterNotFilter, Iterable[FilterFilterNotUnionMember1]]


class FilterFilterOrFilterAndUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


class FilterFilterOrFilterAndUnionMember0FilterNotUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterFilterOrFilterAndUnionMember0FilterNotUnionMember0: TypeAlias = Union[
    FilterFilterOrFilterAndUnionMember0FilterNotUnionMember0Condition, object
]


class FilterFilterOrFilterAndUnionMember0Filter(TypedDict, total=False):
    and_: object

    not_: Union[Iterable[FilterFilterOrFilterAndUnionMember0FilterNotUnionMember0], object]
    """List of conditions or filters to be NOTed"""

    or_: object


FilterFilterOrFilterAndUnionMember0: TypeAlias = Union[
    FilterFilterOrFilterAndUnionMember0Condition, FilterFilterOrFilterAndUnionMember0Filter
]


class FilterFilterOrFilterNotUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


class FilterFilterOrFilterNotUnionMember0FilterAndUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterFilterOrFilterNotUnionMember0FilterAndUnionMember0: TypeAlias = Union[
    FilterFilterOrFilterNotUnionMember0FilterAndUnionMember0Condition, object
]


class FilterFilterOrFilterNotUnionMember0Filter(TypedDict, total=False):
    and_: Union[Iterable[FilterFilterOrFilterNotUnionMember0FilterAndUnionMember0], object]
    """List of conditions or filters to be ANDed together"""

    not_: object

    or_: object


FilterFilterOrFilterNotUnionMember0: TypeAlias = Union[
    FilterFilterOrFilterNotUnionMember0Condition, FilterFilterOrFilterNotUnionMember0Filter
]


class FilterFilterOrFilter(TypedDict, total=False):
    and_: Union[Iterable[FilterFilterOrFilterAndUnionMember0], object]
    """List of conditions or filters to be ANDed together"""

    not_: Union[Iterable[FilterFilterOrFilterNotUnionMember0], object]
    """List of conditions or filters to be NOTed"""

    or_: object


class FilterFilterOrUnionMember1Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


class FilterFilterOrUnionMember1FilterAndFilterNotUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterFilterOrUnionMember1FilterAndFilterNotUnionMember0: TypeAlias = Union[
    FilterFilterOrUnionMember1FilterAndFilterNotUnionMember0Condition, object
]


class FilterFilterOrUnionMember1FilterAndFilter(TypedDict, total=False):
    and_: object

    not_: Union[Iterable[FilterFilterOrUnionMember1FilterAndFilterNotUnionMember0], object]
    """List of conditions or filters to be NOTed"""

    or_: object


class FilterFilterOrUnionMember1FilterAndUnionMember1Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterFilterOrUnionMember1FilterAndUnionMember1: TypeAlias = Union[
    FilterFilterOrUnionMember1FilterAndUnionMember1Condition, object
]

FilterFilterOrUnionMember1FilterAnd: TypeAlias = Union[
    FilterFilterOrUnionMember1FilterAndFilter, Iterable[FilterFilterOrUnionMember1FilterAndUnionMember1]
]


class FilterFilterOrUnionMember1FilterNotFilterAndUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterFilterOrUnionMember1FilterNotFilterAndUnionMember0: TypeAlias = Union[
    FilterFilterOrUnionMember1FilterNotFilterAndUnionMember0Condition, object
]


class FilterFilterOrUnionMember1FilterNotFilter(TypedDict, total=False):
    and_: Union[Iterable[FilterFilterOrUnionMember1FilterNotFilterAndUnionMember0], object]
    """List of conditions or filters to be ANDed together"""

    not_: object

    or_: object


class FilterFilterOrUnionMember1FilterNotUnionMember1Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterFilterOrUnionMember1FilterNotUnionMember1: TypeAlias = Union[
    FilterFilterOrUnionMember1FilterNotUnionMember1Condition, object
]

FilterFilterOrUnionMember1FilterNot: TypeAlias = Union[
    FilterFilterOrUnionMember1FilterNotFilter, Iterable[FilterFilterOrUnionMember1FilterNotUnionMember1]
]


class FilterFilterOrUnionMember1Filter(TypedDict, total=False):
    and_: FilterFilterOrUnionMember1FilterAnd
    """List of conditions or filters to be ANDed together"""

    not_: FilterFilterOrUnionMember1FilterNot
    """List of conditions or filters to be NOTed"""

    or_: object


FilterFilterOrUnionMember1: TypeAlias = Union[FilterFilterOrUnionMember1Condition, FilterFilterOrUnionMember1Filter]

FilterFilterOr: TypeAlias = Union[FilterFilterOrFilter, Iterable[FilterFilterOrUnionMember1]]


class FilterFilter(TypedDict, total=False):
    and_: FilterFilterAnd
    """List of conditions or filters to be ANDed together"""

    not_: FilterFilterNot
    """List of conditions or filters to be NOTed"""

    or_: FilterFilterOr
    """List of conditions or filters to be ORed together"""


class FilterUnionMember1Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


class FilterUnionMember1FilterAndFilterNotUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


class FilterUnionMember1FilterAndFilterNotUnionMember0FilterOrUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterUnionMember1FilterAndFilterNotUnionMember0FilterOrUnionMember0: TypeAlias = Union[
    FilterUnionMember1FilterAndFilterNotUnionMember0FilterOrUnionMember0Condition, object
]


class FilterUnionMember1FilterAndFilterNotUnionMember0Filter(TypedDict, total=False):
    and_: object

    not_: object

    or_: Union[Iterable[FilterUnionMember1FilterAndFilterNotUnionMember0FilterOrUnionMember0], object]
    """List of conditions or filters to be ORed together"""


FilterUnionMember1FilterAndFilterNotUnionMember0: TypeAlias = Union[
    FilterUnionMember1FilterAndFilterNotUnionMember0Condition, FilterUnionMember1FilterAndFilterNotUnionMember0Filter
]


class FilterUnionMember1FilterAndFilterOrUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


class FilterUnionMember1FilterAndFilterOrUnionMember0FilterNotUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterUnionMember1FilterAndFilterOrUnionMember0FilterNotUnionMember0: TypeAlias = Union[
    FilterUnionMember1FilterAndFilterOrUnionMember0FilterNotUnionMember0Condition, object
]


class FilterUnionMember1FilterAndFilterOrUnionMember0Filter(TypedDict, total=False):
    and_: object

    not_: Union[Iterable[FilterUnionMember1FilterAndFilterOrUnionMember0FilterNotUnionMember0], object]
    """List of conditions or filters to be NOTed"""

    or_: object


FilterUnionMember1FilterAndFilterOrUnionMember0: TypeAlias = Union[
    FilterUnionMember1FilterAndFilterOrUnionMember0Condition, FilterUnionMember1FilterAndFilterOrUnionMember0Filter
]


class FilterUnionMember1FilterAndFilter(TypedDict, total=False):
    and_: object

    not_: Union[Iterable[FilterUnionMember1FilterAndFilterNotUnionMember0], object]
    """List of conditions or filters to be NOTed"""

    or_: Union[Iterable[FilterUnionMember1FilterAndFilterOrUnionMember0], object]
    """List of conditions or filters to be ORed together"""


class FilterUnionMember1FilterAndUnionMember1Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


class FilterUnionMember1FilterAndUnionMember1FilterNotFilterOrUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterUnionMember1FilterAndUnionMember1FilterNotFilterOrUnionMember0: TypeAlias = Union[
    FilterUnionMember1FilterAndUnionMember1FilterNotFilterOrUnionMember0Condition, object
]


class FilterUnionMember1FilterAndUnionMember1FilterNotFilter(TypedDict, total=False):
    and_: object

    not_: object

    or_: Union[Iterable[FilterUnionMember1FilterAndUnionMember1FilterNotFilterOrUnionMember0], object]
    """List of conditions or filters to be ORed together"""


class FilterUnionMember1FilterAndUnionMember1FilterNotUnionMember1Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterUnionMember1FilterAndUnionMember1FilterNotUnionMember1: TypeAlias = Union[
    FilterUnionMember1FilterAndUnionMember1FilterNotUnionMember1Condition, object
]

FilterUnionMember1FilterAndUnionMember1FilterNot: TypeAlias = Union[
    FilterUnionMember1FilterAndUnionMember1FilterNotFilter,
    Iterable[FilterUnionMember1FilterAndUnionMember1FilterNotUnionMember1],
]


class FilterUnionMember1FilterAndUnionMember1FilterOrFilterNotUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterUnionMember1FilterAndUnionMember1FilterOrFilterNotUnionMember0: TypeAlias = Union[
    FilterUnionMember1FilterAndUnionMember1FilterOrFilterNotUnionMember0Condition, object
]


class FilterUnionMember1FilterAndUnionMember1FilterOrFilter(TypedDict, total=False):
    and_: object

    not_: Union[Iterable[FilterUnionMember1FilterAndUnionMember1FilterOrFilterNotUnionMember0], object]
    """List of conditions or filters to be NOTed"""

    or_: object


class FilterUnionMember1FilterAndUnionMember1FilterOrUnionMember1Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterUnionMember1FilterAndUnionMember1FilterOrUnionMember1: TypeAlias = Union[
    FilterUnionMember1FilterAndUnionMember1FilterOrUnionMember1Condition, object
]

FilterUnionMember1FilterAndUnionMember1FilterOr: TypeAlias = Union[
    FilterUnionMember1FilterAndUnionMember1FilterOrFilter,
    Iterable[FilterUnionMember1FilterAndUnionMember1FilterOrUnionMember1],
]


class FilterUnionMember1FilterAndUnionMember1Filter(TypedDict, total=False):
    and_: object

    not_: FilterUnionMember1FilterAndUnionMember1FilterNot
    """List of conditions or filters to be NOTed"""

    or_: FilterUnionMember1FilterAndUnionMember1FilterOr
    """List of conditions or filters to be ORed together"""


FilterUnionMember1FilterAndUnionMember1: TypeAlias = Union[
    FilterUnionMember1FilterAndUnionMember1Condition, FilterUnionMember1FilterAndUnionMember1Filter
]

FilterUnionMember1FilterAnd: TypeAlias = Union[
    FilterUnionMember1FilterAndFilter, Iterable[FilterUnionMember1FilterAndUnionMember1]
]


class FilterUnionMember1FilterNotFilterAndUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


class FilterUnionMember1FilterNotFilterAndUnionMember0FilterOrUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterUnionMember1FilterNotFilterAndUnionMember0FilterOrUnionMember0: TypeAlias = Union[
    FilterUnionMember1FilterNotFilterAndUnionMember0FilterOrUnionMember0Condition, object
]


class FilterUnionMember1FilterNotFilterAndUnionMember0Filter(TypedDict, total=False):
    and_: object

    not_: object

    or_: Union[Iterable[FilterUnionMember1FilterNotFilterAndUnionMember0FilterOrUnionMember0], object]
    """List of conditions or filters to be ORed together"""


FilterUnionMember1FilterNotFilterAndUnionMember0: TypeAlias = Union[
    FilterUnionMember1FilterNotFilterAndUnionMember0Condition, FilterUnionMember1FilterNotFilterAndUnionMember0Filter
]


class FilterUnionMember1FilterNotFilterOrUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


class FilterUnionMember1FilterNotFilterOrUnionMember0FilterAndUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterUnionMember1FilterNotFilterOrUnionMember0FilterAndUnionMember0: TypeAlias = Union[
    FilterUnionMember1FilterNotFilterOrUnionMember0FilterAndUnionMember0Condition, object
]


class FilterUnionMember1FilterNotFilterOrUnionMember0Filter(TypedDict, total=False):
    and_: Union[Iterable[FilterUnionMember1FilterNotFilterOrUnionMember0FilterAndUnionMember0], object]
    """List of conditions or filters to be ANDed together"""

    not_: object

    or_: object


FilterUnionMember1FilterNotFilterOrUnionMember0: TypeAlias = Union[
    FilterUnionMember1FilterNotFilterOrUnionMember0Condition, FilterUnionMember1FilterNotFilterOrUnionMember0Filter
]


class FilterUnionMember1FilterNotFilter(TypedDict, total=False):
    and_: Union[Iterable[FilterUnionMember1FilterNotFilterAndUnionMember0], object]
    """List of conditions or filters to be ANDed together"""

    not_: object

    or_: Union[Iterable[FilterUnionMember1FilterNotFilterOrUnionMember0], object]
    """List of conditions or filters to be ORed together"""


class FilterUnionMember1FilterNotUnionMember1Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


class FilterUnionMember1FilterNotUnionMember1FilterAndFilterOrUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterUnionMember1FilterNotUnionMember1FilterAndFilterOrUnionMember0: TypeAlias = Union[
    FilterUnionMember1FilterNotUnionMember1FilterAndFilterOrUnionMember0Condition, object
]


class FilterUnionMember1FilterNotUnionMember1FilterAndFilter(TypedDict, total=False):
    and_: object

    not_: object

    or_: Union[Iterable[FilterUnionMember1FilterNotUnionMember1FilterAndFilterOrUnionMember0], object]
    """List of conditions or filters to be ORed together"""


class FilterUnionMember1FilterNotUnionMember1FilterAndUnionMember1Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterUnionMember1FilterNotUnionMember1FilterAndUnionMember1: TypeAlias = Union[
    FilterUnionMember1FilterNotUnionMember1FilterAndUnionMember1Condition, object
]

FilterUnionMember1FilterNotUnionMember1FilterAnd: TypeAlias = Union[
    FilterUnionMember1FilterNotUnionMember1FilterAndFilter,
    Iterable[FilterUnionMember1FilterNotUnionMember1FilterAndUnionMember1],
]


class FilterUnionMember1FilterNotUnionMember1FilterOrFilterAndUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterUnionMember1FilterNotUnionMember1FilterOrFilterAndUnionMember0: TypeAlias = Union[
    FilterUnionMember1FilterNotUnionMember1FilterOrFilterAndUnionMember0Condition, object
]


class FilterUnionMember1FilterNotUnionMember1FilterOrFilter(TypedDict, total=False):
    and_: Union[Iterable[FilterUnionMember1FilterNotUnionMember1FilterOrFilterAndUnionMember0], object]
    """List of conditions or filters to be ANDed together"""

    not_: object

    or_: object


class FilterUnionMember1FilterNotUnionMember1FilterOrUnionMember1Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterUnionMember1FilterNotUnionMember1FilterOrUnionMember1: TypeAlias = Union[
    FilterUnionMember1FilterNotUnionMember1FilterOrUnionMember1Condition, object
]

FilterUnionMember1FilterNotUnionMember1FilterOr: TypeAlias = Union[
    FilterUnionMember1FilterNotUnionMember1FilterOrFilter,
    Iterable[FilterUnionMember1FilterNotUnionMember1FilterOrUnionMember1],
]


class FilterUnionMember1FilterNotUnionMember1Filter(TypedDict, total=False):
    and_: FilterUnionMember1FilterNotUnionMember1FilterAnd
    """List of conditions or filters to be ANDed together"""

    not_: object

    or_: FilterUnionMember1FilterNotUnionMember1FilterOr
    """List of conditions or filters to be ORed together"""


FilterUnionMember1FilterNotUnionMember1: TypeAlias = Union[
    FilterUnionMember1FilterNotUnionMember1Condition, FilterUnionMember1FilterNotUnionMember1Filter
]

FilterUnionMember1FilterNot: TypeAlias = Union[
    FilterUnionMember1FilterNotFilter, Iterable[FilterUnionMember1FilterNotUnionMember1]
]


class FilterUnionMember1FilterOrFilterAndUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


class FilterUnionMember1FilterOrFilterAndUnionMember0FilterNotUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterUnionMember1FilterOrFilterAndUnionMember0FilterNotUnionMember0: TypeAlias = Union[
    FilterUnionMember1FilterOrFilterAndUnionMember0FilterNotUnionMember0Condition, object
]


class FilterUnionMember1FilterOrFilterAndUnionMember0Filter(TypedDict, total=False):
    and_: object

    not_: Union[Iterable[FilterUnionMember1FilterOrFilterAndUnionMember0FilterNotUnionMember0], object]
    """List of conditions or filters to be NOTed"""

    or_: object


FilterUnionMember1FilterOrFilterAndUnionMember0: TypeAlias = Union[
    FilterUnionMember1FilterOrFilterAndUnionMember0Condition, FilterUnionMember1FilterOrFilterAndUnionMember0Filter
]


class FilterUnionMember1FilterOrFilterNotUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


class FilterUnionMember1FilterOrFilterNotUnionMember0FilterAndUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterUnionMember1FilterOrFilterNotUnionMember0FilterAndUnionMember0: TypeAlias = Union[
    FilterUnionMember1FilterOrFilterNotUnionMember0FilterAndUnionMember0Condition, object
]


class FilterUnionMember1FilterOrFilterNotUnionMember0Filter(TypedDict, total=False):
    and_: Union[Iterable[FilterUnionMember1FilterOrFilterNotUnionMember0FilterAndUnionMember0], object]
    """List of conditions or filters to be ANDed together"""

    not_: object

    or_: object


FilterUnionMember1FilterOrFilterNotUnionMember0: TypeAlias = Union[
    FilterUnionMember1FilterOrFilterNotUnionMember0Condition, FilterUnionMember1FilterOrFilterNotUnionMember0Filter
]


class FilterUnionMember1FilterOrFilter(TypedDict, total=False):
    and_: Union[Iterable[FilterUnionMember1FilterOrFilterAndUnionMember0], object]
    """List of conditions or filters to be ANDed together"""

    not_: Union[Iterable[FilterUnionMember1FilterOrFilterNotUnionMember0], object]
    """List of conditions or filters to be NOTed"""

    or_: object


class FilterUnionMember1FilterOrUnionMember1Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


class FilterUnionMember1FilterOrUnionMember1FilterAndFilterNotUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterUnionMember1FilterOrUnionMember1FilterAndFilterNotUnionMember0: TypeAlias = Union[
    FilterUnionMember1FilterOrUnionMember1FilterAndFilterNotUnionMember0Condition, object
]


class FilterUnionMember1FilterOrUnionMember1FilterAndFilter(TypedDict, total=False):
    and_: object

    not_: Union[Iterable[FilterUnionMember1FilterOrUnionMember1FilterAndFilterNotUnionMember0], object]
    """List of conditions or filters to be NOTed"""

    or_: object


class FilterUnionMember1FilterOrUnionMember1FilterAndUnionMember1Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterUnionMember1FilterOrUnionMember1FilterAndUnionMember1: TypeAlias = Union[
    FilterUnionMember1FilterOrUnionMember1FilterAndUnionMember1Condition, object
]

FilterUnionMember1FilterOrUnionMember1FilterAnd: TypeAlias = Union[
    FilterUnionMember1FilterOrUnionMember1FilterAndFilter,
    Iterable[FilterUnionMember1FilterOrUnionMember1FilterAndUnionMember1],
]


class FilterUnionMember1FilterOrUnionMember1FilterNotFilterAndUnionMember0Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterUnionMember1FilterOrUnionMember1FilterNotFilterAndUnionMember0: TypeAlias = Union[
    FilterUnionMember1FilterOrUnionMember1FilterNotFilterAndUnionMember0Condition, object
]


class FilterUnionMember1FilterOrUnionMember1FilterNotFilter(TypedDict, total=False):
    and_: Union[Iterable[FilterUnionMember1FilterOrUnionMember1FilterNotFilterAndUnionMember0], object]
    """List of conditions or filters to be ANDed together"""

    not_: object

    or_: object


class FilterUnionMember1FilterOrUnionMember1FilterNotUnionMember1Condition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    operator: Required[Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]]
    """The operator for the condition"""

    value: Required[object]
    """The value to compare against"""


FilterUnionMember1FilterOrUnionMember1FilterNotUnionMember1: TypeAlias = Union[
    FilterUnionMember1FilterOrUnionMember1FilterNotUnionMember1Condition, object
]

FilterUnionMember1FilterOrUnionMember1FilterNot: TypeAlias = Union[
    FilterUnionMember1FilterOrUnionMember1FilterNotFilter,
    Iterable[FilterUnionMember1FilterOrUnionMember1FilterNotUnionMember1],
]


class FilterUnionMember1FilterOrUnionMember1Filter(TypedDict, total=False):
    and_: FilterUnionMember1FilterOrUnionMember1FilterAnd
    """List of conditions or filters to be ANDed together"""

    not_: FilterUnionMember1FilterOrUnionMember1FilterNot
    """List of conditions or filters to be NOTed"""

    or_: object


FilterUnionMember1FilterOrUnionMember1: TypeAlias = Union[
    FilterUnionMember1FilterOrUnionMember1Condition, FilterUnionMember1FilterOrUnionMember1Filter
]

FilterUnionMember1FilterOr: TypeAlias = Union[
    FilterUnionMember1FilterOrFilter, Iterable[FilterUnionMember1FilterOrUnionMember1]
]


class FilterUnionMember1Filter(TypedDict, total=False):
    and_: FilterUnionMember1FilterAnd
    """List of conditions or filters to be ANDed together"""

    not_: FilterUnionMember1FilterNot
    """List of conditions or filters to be NOTed"""

    or_: FilterUnionMember1FilterOr
    """List of conditions or filters to be ORed together"""


FilterUnionMember1: TypeAlias = Union[FilterUnionMember1Condition, FilterUnionMember1Filter]

Filter: TypeAlias = Union[FilterFilter, Iterable[FilterUnionMember1]]


class Options(TypedDict, total=False):
    min_score: float

    return_chunks: bool

    return_metadata: bool
