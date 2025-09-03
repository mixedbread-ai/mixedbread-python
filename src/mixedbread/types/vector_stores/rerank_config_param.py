# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["RerankConfigParam"]


class RerankConfigParam(TypedDict, total=False):
    model: str
    """The name of the reranking model"""

    with_metadata: Union[bool, SequenceNotStr[str]]
    """Whether to include metadata in the reranked results"""

    top_k: Optional[int]
    """Maximum number of results to return after reranking.

    If None, returns all reranked results.
    """
