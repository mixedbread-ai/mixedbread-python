# Base

Types:

```python
from mixedbread.types import BaseStatusResponse
```

Methods:

- <code title="get /">client.base.<a href="./src/mixedbread/resources/base.py">status</a>() -> <a href="./src/mixedbread/types/base_status_response.py">BaseStatusResponse</a></code>

# VectorStores

Types:

```python
from mixedbread.types import (
    VectorStoreCreateResponse,
    VectorStoreRetrieveResponse,
    VectorStoreUpdateResponse,
    VectorStoreListResponse,
    VectorStoreDeleteResponse,
    VectorStoreSearchResponse,
)
```

Methods:

- <code title="post /v1/vector_stores">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">create</a>(\*\*<a href="src/mixedbread/types/vector_store_create_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_store_create_response.py">VectorStoreCreateResponse</a></code>
- <code title="get /v1/vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">retrieve</a>(vector_store_id) -> <a href="./src/mixedbread/types/vector_store_retrieve_response.py">VectorStoreRetrieveResponse</a></code>
- <code title="put /v1/vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">update</a>(vector_store_id, \*\*<a href="src/mixedbread/types/vector_store_update_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_store_update_response.py">VectorStoreUpdateResponse</a></code>
- <code title="get /v1/vector_stores">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">list</a>(\*\*<a href="src/mixedbread/types/vector_store_list_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_store_list_response.py">VectorStoreListResponse</a></code>
- <code title="delete /v1/vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">delete</a>(vector_store_id) -> <a href="./src/mixedbread/types/vector_store_delete_response.py">VectorStoreDeleteResponse</a></code>
- <code title="post /v1/vector_stores/search">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">search</a>(\*\*<a href="src/mixedbread/types/vector_store_search_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_store_search_response.py">VectorStoreSearchResponse</a></code>

## Files

Types:

```python
from mixedbread.types.vector_stores import (
    FileCreateResponse,
    FileRetrieveResponse,
    FileListResponse,
    FileDeleteResponse,
)
```

Methods:

- <code title="post /v1/vector_stores/{vector_store_id}/files">client.vector_stores.files.<a href="./src/mixedbread/resources/vector_stores/files.py">create</a>(vector_store_id, \*\*<a href="src/mixedbread/types/vector_stores/file_create_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_stores/file_create_response.py">FileCreateResponse</a></code>
- <code title="get /v1/vector_stores/{vector_store_id}/files/{file_id}">client.vector_stores.files.<a href="./src/mixedbread/resources/vector_stores/files.py">retrieve</a>(file_id, \*, vector_store_id) -> <a href="./src/mixedbread/types/vector_stores/file_retrieve_response.py">FileRetrieveResponse</a></code>
- <code title="get /v1/vector_stores/{vector_store_id}/files">client.vector_stores.files.<a href="./src/mixedbread/resources/vector_stores/files.py">list</a>(vector_store_id, \*\*<a href="src/mixedbread/types/vector_stores/file_list_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_stores/file_list_response.py">FileListResponse</a></code>
- <code title="delete /v1/vector_stores/{vector_store_id}/files/{file_id}">client.vector_stores.files.<a href="./src/mixedbread/resources/vector_stores/files.py">delete</a>(file_id, \*, vector_store_id) -> <a href="./src/mixedbread/types/vector_stores/file_delete_response.py">FileDeleteResponse</a></code>

# DocumentAI

## Parse

Types:

```python
from mixedbread.types.document_ai import ParseCreateResponse, ParseRetrieveResponse
```

Methods:

- <code title="post /v1/document-ai/parse">client.document_ai.parse.<a href="./src/mixedbread/resources/document_ai/parse.py">create</a>(\*\*<a href="src/mixedbread/types/document_ai/parse_create_params.py">params</a>) -> <a href="./src/mixedbread/types/document_ai/parse_create_response.py">ParseCreateResponse</a></code>
- <code title="get /v1/document-ai/parse/{job_id}">client.document_ai.parse.<a href="./src/mixedbread/resources/document_ai/parse.py">retrieve</a>(job_id) -> <a href="./src/mixedbread/types/document_ai/parse_retrieve_response.py">ParseRetrieveResponse</a></code>

# Embeddings

Types:

```python
from mixedbread.types import EmbeddingCreateResponse
```

Methods:

- <code title="post /v1/embeddings">client.embeddings.<a href="./src/mixedbread/resources/embeddings.py">create</a>(\*\*<a href="src/mixedbread/types/embedding_create_params.py">params</a>) -> <a href="./src/mixedbread/types/embedding_create_response.py">EmbeddingCreateResponse</a></code>

# Reranking

Types:

```python
from mixedbread.types import RerankingCreateResponse
```

Methods:

- <code title="post /v1/reranking">client.reranking.<a href="./src/mixedbread/resources/reranking.py">create</a>(\*\*<a href="src/mixedbread/types/reranking_create_params.py">params</a>) -> <a href="./src/mixedbread/types/reranking_create_response.py">RerankingCreateResponse</a></code>

# Files

Types:

```python
from mixedbread.types import (
    FileCreateResponse,
    FileRetrieveResponse,
    FileUpdateResponse,
    FileListResponse,
    FileDeleteResponse,
)
```

Methods:

- <code title="post /v1/files">client.files.<a href="./src/mixedbread/resources/files.py">create</a>(\*\*<a href="src/mixedbread/types/file_create_params.py">params</a>) -> <a href="./src/mixedbread/types/file_create_response.py">FileCreateResponse</a></code>
- <code title="get /v1/files/{file_id}">client.files.<a href="./src/mixedbread/resources/files.py">retrieve</a>(file_id) -> <a href="./src/mixedbread/types/file_retrieve_response.py">FileRetrieveResponse</a></code>
- <code title="put /v1/files/{file_id}">client.files.<a href="./src/mixedbread/resources/files.py">update</a>(file_id, \*\*<a href="src/mixedbread/types/file_update_params.py">params</a>) -> <a href="./src/mixedbread/types/file_update_response.py">FileUpdateResponse</a></code>
- <code title="get /v1/files">client.files.<a href="./src/mixedbread/resources/files.py">list</a>(\*\*<a href="src/mixedbread/types/file_list_params.py">params</a>) -> <a href="./src/mixedbread/types/file_list_response.py">FileListResponse</a></code>
- <code title="delete /v1/files/{file_id}">client.files.<a href="./src/mixedbread/resources/files.py">delete</a>(file_id) -> <a href="./src/mixedbread/types/file_delete_response.py">FileDeleteResponse</a></code>
- <code title="get /v1/files/{file_id}/content">client.files.<a href="./src/mixedbread/resources/files.py">content</a>(file_id) -> BinaryAPIResponse</code>

# Jobs

Types:

```python
from mixedbread.types import JobRetrieveResponse, JobDeleteResponse
```

Methods:

- <code title="get /v1/jobs/{job_id}">client.jobs.<a href="./src/mixedbread/resources/jobs.py">retrieve</a>(job_id) -> JobRetrieveResponse</code>
- <code title="delete /v1/jobs/{job_id}">client.jobs.<a href="./src/mixedbread/resources/jobs.py">delete</a>(job_id) -> <a href="./src/mixedbread/types/job_delete_response.py">JobDeleteResponse</a></code>
