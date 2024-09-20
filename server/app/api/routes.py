from fastapi import APIRouter, HTTPException
from app.services.document_loader_service import load_and_store_service
from app.services.chroma_service import peek_document_service, search_service
from app.services.llm_service import (
    query_with_retrieval_service,
    query_without_retrieval_service,
)
from app.models import (
    LoadAndStoreRequest,
    PeekDocumentRequest,
    SearchRequest,
    QueryWithRetrievalRequest,
    QueryWithoutRetrievalRequest,
)

# Initialize the APIRouter
router = APIRouter()


# Helper function to format errors
def format_error(status: str, message: str):
    return {"status": status, "message": message, "data": []}


@router.post("/load-and-store")
async def load_and_store(request: LoadAndStoreRequest):
    """
    Load data from the specified URL and store it in the Chroma vector store.
    """
    try:
        result = await load_and_store_service(
            url=request.url,
            chunk_size=request.chunk_size,
            chunk_overlap=request.chunk_overlap,
            collection_name=request.collection_name,
        )
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=format_error("error", f"Error in loading and storing document: {e}"),
        )


@router.post("/peek-document")
async def peek_document(request: PeekDocumentRequest):
    """
    Peek at the top document in the specified Chroma collection.
    """
    try:
        result = await peek_document_service(request.collection_name)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=format_error("error", f"Error in peeking document: {e}"),
        )


@router.post("/search")
async def search(request: SearchRequest):
    """
    Search for a query in the specified Chroma collection.
    """
    try:
        result = await search_service(request.query, request.collection_name)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=format_error("error", f"Error in searching: {e}")
        )


@router.post("/query-with-retrieval")
async def query_with_retrieval(request: QueryWithRetrievalRequest):
    """
    Query with retrieval using the specified Chroma collection.
    """
    try:
        result = await query_with_retrieval_service(
            request.query, request.collection_name
        )
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=format_error("error", f"Error in query with retrieval: {e}"),
        )


@router.post("/query-without-retrieval")
async def query_without_retrieval(request: QueryWithoutRetrievalRequest):
    """
    Query without retrieval.
    """
    try:
        result = await query_without_retrieval_service(request.query)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=format_error("error", f"Error in query without retrieval: {e}"),
        )
