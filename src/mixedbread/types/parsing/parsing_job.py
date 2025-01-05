# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ParsingJob", "Result", "ResultChunk", "ResultChunkElement"]


class ResultChunkElement(BaseModel):
    bbox: List[object]
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


class ResultChunk(BaseModel):
    content: str
    """The full content of the chunk"""

    content_to_embed: str
    """The content to be used for embedding"""

    elements: List[ResultChunkElement]
    """List of elements contained in this chunk"""


class Result(BaseModel):
    chunking_strategy: Literal["page"]
    """The strategy used for chunking the document"""

    chunks: List[ResultChunk]
    """List of extracted chunks from the document"""

    element_types: List[
        Literal[
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
    ]
    """The types of elements extracted"""

    return_format: Literal["html", "markdown", "plain"]
    """The format of the returned content"""


class ParsingJob(BaseModel):
    id: str
    """The ID of the job"""

    status: Literal["none", "running", "canceled", "successful", "failed", "resumable", "pending"]
    """The status of the job"""

    created_at: Optional[datetime] = None
    """The creation time of the job"""

    errors: Optional[List[str]] = None
    """The errors of the job"""

    finished_at: Optional[datetime] = None
    """The finished time of the job"""

    object: Optional[Literal["job"]] = None
    """The type of the object"""

    result: Optional[Result] = None
    """Result of document parsing operation."""
