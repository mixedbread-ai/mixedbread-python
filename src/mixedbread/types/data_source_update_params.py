# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .data_source_type import DataSourceType

__all__ = [
    "DataSourceUpdateParams",
    "NotionDataSourceCreateOrUpdateParams",
    "NotionDataSourceCreateOrUpdateParamsAuthParams",
    "NotionDataSourceCreateOrUpdateParamsAuthParamsOAuth2CreateOrUpdateParams",
    "NotionDataSourceCreateOrUpdateParamsAuthParamsAPIKeyCreateOrUpdateParams",
    "LinearDataSourceCreateOrUpdateParams",
    "LinearDataSourceCreateOrUpdateParamsAuthParams",
]


class NotionDataSourceCreateOrUpdateParams(TypedDict, total=False):
    type: DataSourceType
    """The type of data source to create"""

    name: Required[str]
    """The name of the data source"""

    metadata: object
    """The metadata of the data source"""

    auth_params: Optional[NotionDataSourceCreateOrUpdateParamsAuthParams]
    """The authentication parameters of the data source.

    Notion supports OAuth2 and API key.
    """


class NotionDataSourceCreateOrUpdateParamsAuthParamsOAuth2CreateOrUpdateParams(TypedDict, total=False):
    type: Literal["oauth2"]


class NotionDataSourceCreateOrUpdateParamsAuthParamsAPIKeyCreateOrUpdateParams(TypedDict, total=False):
    type: Literal["api_key"]

    api_key: Required[str]
    """The API key"""


NotionDataSourceCreateOrUpdateParamsAuthParams: TypeAlias = Union[
    NotionDataSourceCreateOrUpdateParamsAuthParamsOAuth2CreateOrUpdateParams,
    NotionDataSourceCreateOrUpdateParamsAuthParamsAPIKeyCreateOrUpdateParams,
]


class LinearDataSourceCreateOrUpdateParams(TypedDict, total=False):
    type: DataSourceType
    """The type of data source to create"""

    name: Required[str]
    """The name of the data source"""

    metadata: object
    """The metadata of the data source"""

    auth_params: Optional[LinearDataSourceCreateOrUpdateParamsAuthParams]
    """Base class for OAuth2 create or update parameters."""


class LinearDataSourceCreateOrUpdateParamsAuthParams(TypedDict, total=False):
    type: Literal["oauth2"]


DataSourceUpdateParams: TypeAlias = Union[NotionDataSourceCreateOrUpdateParams, LinearDataSourceCreateOrUpdateParams]
