# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, List, Union, Mapping, Iterable, Optional, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from .types import client_embed_params, client_rerank_params
from ._types import (
    NOT_GIVEN,
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    maybe_transform,
    get_async_library,
    async_maybe_transform,
)
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .resources import files, embeddings
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, MixedbreadError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .resources.parsing import parsing
from .types.info_response import InfoResponse
from .resources.extractions import extractions
from .types.rerank_response import RerankResponse
from .resources.vector_stores import vector_stores
from .types.embedding_create_response import EmbeddingCreateResponse

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Mixedbread",
    "AsyncMixedbread",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api.mixedbread.com",
    "local": "http://127.0.0.1:8000",
}


class Mixedbread(SyncAPIClient):
    vector_stores: vector_stores.VectorStoresResource
    parsing: parsing.ParsingResource
    files: files.FilesResource
    extractions: extractions.ExtractionsResource
    embeddings: embeddings.EmbeddingsResource
    with_raw_response: MixedbreadWithRawResponse
    with_streaming_response: MixedbreadWithStreamedResponse

    # client options
    api_key: str

    _environment: Literal["production", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "local"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Mixedbread client instance.

        This automatically infers the `api_key` argument from the `MXBAI_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("MXBAI_API_KEY")
        if api_key is None:
            raise MixedbreadError(
                "The api_key client option must be set either by passing api_key to the client or by setting the MXBAI_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("MIXEDBREAD_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `MIXEDBREAD_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.vector_stores = vector_stores.VectorStoresResource(self)
        self.parsing = parsing.ParsingResource(self)
        self.files = files.FilesResource(self)
        self.extractions = extractions.ExtractionsResource(self)
        self.embeddings = embeddings.EmbeddingsResource(self)
        self.with_raw_response = MixedbreadWithRawResponse(self)
        self.with_streaming_response = MixedbreadWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def embed(
        self,
        *,
        model: str,
        input: Union[str, List[str]],
        dimensions: Optional[int] | NotGiven = NOT_GIVEN,
        prompt: Optional[str] | NotGiven = NOT_GIVEN,
        normalized: bool | NotGiven = NOT_GIVEN,
        encoding_format: Union[
            Literal["float", "float16", "base64", "binary", "ubinary", "int8", "uint8"],
            List[Literal["float", "float16", "base64", "binary", "ubinary", "int8", "uint8"]],
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmbeddingCreateResponse:
        """
        Create embeddings for text or images using the specified model, encoding format,
        and normalization.

        Args: params: The parameters for creating embeddings.

        Returns: EmbeddingCreateResponse: The response containing the embeddings.

        Args:
          model: The model to use for creating embeddings.

          input: The input to create embeddings for.

          dimensions: The number of dimensions to use for the embeddings.

          prompt: The prompt to use for the embedding creation.

          normalized: Whether to normalize the embeddings.

          encoding_format: The encoding format(s) of the embeddings. Can be a single format or a list of
              formats.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.post(
            "/v1/embeddings",
            body=maybe_transform(
                {
                    "model": model,
                    "input": input,
                    "dimensions": dimensions,
                    "prompt": prompt,
                    "normalized": normalized,
                    "encoding_format": encoding_format,
                },
                client_embed_params.ClientEmbedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbeddingCreateResponse,
        )

    def info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InfoResponse:
        """
        Returns service information, including name and version.

        Returns: InfoResponse: A response containing the service name and version.
        """
        return self.get(
            "/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InfoResponse,
        )

    def rerank(
        self,
        *,
        model: str | NotGiven = NOT_GIVEN,
        query: str,
        input: List[Union[str, Iterable[object], object]],
        rank_fields: Optional[List[str]] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        return_input: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RerankResponse:
        """
        Rerank different kind of documents for a given query.

        Args: params: RerankParams: The parameters for reranking.

        Returns: RerankResponse: The reranked documents for the input query.

        Args:
          model: The model to use for reranking documents.

          query: The query to rerank the documents.

          input: The input documents to rerank.

          rank_fields: The fields of the documents to rank.

          top_k: The number of documents to return.

          return_input: Whether to return the documents.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.post(
            "/v1/reranking",
            body=maybe_transform(
                {
                    "model": model,
                    "query": query,
                    "input": input,
                    "rank_fields": rank_fields,
                    "top_k": top_k,
                    "return_input": return_input,
                },
                client_rerank_params.ClientRerankParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RerankResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncMixedbread(AsyncAPIClient):
    vector_stores: vector_stores.AsyncVectorStoresResource
    parsing: parsing.AsyncParsingResource
    files: files.AsyncFilesResource
    extractions: extractions.AsyncExtractionsResource
    embeddings: embeddings.AsyncEmbeddingsResource
    with_raw_response: AsyncMixedbreadWithRawResponse
    with_streaming_response: AsyncMixedbreadWithStreamedResponse

    # client options
    api_key: str

    _environment: Literal["production", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "local"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncMixedbread client instance.

        This automatically infers the `api_key` argument from the `MXBAI_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("MXBAI_API_KEY")
        if api_key is None:
            raise MixedbreadError(
                "The api_key client option must be set either by passing api_key to the client or by setting the MXBAI_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("MIXEDBREAD_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `MIXEDBREAD_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.vector_stores = vector_stores.AsyncVectorStoresResource(self)
        self.parsing = parsing.AsyncParsingResource(self)
        self.files = files.AsyncFilesResource(self)
        self.extractions = extractions.AsyncExtractionsResource(self)
        self.embeddings = embeddings.AsyncEmbeddingsResource(self)
        self.with_raw_response = AsyncMixedbreadWithRawResponse(self)
        self.with_streaming_response = AsyncMixedbreadWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    async def embed(
        self,
        *,
        model: str,
        input: Union[str, List[str]],
        dimensions: Optional[int] | NotGiven = NOT_GIVEN,
        prompt: Optional[str] | NotGiven = NOT_GIVEN,
        normalized: bool | NotGiven = NOT_GIVEN,
        encoding_format: Union[
            Literal["float", "float16", "base64", "binary", "ubinary", "int8", "uint8"],
            List[Literal["float", "float16", "base64", "binary", "ubinary", "int8", "uint8"]],
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmbeddingCreateResponse:
        """
        Create embeddings for text or images using the specified model, encoding format,
        and normalization.

        Args: params: The parameters for creating embeddings.

        Returns: EmbeddingCreateResponse: The response containing the embeddings.

        Args:
          model: The model to use for creating embeddings.

          input: The input to create embeddings for.

          dimensions: The number of dimensions to use for the embeddings.

          prompt: The prompt to use for the embedding creation.

          normalized: Whether to normalize the embeddings.

          encoding_format: The encoding format(s) of the embeddings. Can be a single format or a list of
              formats.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.post(
            "/v1/embeddings",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "input": input,
                    "dimensions": dimensions,
                    "prompt": prompt,
                    "normalized": normalized,
                    "encoding_format": encoding_format,
                },
                client_embed_params.ClientEmbedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbeddingCreateResponse,
        )

    async def info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InfoResponse:
        """
        Returns service information, including name and version.

        Returns: InfoResponse: A response containing the service name and version.
        """
        return await self.get(
            "/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InfoResponse,
        )

    async def rerank(
        self,
        *,
        model: str | NotGiven = NOT_GIVEN,
        query: str,
        input: List[Union[str, Iterable[object], object]],
        rank_fields: Optional[List[str]] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        return_input: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RerankResponse:
        """
        Rerank different kind of documents for a given query.

        Args: params: RerankParams: The parameters for reranking.

        Returns: RerankResponse: The reranked documents for the input query.

        Args:
          model: The model to use for reranking documents.

          query: The query to rerank the documents.

          input: The input documents to rerank.

          rank_fields: The fields of the documents to rank.

          top_k: The number of documents to return.

          return_input: Whether to return the documents.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.post(
            "/v1/reranking",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "query": query,
                    "input": input,
                    "rank_fields": rank_fields,
                    "top_k": top_k,
                    "return_input": return_input,
                },
                client_rerank_params.ClientRerankParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RerankResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class MixedbreadWithRawResponse:
    def __init__(self, client: Mixedbread) -> None:
        self.vector_stores = vector_stores.VectorStoresResourceWithRawResponse(client.vector_stores)
        self.parsing = parsing.ParsingResourceWithRawResponse(client.parsing)
        self.files = files.FilesResourceWithRawResponse(client.files)
        self.extractions = extractions.ExtractionsResourceWithRawResponse(client.extractions)
        self.embeddings = embeddings.EmbeddingsResourceWithRawResponse(client.embeddings)

        self.embed = to_raw_response_wrapper(
            client.embed,
        )
        self.info = to_raw_response_wrapper(
            client.info,
        )
        self.rerank = to_raw_response_wrapper(
            client.rerank,
        )


class AsyncMixedbreadWithRawResponse:
    def __init__(self, client: AsyncMixedbread) -> None:
        self.vector_stores = vector_stores.AsyncVectorStoresResourceWithRawResponse(client.vector_stores)
        self.parsing = parsing.AsyncParsingResourceWithRawResponse(client.parsing)
        self.files = files.AsyncFilesResourceWithRawResponse(client.files)
        self.extractions = extractions.AsyncExtractionsResourceWithRawResponse(client.extractions)
        self.embeddings = embeddings.AsyncEmbeddingsResourceWithRawResponse(client.embeddings)

        self.embed = async_to_raw_response_wrapper(
            client.embed,
        )
        self.info = async_to_raw_response_wrapper(
            client.info,
        )
        self.rerank = async_to_raw_response_wrapper(
            client.rerank,
        )


class MixedbreadWithStreamedResponse:
    def __init__(self, client: Mixedbread) -> None:
        self.vector_stores = vector_stores.VectorStoresResourceWithStreamingResponse(client.vector_stores)
        self.parsing = parsing.ParsingResourceWithStreamingResponse(client.parsing)
        self.files = files.FilesResourceWithStreamingResponse(client.files)
        self.extractions = extractions.ExtractionsResourceWithStreamingResponse(client.extractions)
        self.embeddings = embeddings.EmbeddingsResourceWithStreamingResponse(client.embeddings)

        self.embed = to_streamed_response_wrapper(
            client.embed,
        )
        self.info = to_streamed_response_wrapper(
            client.info,
        )
        self.rerank = to_streamed_response_wrapper(
            client.rerank,
        )


class AsyncMixedbreadWithStreamedResponse:
    def __init__(self, client: AsyncMixedbread) -> None:
        self.vector_stores = vector_stores.AsyncVectorStoresResourceWithStreamingResponse(client.vector_stores)
        self.parsing = parsing.AsyncParsingResourceWithStreamingResponse(client.parsing)
        self.files = files.AsyncFilesResourceWithStreamingResponse(client.files)
        self.extractions = extractions.AsyncExtractionsResourceWithStreamingResponse(client.extractions)
        self.embeddings = embeddings.AsyncEmbeddingsResourceWithStreamingResponse(client.embeddings)

        self.embed = async_to_streamed_response_wrapper(
            client.embed,
        )
        self.info = async_to_streamed_response_wrapper(
            client.info,
        )
        self.rerank = async_to_streamed_response_wrapper(
            client.rerank,
        )


Client = Mixedbread

AsyncClient = AsyncMixedbread
