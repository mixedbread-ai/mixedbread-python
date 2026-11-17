# File generated from our OpenAPI spec by sdkgen. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared_params.search_filter import SearchFilter
from .extractions.text_input_param import TextInputParam
from .store_chunk_search_options_param import StoreChunkSearchOptionsParam
from .extractions.image_url_input_param import ImageURLInputParam
from .shared_params.search_filter_condition import SearchFilterCondition

__all__ = ["StoreSearchParams", "Filters", "FiltersUnionMember2", "Query"]


class StoreSearchParams(TypedDict, total=False):
    x_mxbai_tool_ticket: Annotated[str, PropertyInfo(alias="X-Mxbai-Tool-Ticket")]
    """
    Ticket from a chat completion's `tool_tickets`, proving this call runs a tool
    call that completion asked for. Redeems once, and bills the operation at the
    discounted agent rate.
    """

    store_identifiers: Required[SequenceNotStr[str]]
    """IDs or names of stores"""

    filters: Optional[Filters]
    """Optional filter conditions"""

    file_ids: Union[Iterable[object], SequenceNotStr[str], None]
    """Optional list of file IDs to filter chunks by (inclusion filter)"""

    query: Required[Query]
    """Search query text"""

    top_k: Optional[int]
    """Maximum number of results to return.

    When omitted or null, agentic search returns all chunks selected by the agent
    without a final-result cap; non-agentic search returns up to 10. Required when
    strict_top_k is true.
    """

    search_options: StoreChunkSearchOptionsParam
    """Search configuration options"""

    stream: bool
    """
    When true, return the search as a server-sent event stream: live agentic-search
    trace events when the search is agentic, and nothing before the results
    otherwise. A successful stream ends with a search.completed event containing the
    final search response, followed by [DONE].
    """


FiltersUnionMember2: TypeAlias = Union[SearchFilter, SearchFilterCondition]

Filters: TypeAlias = Union[SearchFilter, SearchFilterCondition, Iterable[FiltersUnionMember2]]

Query: TypeAlias = Union[str, ImageURLInputParam, TextInputParam]
