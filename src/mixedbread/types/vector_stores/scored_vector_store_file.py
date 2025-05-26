# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from ..scored_text_input_chunk import ScoredTextInputChunk
from ..scored_audio_url_input_chunk import ScoredAudioURLInputChunk
from ..scored_image_url_input_chunk import ScoredImageURLInputChunk
from ..scored_video_url_input_chunk import ScoredVideoURLInputChunk

__all__ = ["ScoredVectorStoreFile", "Chunk"]

Chunk: TypeAlias = Annotated[
    Union[ScoredTextInputChunk, ScoredImageURLInputChunk, ScoredAudioURLInputChunk, ScoredVideoURLInputChunk],
    PropertyInfo(discriminator="type"),
]


class ScoredVectorStoreFile(BaseModel):
    id: str
    """Unique identifier for the file"""

    filename: Optional[str] = None
    """Name of the file"""

    metadata: Optional[object] = None
    """Optional file metadata"""

    status: Optional[str] = None
    """Processing status of the file"""

    last_error: Optional[object] = None
    """Last error message if processing failed"""

    vector_store_id: str
    """ID of the containing vector store"""

    created_at: datetime
    """Timestamp of vector store file creation"""

    version: Optional[int] = None
    """Version number of the file"""

    usage_bytes: Optional[int] = None
    """Storage usage in bytes"""

    object: Optional[Literal["vector_store.file"]] = None
    """Type of the object"""

    score: float
    """score of the file"""

    chunks: Optional[List[Chunk]] = None
    """chunks"""
