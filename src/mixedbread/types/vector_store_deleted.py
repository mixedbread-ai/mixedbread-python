# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["VectorStoreDeleted"]


class VectorStoreDeleted(BaseModel):
    id: str

    deleted: bool
