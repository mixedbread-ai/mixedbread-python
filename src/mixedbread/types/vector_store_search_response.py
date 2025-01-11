# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "VectorStoreSearchResponse",
    "Data",
    "DataValue",
    "DataValueImageURLInput",
    "DataValueImageURLInputImage",
    "DataValueTextInput",
]


class DataValueImageURLInputImage(BaseModel):
    url: str
    """The image URL. Can be either a URL or a Data URI."""


class DataValueImageURLInput(BaseModel):
    image: DataValueImageURLInputImage
    """The image input specification."""

    type: Optional[Literal["image_url"]] = None
    """Input type identifier"""


class DataValueTextInput(BaseModel):
    text: str
    """Text content to process"""

    type: Optional[Literal["text"]] = None
    """Input type identifier"""


DataValue: TypeAlias = Union[str, DataValueImageURLInput, DataValueTextInput, Dict[str, object], None]


class Data(BaseModel):
    file_id: str
    """file id"""

    position: int
    """position of the chunk in a file"""

    score: float
    """score of the chunk"""

    vector_store_id: str
    """vector store id"""

    content: Optional[str] = None
    """content of the chunk"""

    metadata: Optional[object] = None
    """file metadata"""

    value: Optional[DataValue] = None
    """value of the chunk"""


class VectorStoreSearchResponse(BaseModel):
    data: List[Data]
    """The list of scored vector store file chunks"""

    object: Optional[Literal["list"]] = None
    """The object type of the response"""
