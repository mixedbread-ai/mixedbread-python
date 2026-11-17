# File generated from our OpenAPI spec by sdkgen. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SearchDistinctParam"]


class SearchDistinctParam(TypedDict, total=False):
    """Keep at most `per_value` results per value of a field."""

    field: Required[str]
    """
    Field whose values must differ between results, named like a filter key:
    `file_id` for one result per file, `user_id` for a metadata field,
    `generated_metadata.<key>`. Results without the field are always kept. Only
    Wholembed V4 stores support it.
    """

    per_value: int
    """Results kept per field value"""
