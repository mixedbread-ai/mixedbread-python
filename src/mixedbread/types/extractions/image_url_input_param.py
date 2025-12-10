# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ImageURLInputParam", "ImageURL"]


class ImageURL(TypedDict, total=False):
    """The image input specification."""

    url: Required[str]
    """The image URL. Can be either a URL or a Data URI."""

    format: str
    """The image format/mimetype"""


class ImageURLInputParam(TypedDict, total=False):
    """Model for image input validation."""

    type: Literal["image_url"]
    """Input type identifier"""

    image_url: Required[ImageURL]
    """The image input specification."""
