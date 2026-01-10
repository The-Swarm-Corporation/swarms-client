# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["RateLimitWindow"]


class RateLimitWindow(BaseModel):
    count: int
    """The number of requests made in this time window."""

    exceeded: bool
    """Whether the rate limit has been exceeded for this time window."""

    limit: int
    """The maximum number of requests allowed in this time window."""

    remaining: int
    """The number of requests remaining before hitting the limit."""

    reset_time: str
    """ISO timestamp when the rate limit will reset."""
