# 2. ChatModels

ChatModels are a variation on LLMs. While LLMs are "text-in, text-out", ChatModels are "messages-in, messages-out". They are specifically optimized for holding conversations and understanding different message roles like `System`, `Human`, and `AI`.

### Definition
ChatModels use a structured message interface. They are generally more capable of following complex instructions and maintaining context in a dialogue.

### Top Chat Model Providers & Series
Modern ChatModels are generally organized into families. Here are the major ones used in LangChain applications:

*   **Google Gemini Series:**
    *   `gemini-2.5-flash`: Extremely fast and cost-effective.
    *   `gemini-1.5-pro`: Deep reasoning with a massive 2M token context.
*   **OpenAI GPT Series:**
    *   `gpt-4o`: Omni model with native multimodal capabilities.
    *   `gpt-4-turbo`: High logic and performance.
*   **Anthropic Claude Series:**
    *   `claude-3-5-sonnet`: Balanced power and speed.
    *   `claude-3-opus`: The most powerful reasoning model.
*   **Meta Llama (via Groq/Together):**
    *   `llama-3.1-70b`: Highly instruction-tuned open-source model.
    *   `llama-3-8b`: Small but mighty for basic tasks.

### Structure of a Conversation ("Talking" to Models)
When you communicate with a ChatModel, you don't just send a string. You send a list of messages, where each message has a specific **role**:

- **SystemMessage:** Used to give the AI a personality or set the rules (e.g., "You are a helpful travel agent").
- **HumanMessage:** The input from the user.
- **AIMessage:** The response from the AI.

### Example (Multi-Message Conversation)
```python
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

messages = [
    SystemMessage(content="You are a polite assistant that answers in French."),
    HumanMessage(content="What is the capital of Japan?")
]

response = model.invoke(messages)
print(response.content) # Output: "La capitale du Japon est Tokyo."
```

### Using Open-Source Models (Hugging Face)
For ChatModels, LangChain provides `ChatHuggingFace`, which wraps a local or remote model to support the message interface.

*   **Popular Open Models:** `Mistral-7B-Instruct-v0.3`, `Llama-3-8B-Instruct`, `Zephyr-7B-beta`.

#### Example (Chat Interface for Local Model)
```python
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# 1. Load the local model pipeline
llm = HuggingFacePipeline.from_model_id(model_id="gpt2", task="text-generation")

# 2. Wrap it with ChatHuggingFace to support messages
chat_model = ChatHuggingFace(llm=llm)

messages = [HumanMessage(content="Hello! How are you?")]
response = chat_model.invoke(messages)
```

### How to Use
1. **Initialize** the model from the appropriate package.
2. **Invoke** with a simple string or a list of messages.

### Example (Gemini)
```python
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
response = model.invoke("Who founded SpaceX?")
print(response.content)
```

### Example (Local HuggingFace)
```python
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(model_id="gpt2", task="text-generation")
model = ChatHuggingFace(llm=llm)
```

---
**Files in this folder:**
- `_chatmodel_gemini.py`: Basic Gemini implementation.
- `_chatmodel_groq.py`: Groq implementation.
- `_chatmodel_hf_api.py`: Using HuggingFace via Inference API.
- `_chatmodel_hf_local.py`: Loading and running models locally using HuggingFace.
