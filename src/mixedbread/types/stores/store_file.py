# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .text_input_chunk import TextInputChunk
from .store_file_config import StoreFileConfig
from .store_file_status import StoreFileStatus
from .audio_url_input_chunk import AudioURLInputChunk
from .image_url_input_chunk import ImageURLInputChunk
from .video_url_input_chunk import VideoURLInputChunk

__all__ = ["StoreFile", "Chunk"]

Chunk: TypeAlias = Annotated[
    Union[TextInputChunk, ImageURLInputChunk, AudioURLInputChunk, VideoURLInputChunk],
    PropertyInfo(discriminator="type"),
]


class StoreFile(BaseModel):
    """Represents a file stored in a store."""

    id: str
    """Unique identifier for the file"""

    filename: Optional[str] = None
    """Name of the file"""

    metadata: Optional[object] = None
    """Optional file metadata"""

    external_id: Optional[str] = None
    """External identifier for this file in the store"""

    status: Optional[StoreFileStatus] = None
    """Processing status of the file"""

    last_error: Optional[object] = None
    """Last error message if processing failed"""

    store_id: str
    """ID of the containing store"""

    created_at: datetime
    """Timestamp of store file creation"""

    version: Optional[int] = None
    """Version number of the file"""

    usage_bytes: Optional[int] = None
    """Storage usage in bytes"""

    usage_tokens: Optional[int] = None
    """Storage usage in tokens"""

    config: Optional[StoreFileConfig] = None
    """Configuration for a file."""

    object: Optional[Literal["store.file"]] = None
    """Type of the object"""

    chunks: Optional[List[Chunk]] = None
    """chunks"""

    content_url: str
    """Presigned URL for file content"""
