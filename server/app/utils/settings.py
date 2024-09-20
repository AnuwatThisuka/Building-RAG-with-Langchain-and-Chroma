import os
import dotenv  # type: ignore
import openai
from langchain_core.embeddings import FakeEmbeddings
from langchain_openai import OpenAIEmbeddings

# Load environment variables from the .env file
dotenv.load_dotenv()

# Set up directory for Chroma persistence
PERSIST_DIRECTORY = os.getenv("PERSIST_DIRECTORY", "./chroma_db")

# Load OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set the OpenAI API key
openai.api_key = OPENAI_API_KEY

# Choose the embeddings to use: OpenAI embeddings or Fake embeddings
# You can toggle between real and fake embeddings for different use cases
EMBEDDINGS = FakeEmbeddings(size=4096)
