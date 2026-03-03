# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .multipart_upload_part_param import MultipartUploadPartParam

__all__ = ["UploadCompleteParams"]


class UploadCompleteParams(TypedDict, total=False):
    parts: Required[Iterable[MultipartUploadPartParam]]
    """List of completed parts with their ETags"""
