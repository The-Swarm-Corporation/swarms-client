# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .rate_limit_window import RateLimitWindow

__all__ = ["RateGetLimitsResponse", "Limits", "RateLimits"]


class Limits(BaseModel):
    """The configured rate limits based on the user's subscription tier."""

    maximum_requests_per_day: int
    """The maximum number of requests allowed per day."""

    maximum_requests_per_hour: int
    """The maximum number of requests allowed per hour."""

    maximum_requests_per_minute: int
    """The maximum number of requests allowed per minute."""

    tokens_per_agent: int
    """The maximum number of tokens allowed per agent."""


class RateLimits(BaseModel):
    """Current rate limit usage information for different time windows."""

    day: RateLimitWindow
    """Rate limit information for the last day."""

    hour: RateLimitWindow
    """Rate limit information for the last hour."""

    minute: RateLimitWindow
    """Rate limit information for the last minute."""


class RateGetLimitsResponse(BaseModel):
    limits: Optional[Limits] = None
    """The configured rate limits based on the user's subscription tier."""

    rate_limits: Optional[RateLimits] = None
    """Current rate limit usage information for different time windows."""

    tier: Optional[str] = None
    """The user's current subscription tier (free or premium)."""

    timestamp: Optional[str] = None
    """ISO timestamp when the rate limits information was retrieved."""

    success: Optional[bool] = None
    """Indicates whether the rate limits request was successful."""
