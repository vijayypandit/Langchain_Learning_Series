
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv(override=True)

#_______________________# Define Prompts

model1=ChatGroq(model="llama-3.1-8b-instant")

model2 = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


prompt1 = PromptTemplate(
    template = 'Generate short and simple note from following text \n {text}',
    input_variables = ['text']
)

prompt2 = PromptTemplate(
    template = 'Generate 5 short Questin and Answer from following text \n {text}',
    input_variables = ['text']
)

prompt3 = PromptTemplate(
    template = 'Merge the provided notes and quiz into a single document \n   notes -> {notes}  and quiz {quiz}',
    input_variables = ['notes','quiz']
)

parser = StrOutputParser()

#_______________________# Run the chains in parallel 

parallel_chain = RunnableParallel({
    'notes' : prompt1 | model1 | parser,
    'quiz' : prompt2 | model2 | parser
})

merged_chain = prompt3 | model1 | parser

chain = parallel_chain | merged_chain

text  = """
Vector machine is a supervised learning algorithm which can be used for both classification and regression problems. It is based on the concept of finding a hyperplane that best divides a dataset into classes. The main idea is to maximize the margin between the data points of different classes, which helps in improving the generalization ability of the model. Support Vector Machines (SVM) can be used for linear and non-linear classification tasks by using different kernel functions.
It is effective in high-dimensional spaces and is also memory efficient as it uses a subset of training points in the decision function (called support vectors). SVMs are widely used in various applications such as image classification, text categorization, and bioinformatics.
More importantly, SVMs are robust to overfitting, especially in high-dimensional space, making them a popular choice for many machine learning tasks.
"""

result = chain.invoke(text)

print(result)

#Visualize the chain 
chain.get_graph().print_ascii()