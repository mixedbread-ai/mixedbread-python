# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AgenticSearchConfigParam"]


class AgenticSearchConfigParam(TypedDict, total=False):
    """Configuration for agentic multi-query search."""

    max_rounds: int
    """Maximum number of search rounds"""

    queries_per_round: int
    """Maximum queries per round"""

    strict_top_k: bool
    """
    Whether to enforce top_k by truncating agent rankings and backfilling short
    rankings
    """

    multimodal: bool
    """Whether to provide image content to the agent when image URLs are available"""

    instructions: Optional[str]
    """
    Additional custom instructions (followed only when not in conflict with existing
    rules)
    """
