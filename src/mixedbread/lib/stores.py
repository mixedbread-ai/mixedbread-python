"""Hand-written helpers mixed into the generated ``stores`` resource.

The generator emits ``StoresResourceBase``/``AsyncStoresResourceBase`` with the API methods and
declares ``StoresResource(StoreHelpers, StoresResourceBase)``, so anything defined here is part of
``client.stores`` and may call the generated methods through ``self``.
"""

from __future__ import annotations

import functools
from typing import TYPE_CHECKING, Any, Optional

from . import polling
from .._types import Omit, NotGiven, omit, not_given
from ..types.store import Store

if TYPE_CHECKING:
    from ..resources.stores.stores import StoresResourceBase, AsyncStoresResourceBase

    _SyncBase = StoresResourceBase
    _AsyncBase = AsyncStoresResourceBase
else:
    _SyncBase = object
    _AsyncBase = object

_DEFAULT_POLL_INTERVAL_MS = 1000


def _is_settled(store: Store) -> bool:
    return store.status != "in_progress"


class StoreHelpers(_SyncBase):
    def poll(
        self,
        store_identifier: str,
        *,
        poll_interval_ms: int | NotGiven = not_given,
        poll_timeout_ms: float | NotGiven = not_given,
        **kwargs: Any,
    ) -> Store:
        """Poll a store until it is no longer ``in_progress``.

        A store is ``in_progress`` while a copy fills it; it settles as ``completed`` or ``failed``
        (``copy_state`` then carries the error).

        Args:
            store_identifier: The ID or name of the store to poll
            poll_interval_ms: The interval between polls in milliseconds (default 1000)
            poll_timeout_ms: The maximum time to poll for in milliseconds (default: no timeout)
        Returns:
            The store once it has settled
        """
        polling_interval_ms = poll_interval_ms or _DEFAULT_POLL_INTERVAL_MS
        polling_timeout_ms = poll_timeout_ms or None
        return polling.poll(
            fn=functools.partial(self.retrieve, store_identifier, **kwargs),
            condition=_is_settled,
            interval_seconds=polling_interval_ms / 1000,
            timeout_seconds=polling_timeout_ms / 1000 if polling_timeout_ms else None,
        )

    def copy_and_poll(
        self,
        store_identifier: str,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        metadata: object | Omit = omit,
        poll_interval_ms: int | NotGiven = not_given,
        poll_timeout_ms: float | NotGiven = not_given,
        **kwargs: Any,
    ) -> Store:
        """Copy a store into a new store and wait until the copy has finished.

        Returns the new store; check ``status`` (``completed`` or ``failed``) before using it.
        """
        copy = self.copy(store_identifier, name=name, description=description, metadata=metadata, **kwargs)
        return self.poll(copy.id, poll_interval_ms=poll_interval_ms, poll_timeout_ms=poll_timeout_ms, **kwargs)


class AsyncStoreHelpers(_AsyncBase):
    async def poll(
        self,
        store_identifier: str,
        *,
        poll_interval_ms: int | NotGiven = not_given,
        poll_timeout_ms: float | NotGiven = not_given,
        **kwargs: Any,
    ) -> Store:
        """Poll a store until it is no longer ``in_progress``."""
        polling_interval_ms = poll_interval_ms or _DEFAULT_POLL_INTERVAL_MS
        polling_timeout_ms = poll_timeout_ms or None
        return await polling.poll_async(
            fn=functools.partial(self.retrieve, store_identifier, **kwargs),
            condition=_is_settled,
            interval_seconds=polling_interval_ms / 1000,
            timeout_seconds=polling_timeout_ms / 1000 if polling_timeout_ms else None,
        )

    async def copy_and_poll(
        self,
        store_identifier: str,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        metadata: object | Omit = omit,
        poll_interval_ms: int | NotGiven = not_given,
        poll_timeout_ms: float | NotGiven = not_given,
        **kwargs: Any,
    ) -> Store:
        """Copy a store into a new store and wait until the copy has finished."""
        copy = await self.copy(store_identifier, name=name, description=description, metadata=metadata, **kwargs)
        return await self.poll(copy.id, poll_interval_ms=poll_interval_ms, poll_timeout_ms=poll_timeout_ms, **kwargs)
