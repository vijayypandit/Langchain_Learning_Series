# Document Similarity Demo - Find similar documents using embeddings and cosine similarity
# Purpose: Convert documents to embeddings and compute similarity with a query
# Uses: Google Gemini embeddings with scikit-learn cosine similarity
# Requires: GOOGLE_API_KEY in .env file

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
load_dotenv(override=True)
import numpy as np

#embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")   we can use this one as well
embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")


documents = [
    "Sachin Tendulkar is considered one of the greatest batsmen in cricket history.",
    "Sourav Ganguly was the captain of the Indian cricket team during the early 2000s.",
    "MS Dhoni is known for his finishing skills and leadership as captain.",
    "Rohit Sharma holds the record for the highest individual score in ODIs.",
    "Rahul Dravid was nicknamed 'The Wall' for his defensive batting technique."
]

query='Tell me about Sourav'

doc_embeddings=embedding.embed_documents(documents)
query_embedding=embedding.embed_query(query)

print("Cosine Similarity between query and documents:")

scores= cosine_similarity([query_embedding],doc_embeddings)[0]

index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]
print(query)

print(documents[index])
print("Similarity score is : ",score)