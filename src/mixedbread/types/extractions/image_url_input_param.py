# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ImageURLInputParam", "ImageURL"]


class ImageURL(TypedDict, total=False):
    url: Required[str]
    """The image URL. Can be either a URL or a Data URI."""


class ImageURLInputParam(TypedDict, total=False):
    type: Literal["image_url"]
    """Input type identifier"""

    image_url: Required[ImageURL]
    """The image input specification."""
