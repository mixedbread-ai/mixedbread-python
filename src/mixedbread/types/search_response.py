# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .vector_stores.vector_store_file import VectorStoreFile

__all__ = ["SearchResponse", "Pagination"]


class Pagination(BaseModel):
    after: Optional[int] = None

    limit: Optional[int] = None

    total: Optional[int] = None


class SearchResponse(BaseModel):
    data: List[List[VectorStoreFile]]

    pagination: Pagination
