# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from swarms_client import SwarmsClient, AsyncSwarmsClient
from swarms_client.types.client import (
    AutoSwarmBuilderCreateCompletionResponse,
    AutoSwarmBuilderListExecutionTypesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAutoSwarmBuilder:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_completion(self, client: SwarmsClient) -> None:
        auto_swarm_builder = client.client.auto_swarm_builder.create_completion()
        assert_matches_type(AutoSwarmBuilderCreateCompletionResponse, auto_swarm_builder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_completion_with_all_params(self, client: SwarmsClient) -> None:
        auto_swarm_builder = client.client.auto_swarm_builder.create_completion(
            description="description",
            execution_type="return-agents",
            max_loops=0,
            max_tokens=0,
            model_name="model_name",
            name="name",
            task="task",
        )
        assert_matches_type(AutoSwarmBuilderCreateCompletionResponse, auto_swarm_builder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_completion(self, client: SwarmsClient) -> None:
        response = client.client.auto_swarm_builder.with_raw_response.create_completion()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auto_swarm_builder = response.parse()
        assert_matches_type(AutoSwarmBuilderCreateCompletionResponse, auto_swarm_builder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_completion(self, client: SwarmsClient) -> None:
        with client.client.auto_swarm_builder.with_streaming_response.create_completion() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auto_swarm_builder = response.parse()
            assert_matches_type(AutoSwarmBuilderCreateCompletionResponse, auto_swarm_builder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_execution_types(self, client: SwarmsClient) -> None:
        auto_swarm_builder = client.client.auto_swarm_builder.list_execution_types()
        assert_matches_type(AutoSwarmBuilderListExecutionTypesResponse, auto_swarm_builder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_execution_types(self, client: SwarmsClient) -> None:
        response = client.client.auto_swarm_builder.with_raw_response.list_execution_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auto_swarm_builder = response.parse()
        assert_matches_type(AutoSwarmBuilderListExecutionTypesResponse, auto_swarm_builder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_execution_types(self, client: SwarmsClient) -> None:
        with client.client.auto_swarm_builder.with_streaming_response.list_execution_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auto_swarm_builder = response.parse()
            assert_matches_type(AutoSwarmBuilderListExecutionTypesResponse, auto_swarm_builder, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAutoSwarmBuilder:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_completion(self, async_client: AsyncSwarmsClient) -> None:
        auto_swarm_builder = await async_client.client.auto_swarm_builder.create_completion()
        assert_matches_type(AutoSwarmBuilderCreateCompletionResponse, auto_swarm_builder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_completion_with_all_params(self, async_client: AsyncSwarmsClient) -> None:
        auto_swarm_builder = await async_client.client.auto_swarm_builder.create_completion(
            description="description",
            execution_type="return-agents",
            max_loops=0,
            max_tokens=0,
            model_name="model_name",
            name="name",
            task="task",
        )
        assert_matches_type(AutoSwarmBuilderCreateCompletionResponse, auto_swarm_builder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_completion(self, async_client: AsyncSwarmsClient) -> None:
        response = await async_client.client.auto_swarm_builder.with_raw_response.create_completion()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auto_swarm_builder = await response.parse()
        assert_matches_type(AutoSwarmBuilderCreateCompletionResponse, auto_swarm_builder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_completion(self, async_client: AsyncSwarmsClient) -> None:
        async with async_client.client.auto_swarm_builder.with_streaming_response.create_completion() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auto_swarm_builder = await response.parse()
            assert_matches_type(AutoSwarmBuilderCreateCompletionResponse, auto_swarm_builder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_execution_types(self, async_client: AsyncSwarmsClient) -> None:
        auto_swarm_builder = await async_client.client.auto_swarm_builder.list_execution_types()
        assert_matches_type(AutoSwarmBuilderListExecutionTypesResponse, auto_swarm_builder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_execution_types(self, async_client: AsyncSwarmsClient) -> None:
        response = await async_client.client.auto_swarm_builder.with_raw_response.list_execution_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auto_swarm_builder = await response.parse()
        assert_matches_type(AutoSwarmBuilderListExecutionTypesResponse, auto_swarm_builder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_execution_types(self, async_client: AsyncSwarmsClient) -> None:
        async with async_client.client.auto_swarm_builder.with_streaming_response.list_execution_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auto_swarm_builder = await response.parse()
            assert_matches_type(AutoSwarmBuilderListExecutionTypesResponse, auto_swarm_builder, path=["response"])

        assert cast(Any, response.is_closed) is True
