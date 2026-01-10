# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["GraphWorkflowExecuteWorkflowResponse", "Usage"]


class Usage(BaseModel):
    """The usage statistics of the workflow."""

    cost_per_agent: float
    """The cost in credits for the agents."""

    input_tokens: int
    """The number of input tokens."""

    output_tokens: int
    """The number of output tokens."""

    token_cost: float
    """The cost in credits for the tokens."""

    total_tokens: int
    """The total number of tokens."""


class GraphWorkflowExecuteWorkflowResponse(BaseModel):
    """Output schema for GraphWorkflow completion responses."""

    job_id: str
    """The job ID of the graph workflow."""

    outputs: object
    """The outputs of the graph workflow."""

    status: str
    """The status of the graph workflow."""

    timestamp: str
    """The timestamp of the graph workflow execution."""

    usage: Usage
    """The usage statistics of the workflow."""

    description: Optional[str] = None
    """The description of the graph workflow."""

    name: Optional[str] = None
    """The name of the graph workflow."""
