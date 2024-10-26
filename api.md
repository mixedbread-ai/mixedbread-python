# ServiceStatus

Types:

```python
from mixedbread.types import InfoResponse
```

Methods:

- <code title="get /">client.service_status.<a href="./src/mixedbread/resources/service_status.py">retrieve</a>() -> <a href="./src/mixedbread/types/info_response.py">InfoResponse</a></code>

# Di

## Parse

Types:

```python
from mixedbread.types.di import ParseResponse
```

Methods:

- <code title="post /v1/document-intelligence/parse">client.di.parse.<a href="./src/mixedbread/resources/di/parse.py">create</a>(\*\*<a href="src/mixedbread/types/di/parse_create_params.py">params</a>) -> <a href="./src/mixedbread/types/di/parse_response.py">ParseResponse</a></code>
- <code title="get /v1/document-intelligence/parse/{job_id}">client.di.parse.<a href="./src/mixedbread/resources/di/parse.py">retrieve</a>(job_id) -> <a href="./src/mixedbread/types/di/parse_response.py">ParseResponse</a></code>

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
- <code title="get /v1/files/{file_id}/content">client.files.<a href="./src/mixedbread/resources/files.py">content</a>(file_id) -> None</code>
- <code title="delete /v1/files/{file_id}">client.files.<a href="./src/mixedbread/resources/files.py">delete</a>(file_id) -> <a href="./src/mixedbread/types/file_object.py">FileObject</a></code>

# Jobs

Types:

```python
from mixedbread.types import JobDeleteResponse, JobStatusResponse
```

Methods:

- <code title="get /v1/jobs/{job_id}">client.jobs.<a href="./src/mixedbread/resources/jobs.py">retrieve</a>(job_id) -> <a href="./src/mixedbread/types/job_status_response.py">JobStatusResponse</a></code>
- <code title="delete /v1/jobs/{job_id}">client.jobs.<a href="./src/mixedbread/resources/jobs.py">delete</a>(job_id) -> <a href="./src/mixedbread/types/job_delete_response.py">JobDeleteResponse</a></code>

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
