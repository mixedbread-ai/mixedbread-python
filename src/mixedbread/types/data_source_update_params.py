# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .data_source_oauth2_params_param import DataSourceOauth2ParamsParam

__all__ = ["DataSourceUpdateParams"]


class DataSourceUpdateParams(TypedDict, total=False):
    name: Optional[str]
    """The name of the data source"""

    metadata: object
    """The metadata of the data source"""

    auth_params: Optional[DataSourceOauth2ParamsParam]
    """Authentication parameters for a OAuth data source."""
