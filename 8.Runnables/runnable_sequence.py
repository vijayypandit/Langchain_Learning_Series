#RunnableSequence allows you to chain together multiple runnables, where the output of one runnable can be used as the input for the next. This is useful for creating complex workflows that involve multiple steps.

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv(override=True)

#_______________________# Define Prompts

model=ChatGroq(model="llama-3.1-8b-instant")

prompt = PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic']

)
#_______________________# Define Output Parser
parser = StrOutputParser()

prompt2 = PromptTemplate(
    template = 'Explain about the joke: {joke}',
    input_variables=['joke']
)
#_______________________# Chain Runnables 
# Here we create a RunnableSequence that consists of the first prompt, the model, the parser, the second prompt, the model again, and the parser again. The output of each step is passed as input to the next step in the sequence.
chain = RunnableSequence( prompt ,model, parser, prompt2 , model, parser)
print(chain.invoke({'topic':'AI'}))