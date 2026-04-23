# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AudioURL"]


class AudioURL(BaseModel):
    """Model for audio URL validation."""

    url: str
    """The audio URL. Can be either a URL or a Data URI."""
