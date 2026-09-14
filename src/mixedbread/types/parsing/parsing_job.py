# File generated from our OpenAPI spec by sdkgen. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .parsing_job_status import ParsingJobStatus
from .document_parser_result import DocumentParserResult

__all__ = ["ParsingJob"]


class ParsingJob(BaseModel):
    """A parsing job with its result narrowed to the public fields."""

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

    result: Optional[DocumentParserResult] = None
    """The public result of a parsing job."""

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
