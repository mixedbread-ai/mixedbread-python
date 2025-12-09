# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TextInputParam"]


class TextInputParam(TypedDict, total=False):
    """Model for text input validation.

    Attributes:
        type: Input type identifier, always "text"
        text: The actual text content, with length and whitespace constraints
    """

    type: Literal["text"]
    """Input type identifier"""

    text: Required[str]
    """Text content to process"""
