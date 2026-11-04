# File generated from our OpenAPI spec by sdkgen. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .store_file_config_param import StoreFileConfigParam

__all__ = ["FileBatchCreateParams", "File"]


class File(TypedDict, total=False):
    """Files to add"""

    file_id: Required[str]
    """ID of the file to add"""

    external_id: Optional[str]
    """External identifier for this file in the store"""

    metadata: object
    """Optional metadata for the file"""

    config: StoreFileConfigParam
    """Configuration for adding the file"""


class FileBatchCreateParams(TypedDict, total=False):
    files: Required[Iterable[File]]
    """Files to add"""
