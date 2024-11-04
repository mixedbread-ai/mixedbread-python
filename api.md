# Mixedbread

Types:

```python
from mixedbread.types import InfoResponse
```

Methods:

- <code title="get /">client.<a href="./src/mixedbread/_client.py">info</a>() -> <a href="./src/mixedbread/types/info_response.py">InfoResponse</a></code>

# DocAI

## Parse

Types:

```python
from mixedbread.types.doc_ai import ParseResponse
```

Methods:

- <code title="post /v1/document-intelligence/parse">client.doc_ai.parse.<a href="./src/mixedbread/resources/doc_ai/parse.py">create</a>(\*\*<a href="src/mixedbread/types/doc_ai/parse_create_params.py">params</a>) -> <a href="./src/mixedbread/types/doc_ai/parse_response.py">ParseResponse</a></code>
- <code title="get /v1/document-intelligence/parse/{job_id}">client.doc_ai.parse.<a href="./src/mixedbread/resources/doc_ai/parse.py">retrieve</a>(job_id) -> <a href="./src/mixedbread/types/doc_ai/parse_response.py">ParseResponse</a></code>

# Files

Types:

```python
from mixedbread.types import FileObject, FileListResponse, FileDeleteResponse
```

Methods:

- <code title="post /v1/files">client.files.<a href="./src/mixedbread/resources/files.py">create</a>(\*\*<a href="src/mixedbread/types/file_create_params.py">params</a>) -> <a href="./src/mixedbread/types/file_object.py">FileObject</a></code>
- <code title="get /v1/files/{file_id}">client.files.<a href="./src/mixedbread/resources/files.py">retrieve</a>(file_id) -> <a href="./src/mixedbread/types/file_object.py">FileObject</a></code>
- <code title="put /v1/files/{file_id}">client.files.<a href="./src/mixedbread/resources/files.py">update</a>(file_id, \*\*<a href="src/mixedbread/types/file_update_params.py">params</a>) -> <a href="./src/mixedbread/types/file_object.py">FileObject</a></code>
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

# VectorStores

Types:

```python
from mixedbread.types import (
    SearchResponse,
    VectorStoreCreate,
    VectorStoreDeleted,
    VectorStoreListResponse,
    VectorStoreObject,
)
```

Methods:

- <code title="post /v1/vector_stores">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">create</a>(\*\*<a href="src/mixedbread/types/vector_store_create_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_store_object.py">VectorStoreObject</a></code>
- <code title="get /v1/vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">retrieve</a>(vector_store_id) -> <a href="./src/mixedbread/types/vector_store_object.py">VectorStoreObject</a></code>
- <code title="put /v1/vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">update</a>(vector_store_id, \*\*<a href="src/mixedbread/types/vector_store_update_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_store_object.py">VectorStoreObject</a></code>
- <code title="get /v1/vector_stores">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">list</a>(\*\*<a href="src/mixedbread/types/vector_store_list_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_store_list_response.py">VectorStoreListResponse</a></code>
- <code title="delete /v1/vector_stores/{vector_store_id}">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">delete</a>(vector_store_id) -> <a href="./src/mixedbread/types/vector_store_deleted.py">VectorStoreDeleted</a></code>
- <code title="post /v1/vector_stores/search">client.vector_stores.<a href="./src/mixedbread/resources/vector_stores/vector_stores.py">search</a>(\*\*<a href="src/mixedbread/types/vector_store_search_params.py">params</a>) -> <a href="./src/mixedbread/types/search_response.py">SearchResponse</a></code>

## Files

Types:

```python
from mixedbread.types.vector_stores import (
    VectorStoreFileDeleted,
    VectorStoreFileListResponse,
    VectorStoreFileObject,
)
```

Methods:

- <code title="post /v1/vector_stores/{vector_store_id}/files">client.vector_stores.files.<a href="./src/mixedbread/resources/vector_stores/files.py">create</a>(vector_store_id, \*\*<a href="src/mixedbread/types/vector_stores/file_create_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_stores/vector_store_file_object.py">VectorStoreFileObject</a></code>
- <code title="get /v1/vector_stores/{vector_store_id}/files/{file_id}">client.vector_stores.files.<a href="./src/mixedbread/resources/vector_stores/files.py">retrieve</a>(file_id, \*, vector_store_id) -> <a href="./src/mixedbread/types/vector_stores/vector_store_file_object.py">VectorStoreFileObject</a></code>
- <code title="get /v1/vector_stores/{vector_store_id}/files">client.vector_stores.files.<a href="./src/mixedbread/resources/vector_stores/files.py">list</a>(vector_store_id, \*\*<a href="src/mixedbread/types/vector_stores/file_list_params.py">params</a>) -> <a href="./src/mixedbread/types/vector_stores/vector_store_file_list_response.py">VectorStoreFileListResponse</a></code>
- <code title="delete /v1/vector_stores/{vector_store_id}/files/{file_id}">client.vector_stores.files.<a href="./src/mixedbread/resources/vector_stores/files.py">delete</a>(file_id, \*, vector_store_id) -> <a href="./src/mixedbread/types/vector_stores/vector_store_file_deleted.py">VectorStoreFileDeleted</a></code>
