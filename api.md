# Shared Types

```python
from mixedbread.types import SearchFilter, SearchFilterCondition
```

# Mixedbread

Types:

```python
from mixedbread.types import InfoResponse
```

Methods:

- <code title="get /">client.<a href="./src/mixedbread/_client.py">info</a>() -> <a href="./src/mixedbread/types/info_response.py">InfoResponse</a></code>

# Embeddings

Types:

```python
from mixedbread.types import Embedding, EmbeddingCreateResponse
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

# Parsing

## Jobs

Types:

```python
from mixedbread.types.parsing import ParsingJob
```

Methods:

- <code title="post /v1/parsing/jobs">client.parsing.jobs.<a href="./src/mixedbread/resources/parsing/jobs.py">create</a>(\*\*<a href="src/mixedbread/types/parsing/job_create_params.py">params</a>) -> <a href="./src/mixedbread/types/parsing/parsing_job.py">ParsingJob</a></code>
- <code title="get /v1/parsing/jobs/{job_id}">client.parsing.jobs.<a href="./src/mixedbread/resources/parsing/jobs.py">retrieve</a>(job_id) -> <a href="./src/mixedbread/types/parsing/parsing_job.py">ParsingJob</a></code>
- <code title="get /v1/parsing/jobs">client.parsing.jobs.<a href="./src/mixedbread/resources/parsing/jobs.py">list</a>(\*\*<a href="src/mixedbread/types/parsing/job_list_params.py">params</a>) -> <a href="./src/mixedbread/types/parsing/parsing_job.py">SyncLimitOffset[ParsingJob]</a></code>
- <code title="delete /v1/parsing/jobs/{job_id}">client.parsing.jobs.<a href="./src/mixedbread/resources/parsing/jobs.py">cancel</a>(job_id) -> <a href="./src/mixedbread/types/parsing/parsing_job.py">ParsingJob</a></code>

# Files

Types:

```python
from mixedbread.types import FileObject, FileDeleteResponse
```

Methods:

- <code title="post /v1/files">client.files.<a href="./src/mixedbread/resources/files.py">create</a>(\*\*<a href="src/mixedbread/types/file_create_params.py">params</a>) -> <a href="./src/mixedbread/types/file_object.py">FileObject</a></code>
- <code title="get /v1/files/{file_id}">client.files.<a href="./src/mixedbread/resources/files.py">retrieve</a>(file_id) -> <a href="./src/mixedbread/types/file_object.py">FileObject</a></code>
- <code title="post /v1/files/{file_id}">client.files.<a href="./src/mixedbread/resources/files.py">update</a>(file_id, \*\*<a href="src/mixedbread/types/file_update_params.py">params</a>) -> <a href="./src/mixedbread/types/file_object.py">FileObject</a></code>
- <code title="get /v1/files">client.files.<a href="./src/mixedbread/resources/files.py">list</a>(\*\*<a href="src/mixedbread/types/file_list_params.py">params</a>) -> <a href="./src/mixedbread/types/file_object.py">SyncLimitOffset[FileObject]</a></code>
- <code title="delete /v1/files/{file_id}">client.files.<a href="./src/mixedbread/resources/files.py">delete</a>(file_id) -> <a href="./src/mixedbread/types/file_delete_response.py">FileDeleteResponse</a></code>
- <code title="get /v1/files/{file_id}/content">client.files.<a href="./src/mixedbread/resources/files.py">content</a>(file_id) -> BinaryAPIResponse</code>

# VectorStores

Types:

```python
from mixedbread.types import (
    ExpiresAfter,
    FileCounts,
    ScoredVectorStoreChunk,
    VectorStore,
    VectorStoreSearchOptions,
    VectorStoreDeleteResponse,
    VectorStoreQuestionAnsweringResponse,
    VectorStoreSearchResponse,
)
```

Methods:

- <code title="post /v1/vector_stores">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">create</a>(\*\*<a href="src/mixedbread/types/vector_store_create_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_store.py">VectorStore</a></code>
- <code title="get /v1/vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">retrieve</a>(vector_store_id) -> <a href="./src/mixedbread/types/vector_store.py">VectorStore</a></code>
- <code title="put /v1/vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">update</a>(vector_store_id, \*\*<a href="src/mixedbread/types/vector_store_update_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_store.py">VectorStore</a></code>
- <code title="get /v1/vector_stores">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">list</a>(\*\*<a href="src/mixedbread/types/vector_store_list_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_store.py">SyncLimitOffset[VectorStore]</a></code>
- <code title="delete /v1/vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">delete</a>(vector_store_id) -> <a href="./src/mixedbread/types/vector_store_delete_response.py">VectorStoreDeleteResponse</a></code>
- <code title="post /v1/vector_stores/question-answering">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">question_answering</a>(\*\*<a href="src/mixedbread/types/vector_store_question_answering_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_store_question_answering_response.py">object</a></code>
- <code title="post /v1/vector_stores/search">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">search</a>(\*\*<a href="src/mixedbread/types/vector_store_search_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_store_search_response.py">VectorStoreSearchResponse</a></code>

## Files

Types:

```python
from mixedbread.types.vector_stores import (
    ScoredVectorStoreFile,
    VectorStoreFile,
    FileDeleteResponse,
    FileSearchResponse,
)
```

Methods:

- <code title="post /v1/vector_stores/{vector_store_id}/files">client.vector_stores.files.<a href="./src/mixedbread/resources/vector_stores/files.py">create</a>(vector_store_id, \*\*<a href="src/mixedbread/types/vector_stores/file_create_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_stores/vector_store_file.py">VectorStoreFile</a></code>
- <code title="get /v1/vector_stores/{vector_store_id}/files/{file_id}">client.vector_stores.files.<a href="./src/mixedbread/resources/vector_stores/files.py">retrieve</a>(file_id, \*, vector_store_id) -> <a href="./src/mixedbread/types/vector_stores/vector_store_file.py">VectorStoreFile</a></code>
- <code title="get /v1/vector_stores/{vector_store_id}/files">client.vector_stores.files.<a href="./src/mixedbread/resources/vector_stores/files.py">list</a>(vector_store_id, \*\*<a href="src/mixedbread/types/vector_stores/file_list_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_stores/vector_store_file.py">SyncLimitOffset[VectorStoreFile]</a></code>
- <code title="delete /v1/vector_stores/{vector_store_id}/files/{file_id}">client.vector_stores.files.<a href="./src/mixedbread/resources/vector_stores/files.py">delete</a>(file_id, \*, vector_store_id) -> <a href="./src/mixedbread/types/vector_stores/file_delete_response.py">FileDeleteResponse</a></code>
- <code title="post /v1/vector_stores/files/search">client.vector_stores.files.<a href="./src/mixedbread/resources/vector_stores/files.py">search</a>(\*\*<a href="src/mixedbread/types/vector_stores/file_search_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_stores/file_search_response.py">FileSearchResponse</a></code>

# Completions

Types:

```python
from mixedbread.types import CompletionCreateResponse
```

Methods:

- <code title="post /v1/chat/completions">client.completions.<a href="./src/mixedbread/resources/completions.py">create</a>() -> <a href="./src/mixedbread/types/completion_create_response.py">object</a></code>

# Extractions

## Jobs

Types:

```python
from mixedbread.types.extractions import ExtractionJob
```

Methods:

- <code title="post /v1/extractions/jobs">client.extractions.jobs.<a href="./src/mixedbread/resources/extractions/jobs.py">create</a>(\*\*<a href="src/mixedbread/types/extractions/job_create_params.py">params</a>) -> <a href="./src/mixedbread/types/extractions/extraction_job.py">ExtractionJob</a></code>
- <code title="get /v1/extractions/jobs/{job_id}">client.extractions.jobs.<a href="./src/mixedbread/resources/extractions/jobs.py">retrieve</a>(job_id) -> <a href="./src/mixedbread/types/extractions/extraction_job.py">ExtractionJob</a></code>

## Schema

Types:

```python
from mixedbread.types.extractions import CreatedJsonSchema, EnhancedJsonSchema, ValidatedJsonSchema
```

Methods:

- <code title="post /v1/extractions/schema">client.extractions.schema.<a href="./src/mixedbread/resources/extractions/schema.py">create</a>(\*\*<a href="src/mixedbread/types/extractions/schema_create_params.py">params</a>) -> <a href="./src/mixedbread/types/extractions/created_json_schema.py">CreatedJsonSchema</a></code>
- <code title="post /v1/extractions/schema/enhance">client.extractions.schema.<a href="./src/mixedbread/resources/extractions/schema.py">enhance</a>(\*\*<a href="src/mixedbread/types/extractions/schema_enhance_params.py">params</a>) -> <a href="./src/mixedbread/types/extractions/enhanced_json_schema.py">EnhancedJsonSchema</a></code>
- <code title="post /v1/extractions/schema/validate">client.extractions.schema.<a href="./src/mixedbread/resources/extractions/schema.py">validate</a>(\*\*<a href="src/mixedbread/types/extractions/schema_validate_params.py">params</a>) -> <a href="./src/mixedbread/types/extractions/validated_json_schema.py">ValidatedJsonSchema</a></code>

## Content

Types:

```python
from mixedbread.types.extractions import ExtractionResult
```

Methods:

- <code title="post /v1/extractions/content">client.extractions.content.<a href="./src/mixedbread/resources/extractions/content.py">create</a>(\*\*<a href="src/mixedbread/types/extractions/content_create_params.py">params</a>) -> <a href="./src/mixedbread/types/extractions/extraction_result.py">ExtractionResult</a></code>
