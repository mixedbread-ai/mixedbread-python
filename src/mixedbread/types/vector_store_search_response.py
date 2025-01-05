# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "VectorStoreSearchResponse",
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


DataChunkValue: TypeAlias = Union[str, DataChunkValueImageURLInput, DataChunkValueTextInput, Dict[str, object], None]


class DataChunk(BaseModel):
    file_id: str
    """file id"""

    rank: int
    """rank of the chunk in a file"""

    score: float
    """score of the chunk"""

    value: Optional[DataChunkValue] = None
    """value of the chunk"""


class Data(BaseModel):
    id: str
    """file id"""

    created_at: datetime
    """Timestamp of vector store file creation"""

    score: float
    """score of the file"""

    usage_bytes: int
    """usage in bytes"""

    vector_store_id: str
    """vector store id"""

    version: int
    """version of the file"""

    chunks: Optional[List[DataChunk]] = None
    """chunks"""

    metadata: Optional[object] = None
    """metadata"""


class Pagination(BaseModel):
    limit: Optional[int] = None
    """Maximum number of items to return per page"""

    offset: Optional[int] = None
    """Cursor from which to start returning items"""

    total: Optional[int] = None
    """Total number of items available"""


class VectorStoreSearchResponse(BaseModel):
    data: List[Data]

    pagination: Pagination
    """Pagination model that includes total count of items."""

    object: Optional[Literal["list"]] = None
    """The object type of the response"""
