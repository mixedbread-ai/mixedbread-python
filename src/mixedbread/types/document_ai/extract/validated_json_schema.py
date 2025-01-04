# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["ValidatedJsonSchema"]


class ValidatedJsonSchema(BaseModel):
    is_valid: bool
    """Whether the schema is valid"""

    json_schema: object
    """The schema definition"""

    errors: Optional[List[str]] = None
    """List of validation errors if any"""
