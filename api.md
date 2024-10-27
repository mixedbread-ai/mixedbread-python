# Mixedbread

Types:

```python
from mixedbread.types import BaseStatusCheckResponse
```

Methods:

- <code title="get /">client.<a href="./src/mixedbread/_client.py">base_status_check</a>() -> <a href="./src/mixedbread/types/base_status_check_response.py">BaseStatusCheckResponse</a></code>

# DocAI

## Parse

Types:

```python
from mixedbread.types.doc_ai import ParseResponse
```

Methods:

- <code title="post /v1/document-intelligence/parse">client.doc_ai.parse.<a href="./src/mixedbread/resources/doc_ai/parse.py">create_job</a>(\*\*<a href="src/mixedbread/types/doc_ai/parse_create_job_params.py">params</a>) -> <a href="./src/mixedbread/types/doc_ai/parse_response.py">ParseResponse</a></code>
- <code title="get /v1/document-intelligence/parse/{job_id}">client.doc_ai.parse.<a href="./src/mixedbread/resources/doc_ai/parse.py">retrieve_job</a>(job_id) -> <a href="./src/mixedbread/types/doc_ai/parse_response.py">ParseResponse</a></code>

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
from mixedbread.types import FileObject, FileListResponse
```

Methods:

- <code title="post /v1/files">client.files.<a href="./src/mixedbread/resources/files.py">create</a>(\*\*<a href="src/mixedbread/types/file_create_params.py">params</a>) -> <a href="./src/mixedbread/types/file_object.py">FileObject</a></code>
- <code title="get /v1/files/{file_id}">client.files.<a href="./src/mixedbread/resources/files.py">retrieve</a>(file_id) -> <a href="./src/mixedbread/types/file_object.py">FileObject</a></code>
- <code title="put /v1/files/{file_id}">client.files.<a href="./src/mixedbread/resources/files.py">update</a>(file_id, \*\*<a href="src/mixedbread/types/file_update_params.py">params</a>) -> <a href="./src/mixedbread/types/file_object.py">FileObject</a></code>
- <code title="get /v1/files">client.files.<a href="./src/mixedbread/resources/files.py">list</a>(\*\*<a href="src/mixedbread/types/file_list_params.py">params</a>) -> <a href="./src/mixedbread/types/file_list_response.py">FileListResponse</a></code>
- <code title="delete /v1/files/{file_id}">client.files.<a href="./src/mixedbread/resources/files.py">delete</a>(file_id) -> <a href="./src/mixedbread/types/file_object.py">FileObject</a></code>
- <code title="get /v1/files/{file_id}/content">client.files.<a href="./src/mixedbread/resources/files.py">content</a>(file_id) -> BinaryAPIResponse</code>

# Jobs

Types:

```python
from mixedbread.types import JobStatusResponse, JobDeleteResponse
```

Methods:

- <code title="get /v1/jobs/{job_id}">client.jobs.<a href="./src/mixedbread/resources/jobs.py">retrieve</a>(job_id) -> <a href="./src/mixedbread/types/job_status_response.py">JobStatusResponse</a></code>
- <code title="delete /v1/jobs/{job_id}">client.jobs.<a href="./src/mixedbread/resources/jobs.py">delete</a>(job_id) -> <a href="./src/mixedbread/types/job_delete_response.py">JobDeleteResponse</a></code>
