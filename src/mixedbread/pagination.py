# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "LimitOffsetPagination",
    "SyncLimitOffset",
    "AsyncLimitOffset",
    "CursorPagination",
    "SyncCursor",
    "AsyncCursor",
]

_T = TypeVar("_T")


class LimitOffsetPagination(BaseModel):
    total: Optional[int] = None

    offset: Optional[int] = None


class SyncLimitOffset(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    pagination: Optional[LimitOffsetPagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = None
        if self.pagination is not None:
            if self.pagination.offset is not None:
                offset = self.pagination.offset
        if offset is None:
            return None  # type: ignore[unreachable]

        length = len(self._get_page_items())
        current_count = offset + length

        total = None
        if self.pagination is not None:
            if self.pagination.total is not None:
                total = self.pagination.total
        if total is None:
            return None

        if current_count < total:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncLimitOffset(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    pagination: Optional[LimitOffsetPagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = None
        if self.pagination is not None:
            if self.pagination.offset is not None:
                offset = self.pagination.offset
        if offset is None:
            return None  # type: ignore[unreachable]

        length = len(self._get_page_items())
        current_count = offset + length

        total = None
        if self.pagination is not None:
            if self.pagination.total is not None:
                total = self.pagination.total
        if total is None:
            return None

        if current_count < total:
            return PageInfo(params={"offset": current_count})

        return None


class CursorPagination(BaseModel):
    first_cursor: Optional[str] = None

    last_cursor: Optional[str] = None

    has_more: Optional[bool] = None

    total: Optional[int] = None


class SyncCursor(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    pagination: Optional[CursorPagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def has_next_page(self) -> bool:
        has_more = None
        if self.pagination is not None:
            if self.pagination.has_more is not None:
                has_more = self.pagination.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        if self._options.params.get("before"):
            first_cursor = None
            if self.pagination is not None:
                if self.pagination.first_cursor is not None:
                    first_cursor = self.pagination.first_cursor
            if not first_cursor:
                return None

            return PageInfo(params={"before": first_cursor})

        last_cursor = None
        if self.pagination is not None:
            if self.pagination.last_cursor is not None:
                last_cursor = self.pagination.last_cursor
        if not last_cursor:
            return None

        return PageInfo(params={"after": last_cursor})


class AsyncCursor(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    pagination: Optional[CursorPagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def has_next_page(self) -> bool:
        has_more = None
        if self.pagination is not None:
            if self.pagination.has_more is not None:
                has_more = self.pagination.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        if self._options.params.get("before"):
            first_cursor = None
            if self.pagination is not None:
                if self.pagination.first_cursor is not None:
                    first_cursor = self.pagination.first_cursor
            if not first_cursor:
                return None

            return PageInfo(params={"before": first_cursor})

        last_cursor = None
        if self.pagination is not None:
            if self.pagination.last_cursor is not None:
                last_cursor = self.pagination.last_cursor
        if not last_cursor:
            return None

        return PageInfo(params={"after": last_cursor})
