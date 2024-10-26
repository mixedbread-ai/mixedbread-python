# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["BaseStatusCheckResponse"]


class BaseStatusCheckResponse(BaseModel):
    name: str

    version: str
