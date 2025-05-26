# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ObjectType"]

ObjectType: TypeAlias = Literal[
    "list",
    "parsing_job",
    "extraction_job",
    "embedding",
    "embedding_dict",
    "rank_result",
    "file",
    "vector_store",
    "vector_store.file",
    "api_key",
    "data_source",
    "data_source.connector",
]
