# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .video_url import VideoURL
from .pdf_chunk_generated_metadata import PdfChunkGeneratedMetadata
from .code_chunk_generated_metadata import CodeChunkGeneratedMetadata
from .text_chunk_generated_metadata import TextChunkGeneratedMetadata
from .audio_chunk_generated_metadata import AudioChunkGeneratedMetadata
from .image_chunk_generated_metadata import ImageChunkGeneratedMetadata
from .video_chunk_generated_metadata import VideoChunkGeneratedMetadata
from .markdown_chunk_generated_metadata import MarkdownChunkGeneratedMetadata

__all__ = ["ScoredVideoURLInputChunk", "GeneratedMetadata"]

GeneratedMetadata: TypeAlias = Annotated[
    Union[
        MarkdownChunkGeneratedMetadata,
        TextChunkGeneratedMetadata,
        PdfChunkGeneratedMetadata,
        CodeChunkGeneratedMetadata,
        AudioChunkGeneratedMetadata,
        VideoChunkGeneratedMetadata,
        ImageChunkGeneratedMetadata,
        None,
    ],
    PropertyInfo(discriminator="type"),
]


class ScoredVideoURLInputChunk(BaseModel):
    chunk_index: int
    """position of the chunk in a file"""

    mime_type: Optional[str] = None
    """mime type of the chunk"""

    generated_metadata: Optional[GeneratedMetadata] = None
    """metadata of the chunk"""

    model: Optional[str] = None
    """model used for this chunk"""

    score: float
    """score of the chunk"""

    file_id: str
    """file id"""

    filename: str
    """filename"""

    store_id: str
    """store id"""

    external_id: Optional[str] = None
    """external identifier for this file"""

    metadata: Optional[object] = None
    """file metadata"""

    type: Optional[Literal["video_url"]] = None
    """Input type identifier"""

    transcription: Optional[str] = None
    """speech recognition (sr) text of the video"""

    summary: Optional[str] = None
    """summary of the video"""

    video_url: Optional[VideoURL] = None
    """Model for video URL validation."""
