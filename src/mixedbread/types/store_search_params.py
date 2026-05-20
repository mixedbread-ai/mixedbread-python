# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .extractions.text_input_param import TextInputParam
from .store_chunk_search_options_param import StoreChunkSearchOptionsParam
from .extractions.image_url_input_param import ImageURLInputParam
from .shared_params.search_filter_condition import SearchFilterCondition

__all__ = [
    "StoreSearchParams",
    "Filters",
    "FiltersSearchFilterInput",
    "FiltersSearchFilterInputAll",
    "FiltersSearchFilterInputAny",
    "FiltersSearchFilterInputNone",
    "FiltersUnionMember2",
    "FiltersUnionMember2SearchFilterInput",
    "FiltersUnionMember2SearchFilterInputAll",
    "FiltersUnionMember2SearchFilterInputAny",
    "FiltersUnionMember2SearchFilterInputNone",
    "Query",
]


class StoreSearchParams(TypedDict, total=False):
    store_identifiers: Required[SequenceNotStr[str]]
    """IDs or names of stores"""

    top_k: int
    """Number of results to return"""

    filters: Optional[Filters]
    """Optional filter conditions"""

    file_ids: Union[Iterable[object], SequenceNotStr[str], None]
    """Optional list of file IDs to filter chunks by (inclusion filter)"""

    query: Required[Query]
    """Search query text"""

    search_options: StoreChunkSearchOptionsParam
    """Search configuration options"""


FiltersSearchFilterInputAll: TypeAlias = Union[SearchFilterCondition, object]

FiltersSearchFilterInputAny: TypeAlias = Union[SearchFilterCondition, object]

FiltersSearchFilterInputNone: TypeAlias = Union[SearchFilterCondition, object]


class FiltersSearchFilterInput(TypedDict, total=False):
    """Represents a filter with AND, OR, and NOT conditions."""

    all: Optional[Iterable[FiltersSearchFilterInputAll]]
    """List of conditions or filters to be ANDed together"""

    any: Optional[Iterable[FiltersSearchFilterInputAny]]
    """List of conditions or filters to be ORed together"""

    none: Optional[Iterable[FiltersSearchFilterInputNone]]
    """List of conditions or filters to be NOTed"""


FiltersUnionMember2SearchFilterInputAll: TypeAlias = Union[SearchFilterCondition, object]

FiltersUnionMember2SearchFilterInputAny: TypeAlias = Union[SearchFilterCondition, object]

FiltersUnionMember2SearchFilterInputNone: TypeAlias = Union[SearchFilterCondition, object]


class FiltersUnionMember2SearchFilterInput(TypedDict, total=False):
    """Represents a filter with AND, OR, and NOT conditions."""

    all: Optional[Iterable[FiltersUnionMember2SearchFilterInputAll]]
    """List of conditions or filters to be ANDed together"""

    any: Optional[Iterable[FiltersUnionMember2SearchFilterInputAny]]
    """List of conditions or filters to be ORed together"""

    none: Optional[Iterable[FiltersUnionMember2SearchFilterInputNone]]
    """List of conditions or filters to be NOTed"""


FiltersUnionMember2: TypeAlias = Union[FiltersUnionMember2SearchFilterInput, SearchFilterCondition]

Filters: TypeAlias = Union[FiltersSearchFilterInput, SearchFilterCondition, Iterable[FiltersUnionMember2]]

Query: TypeAlias = Union[str, ImageURLInputParam, TextInputParam]
