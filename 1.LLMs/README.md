# 1. LLMs (Large Language Models) 🚀

This module introduces the foundational text-completion workflows in LangChain. It shows how to call base LLMs, compare providers, and build simple prompt-based applications.

## 🎯 What this module teaches
- How to invoke a text-based LLM using LangChain.
- The difference between LLMs and chat-based models.
- How provider choice affects quality, speed, and cost.
- How to use environment variables for API keys safely.

## 🧠 Key concepts
- **LLM**: a model that accepts a text prompt and returns text.
- **Prompt engineering**: crafting inputs to get better model outputs.
- **Provider variety**: different vendors offer different model capabilities.

## 📌 Provider Quick Guide
| Provider | Strength | Example Models |
| :--- | :--- | :--- |
| **Google** | Powerful multimodal reasoning | `gemini-2.0-flash`, `gemini-1.5-pro` |
| **OpenAI** | Industry standard for high-quality text | `gpt-4o`, `gpt-4o-mini`, `gpt-3.5-turbo` |
| **Anthropic** | Safety and long context | `claude-3-5-sonnet`, `claude-3-haiku` |
| **Groq** | Ultra-fast inference | `llama-3.1-70b`, `mixtral-8x7b-32768` |
| **Mistral AI** | Efficient open-source models | `mistral-large`, `mistral-small` |
| **Hugging Face** | Open model ecosystem | `Llama-3`, `Mistral`, `Falcon` |

## 🛠️ How to use an LLM
1. Import the provider's LangChain model class.
2. Initialize the model with your API key and settings.
3. Call `.invoke()` with a text prompt.

## 🧪 Example
```python
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(model="llama-3.1-8b-instant")
response = model.invoke("What are the benefits of using LangChain?")
print(response.content)
```

## 💡 Learning tips
- Start with a clear, concise prompt.
- Compare multiple providers with the same prompt.
- Use lower temperature for more deterministic output.
- Keep keys and credentials in `.env`, not in source code.

---
## 📁 Files in this folder
- `_llm_demo.py` — Combined demo showing Groq and Gemini model usage.
