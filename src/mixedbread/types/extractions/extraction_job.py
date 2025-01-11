# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .extraction_result import ExtractionResult

__all__ = ["ExtractionJob"]


class ExtractionJob(BaseModel):
    id: str
    """The ID of the job"""

    result: Optional[ExtractionResult] = None
    """Result of an extraction operation."""

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
