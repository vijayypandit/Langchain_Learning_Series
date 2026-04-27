from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, WebBaseLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv(override=True)

#model initialization
model=ChatGroq(model="llama-3.1-8b-instant")

url ='https://www.myntra.com/watches/titan/titan-karishma-quartz-analog-with-champagne-dial-watch-for-women---nm2594ym01/10832040/buy';
loader = WebBaseLoader(url)

prompt = PromptTemplate(
    template = 'Answer the following question \n {question}  from the following text \n {text}',
    input_variables = ['question', 'text']
)
parser = StrOutputParser()

docs = loader.load()

chain = prompt | model | parser
result = chain.invoke({'question': 'What is the product we are talking about ?', 'text': docs[0].page_content})