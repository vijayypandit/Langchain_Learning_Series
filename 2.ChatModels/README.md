# 2. ChatModels (Conversational AI) 🤖

This module teaches chat-based model usage in LangChain. ChatModels are ideal for building assistants, conversational agents, and any application that uses structured message roles.

## 🎯 What this module teaches
- How chat-based models differ from text-only LLMs.
- How to use `SystemMessage`, `HumanMessage`, and `AIMessage`.
- How to keep conversation context across turns.
- How to work with Gemini, Groq, and Hugging Face chat models.

## 🧠 Key concepts
- **ChatModel**: consumes a list of messages instead of plain text.
- **Roles**: system, human, and AI messages define the conversation flow.
- **Conversation history**: allows the model to remember previous turns.

## 📌 Provider examples
- **Google Gemini**: fast and powerful chat reasoning.
- **OpenAI GPT**: strong general chat capabilities.
- **Anthropic Claude**: safety-focused chat responses.
- **Hugging Face Chat**: open-source local or API chat support.

## 🧪 Example (Conversation)
```python
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
messages = [
    SystemMessage(content="You are a polite assistant that answers in French."),
    HumanMessage(content="What is the capital of Japan?")
]
response = model.invoke(messages)
print(response.content)
```

## 💡 Learning tips
- Use a clear `SystemMessage` to set role and tone.
- Use `HumanMessage` for user queries.
- Keep chat history only when context matters.
- Test with both single-turn and multi-turn prompts.

## 📂 Files in this folder
- `_chatmodel_gemini.py` — Basic Gemini implementation.
- `_chatmodel_groq.py` — Groq chat implementation.
- `_chatmodel_hf_api.py` — Hugging Face chat via API.
- `_chatmodel_hf_local.py` — Local Hugging Face chat execution.

---
**Why this matters**: ChatModels are the best fit for interactive experiences, assistants, and conversational AI workflows.