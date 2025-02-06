# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .extraction_result import ExtractionResult

__all__ = ["ExtractionJob"]


class ExtractionJob(BaseModel):
    result: Optional[ExtractionResult] = None
    """Result of an extraction operation."""
