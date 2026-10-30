# File generated from our OpenAPI spec by sdkgen. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .shared_params.search_filter import SearchFilter
from .store_chunk_search_options_param import StoreChunkSearchOptionsParam
from .shared_params.search_filter_condition import SearchFilterCondition

__all__ = [
    "StoreDecideParams",
    "Filters",
    "FiltersUnionMember2",
    "QuestionsValue",
    "QuestionsValueDecisionNoulQuestion",
    "QuestionsValueDecisionChoiceQuestion",
    "QuestionsValueDecisionScoreQuestion",
]


class StoreDecideParams(TypedDict, total=False):
    store_identifiers: Required[SequenceNotStr[str]]
    """IDs or names of stores"""

    top_k: int
    """Number of chunks retrieved for each question"""

    filters: Optional[Filters]
    """Optional filter conditions"""

    file_ids: Union[Iterable[object], SequenceNotStr[str], None]
    """Optional list of file IDs to filter chunks by (inclusion filter)"""

    search_options: StoreChunkSearchOptionsParam
    """
    Options for each question's search; rerank defaults to true and agentic is not
    supported. Probabilities are comparable only between calls that use the same
    options
    """

    state: Union[str, Dict[str, object], SequenceNotStr[str], None]
    """
    Optional context shared by all questions, such as the subject they are about; it
    also steers the search
    """

    questions: Required[Dict[str, QuestionsValue]]
    """The questions, keyed by name"""


FiltersUnionMember2: TypeAlias = Union[SearchFilter, SearchFilterCondition]

Filters: TypeAlias = Union[SearchFilter, SearchFilterCondition, Iterable[FiltersUnionMember2]]


class QuestionsValueDecisionNoulQuestion(TypedDict, total=False):
    """The questions, keyed by name"""

    type: Required[Literal["noul"]]

    instructions: Required[str]
    """The statement or question to decide, about the state and the stores' contents"""


class QuestionsValueDecisionChoiceQuestion(TypedDict, total=False):
    """The questions, keyed by name"""

    type: Required[Literal["choice"]]

    instructions: Required[str]
    """The statement or question to decide, about the state and the stores' contents"""

    criteria: Required[Dict[str, str]]
    """Each option, mapped to a description of when it applies"""


class QuestionsValueDecisionScoreQuestion(TypedDict, total=False):
    """The questions, keyed by name"""

    type: Required[Literal["score"]]

    instructions: Required[str]
    """The statement or question to decide, about the state and the stores' contents"""

    criteria: Required[SequenceNotStr[str]]
    """Ordered levels, lowest first, each with a concrete description"""


QuestionsValue: TypeAlias = Union[
    QuestionsValueDecisionNoulQuestion, QuestionsValueDecisionChoiceQuestion, QuestionsValueDecisionScoreQuestion
]
