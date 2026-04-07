# Research Assistant UI - Streamlit interface for research paper analysis
# Purpose: Create interactive UI for analyzing research papers with dynamic prompts
# Uses: Streamlit for UI, ChatGroq/Gemini for analysis, PromptTemplate for formatting
# Features: Select paper, explanation style, and summarization length

from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate,load_prompt

import streamlit as st

from dotenv import load_dotenv
load_dotenv(override=True)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview")
# os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
model=ChatGroq(model="llama-3.1-8b-instant")

st.header("Your Research Assistant ")

paper_input = st.selectbox("Select a research Paper to analyze",["Attention is all you need to know","BERT: pre training of Deep Bidirectional Transformers","GPT-3:Language Models are Few-Shot Learners", "Diffusion models Beat GANs on Image Sysnthesis"])

style_input = st.selectbox("Select Explanation Style ",["Beginner-Friendly","Technical","Analogy-based","Mathematical","Code-Oriented"])

length_input = st.selectbox("Select Explanation Length ",["Short","Medium","Long"])

template=load_prompt("template.json")
#Fill the placeholders.

prompt = template.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input
})

if st.button("Summarize"):
        result=model.invoke(prompt)
        st.write(result.content)
             