# File generated from our OpenAPI spec by sdkgen. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .store_file_status import StoreFileStatus

__all__ = ["StoreFileBatch", "Data", "DataError"]


class DataError(BaseModel):
    """Why an item was not added, with the error code the single-file endpoint returns."""

    code: str
    """Error code"""

    message: str
    """Error message"""


class Data(BaseModel):
    """Outcome of each item, in request order"""

    file_id: str
    """ID of the file the item named"""

    store_file_id: Optional[str] = None
    """ID of the created store file"""

    status: Optional[StoreFileStatus] = None
    """The lifecycle of a unit of background work.

    One vocabulary for every job family. The database keeps a separate enum type per
    table (``parsing_job_status``, ``store_file_status``, ...) but they all carry
    these values, so the aliases below are this enum rather than copies of
    it. :class:`SyncStatus` is this set plus ``IDLE`` for connectors, which have a
    resting state between runs.
    """

    error: Optional[DataError] = None
    """Why an item was not added, with the error code the single-file endpoint returns."""


class StoreFileBatch(BaseModel):
    """Outcome of adding a batch of files to a store."""

    data: List[Data]
    """Outcome of each item, in request order"""

    object: Optional[Literal["store.file_batch"]] = None
    """Type of the object"""
