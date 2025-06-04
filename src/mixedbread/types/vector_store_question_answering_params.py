# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import TypeAlias, TypedDict

from .shared_params.search_filter_condition import SearchFilterCondition
from .vector_store_chunk_search_options_param import VectorStoreChunkSearchOptionsParam

__all__ = ["VectorStoreQuestionAnsweringParams", "Filters", "FiltersUnionMember2", "QaOptions"]


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


FiltersUnionMember2: TypeAlias = Union["SearchFilter", SearchFilterCondition]

Filters: TypeAlias = Union["SearchFilter", SearchFilterCondition, Iterable[FiltersUnionMember2]]


class QaOptions(TypedDict, total=False):
    cite: bool
    """Whether to use citations"""

    multimodal: bool
    """Whether to use multimodal context"""


from .shared_params.search_filter import SearchFilter
