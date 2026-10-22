from typing import List
from unittest.mock import Mock, AsyncMock, patch

import pytest

from mixedbread.lib.stores import StoreHelpers, AsyncStoreHelpers
from mixedbread.types.store import Store


def _store(status: str) -> Store:
    return Store.construct(id="vs_copy", name="copy", status=status)


class _Stores(StoreHelpers):
    def __init__(self, statuses: List[str]) -> None:
        self.retrieve_mock = Mock(side_effect=[_store(status) for status in statuses])
        self.copy_mock = Mock(return_value=_store("in_progress"))
        self.retrieve = self.retrieve_mock
        self.copy = self.copy_mock


class _AsyncStores(AsyncStoreHelpers):
    def __init__(self, statuses: List[str]) -> None:
        self.retrieve_mock = AsyncMock(side_effect=[_store(status) for status in statuses])
        self.copy_mock = AsyncMock(return_value=_store("in_progress"))
        self.retrieve = self.retrieve_mock
        self.copy = self.copy_mock


def test_copy_and_poll_polls_the_new_store_until_it_settles() -> None:
    stores = _Stores(["in_progress", "in_progress", "completed"])

    result = stores.copy_and_poll("vs_source", name="copy", poll_interval_ms=1)

    stores.copy_mock.assert_called_once()
    assert stores.copy_mock.call_args.args == ("vs_source",)
    assert stores.copy_mock.call_args.kwargs["name"] == "copy"
    assert stores.retrieve_mock.call_count == 3
    assert stores.retrieve_mock.call_args.args == ("vs_copy",)
    assert result.status == "completed"


def test_poll_returns_a_failed_copy() -> None:
    stores = _Stores(["in_progress", "failed"])

    assert stores.poll("vs_copy", poll_interval_ms=1).status == "failed"


def test_poll_honors_zero_interval() -> None:
    stores = _Stores(["in_progress", "completed"])

    with patch("time.sleep") as sleep_mock:
        assert stores.poll("vs_copy", poll_interval_ms=0).status == "completed"

    sleep_mock.assert_called_once_with(0.0)


def test_poll_honors_zero_timeout() -> None:
    stores = _Stores(["in_progress", "in_progress", "completed"])

    with pytest.raises(TimeoutError):
        stores.poll("vs_copy", poll_interval_ms=1, poll_timeout_ms=0)


@pytest.mark.asyncio
async def test_async_copy_and_poll() -> None:
    stores = _AsyncStores(["in_progress", "completed"])

    result = await stores.copy_and_poll("vs_source", name="copy", poll_interval_ms=1)

    assert result.status == "completed"
    assert stores.retrieve_mock.await_count == 2


@pytest.mark.asyncio
async def test_async_poll_honors_zero_interval() -> None:
    stores = _AsyncStores(["in_progress", "completed"])

    with patch("asyncio.sleep", new=AsyncMock()) as sleep_mock:
        assert (await stores.poll("vs_copy", poll_interval_ms=0)).status == "completed"

    sleep_mock.assert_called_once_with(0.0)


@pytest.mark.asyncio
async def test_async_poll_honors_zero_timeout() -> None:
    stores = _AsyncStores(["in_progress", "in_progress", "completed"])

    with pytest.raises(TimeoutError):
        await stores.poll("vs_copy", poll_interval_ms=1, poll_timeout_ms=0)
