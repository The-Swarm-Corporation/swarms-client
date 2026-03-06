# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["McpConnectionParam"]


class McpConnectionParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    authorization_token: Optional[str]
    """Authentication token for accessing the MCP server"""

    headers: Optional[Dict[str, str]]
    """Headers to send to the MCP server"""

    timeout: Optional[int]
    """Timeout for the MCP server"""

    tool_configurations: Optional[Dict[str, object]]
    """Dictionary containing configuration settings for MCP tools"""

    transport: Optional[str]
    """The transport protocol to use for the MCP server"""

    type: Optional[str]
    """The type of connection, defaults to 'mcp'"""

    url: Optional[str]
    """The URL endpoint for the MCP server"""
