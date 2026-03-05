# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["MultipartUploadPart"]


class MultipartUploadPart(BaseModel):
    part_number: int
    """1-based part number"""

    etag: str
    """ETag returned by the storage backend after uploading the part"""
