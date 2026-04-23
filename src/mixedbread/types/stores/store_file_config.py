# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["StoreFileConfig"]


class StoreFileConfig(BaseModel):
    """Configuration for a file."""

    parsing_strategy: Optional[Literal["fast", "high_quality"]] = None
    """Strategy for adding the file, this overrides the store-level default"""
