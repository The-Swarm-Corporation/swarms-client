# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr
from ..agent_spec_param import AgentSpecParam

__all__ = ["BatchedGridWorkflowCompleteWorkflowParams"]


class BatchedGridWorkflowCompleteWorkflowParams(TypedDict, total=False):
    agent_completions: Optional[Iterable[AgentSpecParam]]
    """The agent completions to be completed by the batched grid workflow."""

    description: Optional[str]
    """The description of the batched grid workflow."""

    imgs: Optional[SequenceNotStr[str]]
    """The images to be used by the batched grid workflow."""

    max_loops: Optional[int]
    """The maximum number of loops to be completed by the batched grid workflow."""

    name: Optional[str]
    """The name of the batched grid workflow."""

    tasks: Optional[SequenceNotStr[str]]
    """The tasks to be completed by the batched grid workflow."""
