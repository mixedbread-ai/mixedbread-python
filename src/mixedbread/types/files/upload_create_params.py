# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UploadCreateParams"]


class UploadCreateParams(TypedDict, total=False):
    filename: Required[str]
    """Name of the file including extension"""

    file_size: Required[int]
    """Total size of the file in bytes"""

    mime_type: Required[str]
    """MIME type of the file"""

    part_count: int
    """Number of parts to split the upload into"""
