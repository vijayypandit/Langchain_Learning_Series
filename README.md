# LangChain Modules Learning Series

LLM and Chat Model demonstrations using LangChain with 4 different providers.
--
### Folder 1: LLMs
- `_llm_demo.py` - ChatGroq & Gemini basics

### Folder 2: ChatModels (4 providers)
- `_chatmodel_groq.py` - Groq (fast)
- `_chatmodel_gemini.py` - Gemini (advanced)
- `_chatmodel_hf_api.py` - HuggingFace API (open-source)
- `_chatmodel_hf_local.py` - HuggingFace Local (private)

---

## ⚡ Quick Start

### 1. Setup
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure `.env`
```env
GROQ_API_KEY=your_key
GOOGLE_API_KEY=your_key
OPENAI_API_KEY=your_key  # Optional
HUGGINGFACEHUB_API_TOKEN=your_token  # Optional
```

Get API Keys:
- [Groq](https://console.groq.com) - Free
- [Gemini](https://makersuite.google.com/app/apikey) - Free
- [OpenAI](https://platform.openai.com) - Paid
- [HuggingFace](https://huggingface.co/settings/tokens) - Free

### 3. Run
```bash
python 1.LLMs/_llm_demo.py
python 2.ChatModels/_chatmodel_groq.py
python 2.ChatModels/_chatmodel_gemini.py
python 2.ChatModels/_chatmodel_hf_api.py
python 2.ChatModels/_chatmodel_hf_local.py
```

---

## 📋 File Summary

| File | Model | Speed | Quality | API Key |
|------|-------|-------|---------|---------|
| `_llm_demo.py` | ChatGroq + Gemini | Fast | Good | GROQ, GOOGLE |
| `_chatmodel_groq.py` | Llama 3.1 | ⚡⚡⚡ | Good | GROQ_API_KEY |
| `_chatmodel_gemini.py` | Gemini 2.5 | ⚡⚡ | ⭐⭐⭐⭐⭐ | GOOGLE_API_KEY |
| `_chatmodel_hf_api.py` | Llama 3.1 | ⚡⚡ | Good | HUGGINGFACEHUB_API_TOKEN |
| `_chatmodel_hf_local.py` | GPT-OSS 120B | ⚡ | Good | None (Local) |

---
## 🔑 Key Points

- **Initialize** → Load environment and create model
- **Invoke** → Send prompt and get response
- **Handle Errors** → Use try-except for API calls
- **Parameters** → temperature (0=fixed, 1=creative), max_tokens
---
## 📦 Dependencies
```
langchain, langchain_groq, langchain_google_genai
langchain_openai, langchain_huggingface, python_dotenv
```
Full list: See `requirements.txt`
---

## 🚀 Push to GitHub

```bash
git add .
git commit -m "feat: Add LLMs and ChatModels demos (Folders 1-2)"
git push origin main
```

---

**Release:** v1.0 | **Status:** ✅ Ready | **Future:** Folders 3-6 Coming

