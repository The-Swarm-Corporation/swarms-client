# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .rate import (
    RateResource,
    AsyncRateResource,
    RateResourceWithRawResponse,
    AsyncRateResourceWithRawResponse,
    RateResourceWithStreamingResponse,
    AsyncRateResourceWithStreamingResponse,
)
from .tools import (
    ToolsResource,
    AsyncToolsResource,
    ToolsResourceWithRawResponse,
    AsyncToolsResourceWithRawResponse,
    ToolsResourceWithStreamingResponse,
    AsyncToolsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .auto_swarm_builder import (
    AutoSwarmBuilderResource,
    AsyncAutoSwarmBuilderResource,
    AutoSwarmBuilderResourceWithRawResponse,
    AsyncAutoSwarmBuilderResourceWithRawResponse,
    AutoSwarmBuilderResourceWithStreamingResponse,
    AsyncAutoSwarmBuilderResourceWithStreamingResponse,
)
from .batched_grid_workflow import (
    BatchedGridWorkflowResource,
    AsyncBatchedGridWorkflowResource,
    BatchedGridWorkflowResourceWithRawResponse,
    AsyncBatchedGridWorkflowResourceWithRawResponse,
    BatchedGridWorkflowResourceWithStreamingResponse,
    AsyncBatchedGridWorkflowResourceWithStreamingResponse,
)
from .advanced_research.advanced_research import (
    AdvancedResearchResource,
    AsyncAdvancedResearchResource,
    AdvancedResearchResourceWithRawResponse,
    AsyncAdvancedResearchResourceWithRawResponse,
    AdvancedResearchResourceWithStreamingResponse,
    AsyncAdvancedResearchResourceWithStreamingResponse,
)

__all__ = ["ClientResource", "AsyncClientResource"]


class ClientResource(SyncAPIResource):
    @cached_property
    def rate(self) -> RateResource:
        return RateResource(self._client)

    @cached_property
    def auto_swarm_builder(self) -> AutoSwarmBuilderResource:
        return AutoSwarmBuilderResource(self._client)

    @cached_property
    def advanced_research(self) -> AdvancedResearchResource:
        return AdvancedResearchResource(self._client)

    @cached_property
    def tools(self) -> ToolsResource:
        return ToolsResource(self._client)

    @cached_property
    def batched_grid_workflow(self) -> BatchedGridWorkflowResource:
        return BatchedGridWorkflowResource(self._client)

    @cached_property
    def with_raw_response(self) -> ClientResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-client#accessing-raw-response-data-eg-headers
        """
        return ClientResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClientResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-client#with_streaming_response
        """
        return ClientResourceWithStreamingResponse(self)


class AsyncClientResource(AsyncAPIResource):
    @cached_property
    def rate(self) -> AsyncRateResource:
        return AsyncRateResource(self._client)

    @cached_property
    def auto_swarm_builder(self) -> AsyncAutoSwarmBuilderResource:
        return AsyncAutoSwarmBuilderResource(self._client)

    @cached_property
    def advanced_research(self) -> AsyncAdvancedResearchResource:
        return AsyncAdvancedResearchResource(self._client)

    @cached_property
    def tools(self) -> AsyncToolsResource:
        return AsyncToolsResource(self._client)

    @cached_property
    def batched_grid_workflow(self) -> AsyncBatchedGridWorkflowResource:
        return AsyncBatchedGridWorkflowResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncClientResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-client#accessing-raw-response-data-eg-headers
        """
        return AsyncClientResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClientResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/The-Swarm-Corporation/swarms-client#with_streaming_response
        """
        return AsyncClientResourceWithStreamingResponse(self)


class ClientResourceWithRawResponse:
    def __init__(self, client: ClientResource) -> None:
        self._client = client

    @cached_property
    def rate(self) -> RateResourceWithRawResponse:
        return RateResourceWithRawResponse(self._client.rate)

    @cached_property
    def auto_swarm_builder(self) -> AutoSwarmBuilderResourceWithRawResponse:
        return AutoSwarmBuilderResourceWithRawResponse(self._client.auto_swarm_builder)

    @cached_property
    def advanced_research(self) -> AdvancedResearchResourceWithRawResponse:
        return AdvancedResearchResourceWithRawResponse(self._client.advanced_research)

    @cached_property
    def tools(self) -> ToolsResourceWithRawResponse:
        return ToolsResourceWithRawResponse(self._client.tools)

    @cached_property
    def batched_grid_workflow(self) -> BatchedGridWorkflowResourceWithRawResponse:
        return BatchedGridWorkflowResourceWithRawResponse(self._client.batched_grid_workflow)


class AsyncClientResourceWithRawResponse:
    def __init__(self, client: AsyncClientResource) -> None:
        self._client = client

    @cached_property
    def rate(self) -> AsyncRateResourceWithRawResponse:
        return AsyncRateResourceWithRawResponse(self._client.rate)

    @cached_property
    def auto_swarm_builder(self) -> AsyncAutoSwarmBuilderResourceWithRawResponse:
        return AsyncAutoSwarmBuilderResourceWithRawResponse(self._client.auto_swarm_builder)

    @cached_property
    def advanced_research(self) -> AsyncAdvancedResearchResourceWithRawResponse:
        return AsyncAdvancedResearchResourceWithRawResponse(self._client.advanced_research)

    @cached_property
    def tools(self) -> AsyncToolsResourceWithRawResponse:
        return AsyncToolsResourceWithRawResponse(self._client.tools)

    @cached_property
    def batched_grid_workflow(self) -> AsyncBatchedGridWorkflowResourceWithRawResponse:
        return AsyncBatchedGridWorkflowResourceWithRawResponse(self._client.batched_grid_workflow)


class ClientResourceWithStreamingResponse:
    def __init__(self, client: ClientResource) -> None:
        self._client = client

    @cached_property
    def rate(self) -> RateResourceWithStreamingResponse:
        return RateResourceWithStreamingResponse(self._client.rate)

    @cached_property
    def auto_swarm_builder(self) -> AutoSwarmBuilderResourceWithStreamingResponse:
        return AutoSwarmBuilderResourceWithStreamingResponse(self._client.auto_swarm_builder)

    @cached_property
    def advanced_research(self) -> AdvancedResearchResourceWithStreamingResponse:
        return AdvancedResearchResourceWithStreamingResponse(self._client.advanced_research)

    @cached_property
    def tools(self) -> ToolsResourceWithStreamingResponse:
        return ToolsResourceWithStreamingResponse(self._client.tools)

    @cached_property
    def batched_grid_workflow(self) -> BatchedGridWorkflowResourceWithStreamingResponse:
        return BatchedGridWorkflowResourceWithStreamingResponse(self._client.batched_grid_workflow)


class AsyncClientResourceWithStreamingResponse:
    def __init__(self, client: AsyncClientResource) -> None:
        self._client = client

    @cached_property
    def rate(self) -> AsyncRateResourceWithStreamingResponse:
        return AsyncRateResourceWithStreamingResponse(self._client.rate)

    @cached_property
    def auto_swarm_builder(self) -> AsyncAutoSwarmBuilderResourceWithStreamingResponse:
        return AsyncAutoSwarmBuilderResourceWithStreamingResponse(self._client.auto_swarm_builder)

    @cached_property
    def advanced_research(self) -> AsyncAdvancedResearchResourceWithStreamingResponse:
        return AsyncAdvancedResearchResourceWithStreamingResponse(self._client.advanced_research)

    @cached_property
    def tools(self) -> AsyncToolsResourceWithStreamingResponse:
        return AsyncToolsResourceWithStreamingResponse(self._client.tools)

    @cached_property
    def batched_grid_workflow(self) -> AsyncBatchedGridWorkflowResourceWithStreamingResponse:
        return AsyncBatchedGridWorkflowResourceWithStreamingResponse(self._client.batched_grid_workflow)
