# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FileRetrieveResponse"]


class FileRetrieveResponse(BaseModel):
    id: str

    created_at: datetime
    """Timestamp of vector store file creation"""

    vector_store_id: str

    errors: Optional[List[str]] = None

    metadata: Optional[object] = None

    status: Optional[Literal["none", "running", "canceled", "successful", "failed", "resumable", "pending"]] = None

    usage_bytes: Optional[int] = None

    version: Optional[int] = None
