# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["JobListResponse"]


class JobListResponse(BaseModel):
    id: str
    """The ID of the job"""

    file_id: str
    """The ID of the file to parse"""

    status: Literal["pending", "in_progress", "cancelled", "completed", "failed"]
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
