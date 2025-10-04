# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel
from ..stores.store_file_status import StoreFileStatus

__all__ = [
    "VectorStoreFile",
    "Chunk",
    "ChunkTextInputChunk",
    "ChunkTextInputChunkGeneratedMetadata",
    "ChunkTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata",
    "ChunkTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading",
    "ChunkTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext",
    "ChunkTextInputChunkGeneratedMetadataTextChunkGeneratedMetadata",
    "ChunkTextInputChunkGeneratedMetadataPdfChunkGeneratedMetadata",
    "ChunkTextInputChunkGeneratedMetadataCodeChunkGeneratedMetadata",
    "ChunkTextInputChunkGeneratedMetadataAudioChunkGeneratedMetadata",
    "ChunkImageURLInputChunk",
    "ChunkImageURLInputChunkGeneratedMetadata",
    "ChunkImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata",
    "ChunkImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading",
    "ChunkImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext",
    "ChunkImageURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata",
    "ChunkImageURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata",
    "ChunkImageURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata",
    "ChunkImageURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata",
    "ChunkImageURLInputChunkImageURL",
    "ChunkAudioURLInputChunk",
    "ChunkAudioURLInputChunkGeneratedMetadata",
    "ChunkAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata",
    "ChunkAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading",
    "ChunkAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext",
    "ChunkAudioURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata",
    "ChunkAudioURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata",
    "ChunkAudioURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata",
    "ChunkAudioURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata",
    "ChunkAudioURLInputChunkAudioURL",
    "ChunkVideoURLInputChunk",
    "ChunkVideoURLInputChunkGeneratedMetadata",
    "ChunkVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata",
    "ChunkVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading",
    "ChunkVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext",
    "ChunkVideoURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata",
    "ChunkVideoURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata",
    "ChunkVideoURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata",
    "ChunkVideoURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata",
    "ChunkVideoURLInputChunkVideoURL",
]


class ChunkTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading(BaseModel):
    level: int

    text: str


class ChunkTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext(BaseModel):
    level: int

    text: str


class ChunkTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata(BaseModel):
    type: Optional[Literal["markdown"]] = None

    file_type: Optional[Literal["text/markdown"]] = None

    language: str

    word_count: int

    file_size: int

    chunk_headings: Optional[List[ChunkTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading]] = (
        None
    )

    heading_context: Optional[
        List[ChunkTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext]
    ] = None

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


class ChunkTextInputChunkGeneratedMetadataTextChunkGeneratedMetadata(BaseModel):
    type: Optional[Literal["text"]] = None

    file_type: Optional[Literal["text/plain"]] = None

    language: str

    word_count: int

    file_size: int

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


class ChunkTextInputChunkGeneratedMetadataPdfChunkGeneratedMetadata(BaseModel):
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


class ChunkTextInputChunkGeneratedMetadataCodeChunkGeneratedMetadata(BaseModel):
    type: Optional[Literal["code"]] = None

    file_type: str

    language: str

    word_count: int

    file_size: int

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


class ChunkTextInputChunkGeneratedMetadataAudioChunkGeneratedMetadata(BaseModel):
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


ChunkTextInputChunkGeneratedMetadata: TypeAlias = Annotated[
    Union[
        ChunkTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata,
        ChunkTextInputChunkGeneratedMetadataTextChunkGeneratedMetadata,
        ChunkTextInputChunkGeneratedMetadataPdfChunkGeneratedMetadata,
        ChunkTextInputChunkGeneratedMetadataCodeChunkGeneratedMetadata,
        ChunkTextInputChunkGeneratedMetadataAudioChunkGeneratedMetadata,
        None,
    ],
    PropertyInfo(discriminator="type"),
]


class ChunkTextInputChunk(BaseModel):
    chunk_index: int
    """position of the chunk in a file"""

    mime_type: Optional[str] = None
    """mime type of the chunk"""

    generated_metadata: Optional[ChunkTextInputChunkGeneratedMetadata] = None
    """metadata of the chunk"""

    model: Optional[str] = None
    """model used for this chunk"""

    type: Optional[Literal["text"]] = None
    """Input type identifier"""

    offset: Optional[int] = None
    """The offset of the text in the file relative to the start of the file."""

    text: str
    """Text content to process"""


class ChunkImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading(BaseModel):
    level: int

    text: str


class ChunkImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext(BaseModel):
    level: int

    text: str


class ChunkImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata(BaseModel):
    type: Optional[Literal["markdown"]] = None

    file_type: Optional[Literal["text/markdown"]] = None

    language: str

    word_count: int

    file_size: int

    chunk_headings: Optional[
        List[ChunkImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading]
    ] = None

    heading_context: Optional[
        List[ChunkImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext]
    ] = None

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


class ChunkImageURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata(BaseModel):
    type: Optional[Literal["text"]] = None

    file_type: Optional[Literal["text/plain"]] = None

    language: str

    word_count: int

    file_size: int

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


class ChunkImageURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata(BaseModel):
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


class ChunkImageURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata(BaseModel):
    type: Optional[Literal["code"]] = None

    file_type: str

    language: str

    word_count: int

    file_size: int

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


class ChunkImageURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata(BaseModel):
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


ChunkImageURLInputChunkGeneratedMetadata: TypeAlias = Annotated[
    Union[
        ChunkImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata,
        ChunkImageURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata,
        ChunkImageURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata,
        ChunkImageURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata,
        ChunkImageURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata,
        None,
    ],
    PropertyInfo(discriminator="type"),
]


class ChunkImageURLInputChunkImageURL(BaseModel):
    url: str
    """The image URL. Can be either a URL or a Data URI."""

    format: Optional[str] = None
    """The image format/mimetype"""


class ChunkImageURLInputChunk(BaseModel):
    chunk_index: int
    """position of the chunk in a file"""

    mime_type: Optional[str] = None
    """mime type of the chunk"""

    generated_metadata: Optional[ChunkImageURLInputChunkGeneratedMetadata] = None
    """metadata of the chunk"""

    model: Optional[str] = None
    """model used for this chunk"""

    type: Optional[Literal["image_url"]] = None
    """Input type identifier"""

    ocr_text: Optional[str] = None
    """ocr text of the image"""

    summary: Optional[str] = None
    """summary of the image"""

    image_url: ChunkImageURLInputChunkImageURL
    """The image input specification."""


class ChunkAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading(BaseModel):
    level: int

    text: str


class ChunkAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext(BaseModel):
    level: int

    text: str


class ChunkAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata(BaseModel):
    type: Optional[Literal["markdown"]] = None

    file_type: Optional[Literal["text/markdown"]] = None

    language: str

    word_count: int

    file_size: int

    chunk_headings: Optional[
        List[ChunkAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading]
    ] = None

    heading_context: Optional[
        List[ChunkAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext]
    ] = None

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


class ChunkAudioURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata(BaseModel):
    type: Optional[Literal["text"]] = None

    file_type: Optional[Literal["text/plain"]] = None

    language: str

    word_count: int

    file_size: int

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


class ChunkAudioURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata(BaseModel):
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


class ChunkAudioURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata(BaseModel):
    type: Optional[Literal["code"]] = None

    file_type: str

    language: str

    word_count: int

    file_size: int

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


class ChunkAudioURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata(BaseModel):
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


ChunkAudioURLInputChunkGeneratedMetadata: TypeAlias = Annotated[
    Union[
        ChunkAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata,
        ChunkAudioURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata,
        ChunkAudioURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata,
        ChunkAudioURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata,
        ChunkAudioURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata,
        None,
    ],
    PropertyInfo(discriminator="type"),
]


class ChunkAudioURLInputChunkAudioURL(BaseModel):
    url: str
    """The audio URL. Can be either a URL or a Data URI."""


class ChunkAudioURLInputChunk(BaseModel):
    chunk_index: int
    """position of the chunk in a file"""

    mime_type: Optional[str] = None
    """mime type of the chunk"""

    generated_metadata: Optional[ChunkAudioURLInputChunkGeneratedMetadata] = None
    """metadata of the chunk"""

    model: Optional[str] = None
    """model used for this chunk"""

    type: Optional[Literal["audio_url"]] = None
    """Input type identifier"""

    transcription: Optional[str] = None
    """speech recognition (sr) text of the audio"""

    summary: Optional[str] = None
    """summary of the audio"""

    audio_url: ChunkAudioURLInputChunkAudioURL
    """The audio input specification."""

    sampling_rate: int
    """The sampling rate of the audio."""


class ChunkVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading(BaseModel):
    level: int

    text: str


class ChunkVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext(BaseModel):
    level: int

    text: str


class ChunkVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata(BaseModel):
    type: Optional[Literal["markdown"]] = None

    file_type: Optional[Literal["text/markdown"]] = None

    language: str

    word_count: int

    file_size: int

    chunk_headings: Optional[
        List[ChunkVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading]
    ] = None

    heading_context: Optional[
        List[ChunkVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext]
    ] = None

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


class ChunkVideoURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata(BaseModel):
    type: Optional[Literal["text"]] = None

    file_type: Optional[Literal["text/plain"]] = None

    language: str

    word_count: int

    file_size: int

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


class ChunkVideoURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata(BaseModel):
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


class ChunkVideoURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata(BaseModel):
    type: Optional[Literal["code"]] = None

    file_type: str

    language: str

    word_count: int

    file_size: int

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


class ChunkVideoURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata(BaseModel):
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


ChunkVideoURLInputChunkGeneratedMetadata: TypeAlias = Annotated[
    Union[
        ChunkVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata,
        ChunkVideoURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata,
        ChunkVideoURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata,
        ChunkVideoURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata,
        ChunkVideoURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata,
        None,
    ],
    PropertyInfo(discriminator="type"),
]


class ChunkVideoURLInputChunkVideoURL(BaseModel):
    url: str
    """The video URL. Can be either a URL or a Data URI."""


class ChunkVideoURLInputChunk(BaseModel):
    chunk_index: int
    """position of the chunk in a file"""

    mime_type: Optional[str] = None
    """mime type of the chunk"""

    generated_metadata: Optional[ChunkVideoURLInputChunkGeneratedMetadata] = None
    """metadata of the chunk"""

    model: Optional[str] = None
    """model used for this chunk"""

    type: Optional[Literal["video_url"]] = None
    """Input type identifier"""

    transcription: Optional[str] = None
    """speech recognition (sr) text of the video"""

    summary: Optional[str] = None
    """summary of the video"""

    video_url: ChunkVideoURLInputChunkVideoURL
    """The video input specification."""


Chunk: TypeAlias = Annotated[
    Union[ChunkTextInputChunk, ChunkImageURLInputChunk, ChunkAudioURLInputChunk, ChunkVideoURLInputChunk],
    PropertyInfo(discriminator="type"),
]


class VectorStoreFile(BaseModel):
    id: str
    """Unique identifier for the file"""

    filename: Optional[str] = None
    """Name of the file"""

    metadata: Optional[object] = None
    """Optional file metadata"""

    status: Optional[StoreFileStatus] = None
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
    """chunks"""
