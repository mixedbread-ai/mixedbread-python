# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ClientEmbedParams"]


class ClientEmbedParams(TypedDict, total=False):
    model: Required[str]
    """The model to use for creating embeddings."""

    input: Required[Union[str, List[str]]]
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
    """The encoding format(s) of the embeddings.

    Can be a single format or a list of formats.
    """
