# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Usage"]


class Usage(BaseModel):
    prompt_tokens: int
    """The number of tokens used for the prompt"""

    total_tokens: int
    """The total number of tokens used"""

    completion_tokens: Optional[int] = None
    """The number of tokens used for the completion"""
