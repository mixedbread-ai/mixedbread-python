# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SearchFilterCondition"]


class SearchFilterCondition(TypedDict, total=False):
    key: Required[str]
    """The field to apply the condition on"""

    value: Required[object]
    """The value to compare against"""

    operator: Required[
        Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "starts_with", "not_like"]
    ]
    """The operator for the condition"""
