# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ConnectorUpdateParams"]


class ConnectorUpdateParams(TypedDict, total=False):
    data_source_id: Required[str]
    """The ID of the data source to update a connector for"""

    name: Optional[str]
    """The name of the connector"""

    metadata: Optional[Dict[str, object]]
    """The metadata of the connector"""

    trigger_sync: Optional[bool]
    """Whether the connector should be synced after update"""

    polling_interval: Optional[str]
    """The polling interval of the connector"""
