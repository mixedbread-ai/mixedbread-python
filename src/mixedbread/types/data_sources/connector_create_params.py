# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ConnectorCreateParams"]


class ConnectorCreateParams(TypedDict, total=False):
    vector_store_id: Required[str]
    """The ID of the vector store"""

    name: str
    """The name of the connector"""

    trigger_sync: bool
    """Whether the connector should be synced after creation"""

    metadata: object
    """The metadata of the connector"""

    polling_interval: Optional[str]
    """The polling interval of the connector"""
