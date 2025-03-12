# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["EmbeddingCreateParams", "Input", "InputImageURLInput", "InputImageURLInputImage", "InputTextInput"]


class EmbeddingCreateParams(TypedDict, total=False):
    model: Required[str]
    """The model to use for creating embeddings."""

    input: Required[Input]
    """The input to create embeddings for."""

    dimensions: Optional[int]
    """The number of dimensions to use for the embeddings."""

    prompt: Optional[str]
    """The prompt to use for the embedding creation."""

    normalized: bool
    """Whether to normalize the embeddings."""

    encoding_format: Union[
        Literal["float", "float16", "base64", "binary", "ubinary", "int8", "uint8"],
        List[Literal["float", "float16", "base64", "binary", "ubinary", "int8", "uint8"]],
    ]
    """The encoding format of the embeddings."""


class InputImageURLInputImage(TypedDict, total=False):
    url: Required[str]
    """The image URL. Can be either a URL or a Data URI."""


class InputImageURLInput(TypedDict, total=False):
    type: Literal["image_url"]
    """Input type identifier"""

    image: Required[InputImageURLInputImage]
    """The image input specification."""


class InputTextInput(TypedDict, total=False):
    type: Literal["text"]
    """Input type identifier"""

    text: Required[str]
    """Text content to process"""


Input: TypeAlias = Union[str, InputImageURLInput, InputTextInput]
