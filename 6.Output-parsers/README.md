# 6. Output Parsers

Output Parsers help you convert free-form LLM text into structured programmatic data. They are ideal when the model cannot directly return typed JSON or when you want explicit parsing control.

## 🚦 Why Use Output Parsers
- Use output parsers when `.with_structured_output()` is not available or not reliable.
- They give you a clear contract for what the model should return.
- They also allow finer prompt control before parsing the raw response.

## 🧩 Output Parser Types

### 1. PydanticOutputParser
- Converts model output into a Pydantic model.
- Best when you want validation, type coercion, and rich Python object behavior.
- Ideal for: data extraction, API payload generation, and typed application workflows.

**When to use:**
- You need strict fields and validation.
- You want attribute access (`result.name`, `result.age`).

**Example:**
```python
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser

class Person(BaseModel):
    name: str = Field(description="Person name")
    age: int = Field(description="Person age")

parser = PydanticOutputParser(pydantic_object=Person)
prompt = (
    "Extract the person's name and age from the text.\n"
    "{format_instructions}"
)
final_prompt = prompt.format(format_instructions=parser.get_format_instructions())

# model_response = model.invoke(final_prompt)
# parsed = parser.parse(model_response.content)
# print(parsed.name, parsed.age)
```

### 2. JsonOutputParser
- Ensures the model returns valid JSON.
- Returns a Python dictionary.
- Great when you want lightweight parsing and flexible schemas.

**When to use:**
- You only need JSON data, no Pydantic validation.
- The structure is simple or dynamic.

**Example:**
```python
from langchain_core.output_parsers import JsonOutputParser

parser = JsonOutputParser()
prompt = (
    "Return a JSON object with keys `title` and `summary`.\n"
    "{format_instructions}"
)
final_prompt = prompt.format(format_instructions=parser.get_format_instructions())

# response = model.invoke(final_prompt)
# data = parser.parse(response.content)
# print(data['title'], data['summary'])
```

### 3. StructuredOutputParser
- Uses schema objects such as `ResponseSchema` definitions.
- Works well when you want a schema-driven result but do not want a full Pydantic model.
- Common in older LangChain versions and schema-first pipelines.

**When to use:**
- You want explicit named fields with descriptions.
- You are working with schema-based prompt generation.

**Example:**
```python
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema

schemas = [
    ResponseSchema(name="title", description="Title of the article"),
    ResponseSchema(name="summary", description="Short summary")
]
parser = StructuredOutputParser.from_response_schemas(schemas)

prompt = (
    "Write a JSON object containing title and summary.\n"
    "{format_instructions}"
)
final_prompt = prompt.format(format_instructions=parser.get_format_instructions())

# response = model.invoke(final_prompt)
# parsed = parser.parse(response.content)
# print(parsed)
```

### 4. String / Custom Parsers
- `stroutputparser.py` and `stroutputparser1.py` show how to craft custom parser logic.
- Useful for free-form or non-JSON outputs.
- This is the most flexible option when the output is not easily aliasable into a schema.

## 🧠 Design Notes for This README
This file is structured for readability:
- Clear section headings for each parser type
- Practical examples with copy/paste-ready code
- Simple explanations for when to use each parser
- A final file list for quick navigation

## 📁 Files in this folder
- `PydanticOutputParser.py` — End-to-end example using Pydantic models and prompt injection.
- `JsonOutputParser.py` — Demonstrates valid JSON extraction and dict parsing.
- `StructuredOutputParser.py.py` — Schema-based output parsing using `ResponseSchema`.
- `JsonOutputParser.py` / `PydanticOutputParser.py` / `StructuredOutputParser.py.py` — Core examples of structured data extraction from raw text.
- `stroutputparser.py` / `stroutputparser1.py` — Custom parsing experiments for flexible output formats.

## 🚀 Quick Start
1. Read the parser type that matches your output format.
2. Use `get_format_instructions()` to inject parser guidance into the prompt.
3. Call `parser.parse()` on the raw model text.
4. Use the parsed result in your application.
