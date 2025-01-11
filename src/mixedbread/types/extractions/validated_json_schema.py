# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["ValidatedJsonSchema"]


class ValidatedJsonSchema(BaseModel):
    errors: List[str]
    """List of validation errors"""

    is_valid: bool
    """Whether the schema is valid"""

    json_schema: object
    """The validated JSON schema"""
