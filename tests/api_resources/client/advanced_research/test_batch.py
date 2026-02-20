# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from swarms_client import SwarmsClient, AsyncSwarmsClient
from swarms_client.types.client.advanced_research import BatchCreateCompletionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_completion(self, client: SwarmsClient) -> None:
        batch = client.client.advanced_research.batch.create_completion(
            input_schemas=[
                {
                    "config": {},
                    "task": "task",
                }
            ],
        )
        assert_matches_type(BatchCreateCompletionResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_completion(self, client: SwarmsClient) -> None:
        response = client.client.advanced_research.batch.with_raw_response.create_completion(
            input_schemas=[
                {
                    "config": {},
                    "task": "task",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchCreateCompletionResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_completion(self, client: SwarmsClient) -> None:
        with client.client.advanced_research.batch.with_streaming_response.create_completion(
            input_schemas=[
                {
                    "config": {},
                    "task": "task",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchCreateCompletionResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBatch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_completion(self, async_client: AsyncSwarmsClient) -> None:
        batch = await async_client.client.advanced_research.batch.create_completion(
            input_schemas=[
                {
                    "config": {},
                    "task": "task",
                }
            ],
        )
        assert_matches_type(BatchCreateCompletionResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_completion(self, async_client: AsyncSwarmsClient) -> None:
        response = await async_client.client.advanced_research.batch.with_raw_response.create_completion(
            input_schemas=[
                {
                    "config": {},
                    "task": "task",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchCreateCompletionResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_completion(self, async_client: AsyncSwarmsClient) -> None:
        async with async_client.client.advanced_research.batch.with_streaming_response.create_completion(
            input_schemas=[
                {
                    "config": {},
                    "task": "task",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchCreateCompletionResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True
