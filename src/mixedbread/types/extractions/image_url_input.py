# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ImageURLInput", "ImageURL"]


class ImageURL(BaseModel):
    url: str
    """The image URL. Can be either a URL or a Data URI."""


class ImageURLInput(BaseModel):
    type: Optional[Literal["image_url"]] = None
    """Input type identifier"""

    image_url: ImageURL
    """The image input specification."""
