# File generated from our OpenAPI spec by sdkgen. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EmailChunkGeneratedMetadata"]


class EmailChunkGeneratedMetadata(BaseModel):
    type: Optional[Literal["email"]] = None

    file_type: Optional[str] = None

    language: Optional[str] = None

    word_count: Optional[int] = None

    file_size: Optional[int] = None

    start_line: Optional[int] = None

    num_lines: Optional[int] = None

    file_extension: Optional[str] = None

    subject: Optional[str] = None

    from_email: Optional[str] = None

    to_emails: Optional[List[str]] = None

    cc_emails: Optional[List[str]] = None

    bcc_emails: Optional[List[str]] = None

    date: Optional[str] = None

    attachment_names: Optional[List[str]] = None

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
