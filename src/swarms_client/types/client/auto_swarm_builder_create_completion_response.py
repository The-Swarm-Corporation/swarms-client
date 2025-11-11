# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["AutoSwarmBuilderCreateCompletionResponse"]


class AutoSwarmBuilderCreateCompletionResponse(BaseModel):
    success: bool
    """Whether the swarm was built successfully."""

    job_id: Optional[str] = None
    """The job ID of the swarm."""

    outputs: Optional[Dict[str, object]] = None
    """The outputs of the auto swarms builder."""

    timestamp: Optional[str] = None
    """The timestamp of the swarm execution."""

    type: Optional[str] = None
    """The type of the swarm execution."""

    usage: Optional[Dict[str, object]] = None
    """The usage of the swarm execution."""
