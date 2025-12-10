# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from ..._models import BaseModel

__all__ = ["CreatedJsonSchema"]


class CreatedJsonSchema(BaseModel):
    """Result of creating a JSON schema."""

    json_schema: Dict[str, object]
    """The created JSON schema"""
