# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .parsing_job_status import ParsingJobStatus

__all__ = ["JobListResponse", "Pagination", "Data"]


class Pagination(BaseModel):
    has_more: bool
    """
    Contextual direction-aware flag: True if more items exist in the requested
    pagination direction. For 'after': more items after this page. For 'before':
    more items before this page.
    """

    first_cursor: Optional[str] = None
    """Cursor of the first item in this page.

    Use for backward pagination. None if page is empty.
    """

    last_cursor: Optional[str] = None
    """Cursor of the last item in this page.

    Use for forward pagination. None if page is empty.
    """

    total: Optional[int] = None
    """Total number of items available across all pages.

    Only included when include_total=true was requested. Expensive operation - use
    sparingly.
    """


class Data(BaseModel):
    id: str
    """The ID of the job"""

    file_id: str
    """The ID of the file to parse"""

    filename: Optional[str] = None
    """The name of the file"""

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
    """Response model for cursor-based pagination.

    Examples: Forward pagination response: { "has_more": true, "first_cursor":
    "eyJjcmVhdGVkX2F0IjoiMjAyNC0xMi0zMSIsImlkIjoiYWJjMTIzIn0=", "last_cursor":
    "eyJjcmVhdGVkX2F0IjoiMjAyNC0xMi0zMCIsImlkIjoieHl6Nzg5In0=", "total": null }

        Final page response:
            {
                "has_more": false,
                "first_cursor": "eyJjcmVhdGVkX2F0IjoiMjAyNC0xMi0yOSIsImlkIjoibGFzdDEyMyJ9",
                "last_cursor": "eyJjcmVhdGVkX2F0IjoiMjAyNC0xMi0yOCIsImlkIjoiZmluYWw0NTYifQ==",
                "total": 42
            }

        Empty results:
            {
                "has_more": false,
                "first_cursor": null,
                "last_cursor": null,
                "total": 0
            }
    """

    data: List[Data]
    """The list of parsing jobs"""

    object: Optional[Literal["list"]] = None
    """The object type of the response"""
