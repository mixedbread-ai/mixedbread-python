# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TextInputParam"]


class TextInputParam(TypedDict, total=False):
    type: Literal["text"]
    """Input type identifier"""

    text: Required[str]
    """Text content to process"""
