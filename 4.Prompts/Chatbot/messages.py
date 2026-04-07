# Message Types Demo - Understanding LangChain message structures
# Purpose: Show how to use different message types (System, Human, AI) for conversations
# Uses: SystemMessage, HumanMessage, AIMessage for structured dialogue
# Example: Simple multi-turn conversation pattern

from langchain_core.messages import SystemMessage, HumanMessage , AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv(override=True)

model = ChatGroq(model="llama-3.1-8b-instant")

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me about a story of villge of 90s ")
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)
