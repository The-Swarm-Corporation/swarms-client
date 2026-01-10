# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["MarketplaceCreateAgentParams"]


class MarketplaceCreateAgentParams(TypedDict, total=False):
    number_of_items: Optional[int]
    """Number of items to return"""
