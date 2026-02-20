# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from swarms_client import SwarmsClient, AsyncSwarmsClient
from swarms_client.types.client import (
    AdvancedResearchCreateCompletionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdvancedResearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_completion(self, client: SwarmsClient) -> None:
        advanced_research = client.client.advanced_research.create_completion(
            config={},
            task="task",
        )
        assert_matches_type(AdvancedResearchCreateCompletionResponse, advanced_research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_completion_with_all_params(self, client: SwarmsClient) -> None:
        advanced_research = client.client.advanced_research.create_completion(
            config={
                "description": "description",
                "director_agent_name": "director_agent_name",
                "director_max_loops": 0,
                "director_max_tokens": 0,
                "director_model_name": "director_model_name",
                "exa_search_max_characters": 0,
                "exa_search_num_results": 0,
                "max_loops": 0,
                "name": "name",
                "worker_model_name": "worker_model_name",
            },
            task="task",
            img="img",
        )
        assert_matches_type(AdvancedResearchCreateCompletionResponse, advanced_research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_completion(self, client: SwarmsClient) -> None:
        response = client.client.advanced_research.with_raw_response.create_completion(
            config={},
            task="task",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        advanced_research = response.parse()
        assert_matches_type(AdvancedResearchCreateCompletionResponse, advanced_research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_completion(self, client: SwarmsClient) -> None:
        with client.client.advanced_research.with_streaming_response.create_completion(
            config={},
            task="task",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            advanced_research = response.parse()
            assert_matches_type(AdvancedResearchCreateCompletionResponse, advanced_research, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAdvancedResearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_completion(self, async_client: AsyncSwarmsClient) -> None:
        advanced_research = await async_client.client.advanced_research.create_completion(
            config={},
            task="task",
        )
        assert_matches_type(AdvancedResearchCreateCompletionResponse, advanced_research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_completion_with_all_params(self, async_client: AsyncSwarmsClient) -> None:
        advanced_research = await async_client.client.advanced_research.create_completion(
            config={
                "description": "description",
                "director_agent_name": "director_agent_name",
                "director_max_loops": 0,
                "director_max_tokens": 0,
                "director_model_name": "director_model_name",
                "exa_search_max_characters": 0,
                "exa_search_num_results": 0,
                "max_loops": 0,
                "name": "name",
                "worker_model_name": "worker_model_name",
            },
            task="task",
            img="img",
        )
        assert_matches_type(AdvancedResearchCreateCompletionResponse, advanced_research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_completion(self, async_client: AsyncSwarmsClient) -> None:
        response = await async_client.client.advanced_research.with_raw_response.create_completion(
            config={},
            task="task",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        advanced_research = await response.parse()
        assert_matches_type(AdvancedResearchCreateCompletionResponse, advanced_research, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_completion(self, async_client: AsyncSwarmsClient) -> None:
        async with async_client.client.advanced_research.with_streaming_response.create_completion(
            config={},
            task="task",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            advanced_research = await response.parse()
            assert_matches_type(AdvancedResearchCreateCompletionResponse, advanced_research, path=["response"])

        assert cast(Any, response.is_closed) is True
