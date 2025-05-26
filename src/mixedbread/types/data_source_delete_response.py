# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DataSourceDeleteResponse"]


class DataSourceDeleteResponse(BaseModel):
    id: str
    """The ID of the data source"""

    deleted: Optional[bool] = None
    """Whether the data source was deleted"""

    object: Optional[Literal["data_source"]] = None
    """The type of the object"""
