# File generated from our OpenAPI spec by sdkgen. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared_params.search_filter import SearchFilter
from .shared_params.search_filter_condition import SearchFilterCondition

__all__ = ["StoreGrepParams", "Filters", "FiltersUnionMember2"]


class StoreGrepParams(TypedDict, total=False):
    x_mxbai_tool_ticket: Annotated[str, PropertyInfo(alias="X-Mxbai-Tool-Ticket")]
    """
    Ticket from a chat completion's `tool_tickets`, proving this call runs a tool
    call that completion asked for. Redeems once, and bills the operation at the
    discounted agent rate.
    """

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


FiltersUnionMember2: TypeAlias = Union[SearchFilter, SearchFilterCondition]

Filters: TypeAlias = Union[SearchFilter, SearchFilterCondition, Iterable[FiltersUnionMember2]]
