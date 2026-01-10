# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from ..._models import BaseModel

__all__ = ["MarketplaceCreateAgentResponse", "Prompt"]


class Prompt(BaseModel):
    """Schema for marketplace prompts from the swarms_cloud_prompts table."""

    id: str
    """Unique identifier for the prompt"""

    created_at: str
    """Timestamp when the prompt was created"""

    user_id: str
    """ID of the user who created the prompt"""

    category: Union[str, List[str], None] = None
    """Category name(s) - can be string or list"""

    description: Optional[str] = None
    """Description of the prompt"""

    links: Union[List[Dict[str, object]], List[str], None] = None
    """Associated links - can be list of dicts or strings"""

    name: Optional[str] = None
    """Name of the prompt"""

    prompt: Optional[str] = None
    """The actual prompt text"""

    status: Optional[str] = None
    """Status of the prompt"""

    tags: Optional[str] = None
    """Tags associated with the prompt"""

    use_cases: Union[Dict[str, object], List[Dict[str, object]], None] = None
    """Use cases - can be dict or list of dicts"""


class MarketplaceCreateAgentResponse(BaseModel):
    """Response schema for marketplace prompts endpoint."""

    prompts: List[Prompt]
    """List of marketplace prompts"""

    total_count: int
    """Total number of prompts available"""

    status: Optional[str] = None
    """The status of the marketplace prompts response."""

    timestamp: Optional[str] = None
    """The timestamp of the marketplace prompts response."""
