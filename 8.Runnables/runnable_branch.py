from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel ,RunnablePassthrough, RunnableLambda, RunnableBranch

load_dotenv(override=True)


#model initialization
model=ChatGroq(model="llama-3.1-8b-instant")

prompt1 = PromptTemplate(
    template = 'write a detailed report on the topic of {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template='summarize the following text \n: {text}',
    input_variables=['text']
)
# Define Output Parser
parser = StrOutputParser()
# Define the main chain to generate the report

# report_gen_chain = RunnableSequence(prompt1, model, parser)
# Alternatively, we can use the pipe operator to chain the runnables together
report_gen_chain = prompt1 | model | parser

# Define the branching logic to decide whether to summarize the report or not

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) >200 ,prompt2 | model | parser),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)
result = final_chain.invoke({'topic':'Russia vs Ukraine war'})
print(result)