# LangChain Retrievers: A Complete Guide

## What is a Retriever?

A **Retriever** is a component in LangChain that searches through a knowledge base (vector store, documents, database, etc.) to find the most relevant information based on a user's query. It acts as the "search engine" between the user's question and the source documents.

In the context of Retrieval-Augmented Generation (RAG), retrievers bridge the gap between:
- **User Query** → **Retriever** → **Relevant Documents** → **LLM** → **Answer**

## Why Are Retrievers Needed?

### Key Problems Retrievers Solve:

1. **Knowledge Cutoff**: LLMs have training data up to a certain date. Retrievers allow them to access current and custom information.
2. **Hallucination Reduction**: By grounding responses in actual documents, retrievers reduce false or made-up information.
3. **Scalability**: Instead of fine-tuning models, you can update your knowledge base instantly.
4. **Cost Efficiency**: Use smaller models with better context instead of expensive large models.
5. **Domain-Specific Knowledge**: Access proprietary documents and specialized information not in training data.

## Real-World Use Cases

### 1. **Customer Support Chatbots**
   - **Scenario**: A company with thousands of support documents
   - **How**: Retriever searches FAQ/documentation when customer asks a question
   - **Benefit**: Consistent, accurate answers without manual lookup
   - **Example**: Bank customer asking about interest rates → Retriever finds relevant policy docs → LLM provides clear answer

### 2. **Legal Document Analysis**
   - **Scenario**: Law firms with thousands of case files and regulations
   - **How**: Retriever finds relevant cases and laws related to a query
   - **Benefit**: Faster research, comprehensive precedent discovery
   - **Example**: "What does the 2023 privacy act say about data retention?" → Retriever finds relevant sections → LLM summarizes

### 3. **Medical Query System**
   - **Scenario**: Hospital with medical literature, patient guidelines, treatment protocols
   - **How**: Retriever finds relevant medical documents
   - **Benefit**: Evidence-based responses for patient/doctor queries
   - **Example**: "Symptoms of hypertension?" → Retriever finds medical guidelines → LLM explains in simple terms

### 4. **E-commerce Product Assistant**
   - **Scenario**: Online store with millions of product descriptions
   - **How**: Retriever finds relevant products based on customer query
   - **Benefit**: Personalized product recommendations with accurate specs
   - **Example**: "Laptops under $1000 with good battery?" → Retriever finds matching products → LLM recommends top options

### 5. **Internal Knowledge Base**
   - **Scenario**: Company wiki, policies, and documentation
   - **How**: Retriever searches knowledge base for employee queries
   - **Benefit**: Self-service support reduces HR burden
   - **Example**: Employee asks "What's the remote work policy?" → Retriever finds policy doc → LLM summarizes

## Types of Retrievers

### 1. **Similarity Retriever (Vector-Based)**
```python
retriever = vectorstore.as_retriever(
    search_type="similarity", 
    search_kwargs={"k": 5}
)
```
- **How it works**: Converts queries to embeddings, finds closest vectors
- **Best for**: Semantic search, conceptual similarity
- **Example in repo**: `vector-store-retriever.ipynb`

### 2. **Multi-Query Retriever**
```python
multiquery_retriever = MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(),
    llm=ChatGroq(model="llama-3.1-8b-instant")
)
```
- **How it works**: LLM generates multiple query variations, retrieves for each, returns combined results
- **Best for**: Complex queries that need rephrasing
- **Advantage**: Catches documents missed by single query
- **Example in repo**: `multi-query-retriever.ipynb`

### 3. **Compression Retriever**
```python
compressor = LLMChainExtractor.from_llm(
    llm, base_compressor=EmbeddingsFilter()
)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor, 
    base_retriever=retriever
)
```
- **How it works**: First retrieves documents, then compresses/filters for relevance
- **Best for**: Large documents, reducing token usage
- **Advantage**: Removes irrelevant parts of retrieved documents
- **Example in repo**: `compression-contextual-retriever.ipynb`

### 4. **Basic Retriever**
- **How it works**: Simple vector similarity search
- **Best for**: Straightforward searches, baseline implementation
- **Speed**: Fastest

### 5. **Custom Retrievers**
- **How it works**: User-defined logic for retrieval
- **Best for**: Specialized use cases, hybrid search (vector + keyword), database queries

## Comparison Table

| Retriever Type | Use Case | Speed | Accuracy | Best For |
|---|---|---|---|---|
| **Similarity** | Basic vector search | Fast | Good | Simple semantic search |
| **Multi-Query** | Complex queries | Medium | Excellent | Nuanced questions |
| **Compression** | Large documents | Medium | Good | Token optimization |
| **Custom** | Specialized needs | Variable | Depends | Unique requirements |

## When to Use Which Retriever

### Use **Similarity Retriever** When:
- ✅ You have straightforward queries
- ✅ Query and documents are well-aligned semantically
- ✅ You need maximum speed
- ✅ Dataset is small to medium
- ❌ NOT good for: Complex multi-faceted queries

### Use **Multi-Query Retriever** When:
- ✅ Queries are complex or ambiguous
- ✅ Single phrasing might miss relevant documents
- ✅ You need comprehensive coverage
- ✅ Slight latency overhead is acceptable
- ❌ NOT good for: Real-time applications, simple queries

### Use **Compression Retriever** When:
- ✅ Documents are long and partially relevant
- ✅ Token budget is limited
- ✅ You want only the most relevant sections
- ✅ Working with expensive LLM APIs
- ❌ NOT good for: Fast response requirements

### Use **Custom Retriever** When:
- ✅ You need hybrid search (vector + keyword + metadata filters)
- ✅ You have database-specific logic
- ✅ You need business rule-based filtering
- ✅ Combining multiple retrieval methods

## Code Examples from This Folder

### Setup (All Examples)
```python
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv(override=True)
embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
vectorstore = FAISS.from_documents(documents=docs, embedding=embedding)
```

### Basic Similarity Retrieval
See: `vector-store-retriever.ipynb`
```python
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})
results = retriever.invoke("your query here")
```

### Advanced: Multi-Query
See: `multi-query-retriever.ipynb`
```python
multiquery_retriever = MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(search_kwargs={"k": 5}),
    llm=ChatGroq(model="llama-3.1-8b-instant")
)
results = multiquery_retriever.invoke("complex query")
```

### Advanced: Compression
See: `compression-contextual-retriever.ipynb`
```python
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

compressor = LLMChainExtractor.from_llm(llm, base_compressor=EmbeddingsFilter())
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor, 
    base_retriever=retriever
)
```

## Performance Considerations

| Factor | Impact | Mitigation |
|--------|--------|-----------|
| **Vector Dimension** | Higher dimensions = slower search | Use appropriate embedding model |
| **Dataset Size** | More documents = slower retrieval | Use vector database indexing |
| **Number of Results (k)** | Higher k = slower but more comprehensive | Balance between quality and speed |
| **Embedding Quality** | Poor embeddings = poor results | Use high-quality embedding model |

## Retriever + LLM Pipeline Example

```python
# Step 1: Retrieve relevant documents
retrieved_docs = retriever.invoke("user question")

# Step 2: Format as context
context = "\n".join([doc.page_content for doc in retrieved_docs])

# Step 3: Create prompt with context
prompt = f"""Based on the following documents:
{context}

Answer this question: user question
"""

# Step 4: Get LLM answer grounded in retrieved docs
answer = llm.invoke(prompt)
```

## Key Takeaways

1. **Retrievers enable RAG**: Connect LLMs to external knowledge
2. **Multiple types available**: Choose based on your use case
3. **Similarity is baseline**: Start here, upgrade if needed
4. **Multi-Query for complexity**: Better recall on complex queries
5. **Compression saves costs**: Reduce tokens passed to LLM
6. **Combine with LLM**: Retrievers alone don't answer—they provide context

## Files in This Folder

- **vector-store-retriever.ipynb** - Basic similarity retrieval from FAISS
- **multi-query-retriever.ipynb** - LLM-powered query expansion and retrieval
- **compression-contextual-retriever.ipynb** - Contextual compression for efficiency
- **langchain-retriever.ipynb** - General retriever patterns and techniques

## Next Steps

1. Start with `vector-store-retriever.ipynb` for basics
2. Move to `multi-query-retriever.ipynb` for advanced querying
3. Use `compression-contextual-retriever.ipynb` for production optimization
4. Experiment with different embedding models and chunk sizes

## Additional Resources

- [LangChain Retrievers Documentation](https://python.langchain.com/docs/modules/data_connection/retrievers/)
- [Retrieval Augmented Generation (RAG) Guide](https://python.langchain.com/docs/use_cases/question_answering/)
- [Vector Stores in LangChain](https://python.langchain.com/docs/modules/data_connection/vectorstores/)
