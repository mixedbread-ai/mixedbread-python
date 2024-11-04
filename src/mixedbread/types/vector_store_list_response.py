# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .vector_store_object import VectorStoreObject

__all__ = ["VectorStoreListResponse", "Pagination"]


class Pagination(BaseModel):
    after: Optional[int] = None

    limit: Optional[int] = None

    total: Optional[int] = None


class VectorStoreListResponse(BaseModel):
    data: List[VectorStoreObject]

    pagination: Pagination
