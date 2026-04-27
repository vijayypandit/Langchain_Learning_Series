from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

# Load all .txt files in the specified directory
loader = DirectoryLoader(
    path='9.Document-Loaders/books',
    glob='*.pdf',
    loader_cls=PyPDFLoader

)
# docs = loader.load()
# print(len(docs))

# print(docs[2].page_content)  # Print the first 500 characters of the first document
# print(docs[0].metadata)  # Print the metadata of the first document

#lazy loading and load 

docs = loader.lazy_load()  # This will return a generator
for doc in docs:
    print(doc.metadata)

