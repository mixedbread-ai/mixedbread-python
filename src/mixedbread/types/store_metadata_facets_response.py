# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["StoreMetadataFacetsResponse"]


class StoreMetadataFacetsResponse(BaseModel):
    facets: Dict[str, Dict[str, object]]
    """Metadata facets"""
