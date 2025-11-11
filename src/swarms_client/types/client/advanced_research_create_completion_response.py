# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["AdvancedResearchCreateCompletionResponse"]


class AdvancedResearchCreateCompletionResponse(BaseModel):
    id: Optional[str] = None
    """The id of the advanced research session"""

    characters_per_source: Optional[int] = None
    """The number of characters per source used for the advanced research session"""

    description: Optional[str] = None
    """The description of the advanced research session"""

    name: Optional[str] = None
    """The name of the advanced research session"""

    outputs: object
    """The outputs of the advanced research session"""

    sources: Optional[int] = None
    """The number of sources used for the advanced research session"""

    timestamp: Optional[str] = None
    """The timestamp of the advanced research session"""

    usage: Optional[Dict[str, object]] = None
    """The usage of the advanced research session"""
