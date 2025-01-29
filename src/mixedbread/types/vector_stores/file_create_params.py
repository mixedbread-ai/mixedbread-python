# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FileCreateParams", "Experimental"]


class FileCreateParams(TypedDict, total=False):
    file_id: Required[str]
    """ID of the file to add"""

    experimental: Experimental
    """Strategy for adding the file"""

    metadata: object
    """Optional metadata for the file"""


class Experimental(TypedDict, total=False):
    parsing_strategy: Literal["fast", "high_quality"]
    """Strategy for adding the file"""
