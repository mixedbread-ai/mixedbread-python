# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["FileRetrieveParams"]


class FileRetrieveParams(TypedDict, total=False):
    store_identifier: Required[str]
    """The ID or name of the store"""

    return_chunks: Union[bool, Iterable[int]]
    """Whether to return the chunks for the file.

    If a list of integers is provided, only the chunks at the specified indices will
    be returned.
    """
