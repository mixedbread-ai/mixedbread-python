# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ExtractCreateJobParams"]


class ExtractCreateJobParams(TypedDict, total=False):
    file_id: Required[str]
    """The file ID to extract data from"""

    json_schema: Required[object]
    """The schema definition to use for extraction"""
