# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DataSourceOauth2Params"]


class DataSourceOauth2Params(BaseModel):
    type: Optional[Literal["oauth2"]] = None

    created_at: Optional[datetime] = None
    """The timestamp when the OAuth2 credentials were created"""

    client_id: str
    """The OAuth2 client ID"""

    client_secret: str
    """The OAuth2 client secret"""

    redirect_uri: str
    """The OAuth2 redirect URI"""

    scope: str
    """The OAuth2 scope"""

    access_token: Optional[str] = None
    """The OAuth2 access token"""

    refresh_token: Optional[str] = None
    """The OAuth2 refresh token"""

    token_type: Optional[str] = None
    """The OAuth2 token type"""

    expires_on: Optional[datetime] = None
    """The OAuth2 token expiration timestamp"""
