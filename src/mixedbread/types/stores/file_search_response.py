# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .scored_store_file import ScoredStoreFile

__all__ = ["FileSearchResponse"]


class FileSearchResponse(BaseModel):
    object: Optional[Literal["list"]] = None
    """The object type of the response"""

    data: List[ScoredStoreFile]
    """The list of scored store files"""
