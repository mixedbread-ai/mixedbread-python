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

# Parsing

## Jobs

Types:

```python
from mixedbread.types.parsing import ParsingJob, JobListResponse, JobDeleteResponse
```

Methods:

- <code title="post /v1/parsing/jobs">client.parsing.jobs.<a href="./src/mixedbread/resources/parsing/jobs.py">create</a>(\*\*<a href="src/mixedbread/types/parsing/job_create_params.py">params</a>) -> <a href="./src/mixedbread/types/parsing/parsing_job.py">ParsingJob</a></code>
- <code title="get /v1/parsing/jobs/{job_id}">client.parsing.jobs.<a href="./src/mixedbread/resources/parsing/jobs.py">retrieve</a>(job_id) -> <a href="./src/mixedbread/types/parsing/parsing_job.py">ParsingJob</a></code>
- <code title="get /v1/parsing/jobs">client.parsing.jobs.<a href="./src/mixedbread/resources/parsing/jobs.py">list</a>(\*\*<a href="src/mixedbread/types/parsing/job_list_params.py">params</a>) -> <a href="./src/mixedbread/types/parsing/job_list_response.py">SyncLimitOffset[JobListResponse]</a></code>
- <code title="delete /v1/parsing/jobs/{job_id}">client.parsing.jobs.<a href="./src/mixedbread/resources/parsing/jobs.py">delete</a>(job_id) -> <a href="./src/mixedbread/types/parsing/job_delete_response.py">JobDeleteResponse</a></code>
- <code title="patch /v1/parsing/jobs/{job_id}">client.parsing.jobs.<a href="./src/mixedbread/resources/parsing/jobs.py">cancel</a>(job_id) -> <a href="./src/mixedbread/types/parsing/parsing_job.py">ParsingJob</a></code>

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
