from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from app.utils.settings import PERSIST_DIRECTORY, EMBEDDINGS


async def load_and_store_service(
    url: str, chunk_size: int, chunk_overlap: int, collection_name: str
):
    loader = WebBaseLoader(url)
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    documents = text_splitter.split_documents(data)

    # Use FakeEmbeddings for testing
    embeddings = EMBEDDINGS

    Chroma.from_documents(
        collection_name=collection_name,
        documents=documents,
        embedding=embeddings,
        persist_directory=PERSIST_DIRECTORY,
    )

    return {
        "status": "success",
        "message": "Document loaded and stored successfully",
        "data": documents,
    }
