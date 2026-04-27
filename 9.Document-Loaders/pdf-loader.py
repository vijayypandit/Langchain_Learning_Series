from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv(override=True)

loader = PyPDFLoader("Resume_2025.pdf")
docs = loader.load()
print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)

#model initialization
model=ChatGroq(model="llama-3.1-8b-instant")