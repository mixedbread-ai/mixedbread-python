# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["FileCreateParams"]


class FileCreateParams(TypedDict, total=False):
    file_id: Required[str]
    """ID of the file to add"""

    metadata: Optional[object]
    """Optional metadata for the file"""
