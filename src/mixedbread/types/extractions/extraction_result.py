# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["ExtractionResult"]


class ExtractionResult(BaseModel):
    data: object

    warnings: List[str]
