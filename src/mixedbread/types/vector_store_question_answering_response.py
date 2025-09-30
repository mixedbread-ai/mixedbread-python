# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "VectorStoreQuestionAnsweringResponse",
    "Source",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunk",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunk",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkImageURL",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunk",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkAudioURL",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunk",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkVideoURL",
]


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunk(BaseModel):
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


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkImageURL(BaseModel):
    url: str
    """The image URL. Can be either a URL or a Data URI."""

    format: Optional[str] = None
    """The image format/mimetype"""


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunk(BaseModel):
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

    image_url: SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkImageURL
    """The image input specification."""


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkAudioURL(BaseModel):
    url: str
    """The audio URL. Can be either a URL or a Data URI."""


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunk(BaseModel):
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

    audio_url: SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkAudioURL
    """The audio input specification."""

    sampling_rate: int
    """The sampling rate of the audio."""


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkVideoURL(BaseModel):
    url: str
    """The video URL. Can be either a URL or a Data URI."""


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunk(BaseModel):
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

    video_url: SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkVideoURL
    """The video input specification."""


Source: TypeAlias = Annotated[
    Union[
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunk,
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunk,
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunk,
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunk,
    ],
    PropertyInfo(discriminator="type"),
]


class VectorStoreQuestionAnsweringResponse(BaseModel):
    answer: str
    """The answer generated by the LLM"""

    sources: Optional[List[Source]] = None
    """Source documents used to generate the answer"""
