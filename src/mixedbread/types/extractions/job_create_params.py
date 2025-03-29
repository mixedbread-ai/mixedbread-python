# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["JobCreateParams"]


class JobCreateParams(TypedDict, total=False):
    file_id: Required[str]
    """The ID of the file to extract from"""

    json_schema: Required[Dict[str, object]]
    """The JSON schema to use for extraction"""
