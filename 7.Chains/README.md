# 7. Chains in LangChain

## What are Chains?

In LangChain, **chains** are the fundamental building blocks for composing multiple components (like prompts, models, parsers) into a single runnable sequence or workflow. They enable complex LLM applications by linking steps together, allowing data to flow from one component to the next.
 
Chains can be:
- **Sequential**: Steps run one after another.
- **Parallel**: Multiple steps run simultaneously.
- **Conditional**: Steps branch based on conditions.
- **Simple**: Basic single-step chaining.

This folder demonstrates 4 types of chains using Groq (Llama), Google Gemini, and parsers.

## Implemented Chain Types

### 1. Simple Chain (`simple_chain.py`)
**Purpose**: Basic chaining of a single prompt → model → parser.

**Key Components**:
- `PromptTemplate`: Generates 2 facts about a topic (e.g., 'Spaceship').
- `ChatGroq` (Llama 3.1 8B).
- `StrOutputParser`.

**Execution**:
```
chain = prompt | model | parser
result = chain.invoke({'topic': 'Spaceship'})
```
**Visualization**: Prints ASCII graph of the chain.

**Output Example**: Interesting facts about the topic.

### 2. Sequential Chain (`sequential_chain.py`)
**Purpose**: Multi-step sequential processing where output of one step feeds the next.

**Key Components**:
- Prompt 1: Detailed report on topic (e.g., 'Climate Change').
- `ChatGroq`.
- Prompt 2: 5-point summary from the report.
- `ChatGroq`.
- `StrOutputParser`.

**Execution**:
```
chain = prompt1 | model | prompt2 | model | parser
result = chain.invoke({'topic': 'Climate Change'})
```
**Visualization**: ASCII graph showing sequential flow.

**Output Example**: Concise 5-point summary of a detailed report.

### 3. Parallel Chain (`parallel_chain.py`)
**Purpose**: Run multiple independent chains in parallel, then merge results.

**Key Components**:
- `RunnableParallel` for two branches:
  - Notes: Short/simple notes from text using `ChatGroq`.
  - Quiz: 5 Q&A from text using `ChatGoogleGenerativeAI` (Gemini 2.5 Flash).
- Merge prompt: Combines notes + quiz.
- `ChatGroq`.
- `StrOutputParser`.

**Execution** (on sample SVM text):
```
parallel_chain = RunnableParallel({'notes': ..., 'quiz': ...})
chain = parallel_chain | merged_chain
result = chain.invoke(text)
```
**Visualization**: ASCII graph of parallel → merge.

**Output Example**: Merged document with notes and quiz.

### 4. Conditional Chain (`conditional_chain.py`)
**Purpose**: Classify input and branch to different responses based on condition.

**Key Components**:
- Classifier: `PydanticOutputParser` (sentiment: positive/negative).
- `RunnableBranch`:
  - Positive → Positive response prompt.
  - Negative → Negative response prompt.
  - Default.
- `ChatGroq`.

**Execution**:
```
classifier_chain = prompt1 | model | parser2
branch_chain = RunnableBranch(...)
chain = classifier_chain | branch_chain
result = chain.invoke({'feedback': 'Pathetic battery life'})
```
**Visualization**: ASCII graph showing conditional branching.

**Output Example**: Appropriate response based on sentiment (e.g., negative feedback handler).

## Setup & Run
1. Install dependencies: `pip install -r requirements.txt` (LangChain, Groq, Google GenAI, etc.).
2. Set `.env` with API keys (GROQ_API_KEY, GOOGLE_API_KEY).
3. Run: `python 7.Chains/[file].py`

Each file visualizes the chain graph via `chain.get_graph().print_ascii()`.

## Next Steps
- Add more chain types (e.g., LLMChain, RetrievalQA).
- Integrate with prior modules (Prompts, Output Parsers).

