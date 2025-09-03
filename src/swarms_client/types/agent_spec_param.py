# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["AgentSpecParam", "McpConfig", "McpConfigs", "McpConfigsConnection"]


class McpConfigTyped(TypedDict, total=False):
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


McpConfig: TypeAlias = Union[McpConfigTyped, Dict[str, object]]


class McpConfigsConnectionTyped(TypedDict, total=False):
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


McpConfigsConnection: TypeAlias = Union[McpConfigsConnectionTyped, Dict[str, object]]


class McpConfigs(TypedDict, total=False):
    connections: Required[Iterable[McpConfigsConnection]]
    """List of MCP connections"""


class AgentSpecParam(TypedDict, total=False):
    agent_name: Required[Optional[str]]
    """
    The unique name assigned to the agent, which identifies its role and
    functionality within the swarm.
    """

    auto_generate_prompt: Optional[bool]
    """
    A flag indicating whether the agent should automatically create prompts based on
    the task requirements.
    """

    description: Optional[str]
    """
    A detailed explanation of the agent's purpose, capabilities, and any specific
    tasks it is designed to perform.
    """

    dynamic_temperature_enabled: Optional[bool]
    """
    A flag indicating whether the agent should dynamically adjust its temperature
    based on the task.
    """

    llm_args: Optional[Dict[str, object]]
    """
    Additional arguments to pass to the LLM such as top_p, frequency_penalty,
    presence_penalty, etc.
    """

    max_loops: Optional[int]
    """
    The maximum number of times the agent is allowed to repeat its task, enabling
    iterative processing if necessary.
    """

    max_tokens: Optional[int]
    """
    The maximum number of tokens that the agent is allowed to generate in its
    responses, limiting output length.
    """

    mcp_config: Optional[McpConfig]
    """The MCP connection to use for the agent."""

    mcp_configs: Optional[McpConfigs]
    """The MCP connections to use for the agent.

    This is a list of MCP connections. Includes multiple MCP connections.
    """

    mcp_url: Optional[str]
    """The URL of the MCP server that the agent can use to complete its task."""

    model_name: Optional[str]
    """
    The name of the AI model that the agent will utilize for processing tasks and
    generating outputs. For example: gpt-4o, gpt-4o-mini, openai/o3-mini
    """

    reasoning_effort: Optional[str]
    """The effort to put into reasoning."""

    reasoning_enabled: Optional[bool]
    """A parameter enabling an agent to use reasoning."""

    role: Optional[str]
    """
    The designated role of the agent within the swarm, which influences its behavior
    and interaction with other agents.
    """

    streaming_on: Optional[bool]
    """A flag indicating whether the agent should stream its output."""

    system_prompt: Optional[str]
    """
    The initial instruction or context provided to the agent, guiding its behavior
    and responses during execution.
    """

    temperature: Optional[float]
    """
    A parameter that controls the randomness of the agent's output; lower values
    result in more deterministic responses.
    """

    thinking_tokens: Optional[int]
    """The number of tokens to use for thinking."""

    tool_call_summary: Optional[bool]
    """A parameter enabling an agent to summarize tool calls."""

    tools_list_dictionary: Optional[Iterable[Dict[str, object]]]
    """A dictionary of tools that the agent can use to complete its task."""
