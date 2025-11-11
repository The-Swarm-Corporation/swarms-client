# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from swarms_client import SwarmsClient, AsyncSwarmsClient
from swarms_client.types.client import (
    BatchedGridWorkflowCompleteWorkflowResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatchedGridWorkflow:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_complete_workflow(self, client: SwarmsClient) -> None:
        batched_grid_workflow = client.client.batched_grid_workflow.complete_workflow()
        assert_matches_type(BatchedGridWorkflowCompleteWorkflowResponse, batched_grid_workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_complete_workflow_with_all_params(self, client: SwarmsClient) -> None:
        batched_grid_workflow = client.client.batched_grid_workflow.complete_workflow(
            agent_completions=[
                {
                    "agent_name": "agent_name",
                    "auto_generate_prompt": True,
                    "description": "description",
                    "dynamic_temperature_enabled": True,
                    "llm_args": {"foo": "bar"},
                    "max_loops": 0,
                    "max_tokens": 0,
                    "mcp_config": {
                        "authorization_token": "authorization_token",
                        "headers": {"foo": "string"},
                        "timeout": 0,
                        "tool_configurations": {"foo": "bar"},
                        "transport": "transport",
                        "type": "type",
                        "url": "url",
                    },
                    "mcp_configs": {
                        "connections": [
                            {
                                "authorization_token": "authorization_token",
                                "headers": {"foo": "string"},
                                "timeout": 0,
                                "tool_configurations": {"foo": "bar"},
                                "transport": "transport",
                                "type": "type",
                                "url": "url",
                            }
                        ]
                    },
                    "mcp_url": "mcp_url",
                    "model_name": "model_name",
                    "reasoning_effort": "reasoning_effort",
                    "reasoning_enabled": True,
                    "role": "role",
                    "streaming_on": True,
                    "system_prompt": "system_prompt",
                    "temperature": 0,
                    "thinking_tokens": 0,
                    "tool_call_summary": True,
                    "tools_list_dictionary": [{"foo": "bar"}],
                }
            ],
            description="description",
            imgs=["string"],
            max_loops=0,
            name="name",
            tasks=["string"],
        )
        assert_matches_type(BatchedGridWorkflowCompleteWorkflowResponse, batched_grid_workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_complete_workflow(self, client: SwarmsClient) -> None:
        response = client.client.batched_grid_workflow.with_raw_response.complete_workflow()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batched_grid_workflow = response.parse()
        assert_matches_type(BatchedGridWorkflowCompleteWorkflowResponse, batched_grid_workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_complete_workflow(self, client: SwarmsClient) -> None:
        with client.client.batched_grid_workflow.with_streaming_response.complete_workflow() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batched_grid_workflow = response.parse()
            assert_matches_type(BatchedGridWorkflowCompleteWorkflowResponse, batched_grid_workflow, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBatchedGridWorkflow:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_complete_workflow(self, async_client: AsyncSwarmsClient) -> None:
        batched_grid_workflow = await async_client.client.batched_grid_workflow.complete_workflow()
        assert_matches_type(BatchedGridWorkflowCompleteWorkflowResponse, batched_grid_workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_complete_workflow_with_all_params(self, async_client: AsyncSwarmsClient) -> None:
        batched_grid_workflow = await async_client.client.batched_grid_workflow.complete_workflow(
            agent_completions=[
                {
                    "agent_name": "agent_name",
                    "auto_generate_prompt": True,
                    "description": "description",
                    "dynamic_temperature_enabled": True,
                    "llm_args": {"foo": "bar"},
                    "max_loops": 0,
                    "max_tokens": 0,
                    "mcp_config": {
                        "authorization_token": "authorization_token",
                        "headers": {"foo": "string"},
                        "timeout": 0,
                        "tool_configurations": {"foo": "bar"},
                        "transport": "transport",
                        "type": "type",
                        "url": "url",
                    },
                    "mcp_configs": {
                        "connections": [
                            {
                                "authorization_token": "authorization_token",
                                "headers": {"foo": "string"},
                                "timeout": 0,
                                "tool_configurations": {"foo": "bar"},
                                "transport": "transport",
                                "type": "type",
                                "url": "url",
                            }
                        ]
                    },
                    "mcp_url": "mcp_url",
                    "model_name": "model_name",
                    "reasoning_effort": "reasoning_effort",
                    "reasoning_enabled": True,
                    "role": "role",
                    "streaming_on": True,
                    "system_prompt": "system_prompt",
                    "temperature": 0,
                    "thinking_tokens": 0,
                    "tool_call_summary": True,
                    "tools_list_dictionary": [{"foo": "bar"}],
                }
            ],
            description="description",
            imgs=["string"],
            max_loops=0,
            name="name",
            tasks=["string"],
        )
        assert_matches_type(BatchedGridWorkflowCompleteWorkflowResponse, batched_grid_workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_complete_workflow(self, async_client: AsyncSwarmsClient) -> None:
        response = await async_client.client.batched_grid_workflow.with_raw_response.complete_workflow()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batched_grid_workflow = await response.parse()
        assert_matches_type(BatchedGridWorkflowCompleteWorkflowResponse, batched_grid_workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_complete_workflow(self, async_client: AsyncSwarmsClient) -> None:
        async with async_client.client.batched_grid_workflow.with_streaming_response.complete_workflow() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batched_grid_workflow = await response.parse()
            assert_matches_type(BatchedGridWorkflowCompleteWorkflowResponse, batched_grid_workflow, path=["response"])

        assert cast(Any, response.is_closed) is True
