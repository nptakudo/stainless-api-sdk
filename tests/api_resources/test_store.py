# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from testAPI import TestAPI, AsyncTestAPI
from tests.utils import assert_matches_type
from testAPI.types import StoreInventoryResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStore:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_inventory(self, client: TestAPI) -> None:
        store = client.store.inventory()
        assert_matches_type(StoreInventoryResponse, store, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_inventory(self, client: TestAPI) -> None:
        response = client.store.with_raw_response.inventory()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        store = response.parse()
        assert_matches_type(StoreInventoryResponse, store, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_inventory(self, client: TestAPI) -> None:
        with client.store.with_streaming_response.inventory() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            store = response.parse()
            assert_matches_type(StoreInventoryResponse, store, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStore:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_inventory(self, async_client: AsyncTestAPI) -> None:
        store = await async_client.store.inventory()
        assert_matches_type(StoreInventoryResponse, store, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_inventory(self, async_client: AsyncTestAPI) -> None:
        response = await async_client.store.with_raw_response.inventory()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        store = await response.parse()
        assert_matches_type(StoreInventoryResponse, store, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_inventory(self, async_client: AsyncTestAPI) -> None:
        async with async_client.store.with_streaming_response.inventory() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            store = await response.parse()
            assert_matches_type(StoreInventoryResponse, store, path=["response"])

        assert cast(Any, response.is_closed) is True
