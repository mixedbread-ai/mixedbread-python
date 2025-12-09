# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["InfoResponse"]


class InfoResponse(BaseModel):
    """Info Pydantic Response Service Message"""

    name: str

    version: str
