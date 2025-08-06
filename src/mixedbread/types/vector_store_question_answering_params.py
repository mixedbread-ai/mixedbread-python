# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import TypeAlias, TypedDict

from .shared_params.search_filter_condition import SearchFilterCondition
from .vector_store_chunk_search_options_param import VectorStoreChunkSearchOptionsParam

__all__ = [
    "VectorStoreQuestionAnsweringParams",
    "Filters",
    "FiltersMxbaiOmniCoreVectorStoreModelsSearchFilter1",
    "FiltersMxbaiOmniCoreVectorStoreModelsSearchFilter1All",
    "FiltersMxbaiOmniCoreVectorStoreModelsSearchFilter1Any",
    "FiltersMxbaiOmniCoreVectorStoreModelsSearchFilter1None",
    "FiltersUnionMember2",
    "FiltersUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter1",
    "FiltersUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter1All",
    "FiltersUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter1Any",
    "FiltersUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter1None",
    "QaOptions",
]


class VectorStoreQuestionAnsweringParams(TypedDict, total=False):
    query: str
    """Question to answer.

    If not provided, the question will be extracted from the passed messages.
    """

    vector_store_identifiers: Optional[List[str]]
    """IDs or names of vector stores to search"""

    vector_store_ids: Optional[List[str]]

    top_k: int
    """Number of results to return"""

    filters: Optional[Filters]
    """Optional filter conditions"""

    file_ids: Union[Iterable[object], List[str], None]
    """Optional list of file IDs to filter chunks by (inclusion filter)"""

    search_options: VectorStoreChunkSearchOptionsParam
    """Search configuration options"""

    stream: bool
    """Whether to stream the answer"""

    qa_options: QaOptions
    """Question answering configuration options"""


FiltersMxbaiOmniCoreVectorStoreModelsSearchFilter1All: TypeAlias = Union[SearchFilterCondition, object]

FiltersMxbaiOmniCoreVectorStoreModelsSearchFilter1Any: TypeAlias = Union[SearchFilterCondition, object]

FiltersMxbaiOmniCoreVectorStoreModelsSearchFilter1None: TypeAlias = Union[SearchFilterCondition, object]


class FiltersMxbaiOmniCoreVectorStoreModelsSearchFilter1(TypedDict, total=False):
    all: Optional[Iterable[FiltersMxbaiOmniCoreVectorStoreModelsSearchFilter1All]]
    """List of conditions or filters to be ANDed together"""

    any: Optional[Iterable[FiltersMxbaiOmniCoreVectorStoreModelsSearchFilter1Any]]
    """List of conditions or filters to be ORed together"""

    none: Optional[Iterable[FiltersMxbaiOmniCoreVectorStoreModelsSearchFilter1None]]
    """List of conditions or filters to be NOTed"""


FiltersUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter1All: TypeAlias = Union[SearchFilterCondition, object]

FiltersUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter1Any: TypeAlias = Union[SearchFilterCondition, object]

FiltersUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter1None: TypeAlias = Union[SearchFilterCondition, object]


class FiltersUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter1(TypedDict, total=False):
    all: Optional[Iterable[FiltersUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter1All]]
    """List of conditions or filters to be ANDed together"""

    any: Optional[Iterable[FiltersUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter1Any]]
    """List of conditions or filters to be ORed together"""

    none: Optional[Iterable[FiltersUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter1None]]
    """List of conditions or filters to be NOTed"""


FiltersUnionMember2: TypeAlias = Union[
    FiltersUnionMember2MxbaiOmniCoreVectorStoreModelsSearchFilter1, SearchFilterCondition
]

Filters: TypeAlias = Union[
    FiltersMxbaiOmniCoreVectorStoreModelsSearchFilter1, SearchFilterCondition, Iterable[FiltersUnionMember2]
]


class QaOptions(TypedDict, total=False):
    cite: bool
    """Whether to use citations"""

    multimodal: bool
    """Whether to use multimodal context"""
