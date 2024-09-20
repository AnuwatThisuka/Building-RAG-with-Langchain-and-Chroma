from app.utils.settings import PERSIST_DIRECTORY, EMBEDDINGS
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQAWithSourcesChain


# Initialize LLM (Language Model)
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)


async def query_with_retrieval_service(
    query: str, collection_name: str, top_k: int = 1
):
    """
    Handles querying the LLM with document retrieval from the Chroma vector store.

    Args:
        query (str): The user's query.
        collection_name (str): The name of the Chroma vector store collection.
        top_k (int): The number of top documents to retrieve for the LLM.

    Returns:
        dict: The response from the LLM with sources from document retrieval.
    """
    # Load the vectorstore with embeddings
    vectorstore = Chroma(
        collection_name=collection_name,
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=EMBEDDINGS,
    )

    # Initialize the retrieval QA chain
    retriever = vectorstore.as_retriever(search_kwargs={"k": top_k})
    qa_chain = RetrievalQAWithSourcesChain.from_chain_type(llm, retriever=retriever)

    # Run the query through the chain
    result = qa_chain({"question": query})
    return {"result": result}


async def query_without_retrieval_service(query: str):
    """
    Handles querying the LLM directly without document retrieval.

    Args:
        query (str): The user's query.

    Returns:
        dict: The LLM's response to the query.
    """
    # Send query directly to the language model
    result = llm.predict(query)
    return {"result": result}
