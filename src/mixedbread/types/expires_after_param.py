# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ExpiresAfterParam"]


class ExpiresAfterParam(TypedDict, total=False):
    anchor: Literal["last_active_at"]
    """Anchor date for the expiration policy"""

    days: int
    """Number of days after which the store expires"""
