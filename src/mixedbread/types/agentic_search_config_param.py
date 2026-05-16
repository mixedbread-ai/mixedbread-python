# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["AgenticSearchConfigParam"]


class AgenticSearchConfigParam(TypedDict, total=False):
    """Configuration for agentic multi-query search."""

    max_rounds: int
    """Maximum number of search rounds"""

    queries_per_round: int
    """Maximum queries per round"""

    strict_top_k: bool
    """Whether the final retrieved chunk list must provide exactly top_k ranked chunks"""

    media_content: Literal["auto", "never", "always"]
    """Controls when retrieved image content is provided to the agent.

    `auto` sends images only when no OCR text or summary is available, `never`
    disables image content, and `always` sends image content when available.
    """

    instructions: Optional[str]
    """
    Additional custom instructions (followed only when not in conflict with existing
    rules)
    """

    verbose: bool
    """
    Internal: when set, the response includes a `trace` field with the full
    tool-call timeline. Used by the Mixedbread playground; not part of the
    documented public API.
    """
