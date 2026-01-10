# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.client import graph_workflow_execute_workflow_params
from ...types.agent_spec_param import AgentSpecParam
from ...types.client.graph_workflow_execute_workflow_response import GraphWorkflowExecuteWorkflowResponse

__all__ = ["GraphWorkflowResource", "AsyncGraphWorkflowResource"]


class GraphWorkflowResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GraphWorkflowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-client#accessing-raw-response-data-eg-headers
        """
        return GraphWorkflowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GraphWorkflowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-client#with_streaming_response
        """
        return GraphWorkflowResourceWithStreamingResponse(self)

    def execute_workflow(
        self,
        *,
        agents: Optional[Iterable[AgentSpecParam]] | Omit = omit,
        auto_compile: Optional[bool] | Omit = omit,
        description: Optional[str] | Omit = omit,
        edges: Optional[Iterable[graph_workflow_execute_workflow_params.Edge]] | Omit = omit,
        end_points: Optional[SequenceNotStr[str]] | Omit = omit,
        entry_points: Optional[SequenceNotStr[str]] | Omit = omit,
        img: Optional[str] | Omit = omit,
        max_loops: Optional[int] | Omit = omit,
        name: Optional[str] | Omit = omit,
        task: Optional[str] | Omit = omit,
        verbose: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GraphWorkflowExecuteWorkflowResponse:
        """Execute a graph workflow with directed agent nodes and edges.

        Enables complex
        multi-agent collaboration with parallel execution, automatic compilation, and
        comprehensive workflow orchestration.

        Args:
          agents: List of agent specifications to be used as nodes in the workflow graph.

          auto_compile: Whether to automatically compile the workflow for optimization.

          description: The description of the graph workflow.

          edges: List of edges connecting nodes. Can be EdgeSpec objects or dictionaries with
              'source' and 'target' keys.

          end_points: List of node IDs that serve as ending points for the workflow.

          entry_points: List of node IDs that serve as starting points for the workflow.

          img: Optional image path for vision-enabled agents.

          max_loops: The maximum number of execution loops for the workflow.

          name: The name of the graph workflow.

          task: The task to be executed by the workflow.

          verbose: Whether to enable detailed logging.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/graph-workflow/completions",
            body=maybe_transform(
                {
                    "agents": agents,
                    "auto_compile": auto_compile,
                    "description": description,
                    "edges": edges,
                    "end_points": end_points,
                    "entry_points": entry_points,
                    "img": img,
                    "max_loops": max_loops,
                    "name": name,
                    "task": task,
                    "verbose": verbose,
                },
                graph_workflow_execute_workflow_params.GraphWorkflowExecuteWorkflowParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphWorkflowExecuteWorkflowResponse,
        )


class AsyncGraphWorkflowResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGraphWorkflowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-client#accessing-raw-response-data-eg-headers
        """
        return AsyncGraphWorkflowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGraphWorkflowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-client#with_streaming_response
        """
        return AsyncGraphWorkflowResourceWithStreamingResponse(self)

    async def execute_workflow(
        self,
        *,
        agents: Optional[Iterable[AgentSpecParam]] | Omit = omit,
        auto_compile: Optional[bool] | Omit = omit,
        description: Optional[str] | Omit = omit,
        edges: Optional[Iterable[graph_workflow_execute_workflow_params.Edge]] | Omit = omit,
        end_points: Optional[SequenceNotStr[str]] | Omit = omit,
        entry_points: Optional[SequenceNotStr[str]] | Omit = omit,
        img: Optional[str] | Omit = omit,
        max_loops: Optional[int] | Omit = omit,
        name: Optional[str] | Omit = omit,
        task: Optional[str] | Omit = omit,
        verbose: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GraphWorkflowExecuteWorkflowResponse:
        """Execute a graph workflow with directed agent nodes and edges.

        Enables complex
        multi-agent collaboration with parallel execution, automatic compilation, and
        comprehensive workflow orchestration.

        Args:
          agents: List of agent specifications to be used as nodes in the workflow graph.

          auto_compile: Whether to automatically compile the workflow for optimization.

          description: The description of the graph workflow.

          edges: List of edges connecting nodes. Can be EdgeSpec objects or dictionaries with
              'source' and 'target' keys.

          end_points: List of node IDs that serve as ending points for the workflow.

          entry_points: List of node IDs that serve as starting points for the workflow.

          img: Optional image path for vision-enabled agents.

          max_loops: The maximum number of execution loops for the workflow.

          name: The name of the graph workflow.

          task: The task to be executed by the workflow.

          verbose: Whether to enable detailed logging.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/graph-workflow/completions",
            body=await async_maybe_transform(
                {
                    "agents": agents,
                    "auto_compile": auto_compile,
                    "description": description,
                    "edges": edges,
                    "end_points": end_points,
                    "entry_points": entry_points,
                    "img": img,
                    "max_loops": max_loops,
                    "name": name,
                    "task": task,
                    "verbose": verbose,
                },
                graph_workflow_execute_workflow_params.GraphWorkflowExecuteWorkflowParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphWorkflowExecuteWorkflowResponse,
        )


class GraphWorkflowResourceWithRawResponse:
    def __init__(self, graph_workflow: GraphWorkflowResource) -> None:
        self._graph_workflow = graph_workflow

        self.execute_workflow = to_raw_response_wrapper(
            graph_workflow.execute_workflow,
        )


class AsyncGraphWorkflowResourceWithRawResponse:
    def __init__(self, graph_workflow: AsyncGraphWorkflowResource) -> None:
        self._graph_workflow = graph_workflow

        self.execute_workflow = async_to_raw_response_wrapper(
            graph_workflow.execute_workflow,
        )


class GraphWorkflowResourceWithStreamingResponse:
    def __init__(self, graph_workflow: GraphWorkflowResource) -> None:
        self._graph_workflow = graph_workflow

        self.execute_workflow = to_streamed_response_wrapper(
            graph_workflow.execute_workflow,
        )


class AsyncGraphWorkflowResourceWithStreamingResponse:
    def __init__(self, graph_workflow: AsyncGraphWorkflowResource) -> None:
        self._graph_workflow = graph_workflow

        self.execute_workflow = async_to_streamed_response_wrapper(
            graph_workflow.execute_workflow,
        )
