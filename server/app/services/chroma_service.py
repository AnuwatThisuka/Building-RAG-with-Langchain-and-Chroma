from langchain_chroma import Chroma
from app.utils.settings import PERSIST_DIRECTORY, EMBEDDINGS


async def peek_document_service(collection_name: str):
    vectorstore = Chroma(
        collection_name=collection_name,
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=EMBEDDINGS,
    )
    top_document = vectorstore._collection.peek()
    return {"Top document in collection": top_document}


async def search_service(query: str, collection_name: str):
    vectorstore = Chroma(
        collection_name=collection_name,
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=EMBEDDINGS,
    )
    result = vectorstore.similarity_search(query, k=1)
    return {"Result": result}
