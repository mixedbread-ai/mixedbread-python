# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ContentCreateParams"]


class ContentCreateParams(TypedDict, total=False):
    content: Required[str]
    """The content to extract from"""

    json_schema: Required[object]
    """The JSON schema to use for extraction"""
