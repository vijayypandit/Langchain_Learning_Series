from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel , RunnableBranch , RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv(override=True)

#_______________________# Define Prompts
# Define the model and parser
model=ChatGroq(model="llama-3.1-8b-instant")

parser = StrOutputParser()

# Define a Pydantic model for the output
class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="Give the sentiment of the feedback")

# Define a PydanticOutputParser with the Feedback model
parser2 = PydanticOutputParser(pydantic_object=Feedback)

# Define a prompt template that includes the format instructions from the parser
prompt1 = PromptTemplate(
    template = 'Classify the sentiment of the following feedback text into positive or negative \n {feedback}  \n {format_instructions}',
    input_variables = ['feedback'],
    partial_variables = {'format_instructions': parser2.get_format_instructions()}

)

#Chian the prompt, model and parser together
classifier_chain = prompt1 | model | parser2

#Invoke the chain with some feedback text  --Testing classifier chain...
# print(classifier_chain.invoke({'feedback':'This is terrible smartphone battery life'}).sentiment)

prompt2 = PromptTemplate(
    template = 'write an appropriate response to this positive feedback \ {feedback} ',
    input_variables = ['feedback']
)

prompt3= PromptTemplate(
    template = 'write an appropriate response to this negative feedback \ {feedback}',
    input_variables = ['feedback']
)
#_______________________# Define conditions and branches
# Define conditions
branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive',prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative',prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not find sentiment in the feedback")
)

chain = classifier_chain | branch_chain
print(chain.invoke({'feedback':'This is pathetic smartphone  having bad battery life'}))

#Visualize the chain 
chain.get_graph().print_ascii()