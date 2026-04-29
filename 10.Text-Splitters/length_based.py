from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
# text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0,separator=' ')
# texts = text_splitter.split_text(text)
# print(texts)

loader = PyPDFLoader("10.Text-Splitters/learning-langchain.pdf")
documents = loader.load()
result = text_splitter.split_documents(documents)
print(result[2])