
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
# from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema
from pydantic import BaseModel, Field

load_dotenv(override=True)
model=ChatGroq(model="llama-3.1-8b-instant")

class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(gt=18,description="Age of the person")
    city: str = Field(description="City of the person")
    

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template = 'Generate name,age and city of fictional {place}  person {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt = template.invoke({'place':'Nepal'})
result = model.invoke(prompt)
final_result = parser.parse(result.content)
print(final_result)
