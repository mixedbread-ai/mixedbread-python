# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .oauth2_params import Oauth2Params

__all__ = ["LinearDataSourceParam"]


class LinearDataSourceParam(TypedDict, total=False):
    """Parameters for creating or updating a Linear data source."""

    type: Literal["linear"]
    """The type of data source to create"""

    name: Required[str]
    """The name of the data source"""

    metadata: object
    """The metadata of the data source"""

    auth_params: Optional[Oauth2Params]
    """Base class for OAuth2 create or update parameters."""
