# Prompt Template Generator - Create reusable prompt templates with variables
# Purpose: Define structured prompts with input variables for paper summarization
# Uses: LangChain PromptTemplate to create flexible, parameterized prompts
# Saves template to JSON for reusability

from  langchain_core.prompts import PromptTemplate

#template
template = PromptTemplate(
    template="""
Please summarize the research paper "{paper_input}" with the following specifications:
Explanation Style: {style_input}
Explanation Length: {length_input}
1. Mathematical Details:
    - Include relevant mathematicla equatios if present in the paper.
    - Explain the mathematical cocepts using simple, intuitive code snippet where applicable.

2.Analogies:
    - Use relatable analogies to simplify complex ideas.
If ertain information is not available in the paper , respond with : "Insufficied infomation availale" instead of guessing or making assumptions.
Ensure the summary is clear , accurate, and aliged with the provided style and length.
""",
input_variables=["paper_input","style_input","length_input"],
validate_template=True
)

template.save("template.json")