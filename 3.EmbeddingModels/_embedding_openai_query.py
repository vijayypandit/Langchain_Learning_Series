# OpenAI Embeddings Demo - Convert single query to vector embedding
# Purpose: Generate semantic embeddings for a single query using OpenAI
# Uses: OpenAI text-embedding-3-large model for high-quality embeddings
# Requires: OPENAI_API_KEY in .env file

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv(override=True)

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

result = embedding.embed_query("Kathmandu is the capital of Nepal")
print(result)