# RAG Utility Functions for YouTube Video Analysis

import re
from typing import List
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough, RunnableParallel


# Extract video ID from YouTube URL or validate if already a video ID
def extract_video_id(youtube_url: str) -> str:
    if len(youtube_url) == 11 and youtube_url.isalnum():
        return youtube_url
    
    patterns = [
        r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=([a-zA-Z0-9_-]{11})',
        r'(?:https?://)?(?:www\.)?youtu\.be/([a-zA-Z0-9_-]{11})',
        r'(?:https?://)?(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]{11})',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, youtube_url)
        if match:
            return match.group(1)
    
    raise ValueError("Invalid YouTube URL or video ID")


# Fetch transcript from YouTube using video ID
def fetch_youtube_transcript(video_id: str) -> str:
    try:
        ytt_api = YouTubeTranscriptApi()
        transcript_list = ytt_api.fetch(video_id, languages=['en'])
        transcript = " ".join(
            getattr(chunk, 'text', chunk.get('text')) if hasattr(chunk, 'get') else getattr(chunk, 'text')
            for chunk in transcript_list
        )
        return transcript
    except TranscriptsDisabled:
        raise Exception("Transcript is disabled for this video")
    except NoTranscriptFound:
        raise Exception("No transcript found for this video")


# Split transcript into chunks with configurable size and overlap
def create_chunks(transcript: str, chunk_size: int = 500, chunk_overlap: int = 100) -> List:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = splitter.create_documents([transcript])
    return chunks


# Create FAISS vector store with Google Gemini embeddings
def create_vector_store(chunks: List, max_chunks: int = 70):
    if len(chunks) > max_chunks:
        chunks = chunks[:max_chunks]
    
    embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")
    vectorstore = FAISS.from_documents(chunks, embedding)
    return vectorstore


# Create similarity-based retriever from vector store
def create_retriever(vectorstore, k: int = 4):
    return vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k}
    )


# Build RAG chain: retriever + prompt + LLM + parser
def create_rag_chain(retriever):
    prompt = PromptTemplate(
        template="""You are a helpful assistant analyzing YouTube video transcripts.
        
Answer ONLY from the provided transcript context. If the context is insufficient to answer the question, say you don't know.

Context:
{context}

Question: {question}

Answer:""",
        input_variables=["context", "question"]
    )
    
    # llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    llm = ChatGroq(model="llama-3.1-8b-instant")

    parser = StrOutputParser()
    
    def format_docs(retrieved_docs):
        return "\n\n".join(doc.page_content for doc in retrieved_docs)
    
    parallel_chain = RunnableParallel({
        "context": retriever | RunnableLambda(format_docs),
        "question": RunnablePassthrough()
    })
    
    chain = parallel_chain | prompt | llm | parser
    
    return chain


# Invoke RAG chain to generate answer for user question
def answer_question(chain, question: str) -> str:
    try:
        answer = chain.invoke(question)
        return answer
    except Exception as e:
        return f"Error generating answer: {str(e)}"
