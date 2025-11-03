# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FileCreateParams", "Config", "Experimental"]


class FileCreateParams(TypedDict, total=False):
    metadata: object
    """Optional metadata for the file"""

    config: Config
    """Configuration for adding the file"""

    external_id: Optional[str]
    """External identifier for this file in the store"""

    overwrite: bool
    """If true, overwrite an existing file with the same external_id"""

    file_id: Required[str]
    """ID of the file to add"""

    experimental: Optional[Experimental]
    """Configuration for a file."""


class Config(TypedDict, total=False):
    parsing_strategy: Literal["fast", "high_quality"]
    """Strategy for adding the file, this overrides the store-level default"""


class Experimental(TypedDict, total=False):
    parsing_strategy: Literal["fast", "high_quality"]
    """Strategy for adding the file, this overrides the store-level default"""
