# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["StoreFileConfigParam"]


class StoreFileConfigParam(TypedDict, total=False):
    """Configuration for a file."""

    parsing_strategy: Literal["fast", "high_quality"]
    """Strategy for adding the file, this overrides the store-level default"""
