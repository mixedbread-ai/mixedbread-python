# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["JobDeleteResponse"]


class JobDeleteResponse(BaseModel):
    """A deleted parsing job."""

    id: str
    """The ID of the deleted job"""

    deleted: Optional[bool] = None
    """Whether the job was deleted"""

    object: Optional[Literal["parsing_job"]] = None
    """The type of the object"""
