# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .scored_vector_store_file import ScoredVectorStoreFile

__all__ = ["FileSearchResponse"]


class FileSearchResponse(BaseModel):
    object: Optional[Literal["list"]] = None
    """The object type of the response"""

    data: List[ScoredVectorStoreFile]
    """The list of scored vector store files"""
