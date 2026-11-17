"""Hand-written helpers for building mxjson files (``.mxjson`` / ``.mxjsonl``).

An mxjson file is a JSON array of items that is uploaded like any other file. A ``file`` item
carries a whole file as base64 (the shape of an OpenAI file input), which Mixedbread parses and chunks in the item's place;
``mxjson_file_item`` builds one.
"""

from __future__ import annotations

import os
import base64
import pathlib
from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes, FileContent

__all__ = ["MxjsonFile", "MxjsonFileItem", "mxjson_file_item"]


class MxjsonFile(TypedDict, total=False):
    """The file of an mxjson ``file`` item."""

    file_data: Required[str]
    """The file, as a base64 data URI (``data:application/pdf;base64,...``) or as plain base64.

    It cannot be another mxjson file.
    """

    filename: str
    """Filename of the file. Its type is detected from it when ``file_data`` is plain base64."""


class MxjsonFileItem(TypedDict, total=False):
    """An mxjson ``file`` item, which carries a file for Mixedbread to parse and chunk."""

    type: Required[Literal["file"]]

    file: Required[MxjsonFile]
    """The file the item carries."""

    generated_metadata: Dict[str, object]
    """Custom fields added to every chunk of the file."""


def _read(content: FileContent) -> bytes:
    if isinstance(content, bytes):
        return content
    if isinstance(content, os.PathLike):
        return pathlib.Path(content).read_bytes()
    data = content.read()
    if not isinstance(data, bytes):  # pyright: ignore[reportUnnecessaryIsInstance]
        raise TypeError("Expected a file opened in binary mode")
    return data


def _name(content: FileContent) -> Optional[str]:
    if isinstance(content, bytes):
        return None
    if isinstance(content, os.PathLike):
        return pathlib.Path(content).name
    name = getattr(content, "name", None)
    return os.path.basename(name) if isinstance(name, str) and name else None


def mxjson_file_item(
    file: FileTypes,
    *,
    filename: Optional[str] = None,
    mime_type: Optional[str] = None,
    generated_metadata: Optional[Dict[str, object]] = None,
) -> MxjsonFileItem:
    """Build an mxjson ``file`` item that carries ``file`` itself, base64 encoded.

    ``file`` is what an upload takes: bytes, a path, a binary file object, or a
    ``(filename, content, mime_type)`` tuple. ``filename`` and ``mime_type`` override what
    ``file`` says. A MIME type makes ``file_data`` a data URI; without one it is plain base64
    and Mixedbread detects the type from the filename and the bytes.

    The file is read into memory, and base64 makes it a third larger.
    """
    content: FileContent
    if isinstance(file, tuple):
        content = file[1]
        filename = filename or file[0]
        if len(file) > 2:
            mime_type = mime_type or file[2]  # type: ignore[misc]
    else:
        content = file
    filename = filename or _name(content)

    encoded = base64.b64encode(_read(content)).decode("ascii")
    carried: MxjsonFile = {"file_data": f"data:{mime_type};base64,{encoded}" if mime_type else encoded}
    if filename:
        carried["filename"] = filename
    item: MxjsonFileItem = {"type": "file", "file": carried}
    if generated_metadata is not None:
        item["generated_metadata"] = generated_metadata
    return item
