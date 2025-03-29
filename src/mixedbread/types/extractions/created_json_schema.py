# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from ..._models import BaseModel

__all__ = ["CreatedJsonSchema"]


class CreatedJsonSchema(BaseModel):
    json_schema: Dict[str, object]
    """The created JSON schema"""
