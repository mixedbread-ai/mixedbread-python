# File generated from our OpenAPI spec by sdkgen. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import TypeAlias, TypedDict

from .contextualization_config_param import ContextualizationConfigParam

__all__ = ["StoreConfigParam", "Contextualization"]

Contextualization: TypeAlias = Union[bool, ContextualizationConfigParam]


class StoreConfigParam(TypedDict, total=False):
    """Configuration for a store."""

    contextualization: Contextualization
    """Include additional context when embedding chunks."""

    save_content: bool
    """Whether to save original content in the store.

    When False, only vectors are indexed without the original content (index-only
    mode). This is useful for data privacy. Note: Reranking is not supported when
    content is not saved.
    """

    lsf: Optional[Dict[str, object]]
    """Learned-scoring-function settings a store opts into; an empty object enables it."""
