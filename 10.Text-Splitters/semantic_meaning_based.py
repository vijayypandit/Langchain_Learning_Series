from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings

from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(override=True)
embedding = OpenAIEmbeddings()

model = ChatGroq(
    model="llama-3.1-8b-instant")

text_splitter = SemanticChunker(
    embedding,
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=3
)

sample = """
Tourism in Nepal is a significant contributor to the country's economy, attracting millions of visitors each year. The diverse landscapes, rich cultural heritage, and unique biodiversity make Nepal a popular destination for travelers from around the world. The tourism industry in Nepal encompasses various activities, including trekking, mountaineering, cultural tours, wildlife safaris, and adventure sports. The iconic Himalayan mountain range, including Mount Everest, draws mountaineers and trekkers seeking to experience the breathtaking beauty of the region. Additionally, Nepal's vibrant culture, ancient temples, and festivals provide a rich tapestry of experiences for tourists. The government of Nepal has been actively promoting sustainable tourism practices to preserve the natural environment and cultural heritage while fostering economic growth through tourism.
"""
docs = text_splitter.create_documents([sample])
print(docs)