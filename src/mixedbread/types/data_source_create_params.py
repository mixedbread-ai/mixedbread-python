# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .data_source_type import DataSourceType
from .data_source_oauth2_params_param import DataSourceOauth2ParamsParam

__all__ = ["DataSourceCreateParams"]


class DataSourceCreateParams(TypedDict, total=False):
    type: Required[DataSourceType]
    """The type of data source to create"""

    name: Required[str]
    """The name of the data source"""

    metadata: object
    """The metadata of the data source"""

    auth_params: Optional[DataSourceOauth2ParamsParam]
    """Authentication parameters for a OAuth data source."""
