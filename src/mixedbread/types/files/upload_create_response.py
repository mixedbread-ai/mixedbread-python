# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .multipart_upload_part_url import MultipartUploadPartURL

__all__ = ["UploadCreateResponse"]


class UploadCreateResponse(BaseModel):
    id: str
    """The multipart upload ID (use this to complete or abort)"""

    part_urls: List[MultipartUploadPartURL]
    """Presigned URLs for uploading parts"""
