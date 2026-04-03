# HuggingFace Local Demo - Run open-source LLMs locally without API calls
# Purpose: Load and run models locally for complete privacy and control
# Uses: HuggingFacePipeline for local inference with GPT-OSS model
# Requires: Disk space for model (~10-50GB) and optional GPU setup

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(override=True)
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Initialize HuggingFace Pipeline for local LLM
llm = HuggingFacePipeline.from_model_id(
    model_id="openai/gpt-oss-120b",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

# Wrap with ChatHuggingFace for chat interface
model = ChatHuggingFace(llm=llm)

# Example: Ask a question
response = model.invoke("What is the capital of India?")

print("\n--- Response ---")
print(response.content)