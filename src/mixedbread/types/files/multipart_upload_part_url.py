# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["MultipartUploadPartURL"]


class MultipartUploadPartURL(BaseModel):
    part_number: int
    """1-based part number"""

    url: str
    """Presigned URL for uploading this part"""
