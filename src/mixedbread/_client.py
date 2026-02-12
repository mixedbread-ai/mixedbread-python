# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, List, Union, Mapping, Iterable, Optional, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from .types import client_embed_params, client_rerank_params
from ._types import (
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    SequenceNotStr,
    omit,
    not_given,
)
from ._utils import (
    is_given,
    maybe_transform,
    get_async_library,
    async_maybe_transform,
)
from ._compat import cached_property
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, MixedbreadError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .types.info_response import InfoResponse
from .types.encoding_format import EncodingFormat
from .types.rerank_response import RerankResponse
from .types.embedding_create_response import EmbeddingCreateResponse

if TYPE_CHECKING:
    from .resources import chat, files, stores, parsing, api_keys, embeddings, extractions, data_sources
    from .resources.chat import ChatResource, AsyncChatResource
    from .resources.files import FilesResource, AsyncFilesResource
    from .resources.api_keys import APIKeysResource, AsyncAPIKeysResource
    from .resources.embeddings import EmbeddingsResource, AsyncEmbeddingsResource
    from .resources.stores.stores import StoresResource, AsyncStoresResource
    from .resources.parsing.parsing import ParsingResource, AsyncParsingResource
    from .resources.extractions.extractions import ExtractionsResource, AsyncExtractionsResource
    from .resources.data_sources.data_sources import DataSourcesResource, AsyncDataSourcesResource

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
    "development": "https://api.dev.mixedbread.com",
    "local": "http://127.0.0.1:8000",
}


class Mixedbread(SyncAPIClient):
    # client options
    api_key: str

    _environment: Literal["production", "development", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "development", "local"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
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

    @cached_property
    def stores(self) -> StoresResource:
        from .resources.stores import StoresResource

        return StoresResource(self)

    @cached_property
    def parsing(self) -> ParsingResource:
        from .resources.parsing import ParsingResource

        return ParsingResource(self)

    @cached_property
    def files(self) -> FilesResource:
        from .resources.files import FilesResource

        return FilesResource(self)

    @cached_property
    def extractions(self) -> ExtractionsResource:
        from .resources.extractions import ExtractionsResource

        return ExtractionsResource(self)

    @cached_property
    def embeddings(self) -> EmbeddingsResource:
        from .resources.embeddings import EmbeddingsResource

        return EmbeddingsResource(self)

    @cached_property
    def data_sources(self) -> DataSourcesResource:
        from .resources.data_sources import DataSourcesResource

        return DataSourcesResource(self)

    @cached_property
    def api_keys(self) -> APIKeysResource:
        from .resources.api_keys import APIKeysResource

        return APIKeysResource(self)

    @cached_property
    def chat(self) -> ChatResource:
        from .resources.chat import ChatResource

        return ChatResource(self)

    @cached_property
    def with_raw_response(self) -> MixedbreadWithRawResponse:
        return MixedbreadWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MixedbreadWithStreamedResponse:
        return MixedbreadWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

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
        environment: Literal["production", "development", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
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
        input: Union[str, SequenceNotStr[str]],
        dimensions: Optional[int] | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        normalized: bool | Omit = omit,
        encoding_format: Union[EncodingFormat, List[EncodingFormat]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        model: str | Omit = omit,
        query: str,
        input: SequenceNotStr[Union[str, Iterable[object], object]],
        rank_fields: Optional[SequenceNotStr[str]] | Omit = omit,
        top_k: int | Omit = omit,
        return_input: bool | Omit = omit,
        rewrite_query: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

          rewrite_query: Wether or not to rewrite the query before passing it to the reranking model

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
                    "rewrite_query": rewrite_query,
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
    # client options
    api_key: str

    _environment: Literal["production", "development", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "development", "local"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
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

    @cached_property
    def stores(self) -> AsyncStoresResource:
        from .resources.stores import AsyncStoresResource

        return AsyncStoresResource(self)

    @cached_property
    def parsing(self) -> AsyncParsingResource:
        from .resources.parsing import AsyncParsingResource

        return AsyncParsingResource(self)

    @cached_property
    def files(self) -> AsyncFilesResource:
        from .resources.files import AsyncFilesResource

        return AsyncFilesResource(self)

    @cached_property
    def extractions(self) -> AsyncExtractionsResource:
        from .resources.extractions import AsyncExtractionsResource

        return AsyncExtractionsResource(self)

    @cached_property
    def embeddings(self) -> AsyncEmbeddingsResource:
        from .resources.embeddings import AsyncEmbeddingsResource

        return AsyncEmbeddingsResource(self)

    @cached_property
    def data_sources(self) -> AsyncDataSourcesResource:
        from .resources.data_sources import AsyncDataSourcesResource

        return AsyncDataSourcesResource(self)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResource:
        from .resources.api_keys import AsyncAPIKeysResource

        return AsyncAPIKeysResource(self)

    @cached_property
    def chat(self) -> AsyncChatResource:
        from .resources.chat import AsyncChatResource

        return AsyncChatResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncMixedbreadWithRawResponse:
        return AsyncMixedbreadWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMixedbreadWithStreamedResponse:
        return AsyncMixedbreadWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

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
        environment: Literal["production", "development", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
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
        input: Union[str, SequenceNotStr[str]],
        dimensions: Optional[int] | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        normalized: bool | Omit = omit,
        encoding_format: Union[EncodingFormat, List[EncodingFormat]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        model: str | Omit = omit,
        query: str,
        input: SequenceNotStr[Union[str, Iterable[object], object]],
        rank_fields: Optional[SequenceNotStr[str]] | Omit = omit,
        top_k: int | Omit = omit,
        return_input: bool | Omit = omit,
        rewrite_query: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

          rewrite_query: Wether or not to rewrite the query before passing it to the reranking model

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
                    "rewrite_query": rewrite_query,
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
    _client: Mixedbread

    def __init__(self, client: Mixedbread) -> None:
        self._client = client

        self.embed = to_raw_response_wrapper(
            client.embed,
        )
        self.info = to_raw_response_wrapper(
            client.info,
        )
        self.rerank = to_raw_response_wrapper(
            client.rerank,
        )

    @cached_property
    def stores(self) -> stores.StoresResourceWithRawResponse:
        from .resources.stores import StoresResourceWithRawResponse

        return StoresResourceWithRawResponse(self._client.stores)

    @cached_property
    def parsing(self) -> parsing.ParsingResourceWithRawResponse:
        from .resources.parsing import ParsingResourceWithRawResponse

        return ParsingResourceWithRawResponse(self._client.parsing)

    @cached_property
    def files(self) -> files.FilesResourceWithRawResponse:
        from .resources.files import FilesResourceWithRawResponse

        return FilesResourceWithRawResponse(self._client.files)

    @cached_property
    def extractions(self) -> extractions.ExtractionsResourceWithRawResponse:
        from .resources.extractions import ExtractionsResourceWithRawResponse

        return ExtractionsResourceWithRawResponse(self._client.extractions)

    @cached_property
    def embeddings(self) -> embeddings.EmbeddingsResourceWithRawResponse:
        from .resources.embeddings import EmbeddingsResourceWithRawResponse

        return EmbeddingsResourceWithRawResponse(self._client.embeddings)

    @cached_property
    def data_sources(self) -> data_sources.DataSourcesResourceWithRawResponse:
        from .resources.data_sources import DataSourcesResourceWithRawResponse

        return DataSourcesResourceWithRawResponse(self._client.data_sources)

    @cached_property
    def api_keys(self) -> api_keys.APIKeysResourceWithRawResponse:
        from .resources.api_keys import APIKeysResourceWithRawResponse

        return APIKeysResourceWithRawResponse(self._client.api_keys)

    @cached_property
    def chat(self) -> chat.ChatResourceWithRawResponse:
        from .resources.chat import ChatResourceWithRawResponse

        return ChatResourceWithRawResponse(self._client.chat)


class AsyncMixedbreadWithRawResponse:
    _client: AsyncMixedbread

    def __init__(self, client: AsyncMixedbread) -> None:
        self._client = client

        self.embed = async_to_raw_response_wrapper(
            client.embed,
        )
        self.info = async_to_raw_response_wrapper(
            client.info,
        )
        self.rerank = async_to_raw_response_wrapper(
            client.rerank,
        )

    @cached_property
    def stores(self) -> stores.AsyncStoresResourceWithRawResponse:
        from .resources.stores import AsyncStoresResourceWithRawResponse

        return AsyncStoresResourceWithRawResponse(self._client.stores)

    @cached_property
    def parsing(self) -> parsing.AsyncParsingResourceWithRawResponse:
        from .resources.parsing import AsyncParsingResourceWithRawResponse

        return AsyncParsingResourceWithRawResponse(self._client.parsing)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithRawResponse:
        from .resources.files import AsyncFilesResourceWithRawResponse

        return AsyncFilesResourceWithRawResponse(self._client.files)

    @cached_property
    def extractions(self) -> extractions.AsyncExtractionsResourceWithRawResponse:
        from .resources.extractions import AsyncExtractionsResourceWithRawResponse

        return AsyncExtractionsResourceWithRawResponse(self._client.extractions)

    @cached_property
    def embeddings(self) -> embeddings.AsyncEmbeddingsResourceWithRawResponse:
        from .resources.embeddings import AsyncEmbeddingsResourceWithRawResponse

        return AsyncEmbeddingsResourceWithRawResponse(self._client.embeddings)

    @cached_property
    def data_sources(self) -> data_sources.AsyncDataSourcesResourceWithRawResponse:
        from .resources.data_sources import AsyncDataSourcesResourceWithRawResponse

        return AsyncDataSourcesResourceWithRawResponse(self._client.data_sources)

    @cached_property
    def api_keys(self) -> api_keys.AsyncAPIKeysResourceWithRawResponse:
        from .resources.api_keys import AsyncAPIKeysResourceWithRawResponse

        return AsyncAPIKeysResourceWithRawResponse(self._client.api_keys)

    @cached_property
    def chat(self) -> chat.AsyncChatResourceWithRawResponse:
        from .resources.chat import AsyncChatResourceWithRawResponse

        return AsyncChatResourceWithRawResponse(self._client.chat)


class MixedbreadWithStreamedResponse:
    _client: Mixedbread

    def __init__(self, client: Mixedbread) -> None:
        self._client = client

        self.embed = to_streamed_response_wrapper(
            client.embed,
        )
        self.info = to_streamed_response_wrapper(
            client.info,
        )
        self.rerank = to_streamed_response_wrapper(
            client.rerank,
        )

    @cached_property
    def stores(self) -> stores.StoresResourceWithStreamingResponse:
        from .resources.stores import StoresResourceWithStreamingResponse

        return StoresResourceWithStreamingResponse(self._client.stores)

    @cached_property
    def parsing(self) -> parsing.ParsingResourceWithStreamingResponse:
        from .resources.parsing import ParsingResourceWithStreamingResponse

        return ParsingResourceWithStreamingResponse(self._client.parsing)

    @cached_property
    def files(self) -> files.FilesResourceWithStreamingResponse:
        from .resources.files import FilesResourceWithStreamingResponse

        return FilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def extractions(self) -> extractions.ExtractionsResourceWithStreamingResponse:
        from .resources.extractions import ExtractionsResourceWithStreamingResponse

        return ExtractionsResourceWithStreamingResponse(self._client.extractions)

    @cached_property
    def embeddings(self) -> embeddings.EmbeddingsResourceWithStreamingResponse:
        from .resources.embeddings import EmbeddingsResourceWithStreamingResponse

        return EmbeddingsResourceWithStreamingResponse(self._client.embeddings)

    @cached_property
    def data_sources(self) -> data_sources.DataSourcesResourceWithStreamingResponse:
        from .resources.data_sources import DataSourcesResourceWithStreamingResponse

        return DataSourcesResourceWithStreamingResponse(self._client.data_sources)

    @cached_property
    def api_keys(self) -> api_keys.APIKeysResourceWithStreamingResponse:
        from .resources.api_keys import APIKeysResourceWithStreamingResponse

        return APIKeysResourceWithStreamingResponse(self._client.api_keys)

    @cached_property
    def chat(self) -> chat.ChatResourceWithStreamingResponse:
        from .resources.chat import ChatResourceWithStreamingResponse

        return ChatResourceWithStreamingResponse(self._client.chat)


class AsyncMixedbreadWithStreamedResponse:
    _client: AsyncMixedbread

    def __init__(self, client: AsyncMixedbread) -> None:
        self._client = client

        self.embed = async_to_streamed_response_wrapper(
            client.embed,
        )
        self.info = async_to_streamed_response_wrapper(
            client.info,
        )
        self.rerank = async_to_streamed_response_wrapper(
            client.rerank,
        )

    @cached_property
    def stores(self) -> stores.AsyncStoresResourceWithStreamingResponse:
        from .resources.stores import AsyncStoresResourceWithStreamingResponse

        return AsyncStoresResourceWithStreamingResponse(self._client.stores)

    @cached_property
    def parsing(self) -> parsing.AsyncParsingResourceWithStreamingResponse:
        from .resources.parsing import AsyncParsingResourceWithStreamingResponse

        return AsyncParsingResourceWithStreamingResponse(self._client.parsing)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithStreamingResponse:
        from .resources.files import AsyncFilesResourceWithStreamingResponse

        return AsyncFilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def extractions(self) -> extractions.AsyncExtractionsResourceWithStreamingResponse:
        from .resources.extractions import AsyncExtractionsResourceWithStreamingResponse

        return AsyncExtractionsResourceWithStreamingResponse(self._client.extractions)

    @cached_property
    def embeddings(self) -> embeddings.AsyncEmbeddingsResourceWithStreamingResponse:
        from .resources.embeddings import AsyncEmbeddingsResourceWithStreamingResponse

        return AsyncEmbeddingsResourceWithStreamingResponse(self._client.embeddings)

    @cached_property
    def data_sources(self) -> data_sources.AsyncDataSourcesResourceWithStreamingResponse:
        from .resources.data_sources import AsyncDataSourcesResourceWithStreamingResponse

        return AsyncDataSourcesResourceWithStreamingResponse(self._client.data_sources)

    @cached_property
    def api_keys(self) -> api_keys.AsyncAPIKeysResourceWithStreamingResponse:
        from .resources.api_keys import AsyncAPIKeysResourceWithStreamingResponse

        return AsyncAPIKeysResourceWithStreamingResponse(self._client.api_keys)

    @cached_property
    def chat(self) -> chat.AsyncChatResourceWithStreamingResponse:
        from .resources.chat import AsyncChatResourceWithStreamingResponse

        return AsyncChatResourceWithStreamingResponse(self._client.chat)


Client = Mixedbread

AsyncClient = AsyncMixedbread
