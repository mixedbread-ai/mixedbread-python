# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

__all__ = ["ConnectorCreateParams"]


class ConnectorCreateParams(TypedDict, total=False):
    store_id: Required[str]
    """The ID of the store"""

    name: str
    """The name of the connector"""

    trigger_sync: bool
    """Whether the connector should be synced after creation"""

    metadata: object
    """The metadata of the connector"""

    polling_interval: Union[int, str, None]
    """Polling interval for the connector.

    Defaults to 30 minutes if not specified. Can be provided as:

    - int: Number of seconds (e.g., 1800 for 30 minutes)
    - str: Duration string (e.g., '30m', '1h', '2d') or ISO 8601 format (e.g.,
      'PT30M', 'P1D') Valid range: 15 seconds to 30 days
    """
