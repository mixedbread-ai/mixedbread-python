# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import TypeAlias, TypedDict

from .store_file_status import StoreFileStatus
from ..shared_params.search_filter_condition import SearchFilterCondition

__all__ = [
    "FileListParams",
    "MetadataFilter",
    "MetadataFilterSearchFilterInput",
    "MetadataFilterSearchFilterInputAll",
    "MetadataFilterSearchFilterInputAny",
    "MetadataFilterSearchFilterInputNone",
    "MetadataFilterUnionMember2",
    "MetadataFilterUnionMember2SearchFilterInput",
    "MetadataFilterUnionMember2SearchFilterInputAll",
    "MetadataFilterUnionMember2SearchFilterInputAny",
    "MetadataFilterUnionMember2SearchFilterInputNone",
]


class FileListParams(TypedDict, total=False):
    limit: int
    """Maximum number of items to return per page (1-100)"""

    after: Optional[str]
    """Cursor for forward pagination - get items after this position.

    Use last_cursor from previous response.
    """

    before: Optional[str]
    """Cursor for backward pagination - get items before this position.

    Use first_cursor from previous response.
    """

    include_total: bool
    """Whether to include total count in response (expensive operation)"""

    statuses: Optional[List[StoreFileStatus]]
    """Status to filter by"""

    metadata_filter: Optional[MetadataFilter]
    """Metadata filter to apply to the query"""

    q: Optional[str]
    """Search query for fuzzy matching over name and external_id fields"""


MetadataFilterSearchFilterInputAll: TypeAlias = Union[SearchFilterCondition, object]

MetadataFilterSearchFilterInputAny: TypeAlias = Union[SearchFilterCondition, object]

MetadataFilterSearchFilterInputNone: TypeAlias = Union[SearchFilterCondition, object]


class MetadataFilterSearchFilterInput(TypedDict, total=False):
    """Represents a filter with AND, OR, and NOT conditions."""

    all: Optional[Iterable[MetadataFilterSearchFilterInputAll]]
    """List of conditions or filters to be ANDed together"""

    any: Optional[Iterable[MetadataFilterSearchFilterInputAny]]
    """List of conditions or filters to be ORed together"""

    none: Optional[Iterable[MetadataFilterSearchFilterInputNone]]
    """List of conditions or filters to be NOTed"""


MetadataFilterUnionMember2SearchFilterInputAll: TypeAlias = Union[SearchFilterCondition, object]

MetadataFilterUnionMember2SearchFilterInputAny: TypeAlias = Union[SearchFilterCondition, object]

MetadataFilterUnionMember2SearchFilterInputNone: TypeAlias = Union[SearchFilterCondition, object]


class MetadataFilterUnionMember2SearchFilterInput(TypedDict, total=False):
    """Represents a filter with AND, OR, and NOT conditions."""

    all: Optional[Iterable[MetadataFilterUnionMember2SearchFilterInputAll]]
    """List of conditions or filters to be ANDed together"""

    any: Optional[Iterable[MetadataFilterUnionMember2SearchFilterInputAny]]
    """List of conditions or filters to be ORed together"""

    none: Optional[Iterable[MetadataFilterUnionMember2SearchFilterInputNone]]
    """List of conditions or filters to be NOTed"""


MetadataFilterUnionMember2: TypeAlias = Union[MetadataFilterUnionMember2SearchFilterInput, SearchFilterCondition]

MetadataFilter: TypeAlias = Union[
    MetadataFilterSearchFilterInput, SearchFilterCondition, Iterable[MetadataFilterUnionMember2]
]
