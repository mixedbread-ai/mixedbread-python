# File generated from our OpenAPI spec by sdkgen. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .shared.usage import Usage
from .scored_text_input_chunk import ScoredTextInputChunk
from .scored_audio_url_input_chunk import ScoredAudioURLInputChunk
from .scored_image_url_input_chunk import ScoredImageURLInputChunk
from .scored_video_url_input_chunk import ScoredVideoURLInputChunk

__all__ = [
    "StoreDecideResponse",
    "AnswersValue",
    "AnswersValueDecisionNoulAnswer",
    "AnswersValueDecisionNoulAnswerSource",
    "AnswersValueDecisionChoiceAnswer",
    "AnswersValueDecisionChoiceAnswerSource",
    "AnswersValueDecisionScoreAnswer",
    "AnswersValueDecisionScoreAnswerSource",
    "AnswersValueDecisionRefusalAnswer",
    "AnswersValueDecisionRefusalAnswerSource",
]

AnswersValueDecisionNoulAnswerSource: TypeAlias = Annotated[
    Union[ScoredTextInputChunk, ScoredImageURLInputChunk, ScoredAudioURLInputChunk, ScoredVideoURLInputChunk],
    PropertyInfo(discriminator="type"),
]


class AnswersValueDecisionNoulAnswer(BaseModel):
    """The answers, keyed by question name"""

    grounding: Optional[Literal["grounded", "not_found", "conflicting"]] = None
    """
    Whether the store settles the question: act on the answer only when 'grounded';
    'not_found' means the store doesn't contain the answer, 'conflicting' that its
    documents disagree
    """

    sources: Optional[List[AnswersValueDecisionNoulAnswerSource]] = None
    """The chunks retrieved for this question, most relevant first"""

    type: Literal["noul"]

    noul: float
    """Probability that the statement is true"""


AnswersValueDecisionChoiceAnswerSource: TypeAlias = Annotated[
    Union[ScoredTextInputChunk, ScoredImageURLInputChunk, ScoredAudioURLInputChunk, ScoredVideoURLInputChunk],
    PropertyInfo(discriminator="type"),
]


class AnswersValueDecisionChoiceAnswer(BaseModel):
    """The answers, keyed by question name"""

    grounding: Optional[Literal["grounded", "not_found", "conflicting"]] = None
    """
    Whether the store settles the question: act on the answer only when 'grounded';
    'not_found' means the store doesn't contain the answer, 'conflicting' that its
    documents disagree
    """

    sources: Optional[List[AnswersValueDecisionChoiceAnswerSource]] = None
    """The chunks retrieved for this question, most relevant first"""

    type: Literal["choice"]

    choice: str
    """The most likely option"""

    probabilities: Dict[str, float]
    """Probability of each option"""

    confidence: Optional[float] = None
    """Confidence in the chosen option"""


AnswersValueDecisionScoreAnswerSource: TypeAlias = Annotated[
    Union[ScoredTextInputChunk, ScoredImageURLInputChunk, ScoredAudioURLInputChunk, ScoredVideoURLInputChunk],
    PropertyInfo(discriminator="type"),
]


class AnswersValueDecisionScoreAnswer(BaseModel):
    """The answers, keyed by question name"""

    grounding: Optional[Literal["grounded", "not_found", "conflicting"]] = None
    """
    Whether the store settles the question: act on the answer only when 'grounded';
    'not_found' means the store doesn't contain the answer, 'conflicting' that its
    documents disagree
    """

    sources: Optional[List[AnswersValueDecisionScoreAnswerSource]] = None
    """The chunks retrieved for this question, most relevant first"""

    type: Literal["score"]

    score: float
    """Probability-weighted mean of the zero-based level indices"""

    legend: Dict[str, str]
    """Each level, keyed by its index"""

    probabilities: Dict[str, float]
    """Probability of each level, keyed by its index"""

    confidence: Optional[float] = None
    """Confidence in the score"""


AnswersValueDecisionRefusalAnswerSource: TypeAlias = Annotated[
    Union[ScoredTextInputChunk, ScoredImageURLInputChunk, ScoredAudioURLInputChunk, ScoredVideoURLInputChunk],
    PropertyInfo(discriminator="type"),
]


class AnswersValueDecisionRefusalAnswer(BaseModel):
    """The answers, keyed by question name"""

    grounding: Optional[Literal["grounded", "not_found", "conflicting"]] = None
    """
    Whether the store settles the question: act on the answer only when 'grounded';
    'not_found' means the store doesn't contain the answer, 'conflicting' that its
    documents disagree
    """

    sources: Optional[List[AnswersValueDecisionRefusalAnswerSource]] = None
    """The chunks retrieved for this question, most relevant first"""

    type: Literal["refusal"]


AnswersValue: TypeAlias = Annotated[
    Union[
        AnswersValueDecisionNoulAnswer,
        AnswersValueDecisionChoiceAnswer,
        AnswersValueDecisionScoreAnswer,
        AnswersValueDecisionRefusalAnswer,
    ],
    PropertyInfo(discriminator="type"),
]


class StoreDecideResponse(BaseModel):
    answers: Dict[str, AnswersValue]
    """The answers, keyed by question name"""

    usage: Usage
    """Tokens the decision model read and wrote"""
