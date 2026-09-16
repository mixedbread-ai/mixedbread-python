# File generated from our OpenAPI spec by sdkgen. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["StoreCopyParams"]


class StoreCopyParams(TypedDict, total=False):
    name: Required[str]
    """Name for the copy.

    Can only contain lowercase letters, numbers, periods (.), and hyphens (-).
    """

    description: Optional[str]
    """Description of the copy; defaults to the source store's description"""

    metadata: object
    """Metadata for the copy; defaults to the source store's metadata"""

    tags: Optional[SequenceNotStr[str]]
    """Tags for the copy; defaults to the source store's tags"""
