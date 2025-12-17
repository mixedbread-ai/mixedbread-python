# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["FileUpdateParams"]


class FileUpdateParams(TypedDict, total=False):
    store_identifier: Required[str]
    """The ID or name of the store"""

    metadata: Optional[Dict[str, object]]
    """Updated metadata for the file"""
