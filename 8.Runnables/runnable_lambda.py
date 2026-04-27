from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel ,RunnablePassthrough, RunnableLambda

load_dotenv(override=True)

def word_count(text):
    return len(text.split())

#model initialization
model=ChatGroq(model="llama-3.1-8b-instant")
#_______________________# Define Prompts
prompt1 = PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic']

)
#_______________________# Define Output Parser
parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt1,model,parser)

# RunnableParallel to run joke generation and word count in parallel
parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "word_count": RunnableLambda(word_count)
})

# Combine the joke generation and word count into a final chain
final_chain = RunnableSequence(joke_gen_chain, parallel_chain)
result = final_chain.invoke({'topic':'AI ML'})

# Format the final output
final_result = """{} \n word count: {}""".format(result['joke'], result['word_count'])
print(final_result)

