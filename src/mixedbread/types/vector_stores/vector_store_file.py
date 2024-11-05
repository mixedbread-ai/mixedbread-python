# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from ..job_status import JobStatus

__all__ = ["VectorStoreFile"]


class VectorStoreFile(BaseModel):
    id: str

    created_at: datetime
    """Timestamp of vector store file creation"""

    vector_store_id: str

    errors: Optional[List[str]] = None

    metadata: Optional[object] = None

    status: Optional[JobStatus] = None

    usage_bytes: Optional[int] = None

    version: Optional[int] = None
