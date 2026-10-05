# File generated from our OpenAPI spec by sdkgen. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel
from .contextualization_config import ContextualizationConfig

__all__ = ["StoreConfig", "Contextualization"]

Contextualization: TypeAlias = Union[bool, ContextualizationConfig]


class StoreConfig(BaseModel):
    """Configuration for a store."""

    contextualization: Optional[Contextualization] = None
    """Include additional context when embedding chunks."""

    lsf: Optional[Dict[str, object]] = None
    """Learned-scoring-function settings a store opts into; an empty object enables it."""
