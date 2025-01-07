# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["LimitOffsetPagination", "SyncLimitOffset", "AsyncLimitOffset"]

_T = TypeVar("_T")


class LimitOffsetPagination(BaseModel):
    offset: Optional[int] = None
    total: Optional[int] = None


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
        count = None
        if self.pagination is not None:
            if self.pagination.count is not None:
                count = self.pagination.count
        if count is None:
            return None

        length = len(self._get_page_items())
        current_count = count + length

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
        count = None
        if self.pagination is not None:
            if self.pagination.count is not None:
                count = self.pagination.count
        if count is None:
            return None

        length = len(self._get_page_items())
        current_count = count + length

        total = None
        if self.pagination is not None:
            if self.pagination.total is not None:
                total = self.pagination.total
        if total is None:
            return None

        if current_count < total:
            return PageInfo(params={"offset": current_count})

        return None
