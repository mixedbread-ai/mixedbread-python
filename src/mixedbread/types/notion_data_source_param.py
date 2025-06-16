# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .oauth2_params import Oauth2Params
from .data_source_type import DataSourceType

__all__ = ["NotionDataSourceParam", "AuthParams", "AuthParamsAPIKeyCreateOrUpdateParams"]


class AuthParamsAPIKeyCreateOrUpdateParams(TypedDict, total=False):
    type: Literal["api_key"]

    api_key: Required[str]
    """The API key"""


AuthParams: TypeAlias = Union[Oauth2Params, AuthParamsAPIKeyCreateOrUpdateParams]


class NotionDataSourceParam(TypedDict, total=False):
    type: DataSourceType
    """The type of data source to create"""

    name: Required[str]
    """The name of the data source"""

    metadata: object
    """The metadata of the data source"""

    auth_params: Optional[AuthParams]
    """The authentication parameters of the data source.

    Notion supports OAuth2 and API key.
    """
