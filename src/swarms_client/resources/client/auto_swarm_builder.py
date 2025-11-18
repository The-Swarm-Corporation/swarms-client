# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.client import auto_swarm_builder_create_completion_params
from ...types.client.auto_swarm_builder_create_completion_response import AutoSwarmBuilderCreateCompletionResponse
from ...types.client.auto_swarm_builder_list_execution_types_response import AutoSwarmBuilderListExecutionTypesResponse

__all__ = ["AutoSwarmBuilderResource", "AsyncAutoSwarmBuilderResource"]


class AutoSwarmBuilderResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutoSwarmBuilderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-client#accessing-raw-response-data-eg-headers
        """
        return AutoSwarmBuilderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutoSwarmBuilderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-client#with_streaming_response
        """
        return AutoSwarmBuilderResourceWithStreamingResponse(self)

    def create_completion(
        self,
        *,
        description: Optional[str] | Omit = omit,
        execution_type: Optional[
            Literal["return-agents", "execute-swarm-router", "return-swarm-router-config", "return-agents-objects"]
        ]
        | Omit = omit,
        max_loops: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        model_name: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        task: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoSwarmBuilderCreateCompletionResponse:
        """
        Generate and orchestrate agent swarms autonomously using AI-powered swarm
        composition and task decomposition.

        Args:
          description: A description of the swarm.

          execution_type: The type of execution to perform.

          max_loops: Maximum number of loops to run.

          max_tokens: The maximum number of tokens to use for the swarm.

          model_name: The model name to use for the swarm.

          name: The name of the swarm.

          task: The task for the swarm, if any.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/auto-swarm-builder/completions",
            body=maybe_transform(
                {
                    "description": description,
                    "execution_type": execution_type,
                    "max_loops": max_loops,
                    "max_tokens": max_tokens,
                    "model_name": model_name,
                    "name": name,
                    "task": task,
                },
                auto_swarm_builder_create_completion_params.AutoSwarmBuilderCreateCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoSwarmBuilderCreateCompletionResponse,
        )

    def list_execution_types(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoSwarmBuilderListExecutionTypesResponse:
        """
        Retrieve all available execution types and return formats for the Auto Swarm
        Builder endpoint.
        """
        return self._get(
            "/v1/auto-swarm-builder/execution-types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoSwarmBuilderListExecutionTypesResponse,
        )


class AsyncAutoSwarmBuilderResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutoSwarmBuilderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-client#accessing-raw-response-data-eg-headers
        """
        return AsyncAutoSwarmBuilderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutoSwarmBuilderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-client#with_streaming_response
        """
        return AsyncAutoSwarmBuilderResourceWithStreamingResponse(self)

    async def create_completion(
        self,
        *,
        description: Optional[str] | Omit = omit,
        execution_type: Optional[
            Literal["return-agents", "execute-swarm-router", "return-swarm-router-config", "return-agents-objects"]
        ]
        | Omit = omit,
        max_loops: Optional[int] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        model_name: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        task: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoSwarmBuilderCreateCompletionResponse:
        """
        Generate and orchestrate agent swarms autonomously using AI-powered swarm
        composition and task decomposition.

        Args:
          description: A description of the swarm.

          execution_type: The type of execution to perform.

          max_loops: Maximum number of loops to run.

          max_tokens: The maximum number of tokens to use for the swarm.

          model_name: The model name to use for the swarm.

          name: The name of the swarm.

          task: The task for the swarm, if any.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/auto-swarm-builder/completions",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "execution_type": execution_type,
                    "max_loops": max_loops,
                    "max_tokens": max_tokens,
                    "model_name": model_name,
                    "name": name,
                    "task": task,
                },
                auto_swarm_builder_create_completion_params.AutoSwarmBuilderCreateCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoSwarmBuilderCreateCompletionResponse,
        )

    async def list_execution_types(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutoSwarmBuilderListExecutionTypesResponse:
        """
        Retrieve all available execution types and return formats for the Auto Swarm
        Builder endpoint.
        """
        return await self._get(
            "/v1/auto-swarm-builder/execution-types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoSwarmBuilderListExecutionTypesResponse,
        )


class AutoSwarmBuilderResourceWithRawResponse:
    def __init__(self, auto_swarm_builder: AutoSwarmBuilderResource) -> None:
        self._auto_swarm_builder = auto_swarm_builder

        self.create_completion = to_raw_response_wrapper(
            auto_swarm_builder.create_completion,
        )
        self.list_execution_types = to_raw_response_wrapper(
            auto_swarm_builder.list_execution_types,
        )


class AsyncAutoSwarmBuilderResourceWithRawResponse:
    def __init__(self, auto_swarm_builder: AsyncAutoSwarmBuilderResource) -> None:
        self._auto_swarm_builder = auto_swarm_builder

        self.create_completion = async_to_raw_response_wrapper(
            auto_swarm_builder.create_completion,
        )
        self.list_execution_types = async_to_raw_response_wrapper(
            auto_swarm_builder.list_execution_types,
        )


class AutoSwarmBuilderResourceWithStreamingResponse:
    def __init__(self, auto_swarm_builder: AutoSwarmBuilderResource) -> None:
        self._auto_swarm_builder = auto_swarm_builder

        self.create_completion = to_streamed_response_wrapper(
            auto_swarm_builder.create_completion,
        )
        self.list_execution_types = to_streamed_response_wrapper(
            auto_swarm_builder.list_execution_types,
        )


class AsyncAutoSwarmBuilderResourceWithStreamingResponse:
    def __init__(self, auto_swarm_builder: AsyncAutoSwarmBuilderResource) -> None:
        self._auto_swarm_builder = auto_swarm_builder

        self.create_completion = async_to_streamed_response_wrapper(
            auto_swarm_builder.create_completion,
        )
        self.list_execution_types = async_to_streamed_response_wrapper(
            auto_swarm_builder.list_execution_types,
        )
