# 5. Structured Output

Structured output is the modern LangChain pattern for making LLM responses predictable and directly usable in code. Instead of parsing text after the fact, we declare the result shape up front and let the model return a typed object.

## 🚀 What Structured Output Solves
- Avoids fragile string parsing.
- Reduces runtime errors by validating output before use.
- Makes prompts more reliable and easier to maintain.

## 🧩 Structured Output Types

### 1. Pydantic Models
- Best-in-class option for Python apps.
- Use typed fields, validation, defaults, and helpful error messages.
- Works well for form-like outputs and API-style responses.

**When to use:**
- You want typed objects with validation.
- You need nested data structures or detailed schemas.

**Sample:**
```python
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI

class Scientist(BaseModel):
    name: str = Field(description="Name of the scientist")
    field: str = Field(description="Their primary field of study")

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
structured_llm = model.with_structured_output(Scientist)

result = structured_llm.invoke("Tell me about Albert Einstein")
print(result.name)
print(result.field)
```

### 2. TypedDict
- Uses Python's `TypedDict` for flexible dictionary-like structured output.
- Good when you want lighter-weight typing than Pydantic.
- Still enforces field names and expected types in your code.

**When to use:**
- You prefer plain dictionaries over model objects.
- Your structure is simple and you want fast validation.

**Sample:**
```python
from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI

class ArticleInfo(TypedDict):
    title: str
    summary: str

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
structured_llm = model.with_structured_output(ArticleInfo)

result = structured_llm.invoke("Write a short article title and summary.")
print(result['title'])
print(result['summary'])
```

### 3. JSON Schema
- Defines output as raw JSON schema.
- Great for language-agnostic or schema-first pipelines.
- Useful when you want a contract that is easily shared across systems.

**When to use:**
- You need a schema that can be used outside Python.
- You want strong control over JSON shape and types.

**Sample:**
```python
from langchain_core.output_parsers import JsonSchemaOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

json_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "summary": {"type": "string"}
    },
    "required": ["title", "summary"]
}

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
structured_llm = model.with_structured_output(json_schema)

result = structured_llm.invoke("Create a title and summary in JSON format.")
print(result)
```

## 🧠 Design Notes for This README
This README is designed for quick scanning:
- High-level comparisons of output methods.
- Clear examples for each type.
- Practical usage guidance for choosing the right structure.

## 📂 Files in this folder
- `pydantic_demo.ipynb` — Learn Pydantic validation and model creation.
- `pydantic_with_structured.ipynb` — Combine structured output with Pydantic classes.
- `typeddict_demo.ipynb` — Use `TypedDict` for structured LLM responses.
- `with_structured_output_json.ipynb` — Use raw JSON schemas for output contracts.

## ✅ Recommended Workflow
1. Start with Pydantic for Python-native structured output.
2. Use `TypedDict` when you want lightweight dictionary typing.
3. Use JSON Schema when interoperability is the priority.
4. Keep prompts explicit and let the model return typed results directly.
