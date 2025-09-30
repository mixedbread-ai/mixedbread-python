# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import shared
from .. import _compat
from .shared import Usage as Usage, SearchFilter as SearchFilter, SearchFilterCondition as SearchFilterCondition
from .api_key import APIKey as APIKey
from .embedding import Embedding as Embedding
from .data_source import DataSource as DataSource
from .file_object import FileObject as FileObject
from .vector_store import VectorStore as VectorStore
from .expires_after import ExpiresAfter as ExpiresAfter
from .info_response import InfoResponse as InfoResponse
from .oauth2_params import Oauth2Params as Oauth2Params
from .api_key_created import APIKeyCreated as APIKeyCreated
from .encoding_format import EncodingFormat as EncodingFormat
from .rerank_response import RerankResponse as RerankResponse
from .data_source_type import DataSourceType as DataSourceType
from .file_list_params import FileListParams as FileListParams
from .file_create_params import FileCreateParams as FileCreateParams
from .file_update_params import FileUpdateParams as FileUpdateParams
from .api_key_list_params import APIKeyListParams as APIKeyListParams
from .client_embed_params import ClientEmbedParams as ClientEmbedParams
from .expires_after_param import ExpiresAfterParam as ExpiresAfterParam
from .client_rerank_params import ClientRerankParams as ClientRerankParams
from .file_delete_response import FileDeleteResponse as FileDeleteResponse
from .api_key_create_params import APIKeyCreateParams as APIKeyCreateParams
from .pagination_with_total import PaginationWithTotal as PaginationWithTotal
from .api_key_delete_response import APIKeyDeleteResponse as APIKeyDeleteResponse
from .data_source_list_params import DataSourceListParams as DataSourceListParams
from .embedding_create_params import EmbeddingCreateParams as EmbeddingCreateParams
from .linear_data_source_param import LinearDataSourceParam as LinearDataSourceParam
from .multi_encoding_embedding import MultiEncodingEmbedding as MultiEncodingEmbedding
from .notion_data_source_param import NotionDataSourceParam as NotionDataSourceParam
from .vector_store_list_params import VectorStoreListParams as VectorStoreListParams
from .data_source_create_params import DataSourceCreateParams as DataSourceCreateParams
from .data_source_oauth2_params import DataSourceOauth2Params as DataSourceOauth2Params
from .data_source_update_params import DataSourceUpdateParams as DataSourceUpdateParams
from .embedding_create_response import EmbeddingCreateResponse as EmbeddingCreateResponse
from .vector_store_create_params import VectorStoreCreateParams as VectorStoreCreateParams
from .vector_store_search_params import VectorStoreSearchParams as VectorStoreSearchParams
from .vector_store_update_params import VectorStoreUpdateParams as VectorStoreUpdateParams
from .data_source_delete_response import DataSourceDeleteResponse as DataSourceDeleteResponse
from .vector_store_delete_response import VectorStoreDeleteResponse as VectorStoreDeleteResponse
from .vector_store_search_response import VectorStoreSearchResponse as VectorStoreSearchResponse
from .vector_store_question_answering_params import (
    VectorStoreQuestionAnsweringParams as VectorStoreQuestionAnsweringParams,
)
from .vector_store_chunk_search_options_param import (
    VectorStoreChunkSearchOptionsParam as VectorStoreChunkSearchOptionsParam,
)
from .vector_store_question_answering_response import (
    VectorStoreQuestionAnsweringResponse as VectorStoreQuestionAnsweringResponse,
)

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    shared.search_filter.SearchFilter.update_forward_refs()  # type: ignore
else:
    shared.search_filter.SearchFilter.model_rebuild(_parent_namespace_depth=0)
