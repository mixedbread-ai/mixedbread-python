# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .parsing_job_status import ParsingJobStatus

__all__ = ["JobListResponse"]


class JobListResponse(BaseModel):
    """A parsing job item for list responses."""

    id: str
    """The ID of the job"""

    file_id: str
    """The ID of the file to parse"""

    filename: Optional[str] = None
    """The name of the file"""

    status: ParsingJobStatus
    """The status of the job"""

    error: Optional[Dict[str, object]] = None
    """The error of the job"""

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
