<div align="center">
  <h1>🧠 LangChain Modules Learning Series</h1>
  <p><b>A comprehensive, step-by-step practical guide to mastering LangChain components.</b></p>
  <br/>
  <p>
    <img src="https://img.shields.io/badge/Status-Active_Learning-success?style=for-the-badge" alt="Status" />
    <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python" alt="Python" />
    <img src="https://img.shields.io/badge/LangChain-Integration-orange?style=for-the-badge" alt="LangChain" />
  </p>
</div>

---

## 🎯 About This Series
Welcome to the **LangChain Modules Learning Series**. This repository contains practical demonstrations of different LangChain modules, providing a clear path to building advanced AI applications. We are progressively exploring LLMs, Chat Models, Embeddings, Prompts, and Output Parsers!

---

## 📂 Learning Modules

### 📁 Module 1: LLMs (Foundations)
*Foundational Large Language Models.*
- `_llm_demo.py` - Basics of initializing and querying ChatGroq & Google Gemini.

### 📁 Module 2: ChatModels (Conversational AI)
*Exploring advanced conversational models across 4 different providers.*
- `_chatmodel_groq.py` - ⚡ **Groq** (Ultra-fast inference)
- `_chatmodel_gemini.py` - ⭐ **Gemini** (Advanced reasoning)
- `_chatmodel_hf_api.py` - 🌐 **HuggingFace API** (Access to open-source models)
- `_chatmodel_hf_local.py` - 💻 **HuggingFace Local** (Private, on-premise execution)

### 📁 Module 3: Embedding Models (Semantic Search) 🚀
*Converting text into numerical vectors to capture "meaning" and semantic essence.*
- `_embedding_openai_query.py` & `_embedding_openai_docs.py` - 🟢 **OpenAI** (Industry-standard `text-embedding-3-small/large`)
- `_embedding_gemini_query.py` - 🔵 **Google Gemini** (`text-embedding-004`)
- `_embedding_hf_local.py` - 🤗 **HuggingFace Local** (Cost-free, private execution e.g., `all-MiniLM-L6-v2`)
- `_document_similariity.py` - 📐 **Cosine Similarity** (Mathematical comparison of text vectors)

### 📁 Module 4: Prompts & Chatbots (Prompt Engineering)
*Building reusable prompt templates, Streamlit UI, and structured chat conversations.*
- `prompt_generator.py` - Generate and save reusable `PromptTemplate` definitions.
- `prompt_ui.py` - Interactive Streamlit interface for prompt-driven applications.
- `Chatbot/chatbot.py` - State-aware chatbot with chat history persistence.
- `Chatbot/messages.py` - Structured message roles (`SystemMessage`, `HumanMessage`, `AIMessage`).
- `Chatbot/chat_prompt_template.ipynb` - Chat prompt template examples with conversation memory.

### 📁 Module 5: Structured Output (Validated Responses)
*Forcing models to return data in a predictable, typed structure.*
- `pydantic_demo.ipynb` - Pydantic data modeling and validation examples.
- `pydantic_with_structured.ipynb` - Combining Pydantic with `.with_structured_output()`.
- `typeddict_demo.ipynb` - Using `TypedDict` for structured response validation.
- `with_structured_output_json.ipynb` - Raw JSON Schema structured output examples.

### 📁 Module 6: Output Parsers (Legacy Structured Parsing)
*Parsing raw model text into JSON, dicts, or typed objects when structured output isn't available.*
- `PydanticOutputParser.py` - Prompt injection and parsing via Pydantic models.
- `JsonOutputParser.py` - Ensure valid JSON output and convert it into Python dicts.
- `StructuredOutputParser.py.py` - Schema-based parsing using `ResponseSchema` definitions.
- `JsonOutputParser.py` / `PydanticOutputParser.py` / `StructuredOutputParser.py.py` - End-to-end examples of extracting structured data from plain text output.
- `stroutputparser.py` / `stroutputparser1.py` - Additional parser experimentation and raw text formatting examples.

---

## ⚡ Quick Start & Setup

### 1️⃣ Virtual Environment Setup
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### 2️⃣ Configure Environment Variables
Create a `.env` file in the root directory:
```env
# API Keys (Only populate what you need)
GROQ_API_KEY=your_groq_key
GOOGLE_API_KEY=your_gemini_key
OPENAI_API_KEY=your_openai_key
HUGGINGFACEHUB_API_TOKEN=your_hf_token
```

### 3️⃣ Run Demonstrations
Navigate to any module and execute the scripts:
```bash
# Example: Running an embedding similarity check
python 3.EmbeddingModels/_document_similariity.py
```

---

## 📋 Provider Summary Matrix

| Provider / Module | Type | Speed | API Key Requirement | Key Benefit |
|-------------------|------|-------|---------------------|-------------|
| **Groq** | Chat | ⚡⚡⚡ | `GROQ_API_KEY` | Real-time inference |
| **Gemini** | Chat / Embed | ⚡⚡ | `GOOGLE_API_KEY` | Powerful ecosystem |
| **OpenAI** | Embed | ⚡ | `OPENAI_API_KEY` | Industry-leading embeddings |
| **HuggingFace (API)** | Chat | ⚡⚡ | `HUGGINGFACEHUB_API_TOKEN` | Huge OSS variety |
| **HuggingFace (Local)**| Chat / Embed | ⚡ | **None** | 100% Data Privacy & Free |

---

## 🔑 Key Engineering Concepts Learned
- **Initialization:** Loading environment variables and instantiating specific model classes.
- **Invocation:** Executing models synchronously vs. asynchronously (`invoke`, `stream`).
- **Vector Embeddings:** Mapping natural language to high-dimensional mathematical space.
- **Distance Metrics:** Using Cosine Similarity to find semantic relationships between documents.

---

---
<div align="center">
  <p><b>Release:</b> v1.1 | <b>Status:</b> ✅ Modules 1-6 Completed | <b>Future:</b> Module 7 (Chains) and Module 8 (Runnables) Coming Next!</p>
  <i>Built with ❤️ for AI Engineering</i>
</div>