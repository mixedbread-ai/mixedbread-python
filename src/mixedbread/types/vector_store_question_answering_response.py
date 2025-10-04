# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "VectorStoreQuestionAnsweringResponse",
    "Source",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunk",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadata",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataTextChunkGeneratedMetadata",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataPdfChunkGeneratedMetadata",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataCodeChunkGeneratedMetadata",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataAudioChunkGeneratedMetadata",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunk",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadata",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkImageURL",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunk",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadata",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkAudioURL",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunk",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadata",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata",
    "SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkVideoURL",
]


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading(
    BaseModel
):
    level: int

    text: str


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext(
    BaseModel
):
    level: int

    text: str


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata(
    BaseModel
):
    type: Optional[Literal["markdown"]] = None

    file_type: Optional[Literal["text/markdown"]] = None

    language: str

    word_count: int

    file_size: int

    chunk_headings: Optional[
        List[
            SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading
        ]
    ] = None

    heading_context: Optional[
        List[
            SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext
        ]
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


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataTextChunkGeneratedMetadata(
    BaseModel
):
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


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataPdfChunkGeneratedMetadata(
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


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataCodeChunkGeneratedMetadata(
    BaseModel
):
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


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataAudioChunkGeneratedMetadata(
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


SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadata: TypeAlias = Annotated[
    Union[
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata,
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataTextChunkGeneratedMetadata,
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataPdfChunkGeneratedMetadata,
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataCodeChunkGeneratedMetadata,
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataAudioChunkGeneratedMetadata,
        None,
    ],
    PropertyInfo(discriminator="type"),
]


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunk(BaseModel):
    chunk_index: int
    """position of the chunk in a file"""

    mime_type: Optional[str] = None
    """mime type of the chunk"""

    generated_metadata: Optional[
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadata
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


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading(
    BaseModel
):
    level: int

    text: str


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext(
    BaseModel
):
    level: int

    text: str


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata(
    BaseModel
):
    type: Optional[Literal["markdown"]] = None

    file_type: Optional[Literal["text/markdown"]] = None

    language: str

    word_count: int

    file_size: int

    chunk_headings: Optional[
        List[
            SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading
        ]
    ] = None

    heading_context: Optional[
        List[
            SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext
        ]
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


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata(
    BaseModel
):
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


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata(
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


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata(
    BaseModel
):
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


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata(
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


SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadata: TypeAlias = Annotated[
    Union[
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata,
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata,
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata,
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata,
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata,
        None,
    ],
    PropertyInfo(discriminator="type"),
]


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

    generated_metadata: Optional[
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadata
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

    image_url: SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkImageURL
    """The image input specification."""


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading(
    BaseModel
):
    level: int

    text: str


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext(
    BaseModel
):
    level: int

    text: str


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata(
    BaseModel
):
    type: Optional[Literal["markdown"]] = None

    file_type: Optional[Literal["text/markdown"]] = None

    language: str

    word_count: int

    file_size: int

    chunk_headings: Optional[
        List[
            SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading
        ]
    ] = None

    heading_context: Optional[
        List[
            SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext
        ]
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


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata(
    BaseModel
):
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


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata(
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


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata(
    BaseModel
):
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


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata(
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


SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadata: TypeAlias = Annotated[
    Union[
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata,
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata,
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata,
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata,
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata,
        None,
    ],
    PropertyInfo(discriminator="type"),
]


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkAudioURL(BaseModel):
    url: str
    """The audio URL. Can be either a URL or a Data URI."""


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunk(BaseModel):
    chunk_index: int
    """position of the chunk in a file"""

    mime_type: Optional[str] = None
    """mime type of the chunk"""

    generated_metadata: Optional[
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadata
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

    audio_url: SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkAudioURL
    """The audio input specification."""

    sampling_rate: int
    """The sampling rate of the audio."""


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading(
    BaseModel
):
    level: int

    text: str


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext(
    BaseModel
):
    level: int

    text: str


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata(
    BaseModel
):
    type: Optional[Literal["markdown"]] = None

    file_type: Optional[Literal["text/markdown"]] = None

    language: str

    word_count: int

    file_size: int

    chunk_headings: Optional[
        List[
            SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading
        ]
    ] = None

    heading_context: Optional[
        List[
            SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext
        ]
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


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata(
    BaseModel
):
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


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata(
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


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata(
    BaseModel
):
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


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata(
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


SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadata: TypeAlias = Annotated[
    Union[
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata,
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata,
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata,
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata,
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata,
        None,
    ],
    PropertyInfo(discriminator="type"),
]


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkVideoURL(BaseModel):
    url: str
    """The video URL. Can be either a URL or a Data URI."""


class SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunk(BaseModel):
    chunk_index: int
    """position of the chunk in a file"""

    mime_type: Optional[str] = None
    """mime type of the chunk"""

    generated_metadata: Optional[
        SourceMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadata
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
