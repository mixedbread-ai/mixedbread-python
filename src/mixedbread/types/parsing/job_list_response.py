# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .parsing_job_status import ParsingJobStatus

__all__ = ["JobListResponse", "Pagination", "Data"]


class Pagination(BaseModel):
    next_cursor: Optional[str] = None
    """Cursor for the next page, null if no more pages"""

    prev_cursor: Optional[str] = None
    """Cursor for the previous page, null if no previous pages"""

    has_more: bool
    """Whether there are more items available"""

    has_prev: bool
    """Whether there are previous items available"""

    total: Optional[int] = None
    """Total number of items available"""


class Data(BaseModel):
    id: str
    """The ID of the job"""

    file_id: str
    """The ID of the file to parse"""

    status: ParsingJobStatus
    """The status of the job"""

    started_at: Optional[datetime] = None
    """The started time of the job"""

    finished_at: Optional[datetime] = None
    """The finished time of the job"""

    created_at: Optional[datetime] = None
    """The creation time of the job"""

    updated_at: Optional[datetime] = None
    """The updated time of the job"""

    object: Optional[Literal["parsing_job"]] = None
    """The type of the object"""


class JobListResponse(BaseModel):
    pagination: Pagination
    """Response model for cursor-based pagination."""

    data: List[Data]
    """The list of parsing jobs"""

    object: Optional[Literal["list"]] = None
    """The object type of the response"""
