# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["Result"]


class Result(BaseModel):
    data: object
    """The extracted data from the extraction operation"""
