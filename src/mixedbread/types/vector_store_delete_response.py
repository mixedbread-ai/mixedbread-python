# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VectorStoreDeleteResponse"]


class VectorStoreDeleteResponse(BaseModel):
    id: str
    """ID of the deleted vector store"""

    deleted: bool
    """Whether the deletion was successful"""

    object: Optional[Literal["vector_store"]] = None
    """Type of the deleted object"""
