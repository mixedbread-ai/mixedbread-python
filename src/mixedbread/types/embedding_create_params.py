# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["EmbeddingCreateParams", "Input", "InputTextInput"]


class EmbeddingCreateParams(TypedDict, total=False):
    input: Required[Input]
    """The input to create embeddings for."""

    model: Required[str]
    """The model to use for creating embeddings."""

    dimensions: Optional[int]
    """The number of dimensions to use for the embeddings."""

    encoding_format: Union[
        Literal["float", "float16", "base64", "binary", "ubinary", "int8", "uint8"],
        List[Literal["float", "float16", "base64", "binary", "ubinary", "int8", "uint8"]],
    ]
    """The encoding format of the embeddings."""

    normalized: bool
    """Whether to normalize the embeddings."""

    prompt: Optional[str]
    """The prompt to use for the embedding creation."""

    truncation_strategy: Literal["none", "start", "end"]
    """The truncation strategy to use for the input."""


class InputTextInput(TypedDict, total=False):
    text: Required[str]
    """The text to be processed"""


Input: TypeAlias = Union[str, InputTextInput, object]
