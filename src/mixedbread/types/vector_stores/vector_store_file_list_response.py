# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .vector_store_file_object import VectorStoreFileObject

__all__ = ["VectorStoreFileListResponse", "Pagination"]


class Pagination(BaseModel):
    after: Optional[int] = None

    limit: Optional[int] = None

    total: Optional[int] = None


class VectorStoreFileListResponse(BaseModel):
    data: List[VectorStoreFileObject]

    pagination: Pagination
