# String Parser with LLM Chain Demo - Advanced chaining with output parsing
# Purpose: Create pipeline chains combining prompts, models, and parsers
# Uses: Pipe operator (|) to chain PromptTemplate → Model → Parser → PromptTemplate
# Example: Generate detailed report, parse output, then summarize it

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
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
    template='Summarize the following report in 3 lines: /n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

#Pipeline chaining of entire flow

chain = template1 | model | parser | template2 | model | parser
result =  chain.invoke({'topic':'Blackhole'})

print(result)