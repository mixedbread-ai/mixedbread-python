# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .shared_params.search_filter_condition import SearchFilterCondition

__all__ = [
    "StoreGrepParams",
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


class StoreGrepParams(TypedDict, total=False):
    store_identifiers: Required[SequenceNotStr[str]]
    """IDs or names of stores"""

    top_k: int
    """Number of results to return"""

    filters: Optional[Filters]
    """Optional filter conditions"""

    file_ids: Union[Iterable[object], SequenceNotStr[str], None]
    """Optional list of file IDs to filter chunks by (inclusion filter)"""

    pattern: Required[str]
    """Regular expression (RE2 syntax) matched against chunk text"""

    targets: List[Literal["text", "generated"]]
    """Chunk content groups to match against.

    `text` matches the original text of text chunks; `generated` matches
    ingestion-derived fields (transcription, OCR text, summaries).
    """

    case_sensitive: bool
    """Whether the regular expression is case-sensitive"""

    return_metadata: bool
    """Whether to return file metadata"""


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
