# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ToolListAvailableResponse"]


class ToolListAvailableResponse(BaseModel):
    status: Optional[str] = None
    """The status of the available tools."""

    tools: Optional[List[str]] = None
    """The list of available tools."""
