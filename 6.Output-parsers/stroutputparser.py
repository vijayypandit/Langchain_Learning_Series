# String Output Parser Demo - Extract and parse string responses from LLMs
# Purpose: Generate detailed reports and summaries using prompt chaining
# Uses: StrOutputParser to convert LLM output to plain text
# Example: Two-step process (detailed report → summary)

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os

load_dotenv(override=True)
model=ChatGroq(model="llama-3.1-8b-instant")
#1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on the following topic: {topic}',
    input_variables=['topic']
)


#2nd prompt -> summary
template2 = PromptTemplate(
    template='Summarize the following report in 5 lines: /n {text}',
    input_variables=['text']
)


prompt1 = template1.invoke({"topic":"Blackhole"})
result = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result.content})

result1 = model.invoke(prompt2)

print(result1)