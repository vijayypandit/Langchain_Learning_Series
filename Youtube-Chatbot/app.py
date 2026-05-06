"""
YouTube Video Chat Application
A beautiful Streamlit app for analyzing YouTube videos using RAG and LLM.
"""

import streamlit as st
from dotenv import load_dotenv
from rag_utils import (
    extract_video_id,
    fetch_youtube_transcript,
    create_chunks,
    create_vector_store,
    create_retriever,
    create_rag_chain,
    answer_question
)

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Video Assistant",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful UI
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    .stApp {
        background: radial-gradient(circle at top left, rgba(99, 102, 241, 0.18), transparent 22%),
                    radial-gradient(circle at bottom right, rgba(16, 185, 129, 0.14), transparent 18%),
                    linear-gradient(180deg, #060a14 0%, #0e1724 100%);
        color: #f8fafc;
        font-family: Inter, system-ui, sans-serif;
    }

    .header-container {
        background: rgba(15, 23, 42, 0.86);
        border: 1px solid rgba(148, 163, 184, 0.12);
        backdrop-filter: blur(22px);
        padding: 2rem 1.5rem;
        border-radius: 28px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 24px 80px rgba(15, 23, 42, 0.4);
    }

    .header-container h1 {
        color: #eff6ff;
        font-size: 2.6rem;
        font-weight: 800;
        margin-bottom: 0.4rem;
        letter-spacing: -0.04em;
    }

    .header-container p {
        color: #cbd5e1;
        font-size: 1.05rem;
        max-width: 720px;
        margin: 0 auto;
    }

    .input-section,
    .chat-section,
    .stSidebar {
        background: rgba(15, 23, 42, 0.82);
        border: 1px solid rgba(148, 163, 184, 0.14);
        backdrop-filter: blur(20px);
        border-radius: 28px;
        box-shadow: 0 30px 90px rgba(15, 23, 42, 0.4);
    }

    .input-section {
        padding: 2rem;
        margin-bottom: 2rem;
    }

    .chat-section {
        padding: 2rem;
        margin-top: 1rem;
        min-height: 260px;
    }

    .chat-section h3 {
        margin-bottom: 1.2rem;
        color: #f8fafc;
    }

    .user-message,
    .bot-message {
        display: inline-block;
        max-width: 88%;
        border-radius: 24px;
        padding: 1rem 1.3rem;
        margin-bottom: 1rem;
        line-height: 1.8;
        position: relative;
        box-shadow: 0 24px 60px rgba(15, 23, 42, 0.28);
        border: 1px solid rgba(148, 163, 184, 0.12);
        font-size: 0.96rem;
    }

    .user-message {
        background: linear-gradient(135deg, rgba(79, 70, 229, 0.95), rgba(59, 130, 246, 0.95));
        color: #f8fafc;
        margin-left: auto;
        text-align: right;
    }

    .bot-message {
        background: rgba(255, 255, 255, 0.06);
        color: #e2e8f0;
        margin-right: auto;
        text-align: left;
    }

    .message-label {
        display: block;
        margin-bottom: 0.55rem;
        color: rgba(226, 232, 240, 0.8);
        font-size: 0.78rem;
        letter-spacing: 0.02em;
    }

    .status-success,
    .status-error,
    .status-info {
        padding: 1rem 1.2rem;
        border-radius: 18px;
        margin-bottom: 1rem;
        font-size: 0.98rem;
        color: #e2e8f0;
        box-shadow: 0 20px 55px rgba(15, 23, 42, 0.2);
    }

    .status-success {
        background: rgba(16, 185, 129, 0.12);
        border-left: 4px solid #22c55e;
    }

    .status-error {
        background: rgba(239, 68, 68, 0.12);
        border-left: 4px solid #f97316;
    }

    .status-info {
        background: rgba(59, 130, 246, 0.14);
        border-left: 4px solid #3b82f6;
    }

    .stButton>button {
        border-radius: 16px !important;
        background: linear-gradient(135deg, #7c3aed 0%, #2563eb 100%) !important;
        color: #f8fafc !important;
        border: none !important;
        padding: 1rem 1.5rem !important;
        font-weight: 700 !important;
        box-shadow: 0 22px 60px rgba(79, 70, 229, 0.24) !important;
    }

    .stTextInput>div>div>input,
    .stTextArea>div>div>textarea {
        border-radius: 16px !important;
        border: 1px solid rgba(148, 163, 184, 0.16) !important;
        background: rgba(15, 23, 42, 0.9) !important;
        color: #e2e8f0 !important;
        padding: 1rem 1rem !important;
        box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.03);
    }

    .stTextInput>div>div>input::placeholder,
    .stTextArea>div>div>textarea::placeholder {
        color: rgba(226, 232, 240, 0.6) !important;
    }

    .stTextInput>div>div>input:focus,
    .stTextArea>div>div>textarea:focus {
        border-color: rgba(59, 130, 246, 0.6) !important;
        box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.12) !important;
    }

    .sidebar-title {
        color: #a5b4fc;
        font-size: 1.15rem;
        font-weight: 700;
        margin-top: 1rem;
        margin-bottom: 0.6rem;
    }

    .stSidebar .block-container {
        padding-top: 1.5rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .st-bq {
        background: rgba(255,255,255,0.08);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "chain" not in st.session_state:
    st.session_state.chain = None
    st.session_state.video_id = None
    st.session_state.chat_history = []
    st.session_state.transcript = None

# Header
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div class="header-container">
        <h1>🎥 AI Video Assistant</h1>
        <p>Ask questions about any YouTube video using AI</p>
    </div>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### ⚙️ Configuration")
    
    chunk_size = st.slider(
        "Chunk Size",
        min_value=300,
        max_value=1000,
        value=500,
        step=100,
        help="Size of text chunks for processing"
    )
    
    chunk_overlap = st.slider(
        "Chunk Overlap",
        min_value=50,
        max_value=300,
        value=100,
        step=50,
        help="Overlap between chunks for context preservation"
    )
    
    k_retrieval = st.slider(
        "Top K Results",
        min_value=1,
        max_value=10,
        value=4,
        help="Number of context chunks to retrieve"
    )
    
    max_chunks = st.slider(
        "Max Chunks to Index",
        min_value=20,
        max_value=200,
        value=70,
        help="Maximum chunks to keep (limit API calls)"
    )
    
    st.markdown("---")
    st.markdown("### 📚 About")
    st.info(
        """
        This app uses:
        - YouTube Transcript API
        - LangChain for RAG
        - Google Gemini for embeddings & responses
        - FAISS for vector search
        """
    )

# Main content
col1, col2 = st.columns([3, 1])

with col1:
    youtube_input = st.text_input(
        "Enter YouTube URL or YouTube Video ID",
        placeholder="https://www.youtube.com/watch?v=...",
        label_visibility="collapsed"
    )

with col2:
    process_button = st.button(
        "🚀 Process",
        use_container_width=True,
        key="process_btn"
    )

# Process YouTube video
if process_button and youtube_input:
    status_box = st.empty()
    progress_bar = st.progress(0)
    status_box.markdown("### 🔄 Starting processing...")

    try:
        # Extract video ID
        st.session_state.video_id = extract_video_id(youtube_input)
        status_box.info("🔗 Parsing YouTube URL...")

        # Fetch transcript
        status_box.info("📥 Fetching transcript...")
        st.session_state.transcript = fetch_youtube_transcript(st.session_state.video_id)
        progress_bar.progress(20)
        status_box.success("✅ Transcript fetched")

        # Create chunks
        status_box.info("✂️ Splitting transcript into chunks...")
        chunks = create_chunks(
            st.session_state.transcript,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        progress_bar.progress(45)
        status_box.success(f"✅ Created {len(chunks)} chunks")

        # Create vector store
        status_box.info("🔍 Generating embeddings and building vector index...")
        vectorstore = create_vector_store(chunks, max_chunks=max_chunks)
        progress_bar.progress(70)
        status_box.info("🔎 Creating retriever...")
        retriever = create_retriever(vectorstore, k=k_retrieval)
        progress_bar.progress(85)
        status_box.success("✅ Vector search ready")

        # Build chain
        status_box.info("🤖 Preparing the RAG chain...")
        st.session_state.chain = create_rag_chain(retriever)
        progress_bar.progress(100)

        # Success message
        status_box.markdown(f"""
            <div class=\"status-success\">
            <strong>✅ Success!</strong> Youtube video processed with {len(chunks)} chunks. Ready to chat!
            </div>
            """,
            unsafe_allow_html=True
        )
        st.session_state.chat_history = []

    except ValueError as e:
        progress_bar.progress(0)
        status_box.markdown(f"""
            <div class=\"status-error\">
            <strong>❌ Error:</strong> {str(e)}
            </div>
            """,
            unsafe_allow_html=True
        )
    except Exception as e:
        progress_bar.progress(0)
        status_box.markdown(f"""
            <div class=\"status-error\">
            <strong>❌ Error:</strong> {str(e)}
            </div>
            """,
            unsafe_allow_html=True
        )

# Chat section
if st.session_state.chain is not None:
    st.markdown("### 💬 Chat with Youtube Video")

    if not st.session_state.chat_history:
        st.markdown("""
        <div class="status-info">
        <strong>✨ Ready to chat:</strong> Ask the first question about the video below.
        </div>
        """, unsafe_allow_html=True)

    # Display chat history
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f"""
            <div class="user-message">
            <span class="message-label">You</span>
            {message["content"]}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="bot-message">
            <span class="message-label">AI Assistant</span>
            {message["content"]}
            </div>
            """, unsafe_allow_html=True)

    # Input for new question
    with st.form(key="chat_form", clear_on_submit=True):
        input_col, button_col = st.columns([8, 1])
        user_question = input_col.text_input(
            "Ask a question about the video",
            placeholder="Ask something about this video...",
            label_visibility="collapsed",
            key="chat_input"
        )
        submit_chat = button_col.form_submit_button("Send")

    if submit_chat and user_question:
        # Add user message to history
        st.session_state.chat_history.append({
            "role": "user",
            "content": user_question
        })

        # Get response
        with st.spinner("🤔 Thinking..."):
            response = answer_question(st.session_state.chain, user_question)

        # Add bot message to history
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": response
        })

        # Force rerun to show new messages
        st.rerun()

    # Clear chat button
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

else:
    st.markdown("""
    <div class="status-info">
    <strong>📋 Getting Started:</strong> Enter a YouTube URL or video ID above to start analyzing!
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.9rem;'>
    <p>Built with ❤️ using Streamlit, LangChain, and Google Gemini</p>
    <p>© 2024 AI Video Assistant</p>
</div>
""", unsafe_allow_html=True)
