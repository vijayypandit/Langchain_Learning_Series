# 4. Prompts & Chatbots in LangChain 💬

This module explores prompt engineering, prompt templates, and conversational AI design. It helps learners build reusable prompts and interactive chat experiences with LangChain.

## 🧠 What you'll learn
- How to create reusable `PromptTemplate`s.
- How to build a Streamlit UI from prompt templates.
- How chat messages and conversation history work.
- How to make chatbots more reliable with structured prompts.

## 📂 Folder Structure
```text
4.Prompts/
├── prompt_generator.py          # Generates and saves a PromptTemplate
├── prompt_ui.py                 # Streamlit UI consuming the saved template
├── README.md                    # This documentation file
└── Chatbot/                     # Conversational AI implementations
    ├── chatbot.py               # Interactive terminal chatbot with history
    ├── messages.py              # Demonstrates basic message types (System, Human, AI)
    ├── chat_prompt_template.ipynb # ChatPromptTemplate and history integration
    └── chat_history.txt         # Simple file-based chat history persistence
```

## 🎯 What this module builds
1. **Dynamic Prompting System** — a reusable `PromptTemplate` that can adapt to different topics and styles.
2. **Interactive UI** — a Streamlit interface for prompt-driven applications.
3. **Context-aware Chatbot** — a terminal chatbot that preserves conversation history and uses message roles correctly.

## 🛠️ Concepts you will master
### Prompt Templates
- Use templates to separate prompt logic from application code.
- Save and load templates so prompts can be reused without changing code.
- Inject variables like `topic`, `style`, and `instructions` dynamically.

### Chat Messages
- Structure conversations using `SystemMessage`, `HumanMessage`, and `AIMessage`.
- Use system messages to set tone, persona, and behavior.
- Keep chat history only when the conversation needs context.

### Chat Prompt Templates
- Build multi-turn prompts with `ChatPromptTemplate`.
- Inject previous chat history using `MessagesPlaceholder`.
- Use templates to control how the model sees the conversation.

### Interactive Chatbots
- Maintain a session-level history list.
- Append user input and model replies to the conversation.
- Use the full history for multi-turn understanding.

## 🚀 Quick Start
**1. Generate the prompt template:**
```bash
python 4.Prompts/prompt_generator.py
```

**2. Run the Streamlit UI:**
```bash
streamlit run 4.Prompts/prompt_ui.py
```

**3. Start the chatbot:**
```bash
python 4.Prompts/Chatbot/chatbot.py
```

## 💡 Learning tips
- Keep the prompt clear and explicit.
- Use the system role to tell the model how to behave.
- Save prompt templates so you can iterate quickly.
- Use history only when the conversation requires memory.

## 📁 Files in this folder
- `prompt_generator.py` — Build and save reusable prompt templates.
- `prompt_ui.py` — Streamlit UI for a prompt-driven app.
- `Chatbot/chatbot.py` — Terminal chatbot with message history.
- `Chatbot/messages.py` — Message role examples for chat models.
- `Chatbot/chat_prompt_template.ipynb` — Notebook demonstrating chat prompt templates.
- `Chatbot/chat_history.txt` — Simple saved conversation history sample.

---
**Why this matters**: Good prompt engineering and chat structure are the foundation of reliable AI applications.