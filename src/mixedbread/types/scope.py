# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Scope"]


class Scope(BaseModel):
    method: Literal["read", "write", "delete", "list", "create", "search"]

    resource_type: Optional[Literal["store"]] = None

    resource_id: Optional[str] = None
