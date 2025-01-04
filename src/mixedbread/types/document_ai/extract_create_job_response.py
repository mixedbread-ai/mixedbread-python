# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .result import Result
from ..._models import BaseModel

__all__ = ["ExtractCreateJobResponse", "RunningJob", "FailedJob", "SuccessfulExtractionJob"]


class RunningJob(BaseModel):
    id: str
    """The ID of the job"""

    created_at: Optional[datetime] = None
    """The creation time of the job"""

    errors: Optional[List[str]] = None
    """The errors of the job"""

    finished_at: Optional[datetime] = None
    """The finished time of the job"""

    object: Optional[Literal["job"]] = None
    """The type of the object"""

    result: Optional[builtins.object] = None
    """The result of the job"""

    status: Optional[Literal["pending", "running"]] = None
    """The status of the job"""


class FailedJob(BaseModel):
    id: str
    """The ID of the job"""

    errors: List[str]
    """The errors of the job"""

    created_at: Optional[datetime] = None
    """The creation time of the job"""

    finished_at: Optional[datetime] = None
    """The finished time of the job"""

    object: Optional[Literal["job"]] = None
    """The type of the object"""

    result: Optional[builtins.object] = None
    """The result of the job"""

    status: Optional[Literal["failed"]] = None
    """The status of the job"""


class SuccessfulExtractionJob(BaseModel):
    id: str
    """The ID of the job"""

    result: Result
    """The extracted data from the extraction operation"""

    created_at: Optional[datetime] = None
    """The creation time of the job"""

    errors: Optional[List[str]] = None
    """The errors of the job"""

    finished_at: Optional[datetime] = None
    """The finished time of the job"""

    object: Optional[Literal["job"]] = None
    """The type of the object"""

    status: Optional[Literal["successful"]] = None
    """The status of the job"""


ExtractCreateJobResponse: TypeAlias = Union[RunningJob, FailedJob, SuccessfulExtractionJob]
