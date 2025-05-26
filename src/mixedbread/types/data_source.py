# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .data_source_type import DataSourceType
from .data_source_oauth2_params import DataSourceOauth2Params

__all__ = ["DataSource"]


class DataSource(BaseModel):
    id: str
    """The ID of the data source"""

    created_at: datetime
    """The creation time of the data source"""

    updated_at: datetime
    """The last update time of the data source"""

    type: DataSourceType
    """The type of data source"""

    name: str
    """The name of the data source"""

    metadata: object
    """The metadata of the data source"""

    auth_params: Optional[DataSourceOauth2Params] = None
    """Authentication parameters for a OAuth data source."""

    object: Optional[Literal["data_source"]] = None
    """The type of the object"""
