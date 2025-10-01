# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ScoredAudioURLInputChunk", "AudioURL"]


class AudioURL(BaseModel):
    url: str
    """The audio URL. Can be either a URL or a Data URI."""


class ScoredAudioURLInputChunk(BaseModel):
    chunk_index: int
    """position of the chunk in a file"""

    mime_type: Optional[str] = None
    """mime type of the chunk"""

    generated_metadata: Optional[Dict[str, object]] = None
    """metadata of the chunk"""

    model: Optional[str] = None
    """model used for this chunk"""

    score: float
    """score of the chunk"""

    file_id: str
    """file id"""

    filename: str
    """filename"""

    store_id: str
    """store id"""

    metadata: Optional[object] = None
    """file metadata"""

    type: Optional[Literal["audio_url"]] = None
    """Input type identifier"""

    transcription: Optional[str] = None
    """speech recognition (sr) text of the audio"""

    summary: Optional[str] = None
    """summary of the audio"""

    audio_url: AudioURL
    """The audio input specification."""

    sampling_rate: int
    """The sampling rate of the audio."""
