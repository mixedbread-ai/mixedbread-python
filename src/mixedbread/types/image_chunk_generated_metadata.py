# File generated from our OpenAPI spec by sdkgen. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ImageChunkGeneratedMetadata", "Layout", "LayoutElement"]


class LayoutElement(BaseModel):
    """A single detected layout element and its location on the page image."""

    bbox: List[object]

    type: str

    text: Optional[str] = None


class Layout(BaseModel):
    """Per-page layout for chunks parsed in high-quality (visual) mode.

    ``elements`` are ordered by reading order (list position == reading order).
    ``width``/``height`` are the page-image dimensions the ``bbox`` coords are
    relative to, so consumers can normalize/render without a second fetch.

    Layout is part of the generated metadata payload and is returned with the chunk
    whenever present.
    """

    width: Optional[int] = None

    height: Optional[int] = None

    elements: Optional[List[LayoutElement]] = None


class ImageChunkGeneratedMetadata(BaseModel):
    type: Optional[Literal["image"]] = None

    file_type: Optional[str] = None

    file_size: Optional[int] = None

    width: Optional[int] = None

    height: Optional[int] = None

    file_extension: Optional[str] = None

    layout: Optional[Layout] = None
    """Per-page layout for chunks parsed in high-quality (visual) mode.

    ``elements`` are ordered by reading order (list position == reading order).
    ``width``/``height`` are the page-image dimensions the ``bbox`` coords are
    relative to, so consumers can normalize/render without a second fetch.

    Layout is part of the generated metadata payload and is returned with the chunk
    whenever present.
    """

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
