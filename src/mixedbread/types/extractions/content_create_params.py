# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ContentCreateParams",
    "ContentUnionMember2",
    "ContentUnionMember2TextInput",
    "ContentUnionMember2ImageURLInput",
    "ContentUnionMember2ImageURLInputImageURL",
]


class ContentCreateParams(TypedDict, total=False):
    content: Required[Union[str, List[str], Iterable[ContentUnionMember2]]]
    """The content to extract from"""

    json_schema: Required[Dict[str, object]]
    """The JSON schema to use for extraction"""

    instructions: Optional[str]
    """Additional instructions for the extraction"""


class ContentUnionMember2TextInput(TypedDict, total=False):
    type: Literal["text"]
    """Input type identifier"""

    text: Required[str]
    """Text content to process"""


class ContentUnionMember2ImageURLInputImageURL(TypedDict, total=False):
    url: Required[str]
    """The image URL. Can be either a URL or a Data URI."""


class ContentUnionMember2ImageURLInput(TypedDict, total=False):
    type: Literal["image_url"]
    """Input type identifier"""

    image_url: Required[ContentUnionMember2ImageURLInputImageURL]
    """The image input specification."""


ContentUnionMember2: TypeAlias = Union[ContentUnionMember2TextInput, ContentUnionMember2ImageURLInput]
