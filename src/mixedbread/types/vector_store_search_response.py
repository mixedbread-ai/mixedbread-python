# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .scored_video_url_input_chunk import ScoredVideoURLInputChunk

__all__ = [
    "VectorStoreSearchResponse",
    "Data",
    "DataScoredTextInputChunk",
    "DataScoredImageURLInputChunk",
    "DataScoredImageURLInputChunkImageURL",
    "DataScoredAudioURLInputChunk",
    "DataScoredAudioURLInputChunkAudioURL",
]


class DataScoredTextInputChunk(BaseModel):
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


class DataScoredImageURLInputChunkImageURL(BaseModel):
    url: str
    """The image URL. Can be either a URL or a Data URI."""


class DataScoredImageURLInputChunk(BaseModel):
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

    image_url: DataScoredImageURLInputChunkImageURL
    """The image input specification."""

    ocr_text: Optional[str] = None
    """ocr text of the image"""

    summary: Optional[str] = None
    """summary of the image"""


class DataScoredAudioURLInputChunkAudioURL(BaseModel):
    url: str
    """The audio URL. Can be either a URL or a Data URI."""


class DataScoredAudioURLInputChunk(BaseModel):
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

    audio_url: DataScoredAudioURLInputChunkAudioURL
    """The audio input specification."""

    transcription: Optional[str] = None
    """speech recognition (sr) text of the audio"""

    summary: Optional[str] = None
    """summary of the audio"""


Data: TypeAlias = Annotated[
    Union[
        DataScoredTextInputChunk, DataScoredImageURLInputChunk, DataScoredAudioURLInputChunk, ScoredVideoURLInputChunk
    ],
    PropertyInfo(discriminator="type"),
]


class VectorStoreSearchResponse(BaseModel):
    object: Optional[Literal["list"]] = None
    """The object type of the response"""

    data: List[Data]
    """The list of scored vector store file chunks"""
