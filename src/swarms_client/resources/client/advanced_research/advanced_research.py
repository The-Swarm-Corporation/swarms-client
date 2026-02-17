# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .batch import (
    BatchResource,
    AsyncBatchResource,
    BatchResourceWithRawResponse,
    AsyncBatchResourceWithRawResponse,
    BatchResourceWithStreamingResponse,
    AsyncBatchResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.client import advanced_research_create_completion_params
from ....types.client.advanced_research_create_completion_response import AdvancedResearchCreateCompletionResponse

__all__ = ["AdvancedResearchResource", "AsyncAdvancedResearchResource"]


class AdvancedResearchResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AdvancedResearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-client#accessing-raw-response-data-eg-headers
        """
        return AdvancedResearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdvancedResearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-client#with_streaming_response
        """
        return AdvancedResearchResourceWithStreamingResponse(self)

    def create_completion(
        self,
        *,
        config: Optional[advanced_research_create_completion_params.Config],
        task: Optional[str],
        img: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdvancedResearchCreateCompletionResponse:
        """
        Execute comprehensive research sessions with multi-source data collection,
        analysis, and synthesis capabilities.

        Args:
          config: The configuration for the advanced research

          task: The task to be completed

          img: The image to be used for the advanced research

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/advanced-research/completions",
            body=maybe_transform(
                {
                    "config": config,
                    "task": task,
                    "img": img,
                },
                advanced_research_create_completion_params.AdvancedResearchCreateCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdvancedResearchCreateCompletionResponse,
        )


class AsyncAdvancedResearchResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAdvancedResearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-client#accessing-raw-response-data-eg-headers
        """
        return AsyncAdvancedResearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdvancedResearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-client#with_streaming_response
        """
        return AsyncAdvancedResearchResourceWithStreamingResponse(self)

    async def create_completion(
        self,
        *,
        config: Optional[advanced_research_create_completion_params.Config],
        task: Optional[str],
        img: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdvancedResearchCreateCompletionResponse:
        """
        Execute comprehensive research sessions with multi-source data collection,
        analysis, and synthesis capabilities.

        Args:
          config: The configuration for the advanced research

          task: The task to be completed

          img: The image to be used for the advanced research

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/advanced-research/completions",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "task": task,
                    "img": img,
                },
                advanced_research_create_completion_params.AdvancedResearchCreateCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdvancedResearchCreateCompletionResponse,
        )


class AdvancedResearchResourceWithRawResponse:
    def __init__(self, advanced_research: AdvancedResearchResource) -> None:
        self._advanced_research = advanced_research

        self.create_completion = to_raw_response_wrapper(
            advanced_research.create_completion,
        )

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._advanced_research.batch)


class AsyncAdvancedResearchResourceWithRawResponse:
    def __init__(self, advanced_research: AsyncAdvancedResearchResource) -> None:
        self._advanced_research = advanced_research

        self.create_completion = async_to_raw_response_wrapper(
            advanced_research.create_completion,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._advanced_research.batch)


class AdvancedResearchResourceWithStreamingResponse:
    def __init__(self, advanced_research: AdvancedResearchResource) -> None:
        self._advanced_research = advanced_research

        self.create_completion = to_streamed_response_wrapper(
            advanced_research.create_completion,
        )

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._advanced_research.batch)


class AsyncAdvancedResearchResourceWithStreamingResponse:
    def __init__(self, advanced_research: AsyncAdvancedResearchResource) -> None:
        self._advanced_research = advanced_research

        self.create_completion = async_to_streamed_response_wrapper(
            advanced_research.create_completion,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._advanced_research.batch)
