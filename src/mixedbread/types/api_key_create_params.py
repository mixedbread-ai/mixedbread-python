# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["APIKeyCreateParams"]


class APIKeyCreateParams(TypedDict, total=False):
    name: str
    """A name/description for the API key"""

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Optional expiration datetime"""
