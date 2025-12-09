# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .store_file_status import StoreFileStatus
from ..scored_text_input_chunk import ScoredTextInputChunk
from ..scored_audio_url_input_chunk import ScoredAudioURLInputChunk
from ..scored_image_url_input_chunk import ScoredImageURLInputChunk
from ..scored_video_url_input_chunk import ScoredVideoURLInputChunk

__all__ = ["ScoredStoreFile", "Config", "Chunk"]


class Config(BaseModel):
    """Configuration for a file."""

    parsing_strategy: Optional[Literal["fast", "high_quality"]] = None
    """Strategy for adding the file, this overrides the store-level default"""


Chunk: TypeAlias = Annotated[
    Union[ScoredTextInputChunk, ScoredImageURLInputChunk, ScoredAudioURLInputChunk, ScoredVideoURLInputChunk],
    PropertyInfo(discriminator="type"),
]


class ScoredStoreFile(BaseModel):
    """Represents a scored store file."""

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

    config: Optional[Config] = None
    """Configuration for a file."""

    object: Optional[Literal["store.file"]] = None
    """Type of the object"""

    chunks: Optional[List[Chunk]] = None
    """Array of scored file chunks"""

    score: float
    """score of the file"""
