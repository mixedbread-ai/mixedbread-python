# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ImageURLOutput"]


class ImageURLOutput(BaseModel):
    """Model for image URL validation."""

    url: str
    """The image URL. Can be either a URL or a Data URI."""

    format: Optional[str] = None
    """The image format/mimetype"""
