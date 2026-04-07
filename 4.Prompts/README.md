# 4. Prompts & Prompt Templates

Prompts are the instructions we give to an LLM. In real-world applications, you rarely send raw text. Instead, you use **Prompt Templates** to build dynamic prompts that can change based on user input.

### Definition
A `PromptTemplate` is a reproducible way to generate a prompt. It contains a text string with placeholders (variables) that are filled at runtime.

### Key Features
- **Variables:** Use `{variable_name}` syntax to define placeholders.
- **Reusability:** Save templates to JSON files and load them later.
- **Validation:** Ensures all required variables are provided.

### Example
```python
from langchain_core.prompts import PromptTemplate

# Define the template
template = PromptTemplate(
    template="Explain {topic} in a {style} way.",
    input_variables=["topic", "style"]
)

# Format the prompt
prompt = template.format(topic="Quantum Physics", style="poetic")
print(prompt)
```

### Advanced Usage: Saving Templates
You can save your templates to avoid hardcoding long strings in your Python files:
```python
template.save("my_template.json")
```

---
**Files in this folder:**
- `prompt_generator.py`: Demonstrates creating and saving a complex research paper summarization template.
- `prompt_ui.py`: Likely an implementation of these prompts in a UI context (e.g., Streamlit).
