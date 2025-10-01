# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["StoreFileStatus"]

StoreFileStatus: TypeAlias = Literal["pending", "in_progress", "cancelled", "completed", "failed"]
