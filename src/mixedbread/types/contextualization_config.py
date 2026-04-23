# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from .._models import BaseModel

__all__ = ["ContextualizationConfig"]


class ContextualizationConfig(BaseModel):
    with_metadata: Union[bool, List[str], None] = None
    """Include all metadata or specific fields in the contextualization.

    Supports dot notation for nested fields (e.g., 'author.name'). When True, all
    metadata is included (flattened). When a list, only specified fields are
    included.
    """

    with_file_context: Optional[bool] = None
    """
    Use an LLM to generate a short context for each text chunk that situates it
    within the full document, improving retrieval accuracy. Only applies to text
    content during non-sliced ingestion.
    """
