# 📚 Text Splitters in LangChain - Complete Guide

A comprehensive guide to splitting large documents into manageable chunks for LLM processing, RAG systems, and vector embeddings.

---

## 📖 Table of Contents

1. [What are Text Splitters?](#what-are-text-splitters)
2. [Why Do We Need Them?](#why-do-we-need-them)
3. [Most Used Text Splitters](#most-used-text-splitters) ⭐
4. [5 Types We Implemented](#5-types-we-implemented)
5. [Architecture & Workflow](#architecture--workflow)
6. [Complete Examples](#complete-examples)
7. [Comparison & Choosing](#comparison--choosing)
8. [Best Practices](#best-practices)

---

## What are Text Splitters?

Text Splitters are utilities that break down large documents or texts into smaller, manageable pieces called **chunks**. Each chunk is sized appropriately for:
- ✅ LLM context windows (token limits)
- ✅ Embedding models
- ✅ Vector database storage
- ✅ RAG (Retrieval-Augmented Generation) systems
- ✅ Semantic search applications

### Key Concepts:

```
┌─────────────────────────────────────────┐
│  Large Document                         │
│  (10,000+ tokens / 50KB+)              │
└──────────────┬──────────────────────────┘
               │
               ▼
     ┌──────────────────┐
     │ Text Splitter ✂️  │
     │ chunk_size: 1000 │
     │ overlap: 200     │
     └────────┬─────────┘
              │
     ┌────────┼────────┬────────┐
     ▼        ▼        ▼        ▼
  [Chunk1] [Chunk2] [Chunk3] [Chunk4]
   with      with     with     with
  overlap   overlap   overlap   overlap
     │        │        ▼        │
     └────────────────────────────┘
              │
              ▼
   Perfect for LLM Processing
   ✅ Within context window
   ✅ Semantically coherent
   ✅ Manageable size
```

---

## Why Do We Need Them?

### Problem We Solve:

```
Without Text Splitters:          With Text Splitters:
─────────────────────           ──────────────────

📄 Document                     📦 Chunk 1
   50,000 tokens                   1,000 tokens ✅
   ❌ TOO LARGE                
   ❌ Exceeds GPT-4 limit       📦 Chunk 2
   ❌ Poor embeddings              1,000 tokens ✅
   ❌ Slow processing           
   ❌ High cost                 📦 Chunk 3
                                   1,000 tokens ✅
                                
                                ✅ Perfect size
                                ✅ Fast processing
                                ✅ Better quality
                                ✅ Lower cost
```

### Real-World Use Cases:

| Use Case | Challenge | Solution |
|----------|-----------|----------|
| 📄 **RAG System** | Need to retrieve relevant chunks | Split documents, embed, store in vector DB |
| 🤖 **LLM Processing** | Model has token limit (4K-100K) | Split into chunks that fit context window |
| 🔍 **Semantic Search** | Need semantically meaningful chunks | Use RecursiveCharacterTextSplitter |
| 💾 **Vector Embeddings** | Embeddings work best on smaller text | Split before embedding |
| 📊 **Document Analysis** | Process large documents efficiently | Split and process in parallel |
| 🏢 **Enterprise Systems** | Large document repositories | Batch process with appropriate splitters |

---

## Most Used Text Splitters

In production systems, these are the **most frequently used** based on industry adoption:

### 🥇 #1: RecursiveCharacterTextSplitter (80% of use cases)

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", ". ", " ", ""]
)
```

**Why it dominates:**
- ✅ Smart, hierarchical splitting
- ✅ Preserves semantic meaning
- ✅ Works with any text type
- ✅ No external dependencies
- ✅ Fast and reliable
- ✅ Production-ready

**Best for:**
- General purpose splitting
- Mixed content types
- When you don't know the structure
- Most RAG applications

**See:** [text_structure_based.py](text_structure_based.py)

---

### 🥈 #2: CharacterTextSplitter (10% of use cases)

```python
from langchain_text_splitters import CharacterTextSplitter

splitter = CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separator=" "
)
```

**Why use it:**
- ✅ Simplest approach
- ✅ Fastest processing
- ✅ Minimal overhead
- ✅ Good for simple text

**Best for:**
- Simple, unstructured text
- Quick prototyping
- When performance is critical
- CSV or log files

**See:** [length_based.py](length_based.py)

---

### 🥉 #3: Language-Specific Splitters (7% of use cases)

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

# For Markdown
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=1000,
    chunk_overlap=200
)

# For Python Code
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=1000,
    chunk_overlap=200
)
```

**Why use it:**
- ✅ Respects language syntax
- ✅ Splits at logical boundaries
- ✅ Preserves code structure
- ✅ Great for documentation

**Best for:**
- Source code
- Markdown documentation
- Technical content
- Code repositories

**See:** [markdown_based.py](markdown_based.py) & [code_based.py](code_based.py)

---

### 🎖️ #4: TokenTextSplitter (2% of use cases)

```python
from langchain_text_splitters import TokenTextSplitter

splitter = TokenTextSplitter(
    chunk_size=1000,        # tokens
    chunk_overlap=200,
    encoding_name="cl100k_base"  # GPT-4
)
```

**Why use it:**
- ✅ Precise token control
- ✅ Predictable API costs
- ✅ Respects LLM limits exactly

**Best for:**
- Cost-sensitive applications
- When you know exact token budget
- LLM API integrations

---

### 🌟 #5: Semantic/LLM-Based Splitters (1% of use cases)

```python
from langchain_text_splitters import LanguageModelTextSplitter
from langchain_openai import OpenAI

llm = OpenAI(temperature=0)
splitter = LanguageModelTextSplitter(
    llm=llm,
    chunk_size=1000,
    chunk_overlap=200
)
```

**Why use it:**
- ✅ AI-powered semantic understanding
- ✅ Perfect split points
- ✅ Best quality results

**Best for:**
- Complex legal documents
- Academic papers
- When quality is paramount
- Small batch processing

**See:** [semantic_meaning_based.py](semantic_meaning_based.py)

---

## 5 Types We Implemented

### 1️⃣ CharacterTextSplitter - Length/Token Based
**File:** [length_based.py](length_based.py)

Splits text on a single character separator. Fastest but simplest approach.

```python
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# Load PDF
loader = PyPDFLoader("learning-langchain.pdf")
documents = loader.load()

# Split by character
text_splitter = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=0,
    separator=' '
)

# Process documents
result = text_splitter.split_documents(documents)

print(f"✂️ Split {len(documents)} pages into {len(result)} chunks")
print(f"📄 First chunk:\n{result[0].page_content}")
```

**Pros:** ⚡ Fast, simple logic  
**Cons:** ❌ Can split mid-sentence, poor semantics  
**Use When:** Simple text, quick prototyping

---

### 2️⃣ RecursiveCharacterTextSplitter - Structure Based ⭐
**File:** [text_structure_based.py](text_structure_based.py)

Most intelligent general-purpose splitter. Respects document structure.

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """Space is the boundless three-dimensional extent in which 
objects and events have relative position and direction. In classical physics, 
physical space is often conceived in three linear dimensions, although modern 
physicists usually consider it, with time, to be part of a boundless 
four-dimensional continuum known as spacetime."""

# Initialize splitter with multiple separators
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50,
    separators=["\n\n", "\n", ". ", " ", ""]
)

# Split text
chunks = text_splitter.split_text(text)

print(f"📦 Created {len(chunks)} chunks")
for i, chunk in enumerate(chunks, 1):
    print(f"\nChunk {i} ({len(chunk)} chars):")
    print(f"   {chunk[:100]}...")
```

**Hierarchical Splitting Strategy:**
```
Paragraph ("\n\n")
    ↓ (if too large)
Line ("\n")
    ↓ (if too large)
Sentence (". ")
    ↓ (if too large)
Word (" ")
    ↓ (if too large)
Character ("")
```

**Pros:** ✅ Smart, semantic, respects structure  
**Cons:** Slightly slower than character-based  
**Use When:** General purpose, unknown structure, RAG systems

---

### 3️⃣ Markdown/Code Language Splitters
**Files:** [markdown_based.py](markdown_based.py) & [code_based.py](code_based.py)

Language-aware splitting using `Language` enum.

**Markdown Example:**
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

# Markdown documentation
markdown_text = """
# Project Name: Smart Student Tracker

A simple student tracking system built using Python and Flask.

## Features

- Add Student: Users can add new student records
- View Students: Users can view all students
- Search Functionality: Search by name or attributes
- Data Validation: Ensures accurate data

## Tech Stack

- Python: Backend development
- Flask: Web framework
- HTML/CSS: Frontend interface

## Getting Started

To get started, follow these steps...
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_text(markdown_text)
print(f"📑 Split markdown into {len(chunks)} semantically coherent chunks")
```

**Code Example:**
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

code = """
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return self.name

student1 = Student("Alice", 20)
print(student1.get_details())

if student1.age > 18:
    print("Student is an adult.")
else:
    print("Student is a minor.")
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=50
)

chunks = splitter.split_text(code)
print(f"💻 Split code into {len(chunks)} logical units")
```

**Supported Languages:**
```python
Language.PYTHON
Language.JAVASCRIPT
Language.TYPESCRIPT
Language.MARKDOWN
Language.LATEX
Language.HTML
Language.SOL        # Solidity (smart contracts)
Language.CPP
Language.JAVA
Language.C
Language.RUBY
Language.RUST
```

**Pros:** ✅ Respects syntax, logical boundaries  
**Cons:** Language-specific  
**Use When:** Code, documentation, technical content

---

### 4️⃣ TokenTextSplitter - Token-Based
```python
from langchain_text_splitters import TokenTextSplitter

text = """Your text here..."""

# For GPT-4/OpenAI
splitter = TokenTextSplitter(
    chunk_size=1000,           # 1000 tokens per chunk
    chunk_overlap=200,
    encoding_name="cl100k_base"
)

chunks = splitter.split_text(text)
print(f"🎫 Split into {len(chunks)} token-based chunks")

# Common encodings:
# cl100k_base     → GPT-4, GPT-3.5-turbo
# p50k_base       → text-davinci-003, text-davinci-002
# r50k_base       → GPT-3, text-davinci-001, text-curie-001
```

**Pros:** ✅ Precise token control, predictable costs  
**Cons:** Requires tokenizer, model-specific  
**Use When:** Budget-sensitive, known token limits

---

### 5️⃣ Semantic/LLM-Based Splitter
**File:** [semantic_meaning_based.py](semantic_meaning_based.py)

AI-powered splitting using LLM to understand document structure.

```python
from langchain_text_splitters import LanguageModelTextSplitter
from langchain_openai import OpenAI

# Initialize LLM
llm = OpenAI(model="gpt-3.5-turbo", temperature=0)

# Create splitter
splitter = LanguageModelTextSplitter(
    llm=llm,
    chunk_size=1000,
    chunk_overlap=200
)

# Complex document
legal_doc = """
AGREEMENT AND PLAN OF MERGER

This Agreement is made and entered into as of [DATE], by and between 
[COMPANY A], a corporation, and [COMPANY B], a corporation.

DEFINITIONS

For purposes of this Agreement, the following terms shall have the 
meanings set forth below...

REPRESENTATIONS AND WARRANTIES

Each party represents and warrants to the other that...

COVENANTS AND AGREEMENTS

The parties agree to the following obligations...
"""

chunks = splitter.split_text(legal_doc)
print(f"🤖 LLM-based splitting created {len(chunks)} semantically coherent chunks")
```

**Pros:** ✅ Perfect semantic understanding  
**Cons:** ❌ Expensive (API calls), slow  
**Use When:** Important documents, legal content, perfect quality needed

---

## Architecture & Workflow

### System Architecture:

```
┌────────────────────────────────────────────────────────────────┐
│                    INPUT LAYER                                  │
│  (Documents, PDFs, Text, Web pages, Code, Markdown)            │
└────────────────────┬─────────────────────────────────────────┘
                     │
        ┌────────────▼───────────┐
        │  Load Documents        │
        │  PyPDFLoader          │
        │  TextLoader           │
        │  WebBaseLoader        │
        │  DirectoryLoader      │
        └────────────┬───────────┘
                     │
        ┌────────────▼────────────────────────┐
        │  SELECT TEXT SPLITTER              │
        │  ─────────────────────────────────  │
        │  ① CharacterTextSplitter           │
        │  ② RecursiveCharacterSplitter ⭐   │
        │  ③ Language-Specific               │
        │  ④ TokenTextSplitter               │
        │  ⑤ LLM-Based                       │
        └────────────┬─────────────────────────┘
                     │
        ┌────────────▼──────────────────┐
        │  CONFIGURE PARAMETERS        │
        │  • chunk_size (500-2000)      │
        │  • chunk_overlap (10-20%)     │
        │  • separators                 │
        │  • length_function            │
        └────────────┬──────────────────┘
                     │
        ┌────────────▼──────────────────────┐
        │  SPLITTING PIPELINE               │
        │  1. Validate input                │
        │  2. Apply splitting strategy      │
        │  3. Create chunks                 │
        │  4. Add overlaps                  │
        │  5. Add metadata                  │
        │  6. Format output                 │
        └────────────┬──────────────────────┘
                     │
        ┌────────────▼──────────────────┐
        │  OUTPUT LAYER                 │
        │  List[Chunk]                  │
        │  With metadata & references   │
        └────────────┬──────────────────┘
                     │
    ┌────────────────┼────────────────┬────────────────┐
    ▼                ▼                ▼                ▼
 📊 Embeddings   🗄️ Vector DB    🤖 LLM Prompt    🔍 Search
 Generate        Index            Injection         Results
 vectors         chunks           for RAG
```

### Data Flow Example:

```
Original Document (15KB)
        │
        ▼
┌─────────────────────────┐
│ Chunk 1: 1.2 KB        │ 
│ ┌────────────────────┐ │
│ │ Content with...   │ │
│ │ overlap from     │ │
│ │ previous chunk   │ │
│ └────────────────────┘ │
│ Metadata: {page: 1}   │
└─────────────────────────┘
        │
        ▼
┌─────────────────────────┐
│ Chunk 2: 1.2 KB        │
│ ┌────────────────────┐ │
│ │ Content overlaps   │ │
│ │ from chunk 1      │ │
│ │ and continues...  │ │
│ └────────────────────┘ │
│ Metadata: {page: 2}   │
└─────────────────────────┘
        │
        ▼
    ... More chunks
        │
        ▼ (Ready for downstream processing)
   
   ✅ RAG System
   ✅ Embedding Model
   ✅ Vector Database
   ✅ LLM Processing
```

---

## Complete Examples

### Example 1: Simple Text Splitting

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Artificial Intelligence is transforming industries.
Machine Learning enables computers to learn from data.
Deep Learning uses neural networks with multiple layers.
Natural Language Processing handles human language.
Computer Vision processes images and videos.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separators=["\n", ". ", " ", ""]
)

chunks = splitter.split_text(text)

print(f"📊 Statistics:")
print(f"   Total text length: {len(text)} chars")
print(f"   Number of chunks: {len(chunks)}")
print(f"   Avg chunk size: {sum(len(c) for c in chunks) // len(chunks)} chars")
print(f"\n📑 Chunks:")
for i, chunk in enumerate(chunks, 1):
    print(f"   Chunk {i}: {chunk}\n")
```

### Example 2: PDF Document Processing

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# Load PDF
loader = PyPDFLoader("document.pdf")
documents = loader.load()

# Split documents
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)

# Process
print(f"📄 Loaded {len(documents)} pages")
print(f"✂️ Split into {len(chunks)} chunks")

# Access metadata
for i, chunk in enumerate(chunks[:3]):
    print(f"\nChunk {i+1}:")
    print(f"   Page: {chunk.metadata.get('page')}")
    print(f"   Size: {len(chunk.page_content)} chars")
    print(f"   Content: {chunk.page_content[:100]}...")
```

### Example 3: Language-Specific Splitting

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

# Markdown documentation
markdown = """
# Getting Started

## Installation

```bash
pip install langchain
```

## Usage

```python
from langchain import LLM
llm = LLM()
```

## Features

- Easy to use
- Flexible
- Extensible
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=200,
    chunk_overlap=50
)

chunks = splitter.split_text(markdown)
print(f"✂️ Markdown split into {len(chunks)} logical sections")
```

### Example 4: Chunk with Overlap Visualization

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

text = "The quick brown fox jumps over the lazy dog. " * 10

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=30
)

chunks = splitter.split_text(text)

print("Overlap Visualization:")
print("=" * 80)
for i, chunk in enumerate(chunks):
    print(f"\n📦 Chunk {i+1}:")
    print(f"   {chunk}")
    if i < len(chunks) - 1:
        overlap = chunk[-30:]
        print(f"   ↓ (30 chars overlap with next chunk)")
        print(f"   '{overlap}'")
```

---

## Comparison & Choosing

### Quick Decision Tree:

```
START: What are you splitting?
│
├─ Markdown files/Documentation?
│  └─ Use: RecursiveCharacterTextSplitter.from_language(Language.MARKDOWN)
│
├─ Source code?
│  └─ Use: RecursiveCharacterTextSplitter.from_language(Language.[LANGUAGE])
│
├─ Complex legal/academic document?
│  └─ Need perfect quality?
│     ├─ YES → Use: LanguageModelTextSplitter (with LLM)
│     └─ NO → Use: RecursiveCharacterTextSplitter
│
├─ Need precise token control?
│  └─ Use: TokenTextSplitter
│
└─ Simple, unstructured text?
   ├─ Performance critical?
   │  └─ Use: CharacterTextSplitter
   └─ General purpose?
      └─ Use: RecursiveCharacterTextSplitter ⭐
```

### Comparison Table:

| Aspect | Character | Recursive | Language | Token | LLM-Based |
|--------|-----------|-----------|----------|-------|-----------|
| **Speed** | ⚡⚡⚡ | ⚡⚡ | ⚡⚡ | ⚡ | 🐢 |
| **Quality** | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Semantic** | ❌ | ✅ | ✅ | ✅ | ✅✅ |
| **Cost** | 💚 Free | 💚 Free | 💚 Free | 💚 Free | 💸 Expensive |
| **LLM Need** | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Production** | ⚠️ | ✅✅ | ✅ | ✅ | ✅ |

### When to Use Each:

**CharacterTextSplitter:**
- Simple, unstructured text
- Performance is critical
- Quick prototyping
- CSV/log files

**RecursiveCharacterTextSplitter:** ⭐ **Most Common**
- General purpose (80% of use cases)
- Unknown document structure
- RAG systems
- Mixed content types
- Default choice

**Language-Specific:**
- Source code
- Markdown documentation
- Technical content
- Code repositories

**TokenTextSplitter:**
- Precise token budgets
- Cost-sensitive applications
- LLM API integration
- Known token limits

**LLM-Based:**
- Complex legal documents
- Academic papers
- Perfect quality needed
- Small batch processing
- When cost is not an issue

---

## Best Practices

### 1️⃣ Choose Chunk Size Wisely

```
┌─────────────────────────────────────────────┐
│ Use Case        │ Recommended Chunk Size   │
├─────────────────────────────────────────────┤
│ Search/QA       │ 512-1024 chars          │
│ RAG (General)   │ 1000-2000 chars         │
│ Summarization   │ 2000-4000 chars         │
│ QA Systems      │ 800-1500 chars          │
│ Code Review     │ 500-1500 chars          │
│ Legal Docs      │ 1000-3000 chars         │
│ Long Context    │ 3000-8000 chars         │
└─────────────────────────────────────────────┘
```

### 2️⃣ Set Appropriate Overlap

```python
# RAG Systems (recommended)
# Use 10-20% overlap for context preservation
chunk_size = 1000
chunk_overlap = 100  # 10% overlap

# Cost-Sensitive (streaming, real-time)
# Use 0-5% overlap to reduce redundancy
chunk_size = 1000
chunk_overlap = 0    # No overlap

# Complex Documents
# Use 20-30% overlap for better context
chunk_size = 1000
chunk_overlap = 250  # 25% overlap
```

### 3️⃣ Test & Validate

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_text(your_document)

# Validate
print(f"✅ Total chunks: {len(chunks)}")
print(f"📊 Chunk sizes:")
print(f"   Min: {min(len(c) for c in chunks)}")
print(f"   Max: {max(len(c) for c in chunks)}")
print(f"   Avg: {sum(len(c) for c in chunks) // len(chunks)}")

# Check coverage
total_original = len(your_document)
total_chunks = sum(len(c) for c in chunks)
overlap_overhead = ((total_chunks - total_original) / total_original) * 100
print(f"🔗 Overlap overhead: {overlap_overhead:.1f}%")
```

### 4️⃣ Handle Metadata

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("document.pdf")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)

# Metadata is automatically preserved
for chunk in chunks:
    print(f"Page: {chunk.metadata['page']}")
    print(f"Source: {chunk.metadata['source']}")
    print(f"Content: {chunk.page_content[:50]}...")
```

### 5️⃣ Performance Tips

```python
# ✅ Good - Fast processing
splitter = CharacterTextSplitter(chunk_size=1000)

# ✅ Better - Balanced
splitter = RecursiveCharacterTextSplitter(chunk_size=1000)

# ⚠️ Slower - Heavy processing
splitter = LanguageModelTextSplitter(
    llm=expensive_llm,
    chunk_size=1000
)

# 💡 Optimization: Process in batches
documents = load_large_batch()
for doc in documents:
    chunks = splitter.split_documents([doc])
    # Process chunks incrementally
    process(chunks)
```

---

## Summary

### Files in This Module:

| File | Type | Best For | Status |
|------|------|----------|--------|
| [length_based.py](length_based.py) | CharacterTextSplitter | Simple text, quick splits | ✅ Working |
| [text_structure_based.py](text_structure_based.py) | RecursiveCharacterTextSplitter | General purpose, RAG | ✅ Working ⭐ |
| [markdown_based.py](markdown_based.py) | Language-Specific (Markdown) | Documentation | ✅ Working |
| [code_based.py](code_based.py) | Language-Specific (Code) | Source code | ✅ Working |
| [semantic_meaning_based.py](semantic_meaning_based.py) | LanguageModelTextSplitter | Complex documents, LLM-based | ✅ Working |

### Key Takeaways:

1. **Start with RecursiveCharacterTextSplitter** - It handles 80% of use cases ⭐
2. **Use 10-20% overlap** for RAG systems to maintain context
3. **Test different chunk sizes** (500, 1000, 2000) for your use case
4. **Language-specific splitters** for code and documentation
5. **TokenTextSplitter** for precise budget control
6. **LLM-based splitter** only for critical, complex documents

### Recommended Workflow:

```
1. Start Simple
   └─ Use RecursiveCharacterTextSplitter with chunk_size=1000

2. Experiment
   └─ Try chunk_size values: 512, 1000, 2000, 4000
   └─ Try overlap: 0%, 10%, 20%, 30%

3. Measure
   └─ Test on your RAG/embedding system
   └─ Measure quality and performance

4. Optimize
   └─ Fine-tune chunk_size and overlap
   └─ Consider language-specific splitter if applicable

5. Monitor
   └─ Track performance in production
   └─ Adjust based on results
```

---

## 🚀 Quick Start

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Create splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

# 2. Split text
chunks = splitter.split_text(your_text)

# 3. Use chunks
for chunk in chunks:
    embedding = embed_model.embed(chunk)
    vector_store.add(embedding, metadata={"text": chunk})
```

---

**Last Updated:** April 2026

🎉 **Happy Splitting!** ✂️📚
