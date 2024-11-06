# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "SearchResponse",
    "Data",
    "DataChunk",
    "DataChunkValue",
    "DataChunkValueImageURLInput",
    "DataChunkValueImageURLInputImage",
    "DataChunkValueTextInput",
    "Pagination",
]


class DataChunkValueImageURLInputImage(BaseModel):
    url: str
    """The image URL. Can be either a URL or a Data URI."""


class DataChunkValueImageURLInput(BaseModel):
    image: DataChunkValueImageURLInputImage
    """The image input specification."""

    type: Optional[Literal["image_url"]] = None
    """Input type identifier"""


class DataChunkValueTextInput(BaseModel):
    text: str
    """Text content to process"""

    type: Optional[Literal["text"]] = None
    """Input type identifier"""


DataChunkValue: TypeAlias = Union[str, DataChunkValueImageURLInput, DataChunkValueTextInput, None]


class DataChunk(BaseModel):
    rank: int
    """rank of the chunk in a file"""

    value: Optional[DataChunkValue] = None
    """value of the chunk"""


class Data(BaseModel):
    id: str
    """file id"""

    created_at: datetime
    """Timestamp of vector store file creation"""

    usage_bytes: int
    """usage in bytes"""

    vector_store_id: str
    """vector store id"""

    version: int
    """version of the file"""

    chunks: Optional[List[DataChunk]] = None

    metadata: Optional[object] = None
    """metadata"""


class Pagination(BaseModel):
    after: Optional[int] = None

    limit: Optional[int] = None

    total: Optional[int] = None


class SearchResponse(BaseModel):
    data: List[Data]

    pagination: Pagination
