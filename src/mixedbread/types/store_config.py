# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel
from .contextualization_config import ContextualizationConfig

__all__ = ["StoreConfig", "Contextualization"]

Contextualization: TypeAlias = Union[bool, ContextualizationConfig]


class StoreConfig(BaseModel):
    """Configuration for a store."""

    contextualization: Optional[Contextualization] = None
    """Contextualize files with metadata"""

    save_content: Optional[bool] = None
    """Whether to save original content in the store.

    When False, only vectors are indexed without the original content (index-only
    mode). This is useful for data privacy. Note: Reranking is not supported when
    content is not saved.
    """
