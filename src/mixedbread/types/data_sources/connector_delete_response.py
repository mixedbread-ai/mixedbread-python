# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ConnectorDeleteResponse"]


class ConnectorDeleteResponse(BaseModel):
    id: str
    """The ID of the connector"""

    deleted: Optional[bool] = None
    """Whether the connector was deleted"""

    object: Optional[Literal["data_source.connector"]] = None
    """The type of the object"""
