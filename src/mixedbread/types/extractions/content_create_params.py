# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .text_input_param import TextInputParam
from .image_url_input_param import ImageURLInputParam

__all__ = ["ContentCreateParams", "ContentUnionMember2"]


class ContentCreateParams(TypedDict, total=False):
    content: Required[Union[str, List[str], Iterable[ContentUnionMember2]]]
    """The content to extract from"""

    json_schema: Required[Dict[str, object]]
    """The JSON schema to use for extraction"""

    instructions: Optional[str]
    """Additional instructions for the extraction"""


ContentUnionMember2: TypeAlias = Union[TextInputParam, ImageURLInputParam]
