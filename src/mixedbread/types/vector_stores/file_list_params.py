# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import TypeAlias, TypedDict

from .vector_store_file_status import VectorStoreFileStatus
from ..shared_params.search_filter_condition import SearchFilterCondition

__all__ = [
    "FileListParams",
    "MetadataFilter",
    "MetadataFilterMxbaiOmniCoreVectorStoreModelsSearchFilter2",
    "MetadataFilterMxbaiOmniCoreVectorStoreModelsSearchFilter2All",
    "MetadataFilterMxbaiOmniCoreVectorStoreModelsSearchFilter2Any",
    "MetadataFilterMxbaiOmniCoreVectorStoreModelsSearchFilter2None",
    "MetadataFilterUnionMember2",
    "MetadataFilterUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter2",
    "MetadataFilterUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter2All",
    "MetadataFilterUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter2Any",
    "MetadataFilterUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter2None",
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

    statuses: Optional[List[VectorStoreFileStatus]]
    """Status to filter by"""

    metadata_filter: Optional[MetadataFilter]
    """Metadata filter to apply to the query"""


MetadataFilterMxbaiOmniCoreVectorStoreModelsSearchFilter2All: TypeAlias = Union[SearchFilterCondition, object]

MetadataFilterMxbaiOmniCoreVectorStoreModelsSearchFilter2Any: TypeAlias = Union[SearchFilterCondition, object]

MetadataFilterMxbaiOmniCoreVectorStoreModelsSearchFilter2None: TypeAlias = Union[SearchFilterCondition, object]


class MetadataFilterMxbaiOmniCoreVectorStoreModelsSearchFilter2(TypedDict, total=False):
    all: Optional[Iterable[MetadataFilterMxbaiOmniCoreVectorStoreModelsSearchFilter2All]]
    """List of conditions or filters to be ANDed together"""

    any: Optional[Iterable[MetadataFilterMxbaiOmniCoreVectorStoreModelsSearchFilter2Any]]
    """List of conditions or filters to be ORed together"""

    none: Optional[Iterable[MetadataFilterMxbaiOmniCoreVectorStoreModelsSearchFilter2None]]
    """List of conditions or filters to be NOTed"""


MetadataFilterUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter2All: TypeAlias = Union[
    SearchFilterCondition, object
]

MetadataFilterUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter2Any: TypeAlias = Union[
    SearchFilterCondition, object
]

MetadataFilterUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter2None: TypeAlias = Union[
    SearchFilterCondition, object
]


class MetadataFilterUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter2(TypedDict, total=False):
    all: Optional[Iterable[MetadataFilterUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter2All]]
    """List of conditions or filters to be ANDed together"""

    any: Optional[Iterable[MetadataFilterUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter2Any]]
    """List of conditions or filters to be ORed together"""

    none: Optional[Iterable[MetadataFilterUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter2None]]
    """List of conditions or filters to be NOTed"""


MetadataFilterUnionMember2: TypeAlias = Union[
    MetadataFilterUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter2, SearchFilterCondition
]

MetadataFilter: TypeAlias = Union[
    MetadataFilterMxbaiOmniCoreVectorStoreModelsSearchFilter2,
    SearchFilterCondition,
    Iterable[MetadataFilterUnionMember2],
]
