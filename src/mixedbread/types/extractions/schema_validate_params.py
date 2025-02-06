# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SchemaValidateParams"]


class SchemaValidateParams(TypedDict, total=False):
    json_schema: Required[object]
    """The JSON schema to validate"""
