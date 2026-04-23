# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["VideoURL"]


class VideoURL(BaseModel):
    """Model for video URL validation."""

    url: str
    """The video URL. Can be either a URL or a Data URI."""
