# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["JobStatus"]

JobStatus: TypeAlias = Literal["none", "running", "canceled", "successful", "failed", "resumable", "pending"]
