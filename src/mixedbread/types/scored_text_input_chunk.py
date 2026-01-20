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

    language: str

    word_count: int

    file_size: int

    chunk_headings: Optional[List[GeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading]] = None

    heading_context: Optional[List[GeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext]] = None

    start_line: Optional[int] = None

    num_lines: Optional[int] = None

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

    language: str

    word_count: int

    file_size: int

    start_line: Optional[int] = None

    num_lines: Optional[int] = None

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

    total_pages: int

    total_size: int

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

    language: str

    word_count: int

    file_size: int

    start_line: Optional[int] = None

    num_lines: Optional[int] = None

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

    file_type: str

    file_size: int

    total_duration_seconds: float

    sample_rate: int

    channels: int

    audio_format: int

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

    metadata: Optional[object] = None
    """file metadata"""

    type: Optional[Literal["text"]] = None
    """Input type identifier"""

    offset: Optional[int] = None
    """The offset of the text in the file relative to the start of the file."""

    text: Optional[str] = None
    """Text content"""
