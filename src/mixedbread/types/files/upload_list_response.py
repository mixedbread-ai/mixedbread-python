# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["UploadListResponse", "Data"]


class Data(BaseModel):
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


class UploadListResponse(BaseModel):
    data: List[Data]
    """List of in-progress multipart uploads"""
