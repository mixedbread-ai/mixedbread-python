# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SearchFilterCondition"]


class SearchFilterCondition(BaseModel):
    key: str
    """The field to apply the condition on"""

    value: object
    """The value to compare against"""

    operator: Literal["eq", "not_eq", "gt", "gte", "lt", "lte", "in", "not_in", "like", "not_like"]
    """The operator for the condition"""
