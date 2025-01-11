# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..file_object import FileObject

__all__ = ["VectorStoreFile"]


class VectorStoreFile(BaseModel):
    id: str
    """Unique identifier for the file"""

    created_at: datetime
    """Timestamp of vector store file creation"""

    vector_store_id: str
    """ID of the containing vector store"""

    errors: Optional[List[str]] = None
    """List of error messages if processing failed"""

    file_object: Optional[FileObject] = None
    """A model representing a file object in the system.

    This model contains metadata about files stored in the system, including
    identifiers, size information, and timestamps.
    """

    metadata: Optional[object] = None
    """Optional file metadata"""

    object: Optional[Literal["vector_store.file"]] = None
    """Type of the object"""

    status: Optional[Literal["none", "running", "canceled", "successful", "failed", "resumable", "pending"]] = None
    """Processing status of the file"""

    usage_bytes: Optional[int] = None
    """Storage usage in bytes"""

    version: Optional[int] = None
    """Version number of the file"""
