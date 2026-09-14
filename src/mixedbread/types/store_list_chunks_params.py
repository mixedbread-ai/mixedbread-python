# File generated from our OpenAPI spec by sdkgen. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .shared_params.search_filter import SearchFilter
from .store_chunk_search_options_param import StoreChunkSearchOptionsParam
from .shared_params.search_filter_condition import SearchFilterCondition

__all__ = ["StoreListChunksParams", "Filters", "FiltersUnionMember2"]


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
    paths target file metadata; generated_metadata.* targets chunk metadata.
    """

    search_options: StoreChunkSearchOptionsParam
    """Search configuration options"""


FiltersUnionMember2: TypeAlias = Union[SearchFilter, SearchFilterCondition]

Filters: TypeAlias = Union[SearchFilter, SearchFilterCondition, Iterable[FiltersUnionMember2]]
