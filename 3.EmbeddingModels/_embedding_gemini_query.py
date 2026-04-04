# Gemini Embeddings Demo - Convert text to vector embeddings
# Purpose: Generate embeddings for documents and queries using Google Gemini
# Uses: GoogleGenerativeAIEmbeddings for semantic text representation
# Requires: GOOGLE_API_KEY in .env file

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv(override=True)

# embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")   we can use this one as well
embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")

# result = embedding.embed_query("Kathmandu is the capital of Nepal")
# print(result)

documents = [
    "Kathmandu is the capital of Nepal",
    "Pokhara is a city in Nepal",   
    "Delhi is the capital of India"
]

result = embedding.embed_documents(documents)
print(result)