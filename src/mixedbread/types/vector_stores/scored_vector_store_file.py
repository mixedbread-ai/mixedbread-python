# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "ScoredVectorStoreFile",
    "Chunk",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunk",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunk",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkImageURL",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunk",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkAudioURL",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunk",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkVideoURL",
]


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunk(BaseModel):
    chunk_index: int
    """position of the chunk in a file"""

    mime_type: Optional[str] = None
    """mime type of the chunk"""

    generated_metadata: Optional[Dict[str, object]] = None
    """metadata of the chunk"""

    model: Optional[str] = None
    """model used for this chunk"""

    score: float
    """score of the chunk"""

    file_id: str
    """file id"""

    filename: str
    """filename"""

    vector_store_id: str
    """store id"""

    metadata: Optional[object] = None
    """file metadata"""

    type: Optional[Literal["text"]] = None
    """Input type identifier"""

    offset: Optional[int] = None
    """The offset of the text in the file relative to the start of the file."""

    text: str
    """Text content to process"""


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkImageURL(BaseModel):
    url: str
    """The image URL. Can be either a URL or a Data URI."""

    format: Optional[str] = None
    """The image format/mimetype"""


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunk(BaseModel):
    chunk_index: int
    """position of the chunk in a file"""

    mime_type: Optional[str] = None
    """mime type of the chunk"""

    generated_metadata: Optional[Dict[str, object]] = None
    """metadata of the chunk"""

    model: Optional[str] = None
    """model used for this chunk"""

    score: float
    """score of the chunk"""

    file_id: str
    """file id"""

    filename: str
    """filename"""

    vector_store_id: str
    """store id"""

    metadata: Optional[object] = None
    """file metadata"""

    type: Optional[Literal["image_url"]] = None
    """Input type identifier"""

    ocr_text: Optional[str] = None
    """ocr text of the image"""

    summary: Optional[str] = None
    """summary of the image"""

    image_url: ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkImageURL
    """The image input specification."""


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkAudioURL(BaseModel):
    url: str
    """The audio URL. Can be either a URL or a Data URI."""


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunk(BaseModel):
    chunk_index: int
    """position of the chunk in a file"""

    mime_type: Optional[str] = None
    """mime type of the chunk"""

    generated_metadata: Optional[Dict[str, object]] = None
    """metadata of the chunk"""

    model: Optional[str] = None
    """model used for this chunk"""

    score: float
    """score of the chunk"""

    file_id: str
    """file id"""

    filename: str
    """filename"""

    vector_store_id: str
    """store id"""

    metadata: Optional[object] = None
    """file metadata"""

    type: Optional[Literal["audio_url"]] = None
    """Input type identifier"""

    transcription: Optional[str] = None
    """speech recognition (sr) text of the audio"""

    summary: Optional[str] = None
    """summary of the audio"""

    audio_url: ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkAudioURL
    """The audio input specification."""

    sampling_rate: int
    """The sampling rate of the audio."""


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkVideoURL(BaseModel):
    url: str
    """The video URL. Can be either a URL or a Data URI."""


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunk(BaseModel):
    chunk_index: int
    """position of the chunk in a file"""

    mime_type: Optional[str] = None
    """mime type of the chunk"""

    generated_metadata: Optional[Dict[str, object]] = None
    """metadata of the chunk"""

    model: Optional[str] = None
    """model used for this chunk"""

    score: float
    """score of the chunk"""

    file_id: str
    """file id"""

    filename: str
    """filename"""

    vector_store_id: str
    """store id"""

    metadata: Optional[object] = None
    """file metadata"""

    type: Optional[Literal["video_url"]] = None
    """Input type identifier"""

    transcription: Optional[str] = None
    """speech recognition (sr) text of the video"""

    summary: Optional[str] = None
    """summary of the video"""

    video_url: ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkVideoURL
    """The video input specification."""


Chunk: TypeAlias = Annotated[
    Union[
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunk,
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunk,
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunk,
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunk,
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

    status: Optional[Literal["pending", "in_progress", "cancelled", "completed", "failed"]] = None
    """Processing status of the file"""

    last_error: Optional[object] = None
    """Last error message if processing failed"""

    vector_store_id: str
    """ID of the containing store"""

    created_at: datetime
    """Timestamp of store file creation"""

    version: Optional[int] = None
    """Version number of the file"""

    usage_bytes: Optional[int] = None
    """Storage usage in bytes"""

    object: Optional[Literal["vector_store.file"]] = None
    """Type of the object"""

    chunks: Optional[List[Chunk]] = None
    """Array of scored file chunks"""

    score: float
    """score of the file"""
