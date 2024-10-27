# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ParseCreateJobParams"]


class ParseCreateJobParams(TypedDict, total=False):
    file_id: Required[str]
    """The ID of the file to parse"""

    chunking_strategy: Literal["page"]
    """The strategy to use for chunking the content"""

    element_types: Optional[List[str]]
    """The elements to extract from the document"""

    return_format: Literal["html", "markdown", "plain"]
    """The format of the returned content"""
