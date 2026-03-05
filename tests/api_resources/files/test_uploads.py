# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mixedbread import Mixedbread, AsyncMixedbread
from tests.utils import assert_matches_type
from mixedbread.types import FileObject
from mixedbread.types.files import (
    UploadListResponse,
    UploadAbortResponse,
    UploadCreateResponse,
    UploadRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUploads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Mixedbread) -> None:
        upload = client.files.uploads.create(
            filename="document.pdf",
            file_size=10485760,
            mime_type="application/pdf",
        )
        assert_matches_type(UploadCreateResponse, upload, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Mixedbread) -> None:
        upload = client.files.uploads.create(
            filename="document.pdf",
            file_size=10485760,
            mime_type="application/pdf",
            part_count=3,
        )
        assert_matches_type(UploadCreateResponse, upload, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Mixedbread) -> None:
        response = client.files.uploads.with_raw_response.create(
            filename="document.pdf",
            file_size=10485760,
            mime_type="application/pdf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(UploadCreateResponse, upload, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Mixedbread) -> None:
        with client.files.uploads.with_streaming_response.create(
            filename="document.pdf",
            file_size=10485760,
            mime_type="application/pdf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(UploadCreateResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Mixedbread) -> None:
        upload = client.files.uploads.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UploadRetrieveResponse, upload, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Mixedbread) -> None:
        response = client.files.uploads.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(UploadRetrieveResponse, upload, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Mixedbread) -> None:
        with client.files.uploads.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(UploadRetrieveResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            client.files.uploads.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Mixedbread) -> None:
        upload = client.files.uploads.list()
        assert_matches_type(UploadListResponse, upload, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Mixedbread) -> None:
        response = client.files.uploads.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(UploadListResponse, upload, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Mixedbread) -> None:
        with client.files.uploads.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(UploadListResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_abort(self, client: Mixedbread) -> None:
        upload = client.files.uploads.abort(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UploadAbortResponse, upload, path=["response"])

    @parametrize
    def test_raw_response_abort(self, client: Mixedbread) -> None:
        response = client.files.uploads.with_raw_response.abort(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(UploadAbortResponse, upload, path=["response"])

    @parametrize
    def test_streaming_response_abort(self, client: Mixedbread) -> None:
        with client.files.uploads.with_streaming_response.abort(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(UploadAbortResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_abort(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            client.files.uploads.with_raw_response.abort(
                "",
            )

    @parametrize
    def test_method_complete(self, client: Mixedbread) -> None:
        upload = client.files.uploads.complete(
            upload_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parts=[
                {
                    "part_number": 1,
                    "etag": "etag",
                }
            ],
        )
        assert_matches_type(FileObject, upload, path=["response"])

    @parametrize
    def test_raw_response_complete(self, client: Mixedbread) -> None:
        response = client.files.uploads.with_raw_response.complete(
            upload_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parts=[
                {
                    "part_number": 1,
                    "etag": "etag",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(FileObject, upload, path=["response"])

    @parametrize
    def test_streaming_response_complete(self, client: Mixedbread) -> None:
        with client.files.uploads.with_streaming_response.complete(
            upload_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parts=[
                {
                    "part_number": 1,
                    "etag": "etag",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(FileObject, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_complete(self, client: Mixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            client.files.uploads.with_raw_response.complete(
                upload_id="",
                parts=[
                    {
                        "part_number": 1,
                        "etag": "etag",
                    }
                ],
            )


class TestAsyncUploads:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncMixedbread) -> None:
        upload = await async_client.files.uploads.create(
            filename="document.pdf",
            file_size=10485760,
            mime_type="application/pdf",
        )
        assert_matches_type(UploadCreateResponse, upload, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMixedbread) -> None:
        upload = await async_client.files.uploads.create(
            filename="document.pdf",
            file_size=10485760,
            mime_type="application/pdf",
            part_count=3,
        )
        assert_matches_type(UploadCreateResponse, upload, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.files.uploads.with_raw_response.create(
            filename="document.pdf",
            file_size=10485760,
            mime_type="application/pdf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(UploadCreateResponse, upload, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMixedbread) -> None:
        async with async_client.files.uploads.with_streaming_response.create(
            filename="document.pdf",
            file_size=10485760,
            mime_type="application/pdf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(UploadCreateResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMixedbread) -> None:
        upload = await async_client.files.uploads.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UploadRetrieveResponse, upload, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.files.uploads.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(UploadRetrieveResponse, upload, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMixedbread) -> None:
        async with async_client.files.uploads.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(UploadRetrieveResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            await async_client.files.uploads.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncMixedbread) -> None:
        upload = await async_client.files.uploads.list()
        assert_matches_type(UploadListResponse, upload, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.files.uploads.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(UploadListResponse, upload, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMixedbread) -> None:
        async with async_client.files.uploads.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(UploadListResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_abort(self, async_client: AsyncMixedbread) -> None:
        upload = await async_client.files.uploads.abort(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UploadAbortResponse, upload, path=["response"])

    @parametrize
    async def test_raw_response_abort(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.files.uploads.with_raw_response.abort(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(UploadAbortResponse, upload, path=["response"])

    @parametrize
    async def test_streaming_response_abort(self, async_client: AsyncMixedbread) -> None:
        async with async_client.files.uploads.with_streaming_response.abort(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(UploadAbortResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_abort(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            await async_client.files.uploads.with_raw_response.abort(
                "",
            )

    @parametrize
    async def test_method_complete(self, async_client: AsyncMixedbread) -> None:
        upload = await async_client.files.uploads.complete(
            upload_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parts=[
                {
                    "part_number": 1,
                    "etag": "etag",
                }
            ],
        )
        assert_matches_type(FileObject, upload, path=["response"])

    @parametrize
    async def test_raw_response_complete(self, async_client: AsyncMixedbread) -> None:
        response = await async_client.files.uploads.with_raw_response.complete(
            upload_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parts=[
                {
                    "part_number": 1,
                    "etag": "etag",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(FileObject, upload, path=["response"])

    @parametrize
    async def test_streaming_response_complete(self, async_client: AsyncMixedbread) -> None:
        async with async_client.files.uploads.with_streaming_response.complete(
            upload_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parts=[
                {
                    "part_number": 1,
                    "etag": "etag",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(FileObject, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_complete(self, async_client: AsyncMixedbread) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload_id` but received ''"):
            await async_client.files.uploads.with_raw_response.complete(
                upload_id="",
                parts=[
                    {
                        "part_number": 1,
                        "etag": "etag",
                    }
                ],
            )
