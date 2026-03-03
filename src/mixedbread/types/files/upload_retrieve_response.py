# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .multipart_upload_part import MultipartUploadPart
from .multipart_upload_part_url import MultipartUploadPartURL

__all__ = ["UploadRetrieveResponse"]


class UploadRetrieveResponse(BaseModel):
    id: str
    """The multipart upload record ID"""

    filename: str
    """Original filename"""

    file_size: int
    """Total file size in bytes"""

    mime_type: str
    """MIME type of the file"""

    part_count: int
    """Number of parts the file was split into"""

    created_at: str
    """When the upload was initiated"""

    completed_parts: List[MultipartUploadPart]
    """Parts that have already been uploaded"""

    part_urls: List[MultipartUploadPartURL]
    """Presigned URLs for the parts that still need to be uploaded"""
