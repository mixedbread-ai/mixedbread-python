# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .data_source_type import DataSourceType
from .data_source_oauth2_params import DataSourceOauth2Params

__all__ = ["DataSource", "AuthParams", "AuthParamsDataSourceAPIKeyParams"]


class AuthParamsDataSourceAPIKeyParams(BaseModel):
    """Authentication parameters for a API key data source."""

    type: Optional[Literal["api_key"]] = None

    api_key: str
    """The API key"""


AuthParams: TypeAlias = Annotated[
    Union[DataSourceOauth2Params, AuthParamsDataSourceAPIKeyParams, None], PropertyInfo(discriminator="type")
]


class DataSource(BaseModel):
    """Service-level representation of a data source."""

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

    auth_params: Optional[AuthParams] = None
    """Authentication parameters"""

    object: Optional[Literal["data_source"]] = None
    """The type of the object"""
