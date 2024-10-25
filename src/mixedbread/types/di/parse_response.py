# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "ParseResponse",
    "Data",
    "DataRunningJob",
    "DataFailedJob",
    "DataSuccessfulParsingJob",
    "DataSuccessfulParsingJobResult",
    "DataSuccessfulParsingJobResultChunk",
    "DataSuccessfulParsingJobResultChunkElement",
]


class DataRunningJob(BaseModel):
    id: str
    """The ID of the job"""

    created_at: Optional[datetime] = None
    """The creation time of the job"""

    errors: Optional[List[str]] = None
    """The errors of the job"""

    finished_at: Optional[datetime] = None
    """The finished time of the job"""

    result: Optional[object] = None
    """The result of the job"""

    status: Optional[Literal["pending", "running"]] = None
    """The status of the job"""


class DataFailedJob(BaseModel):
    id: str
    """The ID of the job"""

    errors: List[str]
    """The errors of the job"""

    created_at: Optional[datetime] = None
    """The creation time of the job"""

    finished_at: Optional[datetime] = None
    """The finished time of the job"""

    result: Optional[object] = None
    """The result of the job"""

    status: Optional[Literal["failed"]] = None
    """The status of the job"""


class DataSuccessfulParsingJobResultChunkElement(BaseModel):
    bbox: List[float]
    """The bounding box coordinates [x1, y1, x2, y2]"""

    confidence: float
    """The confidence score of the extraction"""

    content: str
    """The full content of the extracted element"""

    page: int
    """The page number where the element was found"""

    type: Literal[
        "caption",
        "footnote",
        "formula",
        "list-item",
        "page-footer",
        "page-header",
        "picture",
        "section-header",
        "table",
        "text",
        "title",
    ]
    """The type of the extracted element"""

    summary: Optional[str] = None
    """A brief summary of the element's content"""


class DataSuccessfulParsingJobResultChunk(BaseModel):
    content: str
    """The full content of the chunk"""

    content_to_embed: str
    """The content to be used for embedding"""

    elements: List[DataSuccessfulParsingJobResultChunkElement]
    """List of elements contained in this chunk"""


class DataSuccessfulParsingJobResult(BaseModel):
    chunking_strategy: Literal["page"]
    """The strategy used for chunking the document"""

    chunks: List[DataSuccessfulParsingJobResultChunk]
    """List of extracted chunks from the document"""


class DataSuccessfulParsingJob(BaseModel):
    id: str
    """The ID of the job"""

    result: DataSuccessfulParsingJobResult
    """The extracted content and metadata from the document"""

    created_at: Optional[datetime] = None
    """The creation time of the job"""

    errors: Optional[List[str]] = None
    """The errors of the job"""

    finished_at: Optional[datetime] = None
    """The finished time of the job"""

    status: Optional[Literal["successful"]] = None
    """The status of the job"""


Data: TypeAlias = Union[DataRunningJob, DataFailedJob, DataSuccessfulParsingJob]


class ParseResponse(BaseModel):
    data: Data
    """Discriminated union of all possible parsing job states"""
