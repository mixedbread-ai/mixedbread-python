# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .store_file_config_param import StoreFileConfigParam

__all__ = ["FileCreateParams"]


class FileCreateParams(TypedDict, total=False):
    metadata: object
    """Optional metadata for the file"""

    config: StoreFileConfigParam
    """Configuration for adding the file"""

    external_id: Optional[str]
    """External identifier for this file in the store"""

    overwrite: bool
    """If true, overwrite an existing file with the same external_id"""

    file_id: Required[str]
    """ID of the file to add"""

    experimental: Optional[StoreFileConfigParam]
    """Configuration for a file."""
