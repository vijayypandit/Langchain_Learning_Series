# ChatGroq Demo - Fast LLM inference using Groq's API
# Purpose: Initialize ChatGroq model with Llama 3.1 and get responses
# Uses: Groq API for rapid, cost-effective LLM inference
# Requires: GROQ_API_KEY in .env file

from langchain_groq import ChatGroq
import os 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Initialize Groq Chat Model
model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,  # Balanced creativity
    max_tokens=1000
)

# Example: Get food recommendations
response = model.invoke("Suggest me 5 popular foods to eat from Janakpur, Nepal")
print("\n--- Response ---")
print(response.content)