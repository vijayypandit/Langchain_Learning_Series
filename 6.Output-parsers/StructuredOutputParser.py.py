
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema


load_dotenv(override=True)
model=ChatGroq(model="llama-3.1-8b-instant")

schema = [
    ResponseSchema(name='fact_1', description='fact 1 abouut the topic'),
    ResponseSchema(name='fact_2', description='fact 2 abouut the topic'),
    ResponseSchema(name='fact_3', description='fact 3 abouut the topic')

]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = 'Give three facts about the  {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instruction()}
)

prompt = template.invoke({'topic':'BlackHole'})
result = model.invoke(prompt)
final_result  = parser.parse(result.content)
print(final_result)

##Using chain - Same output ----
chain  = template | model | parser
result1 = chain.invoke({'topic':'BlackHole'})
print(result1)