# 1. LLMs (Large Language Models)

Large Language Models (LLMs) are the foundational building blocks of LangChain. They are designed to take a string prompt as input and return a string completion as output. While ChatModels (which use messages) have become more common, base LLMs are still used for many text-completion tasks.

### Definition
An LLM in LangChain refers to a model that follows the "text-in, text-out" interface. In this repository, we demonstrate how to use various providers to invoke these models.

### Key Model Provider List
When using LLMs with LangChain, you have access to a wide range of providers. Some of the most popular ones include:

| Provider | Description | Common Models |
| :--- | :--- | :--- |
| **Google** | Powerful multimodal models | `gemini-2.0-flash`, `gemini-1.5-pro` |
| **OpenAI** | Industry leaders in reasoning | `gpt-4o`, `gpt-4o-mini`, `gpt-3.5-turbo` |
| **Anthropic** | Known for safety and long context | `claude-3-5-sonnet`, `claude-3-haiku` |
| **Groq** | Ultra-fast inference engine | `llama-3.1-70b`, `mixtral-8x7b-32768` |
| **Mistral AI** | Open-source efficient models | `mistral-large`, `mistral-small` |
| **Hugging Face** | Access to thousands of open models | `Llama-3`, `Mistral`, `Falcon` |

### How to Use
To use an LLM, you typically:
1. Import the model class from the provider's integration package.
2. Initialize the model with your API key and parameters (temperature, max_tokens, etc.).
3. Call `.invoke()` with a string or object.

### Example
```python
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# Initialize the model
model = ChatGroq(model="llama-3.1-8b-instant")

# Invoke the model
response = model.invoke("What are the benefits of using LangChain?")
print(response.content)
```

### Using Hugging Face Open-Source Models
Hugging Face (HF) provides access to thousands of open-source models. You can use them in two ways:

1.  **HuggingFaceEndpoint (API):** Runs the model on Hugging Face's servers (requires an API token).
2.  **HuggingFacePipeline (Local):** Downloads and runs the model on your local machine (requires `transformers` and `torch`).

#### Example (Local Pipeline)
```python
from langchain_huggingface import HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="gpt2",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 100}
)
response = llm.invoke("Once upon a time")
print(response)
```

---
**Files in this folder:**
- `_llm_demo.py`: A combined demo showing how to use both Groq and Gemini models.
