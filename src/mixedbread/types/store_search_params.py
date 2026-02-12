# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .extractions.text_input_param import TextInputParam
from .store_chunk_search_options_param import StoreChunkSearchOptionsParam
from .extractions.image_url_input_param import ImageURLInputParam
from .shared_params.search_filter_condition import SearchFilterCondition

__all__ = ["StoreSearchParams", "Query", "Filters", "FiltersUnionMember2"]


class StoreSearchParams(TypedDict, total=False):
    query: Required[Query]
    """Search query text"""

    store_identifiers: Required[SequenceNotStr[str]]
    """IDs or names of stores to search"""

    top_k: int
    """Number of results to return"""

    filters: Optional[Filters]
    """Optional filter conditions"""

    file_ids: Union[Iterable[object], SequenceNotStr[str], None]
    """Optional list of file IDs to filter chunks by (inclusion filter)"""

    search_options: StoreChunkSearchOptionsParam
    """Search configuration options"""


Query: TypeAlias = Union[str, ImageURLInputParam, TextInputParam]

FiltersUnionMember2: TypeAlias = Union["SearchFilter", SearchFilterCondition]

Filters: TypeAlias = Union["SearchFilter", SearchFilterCondition, Iterable[FiltersUnionMember2]]

from .shared_params.search_filter import SearchFilter
