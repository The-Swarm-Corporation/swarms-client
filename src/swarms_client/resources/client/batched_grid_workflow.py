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
from ...types.client import batched_grid_workflow_complete_workflow_params
from ...types.agent_spec_param import AgentSpecParam
from ...types.client.batched_grid_workflow_complete_workflow_response import BatchedGridWorkflowCompleteWorkflowResponse

__all__ = ["BatchedGridWorkflowResource", "AsyncBatchedGridWorkflowResource"]


class BatchedGridWorkflowResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatchedGridWorkflowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-client#accessing-raw-response-data-eg-headers
        """
        return BatchedGridWorkflowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatchedGridWorkflowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-client#with_streaming_response
        """
        return BatchedGridWorkflowResourceWithStreamingResponse(self)

    def complete_workflow(
        self,
        *,
        agent_completions: Optional[Iterable[AgentSpecParam]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        imgs: Optional[SequenceNotStr[str]] | Omit = omit,
        max_loops: Optional[int] | Omit = omit,
        name: Optional[str] | Omit = omit,
        tasks: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchedGridWorkflowCompleteWorkflowResponse:
        """Complete a batched grid workflow with the specified input data.

        Enables you to
        run a grid workflow with multiple agents and tasks in a single request.

        Args:
          agent_completions: The agent completions to be completed by the batched grid workflow.

          description: The description of the batched grid workflow.

          imgs: The images to be used by the batched grid workflow.

          max_loops: The maximum number of loops to be completed by the batched grid workflow.

          name: The name of the batched grid workflow.

          tasks: The tasks to be completed by the batched grid workflow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/batched-grid-workflow/completions",
            body=maybe_transform(
                {
                    "agent_completions": agent_completions,
                    "description": description,
                    "imgs": imgs,
                    "max_loops": max_loops,
                    "name": name,
                    "tasks": tasks,
                },
                batched_grid_workflow_complete_workflow_params.BatchedGridWorkflowCompleteWorkflowParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchedGridWorkflowCompleteWorkflowResponse,
        )


class AsyncBatchedGridWorkflowResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatchedGridWorkflowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-client#accessing-raw-response-data-eg-headers
        """
        return AsyncBatchedGridWorkflowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatchedGridWorkflowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-client#with_streaming_response
        """
        return AsyncBatchedGridWorkflowResourceWithStreamingResponse(self)

    async def complete_workflow(
        self,
        *,
        agent_completions: Optional[Iterable[AgentSpecParam]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        imgs: Optional[SequenceNotStr[str]] | Omit = omit,
        max_loops: Optional[int] | Omit = omit,
        name: Optional[str] | Omit = omit,
        tasks: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchedGridWorkflowCompleteWorkflowResponse:
        """Complete a batched grid workflow with the specified input data.

        Enables you to
        run a grid workflow with multiple agents and tasks in a single request.

        Args:
          agent_completions: The agent completions to be completed by the batched grid workflow.

          description: The description of the batched grid workflow.

          imgs: The images to be used by the batched grid workflow.

          max_loops: The maximum number of loops to be completed by the batched grid workflow.

          name: The name of the batched grid workflow.

          tasks: The tasks to be completed by the batched grid workflow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/batched-grid-workflow/completions",
            body=await async_maybe_transform(
                {
                    "agent_completions": agent_completions,
                    "description": description,
                    "imgs": imgs,
                    "max_loops": max_loops,
                    "name": name,
                    "tasks": tasks,
                },
                batched_grid_workflow_complete_workflow_params.BatchedGridWorkflowCompleteWorkflowParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchedGridWorkflowCompleteWorkflowResponse,
        )


class BatchedGridWorkflowResourceWithRawResponse:
    def __init__(self, batched_grid_workflow: BatchedGridWorkflowResource) -> None:
        self._batched_grid_workflow = batched_grid_workflow

        self.complete_workflow = to_raw_response_wrapper(
            batched_grid_workflow.complete_workflow,
        )


class AsyncBatchedGridWorkflowResourceWithRawResponse:
    def __init__(self, batched_grid_workflow: AsyncBatchedGridWorkflowResource) -> None:
        self._batched_grid_workflow = batched_grid_workflow

        self.complete_workflow = async_to_raw_response_wrapper(
            batched_grid_workflow.complete_workflow,
        )


class BatchedGridWorkflowResourceWithStreamingResponse:
    def __init__(self, batched_grid_workflow: BatchedGridWorkflowResource) -> None:
        self._batched_grid_workflow = batched_grid_workflow

        self.complete_workflow = to_streamed_response_wrapper(
            batched_grid_workflow.complete_workflow,
        )


class AsyncBatchedGridWorkflowResourceWithStreamingResponse:
    def __init__(self, batched_grid_workflow: AsyncBatchedGridWorkflowResource) -> None:
        self._batched_grid_workflow = batched_grid_workflow

        self.complete_workflow = async_to_streamed_response_wrapper(
            batched_grid_workflow.complete_workflow,
        )
