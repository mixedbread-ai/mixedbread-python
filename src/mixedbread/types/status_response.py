# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["StatusResponse"]


class StatusResponse(BaseModel):
    name: str

    version: str
