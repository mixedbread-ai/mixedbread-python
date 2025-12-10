# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SearchFilterCondition"]


class SearchFilterCondition(BaseModel):
    """Represents a condition with a field, operator, and value."""

    key: str
    """The field to apply the condition on"""

    value: object
    """The value to compare against"""

    operator: Literal[
        "eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "starts_with", "not_like", "regex"
    ]
    """The operator for the condition"""
