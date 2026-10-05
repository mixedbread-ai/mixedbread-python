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

    lsf: Optional[Dict[str, object]]
    """Learned-scoring-function settings a store opts into; an empty object enables it."""
