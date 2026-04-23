# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DataSourceAPIKeyParams"]


class DataSourceAPIKeyParams(BaseModel):
    """Authentication parameters for a API key data source."""

    type: Optional[Literal["api_key"]] = None

    api_key: str
    """The API key"""
