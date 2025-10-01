# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import TypeAlias, TypedDict

from .store_file_status import StoreFileStatus
from ..shared_params.search_filter_condition import SearchFilterCondition

__all__ = ["FileListParams", "MetadataFilter", "MetadataFilterUnionMember2"]


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


MetadataFilterUnionMember2: TypeAlias = Union["SearchFilter", SearchFilterCondition]

MetadataFilter: TypeAlias = Union["SearchFilter", SearchFilterCondition, Iterable[MetadataFilterUnionMember2]]

from ..shared_params.search_filter import SearchFilter
