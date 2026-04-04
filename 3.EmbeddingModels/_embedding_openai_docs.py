# OpenAI Document Embeddings Demo - Convert multiple documents to embeddings
# Purpose: Generate embeddings for a batch of documents using OpenAI API
# Uses: OpenAI text-embedding-3-large model for document vectorization
# Requires: OPENAI_API_KEY in .env file

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv(override=True)

documents = [
    "Kathmandu is the capital of Nepal",
    "Pokhara is a city in Nepal",   
    "Delhi is the capital of India"
]

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

result = embedding.embed_Documents(documents)
print(result)