# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "VectorStoreSearchResponse",
    "Data",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunk",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadata",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataTextChunkGeneratedMetadata",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataPdfChunkGeneratedMetadata",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataCodeChunkGeneratedMetadata",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataAudioChunkGeneratedMetadata",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunk",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadata",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkImageURL",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunk",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadata",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkAudioURL",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunk",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadata",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata",
    "DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkVideoURL",
]


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading(
    BaseModel
):
    level: int

    text: str


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext(
    BaseModel
):
    level: int

    text: str


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata(
    BaseModel
):
    type: Optional[Literal["markdown"]] = None

    file_type: Optional[Literal["text/markdown"]] = None

    language: str

    word_count: int

    file_size: int

    chunk_headings: Optional[
        List[
            DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading
        ]
    ] = None

    heading_context: Optional[
        List[
            DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext
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


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataTextChunkGeneratedMetadata(
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


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataPdfChunkGeneratedMetadata(
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


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataCodeChunkGeneratedMetadata(
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


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataAudioChunkGeneratedMetadata(
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


DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadata: TypeAlias = Annotated[
    Union[
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata,
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataTextChunkGeneratedMetadata,
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataPdfChunkGeneratedMetadata,
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataCodeChunkGeneratedMetadata,
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadataAudioChunkGeneratedMetadata,
        None,
    ],
    PropertyInfo(discriminator="type"),
]


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunk(BaseModel):
    chunk_index: int
    """position of the chunk in a file"""

    mime_type: Optional[str] = None
    """mime type of the chunk"""

    generated_metadata: Optional[
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredTextInputChunkGeneratedMetadata
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


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading(
    BaseModel
):
    level: int

    text: str


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext(
    BaseModel
):
    level: int

    text: str


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata(
    BaseModel
):
    type: Optional[Literal["markdown"]] = None

    file_type: Optional[Literal["text/markdown"]] = None

    language: str

    word_count: int

    file_size: int

    chunk_headings: Optional[
        List[
            DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading
        ]
    ] = None

    heading_context: Optional[
        List[
            DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext
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


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata(
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


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata(
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


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata(
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


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata(
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


DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadata: TypeAlias = Annotated[
    Union[
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata,
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata,
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata,
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata,
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata,
        None,
    ],
    PropertyInfo(discriminator="type"),
]


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

    generated_metadata: Optional[
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkGeneratedMetadata
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

    image_url: DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredImageURLInputChunkImageURL
    """The image input specification."""


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading(
    BaseModel
):
    level: int

    text: str


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext(
    BaseModel
):
    level: int

    text: str


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata(
    BaseModel
):
    type: Optional[Literal["markdown"]] = None

    file_type: Optional[Literal["text/markdown"]] = None

    language: str

    word_count: int

    file_size: int

    chunk_headings: Optional[
        List[
            DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading
        ]
    ] = None

    heading_context: Optional[
        List[
            DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext
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


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata(
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


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata(
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


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata(
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


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata(
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


DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadata: TypeAlias = Annotated[
    Union[
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata,
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata,
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata,
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata,
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata,
        None,
    ],
    PropertyInfo(discriminator="type"),
]


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkAudioURL(BaseModel):
    url: str
    """The audio URL. Can be either a URL or a Data URI."""


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunk(BaseModel):
    chunk_index: int
    """position of the chunk in a file"""

    mime_type: Optional[str] = None
    """mime type of the chunk"""

    generated_metadata: Optional[
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkGeneratedMetadata
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

    audio_url: DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredAudioURLInputChunkAudioURL
    """The audio input specification."""

    sampling_rate: int
    """The sampling rate of the audio."""


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading(
    BaseModel
):
    level: int

    text: str


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext(
    BaseModel
):
    level: int

    text: str


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata(
    BaseModel
):
    type: Optional[Literal["markdown"]] = None

    file_type: Optional[Literal["text/markdown"]] = None

    language: str

    word_count: int

    file_size: int

    chunk_headings: Optional[
        List[
            DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataChunkHeading
        ]
    ] = None

    heading_context: Optional[
        List[
            DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadataHeadingContext
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


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata(
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


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata(
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


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata(
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


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata(
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


DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadata: TypeAlias = Annotated[
    Union[
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataMarkdownChunkGeneratedMetadata,
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataTextChunkGeneratedMetadata,
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataPdfChunkGeneratedMetadata,
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataCodeChunkGeneratedMetadata,
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadataAudioChunkGeneratedMetadata,
        None,
    ],
    PropertyInfo(discriminator="type"),
]


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkVideoURL(BaseModel):
    url: str
    """The video URL. Can be either a URL or a Data URI."""


class DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunk(BaseModel):
    chunk_index: int
    """position of the chunk in a file"""

    mime_type: Optional[str] = None
    """mime type of the chunk"""

    generated_metadata: Optional[
        DataMxbaiOmniAPIRoutesV1DeprecatedVectorStoresModelsScoredVideoURLInputChunkGeneratedMetadata
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
