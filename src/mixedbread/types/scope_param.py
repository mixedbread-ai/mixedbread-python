# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ScopeParam"]


class ScopeParam(TypedDict, total=False):
    method: Required[Literal["read", "write", "delete", "list", "create", "search"]]

    resource_type: Optional[Literal["store"]]

    resource_id: Optional[str]
