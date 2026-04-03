# LLM Demo - Demonstrates how to use ChatGroq and Gemini models via LangChain
# Purpose: Show basic LLM initialization, configuration, and invocation patterns
# Models: ChatGroq (fast inference) and Gemini (advanced AI)
# Requires: GROQ_API_KEY and GOOGLE_API_KEY in .env file

from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(override=True)

print("\n" + "="*60)
print("LLM DEMO - ChatGroq & Gemini Examples")
print("="*60)

# ============================================================================
# CASE 1: ChatGroq - Fast inference with Mixtral model
# ============================================================================
print("\n" + "-"*60)
print("CASE 1: ChatGroq (Fast LLM Inference)")
print("-"*60)

try:
    # Initialize ChatGroq model
    groq_model = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.7,
        max_tokens=256
    )
    
    # Create prompt and invoke
    prompt1 = "What are the top 5 programming languages in 2024?"
    response1 = groq_model.invoke(prompt1)
    
    print(f"\nPrompt: {prompt1}")
    print(f"\nResponse:\n{response1.content}")
    
except Exception as e:
    print(f"Error in ChatGroq: {str(e)}")

# ============================================================================
# CASE 2: Google Gemini - Advanced multimodal AI
# ============================================================================
print("\n" + "-"*60)
print("CASE 2: Google Gemini (Advanced AI Model)")
print("-"*60)

try:
    # Initialize Google Gemini model
    gemini_model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.8,
        max_tokens=256
    )
    
    # Create prompt and invoke
    prompt2 = "Explain what machine learning is in simple terms."
    response2 = gemini_model.invoke(prompt2)
    
    print(f"\nPrompt: {prompt2}")
    print(f"\nResponse:\n{response2.content}")
    
except Exception as e:
    print(f"Error in Gemini: {str(e)}")

print("\n" + "="*60)
print("Demo completed!")
print("="*60 + "\n")
