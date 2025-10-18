# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["APIKeyCreateParams", "Scope"]


class APIKeyCreateParams(TypedDict, total=False):
    name: str
    """A name/description for the API key"""

    scope: Optional[Iterable[Scope]]
    """The scope of the API key"""

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Optional expiration datetime"""


class Scope(TypedDict, total=False):
    method: Required[Literal["read", "write", "delete", "list", "create"]]

    resource_type: Optional[Literal["store"]]

    resource_id: Optional[str]
