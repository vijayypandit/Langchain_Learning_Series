from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv(override=True)

#model initialization
model=ChatGroq(model="llama-3.1-8b-instant")
prompt = PromptTemplate(
    template = 'Write a summary for the folloowing poem \n {poem}',
    input_variables = ['poem']
)

parser = StrOutputParser()


loader = TextLoader("cricket_poem.txt", encoding="utf-8")
documents = loader.load()

print(documents[0].page_content )
print(documents[0].metadata)

chain = prompt | model | parser
result = chain.invoke({'poem' : documents[0].page_content})
print(result)

