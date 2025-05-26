# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .scored_text_input_chunk import ScoredTextInputChunk
from .scored_audio_url_input_chunk import ScoredAudioURLInputChunk
from .scored_image_url_input_chunk import ScoredImageURLInputChunk
from .scored_video_url_input_chunk import ScoredVideoURLInputChunk

__all__ = ["VectorStoreSearchResponse", "Data"]

Data: TypeAlias = Annotated[
    Union[ScoredTextInputChunk, ScoredImageURLInputChunk, ScoredAudioURLInputChunk, ScoredVideoURLInputChunk],
    PropertyInfo(discriminator="type"),
]


class VectorStoreSearchResponse(BaseModel):
    object: Optional[Literal["list"]] = None
    """The object type of the response"""

    data: List[Data]
    """The list of scored vector store file chunks"""
