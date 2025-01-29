# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .scored_vector_store_chunk import ScoredVectorStoreChunk

__all__ = ["VectorStoreSearchResponse"]


class VectorStoreSearchResponse(BaseModel):
    object: Optional[Literal["list"]] = None
    """The object type of the response"""

    data: List[ScoredVectorStoreChunk]
    """The list of scored vector store file chunks"""
