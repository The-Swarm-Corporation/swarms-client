# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..agent_spec_param import AgentSpecParam

__all__ = ["GraphWorkflowExecuteWorkflowParams", "Edge", "EdgeEdgeSpec"]


class GraphWorkflowExecuteWorkflowParams(TypedDict, total=False):
    agents: Optional[Iterable[AgentSpecParam]]
    """List of agent specifications to be used as nodes in the workflow graph."""

    auto_compile: Optional[bool]
    """Whether to automatically compile the workflow for optimization."""

    description: Optional[str]
    """The description of the graph workflow."""

    edges: Optional[Iterable[Edge]]
    """List of edges connecting nodes.

    Can be EdgeSpec objects or dictionaries with 'source' and 'target' keys.
    """

    end_points: Optional[SequenceNotStr[str]]
    """List of node IDs that serve as ending points for the workflow."""

    entry_points: Optional[SequenceNotStr[str]]
    """List of node IDs that serve as starting points for the workflow."""

    img: Optional[str]
    """Optional image path for vision-enabled agents."""

    max_loops: Optional[int]
    """The maximum number of execution loops for the workflow."""

    name: Optional[str]
    """The name of the graph workflow."""

    task: Optional[str]
    """The task to be executed by the workflow."""

    verbose: Optional[bool]
    """Whether to enable detailed logging."""


class EdgeEdgeSpec(TypedDict, total=False):
    """Schema for defining an edge between nodes in the workflow graph."""

    source: Required[str]
    """The source node ID."""

    target: Required[str]
    """The target node ID."""

    metadata: Optional[Dict[str, object]]
    """Optional metadata for the edge."""


Edge: TypeAlias = Union[EdgeEdgeSpec, Dict[str, object]]
