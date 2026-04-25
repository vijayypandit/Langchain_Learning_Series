
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv(override=True)
model=ChatGroq(model="llama-3.1-8b-instant")

prompt1 = PromptTemplate(
    template = 'Generate detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'Generate  5 point summary from \n: {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = prompt1 | model | prompt2 | model | parser
result =chain.invoke({'topic' : 'Climate Change'})
print(result)

#Visuallize the Chain Steps ---------------------
chain.get_graph().print_ascii()
