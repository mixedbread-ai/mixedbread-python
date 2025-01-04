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

Types:

```python
from mixedbread.types.document_ai import ParseCreateJobResponse, ParseRetrieveJobResponse
```

Methods:

- <code title="post /v1/document-ai/parse">client.document_ai.parse.<a href="./src/mixedbread/resources/document_ai/parse.py">create_job</a>(\*\*<a href="src/mixedbread/types/document_ai/parse_create_job_params.py">params</a>) -> <a href="./src/mixedbread/types/document_ai/parse_create_job_response.py">ParseCreateJobResponse</a></code>
- <code title="get /v1/document-ai/parse/{job_id}">client.document_ai.parse.<a href="./src/mixedbread/resources/document_ai/parse.py">retrieve_job</a>(job_id) -> <a href="./src/mixedbread/types/document_ai/parse_retrieve_job_response.py">ParseRetrieveJobResponse</a></code>

## Extract

Types:

```python
from mixedbread.types.document_ai import (
    Result,
    ExtractCreateJobResponse,
    ExtractRetrieveJobResponse,
)
```

Methods:

- <code title="post /v1/document-ai/extract/content">client.document_ai.extract.<a href="./src/mixedbread/resources/document_ai/extract/extract.py">content</a>(\*\*<a href="src/mixedbread/types/document_ai/extract_content_params.py">params</a>) -> <a href="./src/mixedbread/types/document_ai/result.py">Result</a></code>
- <code title="post /v1/document-ai/extract">client.document_ai.extract.<a href="./src/mixedbread/resources/document_ai/extract/extract.py">create_job</a>(\*\*<a href="src/mixedbread/types/document_ai/extract_create_job_params.py">params</a>) -> <a href="./src/mixedbread/types/document_ai/extract_create_job_response.py">ExtractCreateJobResponse</a></code>
- <code title="get /v1/document-ai/extract/{job_id}">client.document_ai.extract.<a href="./src/mixedbread/resources/document_ai/extract/extract.py">retrieve_job</a>(job_id) -> <a href="./src/mixedbread/types/document_ai/extract_retrieve_job_response.py">ExtractRetrieveJobResponse</a></code>

### Schema

Types:

```python
from mixedbread.types.document_ai.extract import (
    CreatedJsonSchema,
    EnhancedJsonSchema,
    ValidatedJsonSchema,
)
```

Methods:

- <code title="post /v1/document-ai/extract/schema">client.document_ai.extract.schema.<a href="./src/mixedbread/resources/document_ai/extract/schema.py">create</a>(\*\*<a href="src/mixedbread/types/document_ai/extract/schema_create_params.py">params</a>) -> <a href="./src/mixedbread/types/document_ai/extract/created_json_schema.py">CreatedJsonSchema</a></code>
- <code title="post /v1/document-ai/extract/schema/enhance">client.document_ai.extract.schema.<a href="./src/mixedbread/resources/document_ai/extract/schema.py">enhance</a>(\*\*<a href="src/mixedbread/types/document_ai/extract/schema_enhance_params.py">params</a>) -> <a href="./src/mixedbread/types/document_ai/extract/enhanced_json_schema.py">EnhancedJsonSchema</a></code>
- <code title="post /v1/document-ai/extract/schema/validate">client.document_ai.extract.schema.<a href="./src/mixedbread/resources/document_ai/extract/schema.py">validate</a>(\*\*<a href="src/mixedbread/types/document_ai/extract/schema_validate_params.py">params</a>) -> <a href="./src/mixedbread/types/document_ai/extract/validated_json_schema.py">ValidatedJsonSchema</a></code>

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
    SearchResponse,
    VectorStore,
    VectorStoreListResponse,
    VectorStoreDeleteResponse,
    VectorStoreQuestionAnsweringResponse,
)
```

Methods:

- <code title="post /v1/vector_stores">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">create</a>(\*\*<a href="src/mixedbread/types/vector_store_create_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_store.py">VectorStore</a></code>
- <code title="get /v1/vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">retrieve</a>(vector_store_id) -> <a href="./src/mixedbread/types/vector_store.py">VectorStore</a></code>
- <code title="put /v1/vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">update</a>(vector_store_id, \*\*<a href="src/mixedbread/types/vector_store_update_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_store.py">VectorStore</a></code>
- <code title="get /v1/vector_stores">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">list</a>(\*\*<a href="src/mixedbread/types/vector_store_list_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_store_list_response.py">VectorStoreListResponse</a></code>
- <code title="delete /v1/vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">delete</a>(vector_store_id) -> <a href="./src/mixedbread/types/vector_store_delete_response.py">VectorStoreDeleteResponse</a></code>
- <code title="post /v1/vector_stores/question-answering">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">question_answering</a>(\*\*<a href="src/mixedbread/types/vector_store_question_answering_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_store_question_answering_response.py">object</a></code>
- <code title="post /v1/vector_stores/search">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">search</a>(\*\*<a href="src/mixedbread/types/vector_store_search_params.py">params</a>) -> <a href="./src/mixedbread/types/search_response.py">SearchResponse</a></code>

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
