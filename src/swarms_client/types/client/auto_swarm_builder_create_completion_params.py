# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["AutoSwarmBuilderCreateCompletionParams"]


class AutoSwarmBuilderCreateCompletionParams(TypedDict, total=False):
    description: Optional[str]
    """A description of the swarm."""

    execution_type: Optional[Literal["return-agents", "return-swarm-router-config", "return-agents-objects"]]
    """The type of execution to perform."""

    max_loops: Optional[int]
    """Maximum number of loops to run."""

    max_tokens: Optional[int]
    """The maximum number of tokens to use for the swarm."""

    model_name: Optional[str]
    """The model name to use for the swarm."""

    name: Optional[str]
    """The name of the swarm."""

    task: Optional[str]
    """The task for the swarm, if any."""
