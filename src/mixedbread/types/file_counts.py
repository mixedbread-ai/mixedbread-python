# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["FileCounts"]


class FileCounts(BaseModel):
    in_progress: Optional[int] = None
    """Number of files currently being processed"""

    cancelled: Optional[int] = None
    """Number of files whose processing was cancelled"""

    completed: Optional[int] = None
    """Number of successfully processed files"""

    failed: Optional[int] = None
    """Number of files that failed processing"""

    total: Optional[int] = None
    """Total number of files"""
