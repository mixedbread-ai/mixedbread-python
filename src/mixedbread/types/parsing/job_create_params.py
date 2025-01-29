# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["JobCreateParams"]


class JobCreateParams(TypedDict, total=False):
    file_id: Required[str]
    """The ID of the file to parse"""

    element_types: Optional[
        List[
            Literal[
                "caption",
                "footnote",
                "formula",
                "list-item",
                "page-footer",
                "page-header",
                "picture",
                "section-header",
                "table",
                "text",
                "title",
            ]
        ]
    ]
    """The elements to extract from the document"""

    chunking_strategy: Literal["page"]
    """The strategy to use for chunking the content"""

    return_format: Literal["html", "markdown", "plain"]
    """The format of the returned content"""
