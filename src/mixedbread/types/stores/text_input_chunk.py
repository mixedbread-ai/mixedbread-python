# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from ..pdf_chunk_generated_metadata import PdfChunkGeneratedMetadata
from ..code_chunk_generated_metadata import CodeChunkGeneratedMetadata
from ..text_chunk_generated_metadata import TextChunkGeneratedMetadata
from ..audio_chunk_generated_metadata import AudioChunkGeneratedMetadata
from ..image_chunk_generated_metadata import ImageChunkGeneratedMetadata
from ..video_chunk_generated_metadata import VideoChunkGeneratedMetadata
from ..markdown_chunk_generated_metadata import MarkdownChunkGeneratedMetadata

__all__ = ["TextInputChunk", "GeneratedMetadata"]

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


class TextInputChunk(BaseModel):
    chunk_index: int
    """position of the chunk in a file"""

    mime_type: Optional[str] = None
    """mime type of the chunk"""

    generated_metadata: Optional[GeneratedMetadata] = None
    """metadata of the chunk"""

    model: Optional[str] = None
    """model used for this chunk"""

    type: Optional[Literal["text"]] = None
    """Input type identifier"""

    offset: Optional[int] = None
    """The offset of the text in the file relative to the start of the file."""

    text: Optional[str] = None
    """Text content"""

    context: Optional[str] = None
    """LLM-generated context that situates this chunk within its source document"""
