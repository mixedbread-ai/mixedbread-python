# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .oauth2_params import Oauth2Params

__all__ = [
    "DataSourceCreateParams",
    "NotionDataSource",
    "NotionDataSourceAuthParams",
    "NotionDataSourceAuthParamsAPIKeyCreateOrUpdateParams",
    "LinearDataSource",
]


class NotionDataSource(TypedDict, total=False):
    type: Literal["notion"]
    """The type of data source to create"""

    name: Required[str]
    """The name of the data source"""

    metadata: object
    """The metadata of the data source"""

    auth_params: Optional[NotionDataSourceAuthParams]
    """The authentication parameters of the data source.

    Notion supports OAuth2 and API key.
    """


class NotionDataSourceAuthParamsAPIKeyCreateOrUpdateParams(TypedDict, total=False):
    type: Literal["api_key"]

    api_key: Required[str]
    """The API key"""


NotionDataSourceAuthParams: TypeAlias = Union[Oauth2Params, NotionDataSourceAuthParamsAPIKeyCreateOrUpdateParams]


class LinearDataSource(TypedDict, total=False):
    type: Literal["linear"]
    """The type of data source to create"""

    name: Required[str]
    """The name of the data source"""

    metadata: object
    """The metadata of the data source"""

    auth_params: Optional[Oauth2Params]
    """Base class for OAuth2 create or update parameters."""


DataSourceCreateParams: TypeAlias = Union[NotionDataSource, LinearDataSource]
