# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["APIKeyCreateOrUpdateParams"]


class APIKeyCreateOrUpdateParams(TypedDict, total=False):
    """Base class for API key create or update parameters."""

    type: Literal["api_key"]

    api_key: Required[str]
    """The API key"""
