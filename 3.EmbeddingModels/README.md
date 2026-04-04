# 🧩 3. Embedding Models

Embedding models convert text into numerical representations called **vectors**. These vectors capture the "meaning" or semantic essence of the text, allowing computers to compare how similar two pieces of text are. 🧠

### 📖 Definition
An embedding model creates a list of floating-point numbers (a vector) for a given text. If two pieces of text are semantically similar (e.g., "king" and "queen"), their vectors will be "closer" to each other in mathematical space. 📏

### 🎯 Common Use Cases
Why do we need embeddings? Here are some of the most popular applications:
- **🔍 Semantic Search:** Finding documents based on meaning rather than exact keyword matches.
- **🤖 Retrieval-Augmented Generation (RAG):** Providing context to LLMs by fetching relevant documents.
- **📊 Clustering & Classification:** Grouping similar texts together (e.g., topic modeling, sentiment analysis).
- **💡 Recommendations:** Suggesting related articles, products, or content.

### 🏆 Top Embedding Model Providers
Not all embedding models are the same. Some are optimized for cost and speed, while others capture deeper semantic nuances:

| Provider | Recommended Models | Key Features |
| :--- | :--- | :--- |
| **🟢 OpenAI** | `text-embedding-3-small`, `text-embedding-3-large` | Industry standard, highly scalable, variable dimensions. |
| **🔵 Google** | `text-embedding-004`, `multimodal-embedding` | Native support for Gemini ecosystem and multimodal inputs. |
| **🤗 Hugging Face**| `all-MiniLM-L6-v2`, `BAAI/bge-large-en-v1.5` | SOTA performance for open-source and local execution. |
| **🟣 Cohere** | `embed-english-v3.0`, `embed-multilingual-v3.0` | Leading the industry in retrieval quality and multilingual support. |

### 🛠️ How to Use LangChain Embeddings
LangChain provides a standard interface for working with embeddings, primarily through two methods:
- `embed_query(text)`: 📝 Used for embedding a single string (like a search query).
- `embed_documents(texts)`: 📚 Used for embedding a list of strings (like chunks of a document for a knowledge base).

### 🚀 Example: OpenAI Embeddings
```python
from langchain_openai import OpenAIEmbeddings

# Initialize the model
embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

# Embed a single query
vector = embedding.embed_query("Artificial Intelligence is fascinating.")
print(f"Vector dimensions: {len(vector)}")
```

### 💻 Using Local Open-Source Embeddings (Hugging Face)
Hugging Face is the best place to find embedding models that can run locally on your CPU/GPU without recurring API costs. 💸

*   **Top Open Models:**
    *   `all-MiniLM-L6-v2`: Extremely fast and small (~80MB), great for basic tasks.
    *   `BAAI/bge-small-en-v1.5`: State-of-the-art performance for its compact size.

#### Example: Local HF Embeddings
```python
from langchain_huggingface import HuggingFaceEmbeddings

# Load model locally
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Embed a query locally
vector = embedding.embed_query("This is a local embedding.")
print(f"Vector dimensions: {len(vector)}") # Returns 384 dimensions
```

### 📐 Measuring Similarity
Once you have embeddings, you often want to compare them. The most common metric used is **Cosine Similarity**, which measures the angle between two vectors. A score closer to `1` means the texts are highly similar, while `0` means they are unrelated. 🎯

---

### 📂 Files in this folder:
- 📄 `_embedding_openai_query.py`: Simple query embedding using OpenAI's API.
- 📄 `_embedding_openai_docs.py`: Embedding multiple documents with OpenAI.
- 📄 `_embedding_gemini_query.py`: Using Google's Gemini models for embeddings.
- 📄 `_embedding_hf_local.py`: Running local models (like `all-MiniLM-L6-v2`) via HuggingFace without API costs.
- 📄 `_document_similariity.py`: A script calculating cosine similarity between different sentences to find semantic matches.