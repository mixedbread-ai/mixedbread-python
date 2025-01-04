# Mixedbread

Types:

```python
from mixedbread.types import EmbedResponse, InfoResponse, RerankResponse
```

Methods:

- <code title="post /v1/embeddings">client.<a href="./src/mixedbread/_client.py">embed</a>(\*\*<a href="src/mixedbread/types/client_embed_params.py">params</a>) -> <a href="./src/mixedbread/types/embed_response.py">EmbedResponse</a></code>
- <code title="get /">client.<a href="./src/mixedbread/_client.py">info</a>() -> <a href="./src/mixedbread/types/info_response.py">InfoResponse</a></code>
- <code title="post /v1/reranking">client.<a href="./src/mixedbread/_client.py">rerank</a>(\*\*<a href="src/mixedbread/types/client_rerank_params.py">params</a>) -> <a href="./src/mixedbread/types/rerank_response.py">RerankResponse</a></code>

# DocumentAI

## Parse

### Jobs

Types:

```python
from mixedbread.types.document_ai.parse import JobCreateResponse, JobRetrieveResponse
```

Methods:

- <code title="post /v1/document-ai/parse">client.document_ai.parse.jobs.<a href="./src/mixedbread/resources/document_ai/parse/jobs.py">create</a>(\*\*<a href="src/mixedbread/types/document_ai/parse/job_create_params.py">params</a>) -> <a href="./src/mixedbread/types/document_ai/parse/job_create_response.py">JobCreateResponse</a></code>
- <code title="get /v1/document-ai/parse/{job_id}">client.document_ai.parse.jobs.<a href="./src/mixedbread/resources/document_ai/parse/jobs.py">retrieve</a>(job_id) -> <a href="./src/mixedbread/types/document_ai/parse/job_retrieve_response.py">JobRetrieveResponse</a></code>

# Embeddings

Types:

```python
from mixedbread.types import EmbeddingCreateResponse
```

Methods:

- <code title="post /v1/embeddings">client.embeddings.<a href="./src/mixedbread/resources/embeddings.py">create</a>(\*\*<a href="src/mixedbread/types/embedding_create_params.py">params</a>) -> <a href="./src/mixedbread/types/embedding_create_response.py">EmbeddingCreateResponse</a></code>

# Rerankings

Types:

```python
from mixedbread.types import RerankingCreateResponse
```

Methods:

- <code title="post /v1/reranking">client.rerankings.<a href="./src/mixedbread/resources/rerankings.py">create</a>(\*\*<a href="src/mixedbread/types/reranking_create_params.py">params</a>) -> <a href="./src/mixedbread/types/reranking_create_response.py">RerankingCreateResponse</a></code>

# Files

Types:

```python
from mixedbread.types import FileDeleted, FileObject, FileListResponse
```

Methods:

- <code title="post /v1/files">client.files.<a href="./src/mixedbread/resources/files.py">create</a>(\*\*<a href="src/mixedbread/types/file_create_params.py">params</a>) -> <a href="./src/mixedbread/types/file_object.py">FileObject</a></code>
- <code title="get /v1/files/{file_id}">client.files.<a href="./src/mixedbread/resources/files.py">retrieve</a>(file_id) -> <a href="./src/mixedbread/types/file_object.py">FileObject</a></code>
- <code title="post /v1/files/{file_id}">client.files.<a href="./src/mixedbread/resources/files.py">update</a>(file_id, \*\*<a href="src/mixedbread/types/file_update_params.py">params</a>) -> <a href="./src/mixedbread/types/file_object.py">FileObject</a></code>
- <code title="get /v1/files">client.files.<a href="./src/mixedbread/resources/files.py">list</a>(\*\*<a href="src/mixedbread/types/file_list_params.py">params</a>) -> <a href="./src/mixedbread/types/file_list_response.py">FileListResponse</a></code>
- <code title="delete /v1/files/{file_id}">client.files.<a href="./src/mixedbread/resources/files.py">delete</a>(file_id) -> <a href="./src/mixedbread/types/file_deleted.py">FileDeleted</a></code>
- <code title="get /v1/files/{file_id}/content">client.files.<a href="./src/mixedbread/resources/files.py">content</a>(file_id) -> BinaryAPIResponse</code>

# VectorStores

Types:

```python
from mixedbread.types import (
    SearchParams,
    VectorStore,
    VectorStoreListResponse,
    VectorStoreDeleteResponse,
    VectorStoreQaResponse,
    VectorStoreSearchResponse,
)
```

Methods:

- <code title="post /v1/vector_stores">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">create</a>(\*\*<a href="src/mixedbread/types/vector_store_create_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_store.py">VectorStore</a></code>
- <code title="get /v1/vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">retrieve</a>(vector_store_id) -> <a href="./src/mixedbread/types/vector_store.py">VectorStore</a></code>
- <code title="put /v1/vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">update</a>(vector_store_id, \*\*<a href="src/mixedbread/types/vector_store_update_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_store.py">VectorStore</a></code>
- <code title="get /v1/vector_stores">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">list</a>(\*\*<a href="src/mixedbread/types/vector_store_list_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_store_list_response.py">VectorStoreListResponse</a></code>
- <code title="delete /v1/vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">delete</a>(vector_store_id) -> <a href="./src/mixedbread/types/vector_store_delete_response.py">VectorStoreDeleteResponse</a></code>
- <code title="post /v1/vector_stores/question-answering">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">qa</a>(\*\*<a href="src/mixedbread/types/vector_store_qa_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_store_qa_response.py">object</a></code>
- <code title="post /v1/vector_stores/search">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">search</a>(\*\*<a href="src/mixedbread/types/vector_store_search_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_store_search_response.py">VectorStoreSearchResponse</a></code>

## Files

Types:

```python
from mixedbread.types.vector_stores import VectorStoreFile, FileListResponse, FileDeleteResponse
```

Methods:

- <code title="post /v1/vector_stores/{vector_store_id}/files">client.vector_stores.files.<a href="./src/mixedbread/resources/vector_stores/files.py">create</a>(vector_store_id, \*\*<a href="src/mixedbread/types/vector_stores/file_create_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_stores/vector_store_file.py">VectorStoreFile</a></code>
- <code title="get /v1/vector_stores/{vector_store_id}/files/{file_id}">client.vector_stores.files.<a href="./src/mixedbread/resources/vector_stores/files.py">retrieve</a>(file_id, \*, vector_store_id) -> <a href="./src/mixedbread/types/vector_stores/vector_store_file.py">VectorStoreFile</a></code>
- <code title="get /v1/vector_stores/{vector_store_id}/files">client.vector_stores.files.<a href="./src/mixedbread/resources/vector_stores/files.py">list</a>(vector_store_id, \*\*<a href="src/mixedbread/types/vector_stores/file_list_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_stores/file_list_response.py">FileListResponse</a></code>
- <code title="delete /v1/vector_stores/{vector_store_id}/files/{file_id}">client.vector_stores.files.<a href="./src/mixedbread/resources/vector_stores/files.py">delete</a>(file_id, \*, vector_store_id) -> <a href="./src/mixedbread/types/vector_stores/file_delete_response.py">FileDeleteResponse</a></code>

# Chat

## Completions

Types:

```python
from mixedbread.types.chat import CompletionCreateResponse
```

Methods:

- <code title="post /v1/chat/completions">client.chat.completions.<a href="./src/mixedbread/resources/chat/completions.py">create</a>() -> <a href="./src/mixedbread/types/chat/completion_create_response.py">object</a></code>
