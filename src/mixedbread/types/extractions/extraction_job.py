# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .extraction_result import ExtractionResult

__all__ = ["ExtractionJob"]


class ExtractionJob(BaseModel):
    id: str
    """Unique identifier for the extraction job"""

    organization_id: str
    """ID of the organization that owns this job"""

    file_id: str
    """ID of the file being extracted"""

    created_at: datetime
    """When the job was created"""

    updated_at: datetime
    """When the job was last updated"""

    started_at: Optional[datetime] = None
    """When the job started processing"""

    finished_at: Optional[datetime] = None
    """When the job finished processing"""

    status: Literal["pending", "in_progress", "cancelled", "completed", "failed"]
    """Current status of the job"""

    result: Optional[ExtractionResult] = None
    """The result of an extraction job."""

    error: Optional[Dict[str, object]] = None
    """Error information if failed"""

    json_schema: Dict[str, object]
    """The JSON schema used for extraction"""
