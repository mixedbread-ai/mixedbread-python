# BaseStatus

Types:

```python
from mixedbread.types import InfoResponse
```

Methods:

- <code title="get /">client.base_status.<a href="./src/mixedbread/resources/base_status.py">retrieve</a>() -> <a href="./src/mixedbread/types/info_response.py">InfoResponse</a></code>

# DocumentIntelligence

## Parse

Types:

```python
from mixedbread.types.document_intelligence import ParseResponse
```

Methods:

- <code title="post /v1/document-intelligence/parse">client.document_intelligence.parse.<a href="./src/mixedbread/resources/document_intelligence/parse.py">create</a>(\*\*<a href="src/mixedbread/types/document_intelligence/parse_create_params.py">params</a>) -> <a href="./src/mixedbread/types/document_intelligence/parse_response.py">ParseResponse</a></code>
- <code title="get /v1/document-intelligence/parse/{job_id}">client.document_intelligence.parse.<a href="./src/mixedbread/resources/document_intelligence/parse.py">retrieve</a>(job_id) -> <a href="./src/mixedbread/types/document_intelligence/parse_response.py">ParseResponse</a></code>

# Files

Types:

```python
from mixedbread.types import FileListResponse, FileResponse, FileUpdateResponse
```

Methods:

- <code title="post /v1/files">client.files.<a href="./src/mixedbread/resources/files/files.py">create</a>(\*\*<a href="src/mixedbread/types/file_create_params.py">params</a>) -> <a href="./src/mixedbread/types/file_response.py">FileResponse</a></code>
- <code title="get /v1/files/{file_id}">client.files.<a href="./src/mixedbread/resources/files/files.py">retrieve</a>(file_id) -> <a href="./src/mixedbread/types/file_response.py">FileResponse</a></code>
- <code title="put /v1/files/{file_id}">client.files.<a href="./src/mixedbread/resources/files/files.py">update</a>(file_id, \*\*<a href="src/mixedbread/types/file_update_params.py">params</a>) -> <a href="./src/mixedbread/types/file_update_response.py">FileUpdateResponse</a></code>
- <code title="get /v1/files">client.files.<a href="./src/mixedbread/resources/files/files.py">list</a>() -> <a href="./src/mixedbread/types/file_list_response.py">FileListResponse</a></code>
- <code title="delete /v1/files/{file_id}">client.files.<a href="./src/mixedbread/resources/files/files.py">delete</a>(file_id) -> None</code>

## Content

Types:

```python
from mixedbread.types.files import ContentRetrieveResponse
```

Methods:

- <code title="get /v1/files/{file_id}/content">client.files.content.<a href="./src/mixedbread/resources/files/content.py">retrieve</a>(file_id) -> <a href="./src/mixedbread/types/files/content_retrieve_response.py">object</a></code>

# Jobs

Types:

```python
from mixedbread.types import JobDeleteResponse, JobStatusResponse
```

Methods:

- <code title="delete /v1/jobs/{job_id}">client.jobs.<a href="./src/mixedbread/resources/jobs/jobs.py">delete</a>(job_id) -> <a href="./src/mixedbread/types/job_delete_response.py">JobDeleteResponse</a></code>

## Status

Methods:

- <code title="get /v1/jobs/{job_id}">client.jobs.status.<a href="./src/mixedbread/resources/jobs/status.py">retrieve</a>(job_id) -> <a href="./src/mixedbread/types/job_status_response.py">JobStatusResponse</a></code>
