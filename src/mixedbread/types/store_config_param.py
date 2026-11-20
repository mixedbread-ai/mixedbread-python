# File generated from our OpenAPI spec by sdkgen. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias, TypedDict

from .contextualization_config_param import ContextualizationConfigParam

__all__ = ["StoreConfigParam", "Contextualization"]

Contextualization: TypeAlias = Union[bool, ContextualizationConfigParam]


class StoreConfigParam(TypedDict, total=False):
    """Configuration for a store."""

    contextualization: Contextualization
    """Include additional context when embedding chunks."""
