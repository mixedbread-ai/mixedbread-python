# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ExtractContentParams"]


class ExtractContentParams(TypedDict, total=False):
    content: Required[str]
    """The text content to extract structured data from"""

    json_schema: Required[object]
    """The schema definition to use for extraction"""
