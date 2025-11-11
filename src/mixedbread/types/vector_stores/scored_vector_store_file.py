# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel
from ..stores.store_file_status import StoreFileStatus

__all__ = [
    "ScoredVectorStoreFile",
    "Chunk",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunk",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadata",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataTextChunkGeneratedMetadata",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataPdfChunkGeneratedMetadata",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataCodeChunkGeneratedMetadata",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataAudioChunkGeneratedMetadata",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunk",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadata",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkImageURL",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunk",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadata",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkAudioURL",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunk",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadata",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata",
    "ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkVideoURL",
]


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading(
    BaseModel
):
    level: int

    text: str


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext(
    BaseModel
):
    level: int

    text: str


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata(
    BaseModel
):
    type: Optional[Literal["markdown"]] = None

    file_type: Optional[Literal["text/markdown"]] = None

    language: str

    word_count: int

    file_size: int

    chunk_headings: Optional[
        List[
            ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading
        ]
    ] = None

    heading_context: Optional[
        List[
            ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext
        ]
    ] = None

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


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataTextChunkGeneratedMetadata(
    BaseModel
):
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


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataPdfChunkGeneratedMetadata(
    BaseModel
):
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


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataCodeChunkGeneratedMetadata(
    BaseModel
):
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


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataAudioChunkGeneratedMetadata(
    BaseModel
):
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


ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadata: TypeAlias = Annotated[
    Union[
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata,
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataTextChunkGeneratedMetadata,
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataPdfChunkGeneratedMetadata,
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataCodeChunkGeneratedMetadata,
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataAudioChunkGeneratedMetadata,
        None,
    ],
    PropertyInfo(discriminator="type"),
]


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunk(BaseModel):
    chunk_index: int
    """position of the chunk in a file"""

    mime_type: Optional[str] = None
    """mime type of the chunk"""

    generated_metadata: Optional[
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadata
    ] = None
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


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading(
    BaseModel
):
    level: int

    text: str


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext(
    BaseModel
):
    level: int

    text: str


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata(
    BaseModel
):
    type: Optional[Literal["markdown"]] = None

    file_type: Optional[Literal["text/markdown"]] = None

    language: str

    word_count: int

    file_size: int

    chunk_headings: Optional[
        List[
            ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading
        ]
    ] = None

    heading_context: Optional[
        List[
            ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext
        ]
    ] = None

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


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata(
    BaseModel
):
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


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata(
    BaseModel
):
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


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata(
    BaseModel
):
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


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata(
    BaseModel
):
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


ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadata: TypeAlias = Annotated[
    Union[
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata,
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata,
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata,
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata,
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata,
        None,
    ],
    PropertyInfo(discriminator="type"),
]


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

    generated_metadata: Optional[
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadata
    ] = None
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


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading(
    BaseModel
):
    level: int

    text: str


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext(
    BaseModel
):
    level: int

    text: str


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata(
    BaseModel
):
    type: Optional[Literal["markdown"]] = None

    file_type: Optional[Literal["text/markdown"]] = None

    language: str

    word_count: int

    file_size: int

    chunk_headings: Optional[
        List[
            ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading
        ]
    ] = None

    heading_context: Optional[
        List[
            ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext
        ]
    ] = None

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


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata(
    BaseModel
):
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


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata(
    BaseModel
):
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


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata(
    BaseModel
):
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


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata(
    BaseModel
):
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


ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadata: TypeAlias = Annotated[
    Union[
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata,
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata,
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata,
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata,
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata,
        None,
    ],
    PropertyInfo(discriminator="type"),
]


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkAudioURL(BaseModel):
    url: str
    """The audio URL. Can be either a URL or a Data URI."""


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunk(BaseModel):
    chunk_index: int
    """position of the chunk in a file"""

    mime_type: Optional[str] = None
    """mime type of the chunk"""

    generated_metadata: Optional[
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadata
    ] = None
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


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading(
    BaseModel
):
    level: int

    text: str


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext(
    BaseModel
):
    level: int

    text: str


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata(
    BaseModel
):
    type: Optional[Literal["markdown"]] = None

    file_type: Optional[Literal["text/markdown"]] = None

    language: str

    word_count: int

    file_size: int

    chunk_headings: Optional[
        List[
            ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading
        ]
    ] = None

    heading_context: Optional[
        List[
            ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext
        ]
    ] = None

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


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata(
    BaseModel
):
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


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata(
    BaseModel
):
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


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata(
    BaseModel
):
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


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata(
    BaseModel
):
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


ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadata: TypeAlias = Annotated[
    Union[
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata,
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata,
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata,
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata,
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata,
        None,
    ],
    PropertyInfo(discriminator="type"),
]


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkVideoURL(BaseModel):
    url: str
    """The video URL. Can be either a URL or a Data URI."""


class ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunk(BaseModel):
    chunk_index: int
    """position of the chunk in a file"""

    mime_type: Optional[str] = None
    """mime type of the chunk"""

    generated_metadata: Optional[
        ChunkMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadata
    ] = None
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
    """Array of scored file chunks"""

    score: float
    """score of the file"""
