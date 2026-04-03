# HuggingFace API Demo - Access open-source LLMs via HuggingFace API endpoint
# Purpose: Initialize Llama 3.1 model through HuggingFace API without local GPU
# Uses: HuggingFaceEndpoint for API-based inference
# Requires: HUGGINGFACEHUB_API_TOKEN in .env file

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(override=True)
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Initialize HuggingFace Endpoint with open-source model
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

# Wrap with ChatHuggingFace for chat interface
model = ChatHuggingFace(llm=llm)

# Example: Ask a question
response = model.invoke("What is the capital of India?")

print("\n--- Response ---")
print(response.content)