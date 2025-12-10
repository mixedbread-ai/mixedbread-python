# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import TypeAlias, TypedDict

from .._types import SequenceNotStr
from .expires_after_param import ExpiresAfterParam

__all__ = ["StoreCreateParams", "Config", "ConfigContextualization", "ConfigContextualizationContextualizationConfig"]


class StoreCreateParams(TypedDict, total=False):
    name: Optional[str]
    """Name for the new store"""

    description: Optional[str]
    """Description of the store"""

    is_public: bool
    """Whether the store can be accessed by anyone with valid login credentials"""

    expires_after: Optional[ExpiresAfterParam]
    """Represents an expiration policy for a store."""

    metadata: object
    """Optional metadata key-value pairs"""

    config: Optional[Config]
    """Configuration for a store."""

    file_ids: Optional[SequenceNotStr[str]]
    """Optional list of file IDs"""


class ConfigContextualizationContextualizationConfig(TypedDict, total=False):
    with_metadata: Union[bool, SequenceNotStr[str]]
    """Include all metadata or specific fields in the contextualization.

    Supports dot notation for nested fields (e.g., 'author.name'). When True, all
    metadata is included (flattened). When a list, only specified fields are
    included.
    """


ConfigContextualization: TypeAlias = Union[bool, ConfigContextualizationContextualizationConfig]


class Config(TypedDict, total=False):
    """Configuration for a store."""

    contextualization: ConfigContextualization
    """Contextualize files with metadata"""
