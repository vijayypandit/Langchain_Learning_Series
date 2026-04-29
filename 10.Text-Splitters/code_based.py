from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_Details(self)
        return self.name"

#Example usage
student1 = Student("Alice", 20)
print(student1.get_Details())

if(student1.age > 18):
    print("Student is an adult.")
else:
    print("Student is a minor.")
"""

#Initializing the RecursiveCharacterTextSplitter with a chunk size of 100 characters and an overlap of 20 characters

text_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,chunk_size=300, chunk_overlap=0)

#Splitting the text into chunks
chunks = text_splitter.split_text(text)
#Printing the resulting chunks
print(chunks[1])
# print(len(chunks)) 