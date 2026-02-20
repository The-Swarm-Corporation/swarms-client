# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from swarms_client import SwarmsClient, AsyncSwarmsClient
from swarms_client.types.client import MarketplaceCreateAgentResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMarketplace:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_agent(self, client: SwarmsClient) -> None:
        marketplace = client.client.marketplace.create_agent()
        assert_matches_type(MarketplaceCreateAgentResponse, marketplace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_agent_with_all_params(self, client: SwarmsClient) -> None:
        marketplace = client.client.marketplace.create_agent(
            number_of_items=0,
        )
        assert_matches_type(MarketplaceCreateAgentResponse, marketplace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_agent(self, client: SwarmsClient) -> None:
        response = client.client.marketplace.with_raw_response.create_agent()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketplace = response.parse()
        assert_matches_type(MarketplaceCreateAgentResponse, marketplace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_agent(self, client: SwarmsClient) -> None:
        with client.client.marketplace.with_streaming_response.create_agent() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketplace = response.parse()
            assert_matches_type(MarketplaceCreateAgentResponse, marketplace, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMarketplace:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_agent(self, async_client: AsyncSwarmsClient) -> None:
        marketplace = await async_client.client.marketplace.create_agent()
        assert_matches_type(MarketplaceCreateAgentResponse, marketplace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_agent_with_all_params(self, async_client: AsyncSwarmsClient) -> None:
        marketplace = await async_client.client.marketplace.create_agent(
            number_of_items=0,
        )
        assert_matches_type(MarketplaceCreateAgentResponse, marketplace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_agent(self, async_client: AsyncSwarmsClient) -> None:
        response = await async_client.client.marketplace.with_raw_response.create_agent()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        marketplace = await response.parse()
        assert_matches_type(MarketplaceCreateAgentResponse, marketplace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_agent(self, async_client: AsyncSwarmsClient) -> None:
        async with async_client.client.marketplace.with_streaming_response.create_agent() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            marketplace = await response.parse()
            assert_matches_type(MarketplaceCreateAgentResponse, marketplace, path=["response"])

        assert cast(Any, response.is_closed) is True
