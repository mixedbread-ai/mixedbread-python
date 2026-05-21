# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .store_chunk_search_options_param import StoreChunkSearchOptionsParam
from .shared_params.search_filter_condition import SearchFilterCondition

__all__ = [
    "StoreListChunksParams",
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
]


class StoreListChunksParams(TypedDict, total=False):
    store_identifiers: Required[SequenceNotStr[str]]
    """IDs or names of stores"""

    top_k: int
    """Number of results to return"""

    filters: Optional[Filters]
    """Optional filter conditions"""

    file_ids: Union[Iterable[object], SequenceNotStr[str], None]
    """Optional list of file IDs to filter chunks by (inclusion filter)"""

    sort_by: Union[str, Iterable[object], None]
    """Optional sort applied to the returned chunks.

    Pass a metadata field path or a tuple of (field path, ascending). Unprefixed dot
    paths target file metadata; generated_metadata.\\** targets chunk metadata.
    """

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
