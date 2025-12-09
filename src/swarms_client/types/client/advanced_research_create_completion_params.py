# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["AdvancedResearchCreateCompletionParams", "Config"]


class AdvancedResearchCreateCompletionParams(TypedDict, total=False):
    config: Required[Optional[Config]]
    """The configuration for the advanced research"""

    task: Required[Optional[str]]
    """The task to be completed"""

    img: Optional[str]
    """The image to be used for the advanced research"""


class Config(TypedDict, total=False):
    """The configuration for the advanced research"""

    description: Optional[str]
    """Description of the advanced research session"""

    director_agent_name: Optional[str]
    """Name of the director agent"""

    director_max_loops: Optional[int]
    """Maximum loops for the director agent"""

    director_max_tokens: Optional[int]
    """Maximum tokens for the director agent's output"""

    director_model_name: Optional[str]
    """Model name for the director agent"""

    exa_search_max_characters: Optional[int]
    """Maximum characters to return from the Exa search tool"""

    exa_search_num_results: Optional[int]
    """Number of results to return from the Exa search tool"""

    max_loops: Optional[int]
    """Number of research loops to run"""

    name: Optional[str]
    """Name of the advanced research session"""

    worker_model_name: Optional[str]
    """Model name for worker agents"""
