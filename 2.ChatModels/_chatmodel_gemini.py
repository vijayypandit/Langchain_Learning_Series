# ChatGemini Demo - Google's advanced multimodal AI model
# Purpose: Initialize Gemini model and get intelligent responses
# Uses: Google's Gemini 2.5 Flash for fast, high-quality inference
# Requires: GOOGLE_API_KEY in .env file

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(override=True)

# Initialize Google Gemini Chat Model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Example: Ask a question
response = model.invoke("What is the capital of Nepal?")

print("\n--- Response ---")
print(response.content)