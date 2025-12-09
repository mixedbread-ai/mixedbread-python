# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from ..._models import BaseModel

__all__ = ["ExtractionResult"]


class ExtractionResult(BaseModel):
    """The result of an extraction job."""

    data: Dict[str, object]

    warnings: List[str]
