from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv(override=True)

#_______________________# Define Prompts

model=ChatGroq(model="llama-3.1-8b-instant")

prompt1 = PromptTemplate(
    template='Generate a tweet about  {topic}',
    input_variables=['topic']

)
prompt2 = PromptTemplate(
    template='Generate a LinkedIn post about  {topic}',
    input_variables=['topic']

)
#parser to parse the output of the model into a string
parser = StrOutputParser()

#dictionary of runnables to run in parallel with the same input topic to generate a tweet and a linkedin post at the same time.
parallel_chain = RunnableParallel({
    "tweet": RunnableSequence(prompt1, model, parser),
    "linkedin": RunnableSequence(prompt2, model, parser)
})

result = parallel_chain.invoke({'topic':'AI'})
print(result['tweet'])
print(result['linkedin'])