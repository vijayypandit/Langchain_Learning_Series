from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="9.Document-Loaders/user_data.csv", encoding="utf-8")
documents = loader.load()    
print(len(documents))
print(documents[0])