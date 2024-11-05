# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["VectorStoreFileDeleted"]


class VectorStoreFileDeleted(BaseModel):
    id: str

    deleted: bool
