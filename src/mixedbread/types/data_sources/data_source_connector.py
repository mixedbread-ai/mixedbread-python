# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DataSourceConnector"]


class DataSourceConnector(BaseModel):
    id: str
    """The ID of the connector"""

    created_at: datetime
    """The creation time of the connector"""

    updated_at: datetime
    """The last update time of the connector"""

    vector_store_id: str
    """The ID of the vector store"""

    data_source_id: str
    """The ID of the data source"""

    name: Optional[str] = None
    """The name of the connector"""

    metadata: object
    """The metadata of the connector"""

    polling_interval: str
    """The polling interval of the connector"""

    started_at: Optional[datetime] = None
    """The start time of the connector"""

    finished_at: Optional[datetime] = None
    """The finish time of the connector"""

    last_synced_at: Optional[datetime] = None
    """The last sync time of the connector"""

    status: Literal["idle", "pending", "in_progress", "cancelled", "completed", "failed"]
    """The sync status of the connector"""

    error: Optional[Dict[str, object]] = None
    """The sync error of the connector"""

    object: Optional[Literal["data_source.connector"]] = None
    """The type of the object"""
