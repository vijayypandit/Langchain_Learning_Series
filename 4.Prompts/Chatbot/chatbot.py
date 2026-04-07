# Multi-turn Chatbot Demo - Interactive conversational AI with chat history
# Purpose: Demonstrate persistent conversation with message history management
# Uses: ChatGroq/Gemini with SystemMessage, HumanMessage, and AIMessage types
# Features: Real-time conversation loop with continuous context

from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage , AIMessage

from dotenv import load_dotenv
load_dotenv(override=True)
import os

chat_history = [
    SystemMessage(content="You are a helpful assistant.")
]

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
model=ChatGroq(model="llama-3.1-8b-instant")
# model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

while True:
    user_input = input("You : ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)  
    chat_history.append(AIMessage(content=result.content))
    print("AI : " ,result.content)