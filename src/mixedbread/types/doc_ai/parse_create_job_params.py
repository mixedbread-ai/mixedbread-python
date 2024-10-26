# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["ParseCreateJobParams"]


class ParseCreateJobParams(TypedDict, total=False):
    file: Required[FileTypes]
    """The file to parse information from"""
