# JSON Output Parser Demo - Extract structured JSON data from LLM responses
# Purpose: Parse LLM outputs into valid JSON format with defined schema
# Uses: JsonOutputParser to enforce structured output from unstructured LLMs
# Example: Extract person details (name, age, city) as JSON

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import os

load_dotenv(override=True)
model=ChatGroq(model="llama-3.1-8b-instant")

parser = JsonOutputParser()

template = PromptTemplate(
    template = 'Give me the name ,age,city of a fictional person  \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)
prompt = template.format()

print(prompt)

result = model.invoke(prompt)

final_result = parser.parse(result.content)
print(final_result)
print(final_result['name'])
print(type(final_result))
print("**********************************")
####Use chain to do now ...

chain = template | model | parser
result_chained = chain.invoke({})
print(result_chained)