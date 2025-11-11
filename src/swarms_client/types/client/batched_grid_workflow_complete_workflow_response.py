# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["BatchedGridWorkflowCompleteWorkflowResponse", "Usage"]


class Usage(BaseModel):
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


class BatchedGridWorkflowCompleteWorkflowResponse(BaseModel):
    description: str
    """The description of the batched grid workflow."""

    job_id: str
    """The job ID of the batched grid workflow."""

    name: str
    """The name of the batched grid workflow."""

    outputs: object
    """The outputs of the batched grid workflow."""

    status: str
    """The status of the batched grid workflow."""

    timestamp: str
    """The timestamp of the batched grid workflow."""

    usage: Usage
    """The usage of the batched grid workflow."""
