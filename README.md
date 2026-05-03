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

### � Module README Navigation
Click any module README below to open the folder-specific documentation directly.

| Module | Description | README Link |
|-------|-------------|-------------|
| Module 1 | LLMs (Foundations) | [1.LLMs/README.md](1.LLMs/README.md) |
| Module 2 | ChatModels (Conversational AI) | [2.ChatModels/README.md](2.ChatModels/README.md) |
| Module 3 | Embedding Models (Semantic Search) | [3.EmbeddingModels/README.md](3.EmbeddingModels/README.md) |
| Module 4 | Prompts & Chatbots | [4.Prompts/README.md](4.Prompts/README.md) |
| Module 5 | Structured Output | [5.Structured-Output/README.md](5.Structured-Output/README.md) |
| Module 6 | Output Parsers | [6.Output-parsers/README.md](6.Output-parsers/README.md) |
| Module 7 | Chains | [7.Chains/README.md](7.Chains/README.md) |
| Module 8 | Runnables | [8.Runnables/README.md](8.Runnables/README.md) |
| Module 9 | Document Loaders | [9.Document-Loaders/README.md](9.Document-Loaders/README.md) |
| Module 10 | Text Splitters | [10.Text-Splitters/README.md](10.Text-Splitters/README.md) |
| Module 11 | Vector Store | [11.vector-store/README.md](11.vector-store/README.md) |
| Module 12 | Retrievers | [12.Retrievers/README.md](12.Retrievers/README.md) |

### �📁 Module 1: LLMs (Foundations)
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

### 📁 Module 7: Chains (Workflow Composition)
*Building multi-step LangChain workflows and conditional logic.*
- `7.Chains/README.md` - Module overview and chain design patterns.
- `7.Chains/simple_chain.py` - Simple sequential chain composition.
- `7.Chains/sequential_chain.py` - Step-by-step chained execution.
- `7.Chains/conditional_chain.py` - Branching chain logic based on model outputs.
- `7.Chains/parallel_chain.py` - Parallel execution of multiple chains.

### 📁 Module 8: Runnables (Composable Pipelines)
*Encapsulate tasks as reusable, lightweight model pipelines.*
- `8.Runnables/README.md` - Concepts and practical runnable patterns.
- `8.Runnables/runnable_passthrough.py` - Example of a passthrough runnable.
- `8.Runnables/runnable_lambda.py` - Inline function wrapper for custom logic.
- `8.Runnables/runnable_branch.py` - Conditional branching between runnables.
- `8.Runnables/runnable_parallel.py` - Run multiple runnables concurrently.
- `8.Runnables/runnable_sequence.py` - Sequential runnable pipeline example.

### 📁 Module 9: Document Loaders (Data Ingestion)
*Demonstrates how to load text, CSV, directory batches, and web content into LangChain.*
- `9.Document-Loaders/README.md` - Module overview, loader types, and workflow guidance.
- `9.Document-Loaders/text-loader.py` - Plain text ingestion using `TextLoader`.
- `9.Document-Loaders/csv_loader.py` - CSV ingestion example using `CSVLoader` and `user_data.csv`.
- `9.Document-Loaders/directory_loader.py` - Batch loading with `DirectoryLoader` for file collections.
- `9.Document-Loaders/webbase_loader.py` - Web content ingestion example.
- `user_data.csv` - Sample dataset in the repository root with 400 user records for CSV loader experiments.

### 📁 Module 10: Text Splitters (Preprocessing)
*Turn large documents into smaller chunks for embeddings and retrieval.*
- `10.Text-Splitters/README.md` - Splitter strategies and best practices.
- `10.Text-Splitters/length_based.py` - Split text by fixed length.
- `10.Text-Splitters/markdown_based.py` - Split markdown-aware chunking.
- `10.Text-Splitters/code_based.py` - Source code-aware splitting.
- `10.Text-Splitters/semantic_meaning_based.py` - Semantic text boundary splitting.
- `10.Text-Splitters/text_structure_based.py` - Structure-aware document segmentation.

### 📁 Module 11: Vector Store (Indexes & Retrieval)
*Store embeddings for fast semantic search and similarity retrieval.*
- `11.vector-store/README.md` - Vector store concepts and usage notes.
- `11.vector-store/langchain-chroma.ipynb` - Chroma index creation and querying walkthrough.
- `11.vector-store/chroma_db/` - Local Chroma database storage directory.

### 📁 Module 12: Retrievers (Smart Search)
*Retrieve relevant content using retrievers, compression, and multi-query strategies.*
- `12.Retrievers/README.md` - Retriever design and retrieval workflows.
- `12.Retrievers/vector-store-retriever.ipynb` - Vector store retrieval example.
- `12.Retrievers/compression-contextual-retriever.ipynb` - Context compression retriever demo.
- `12.Retrievers/langchain-retriever.ipynb` - Standard LangChain retriever usage.
- `12.Retrievers/multi-query-retriever.ipynb` - Multi-query retrieval patterns.

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

## 📄 Sample CSV Data File
The repository now includes a sample user dataset that is ready for CSV ingestion and data-processing demos.

- File: `user_data.csv`
- Location: repository root
- Rows: 400 synthetic user records
- Columns: `user`, `userid`, `gender`, `age`, `salary`, `purchased`
- Example loader: `9.Document-Loaders/csv_loader.py`

This file is useful for learning how to ingest structured tabular data into LangChain, build prompts over CSV rows, or run simple analytics.

### Example usage
```bash
python -c "import pandas as pd; df = pd.read_csv('user_data.csv'); print(df.head())"
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
  <p><b>Release:</b> v1.1 | <b>Status:</b> ✅ Modules 1-12 Included | <b>Next:</b> Expanded examples, improved notebook walkthroughs, and more integration demos.</p>
  <i>Built with ❤️ for AI Engineering</i>
</div>