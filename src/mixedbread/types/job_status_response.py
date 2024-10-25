# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["JobStatusResponse", "Data"]


class Data(BaseModel):
    job_id: str

    status: str


class JobStatusResponse(BaseModel):
    data: Data
