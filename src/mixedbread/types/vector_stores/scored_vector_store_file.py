# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from ..scored_video_url_input_chunk import ScoredVideoURLInputChunk

__all__ = [
    "ScoredVectorStoreFile",
    "Chunk",
    "ChunkScoredTextInputChunk",
    "ChunkScoredImageURLInputChunk",
    "ChunkScoredImageURLInputChunkImageURL",
    "ChunkScoredAudioURLInputChunk",
    "ChunkScoredAudioURLInputChunkAudioURL",
]


class ChunkScoredTextInputChunk(BaseModel):
    chunk_index: int
    """position of the chunk in a file"""

    mime_type: Optional[str] = None
    """mime type of the chunk"""

    model: Optional[str] = None
    """model used for this chunk"""

    score: float
    """score of the chunk"""

    file_id: str
    """file id"""

    filename: str
    """filename"""

    vector_store_id: str
    """vector store id"""

    metadata: Optional[object] = None
    """file metadata"""

    type: Optional[Literal["text"]] = None
    """Input type identifier"""

    text: str
    """Text content to process"""


class ChunkScoredImageURLInputChunkImageURL(BaseModel):
    url: str
    """The image URL. Can be either a URL or a Data URI."""


class ChunkScoredImageURLInputChunk(BaseModel):
    chunk_index: int
    """position of the chunk in a file"""

    mime_type: Optional[str] = None
    """mime type of the chunk"""

    model: Optional[str] = None
    """model used for this chunk"""

    score: float
    """score of the chunk"""

    file_id: str
    """file id"""

    filename: str
    """filename"""

    vector_store_id: str
    """vector store id"""

    metadata: Optional[object] = None
    """file metadata"""

    type: Optional[Literal["image_url"]] = None
    """Input type identifier"""

    image_url: ChunkScoredImageURLInputChunkImageURL
    """The image input specification."""

    ocr_text: Optional[str] = None
    """ocr text of the image"""

    summary: Optional[str] = None
    """summary of the image"""


class ChunkScoredAudioURLInputChunkAudioURL(BaseModel):
    url: str
    """The audio URL. Can be either a URL or a Data URI."""


class ChunkScoredAudioURLInputChunk(BaseModel):
    chunk_index: int
    """position of the chunk in a file"""

    mime_type: Optional[str] = None
    """mime type of the chunk"""

    model: Optional[str] = None
    """model used for this chunk"""

    score: float
    """score of the chunk"""

    file_id: str
    """file id"""

    filename: str
    """filename"""

    vector_store_id: str
    """vector store id"""

    metadata: Optional[object] = None
    """file metadata"""

    type: Optional[Literal["audio_url"]] = None
    """Input type identifier"""

    audio_url: ChunkScoredAudioURLInputChunkAudioURL
    """The audio input specification."""

    transcription: Optional[str] = None
    """speech recognition (sr) text of the audio"""

    summary: Optional[str] = None
    """summary of the audio"""


Chunk: TypeAlias = Annotated[
    Union[
        ChunkScoredTextInputChunk,
        ChunkScoredImageURLInputChunk,
        ChunkScoredAudioURLInputChunk,
        ScoredVideoURLInputChunk,
    ],
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
