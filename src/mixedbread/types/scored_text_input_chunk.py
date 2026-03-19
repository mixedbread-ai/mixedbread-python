# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "ScoredTextInputChunk",
    "GeneratedMetadata",
    "GeneratedMetadataMarkdownChunkGeneratedMetadata",
    "GeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading",
    "GeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext",
    "GeneratedMetadataTextChunkGeneratedMetadata",
    "GeneratedMetadataPdfChunkGeneratedMetadata",
    "GeneratedMetadataCodeChunkGeneratedMetadata",
    "GeneratedMetadataAudioChunkGeneratedMetadata",
    "GeneratedMetadataVideoChunkGeneratedMetadata",
    "GeneratedMetadataImageChunkGeneratedMetadata",
]


class GeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading(BaseModel):
    level: int

    text: str


class GeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext(BaseModel):
    level: int

    text: str


class GeneratedMetadataMarkdownChunkGeneratedMetadata(BaseModel):
    type: Optional[Literal["markdown"]] = None

    file_type: Optional[Literal["text/markdown"]] = None

    language: Optional[str] = None

    word_count: Optional[int] = None

    file_size: Optional[int] = None

    chunk_headings: Optional[List[GeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading]] = None

    heading_context: Optional[List[GeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext]] = None

    start_line: Optional[int] = None

    num_lines: Optional[int] = None

    file_extension: Optional[str] = None

    frontmatter: Optional[Dict[str, object]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class GeneratedMetadataTextChunkGeneratedMetadata(BaseModel):
    type: Optional[Literal["text"]] = None

    file_type: Optional[Literal["text/plain"]] = None

    language: Optional[str] = None

    word_count: Optional[int] = None

    file_size: Optional[int] = None

    start_line: Optional[int] = None

    num_lines: Optional[int] = None

    file_extension: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class GeneratedMetadataPdfChunkGeneratedMetadata(BaseModel):
    type: Optional[Literal["pdf"]] = None

    file_type: Optional[Literal["application/pdf"]] = None

    total_pages: Optional[int] = None

    total_size: Optional[int] = None

    file_extension: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class GeneratedMetadataCodeChunkGeneratedMetadata(BaseModel):
    type: Optional[Literal["code"]] = None

    file_type: str

    language: Optional[str] = None

    word_count: Optional[int] = None

    file_size: Optional[int] = None

    start_line: Optional[int] = None

    num_lines: Optional[int] = None

    file_extension: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class GeneratedMetadataAudioChunkGeneratedMetadata(BaseModel):
    type: Optional[Literal["audio"]] = None

    file_type: Optional[str] = None

    file_size: Optional[int] = None

    total_duration_seconds: Optional[float] = None

    sample_rate: Optional[int] = None

    channels: Optional[int] = None

    audio_format: Optional[int] = None

    bpm: Optional[int] = None

    file_extension: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class GeneratedMetadataVideoChunkGeneratedMetadata(BaseModel):
    type: Optional[Literal["video"]] = None

    file_type: Optional[str] = None

    file_size: Optional[int] = None

    total_duration_seconds: Optional[float] = None

    fps: Optional[float] = None

    width: Optional[int] = None

    height: Optional[int] = None

    frame_count: Optional[int] = None

    has_audio_stream: Optional[bool] = None

    bpm: Optional[int] = None

    file_extension: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class GeneratedMetadataImageChunkGeneratedMetadata(BaseModel):
    type: Optional[Literal["image"]] = None

    file_type: Optional[str] = None

    file_size: Optional[int] = None

    width: Optional[int] = None

    height: Optional[int] = None

    file_extension: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


GeneratedMetadata: TypeAlias = Annotated[
    Union[
        GeneratedMetadataMarkdownChunkGeneratedMetadata,
        GeneratedMetadataTextChunkGeneratedMetadata,
        GeneratedMetadataPdfChunkGeneratedMetadata,
        GeneratedMetadataCodeChunkGeneratedMetadata,
        GeneratedMetadataAudioChunkGeneratedMetadata,
        GeneratedMetadataVideoChunkGeneratedMetadata,
        GeneratedMetadataImageChunkGeneratedMetadata,
        None,
    ],
    PropertyInfo(discriminator="type"),
]


class ScoredTextInputChunk(BaseModel):
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

    type: Optional[Literal["text"]] = None
    """Input type identifier"""

    offset: Optional[int] = None
    """The offset of the text in the file relative to the start of the file."""

    text: Optional[str] = None
    """Text content"""
