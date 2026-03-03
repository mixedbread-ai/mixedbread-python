# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MultipartUploadPartParam"]


class MultipartUploadPartParam(TypedDict, total=False):
    part_number: Required[int]
    """1-based part number"""

    etag: Required[str]
    """ETag returned by the storage backend after uploading the part"""
