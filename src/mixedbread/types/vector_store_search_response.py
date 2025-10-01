# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "VectorStoreSearchResponse",
    "Data",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunk",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunk",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkImageURL",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunk",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkAudioURL",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunk",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkVideoURL",
]


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunk(BaseModel):
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


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkImageURL(BaseModel):
    url: str
    """The image URL. Can be either a URL or a Data URI."""

    format: Optional[str] = None
    """The image format/mimetype"""


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunk(BaseModel):
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

    image_url: DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkImageURL
    """The image input specification."""


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkAudioURL(BaseModel):
    url: str
    """The audio URL. Can be either a URL or a Data URI."""


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunk(BaseModel):
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

    audio_url: DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkAudioURL
    """The audio input specification."""

    sampling_rate: int
    """The sampling rate of the audio."""


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkVideoURL(BaseModel):
    url: str
    """The video URL. Can be either a URL or a Data URI."""


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunk(BaseModel):
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

    video_url: DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkVideoURL
    """The video input specification."""


Data: TypeAlias = Annotated[
    Union[
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunk,
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunk,
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunk,
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunk,
    ],
    PropertyInfo(discriminator="type"),
]


class VectorStoreSearchResponse(BaseModel):
    object: Optional[Literal["list"]] = None
    """The object type of the response"""

    data: List[Data]
    """The list of scored vector store file chunks"""
