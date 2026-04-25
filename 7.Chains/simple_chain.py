
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv(override=True)
model=ChatGroq(model="llama-3.1-8b-instant")

prompt = PromptTemplate(
    template = 'Generate 2 interesting facts about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

#Using Chaining to connect the prompt, model and parser together
chain = prompt | model | parser
result = chain.invoke({'topic':'Spaceship'})

print(result)

#Visuallize the Chain Steps ---------------------
chain.get_graph().print_ascii()

