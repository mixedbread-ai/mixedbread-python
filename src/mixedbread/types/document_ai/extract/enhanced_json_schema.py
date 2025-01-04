# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ...._models import BaseModel

__all__ = ["EnhancedJsonSchema"]


class EnhancedJsonSchema(BaseModel):
    json_schema: object
    """The enhanced schema with enriched descriptions"""
