# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["ContextualizationConfigParam"]


class ContextualizationConfigParam(TypedDict, total=False):
    with_metadata: Union[bool, SequenceNotStr[str]]
    """Include all metadata or specific fields in the contextualization.

    Supports dot notation for nested fields (e.g., 'author.name'). When True, all
    metadata is included (flattened). When a list, only specified fields are
    included.
    """

    with_file_context: bool
    """
    Use an LLM to generate a short context for each text chunk that situates it
    within the full document, improving retrieval accuracy. Only applies to text
    content during non-sliced ingestion.
    """
