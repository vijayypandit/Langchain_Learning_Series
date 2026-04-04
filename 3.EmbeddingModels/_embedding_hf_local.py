# HuggingFace Local Embeddings Demo - Generate embeddings locally
# Purpose: Create vector embeddings using lightweight HuggingFace models
# Uses: sentence-transformers for local, fast embedding generation
# Requires: No API key needed, runs completely locally

from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv(override=True)

#Using Hugging Face EMbedding Model , smaller in size 
embedding=HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")
vector = embedding.embed_query("Kathmandu")
print(len(vector))   # dimension
print(vector)    # preview first few values