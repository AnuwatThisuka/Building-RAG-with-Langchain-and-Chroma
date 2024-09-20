from pydantic import BaseModel

class LoadAndStoreRequest(BaseModel):
    url: str
    chunk_size: int
    chunk_overlap: int
    collection_name: str

class PeekDocumentRequest(BaseModel):
    collection_name: str

class SearchRequest(BaseModel):
    query: str
    collection_name: str

class QueryWithRetrievalRequest(BaseModel):
    query: str
    collection_name: str

class QueryWithoutRetrievalRequest(BaseModel):
    query: str
