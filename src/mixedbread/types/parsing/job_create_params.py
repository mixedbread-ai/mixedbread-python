# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from .element_type import ElementType
from .return_format import ReturnFormat
from .chunking_strategy import ChunkingStrategy

__all__ = ["JobCreateParams"]


class JobCreateParams(TypedDict, total=False):
    file_id: Required[str]
    """The ID of the file to parse"""

    element_types: Optional[List[ElementType]]
    """The elements to extract from the document"""

    chunking_strategy: ChunkingStrategy
    """The strategy to use for chunking the content"""

    return_format: ReturnFormat
    """The format of the returned content"""

    mode: Literal["fast", "high_quality"]
    """The strategy to use for OCR"""
