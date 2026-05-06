# 🎥 AI Video Assistant - YouTube Chatbot

A beautiful, modern Streamlit application that lets you chat with YouTube videos using AI-powered RAG (Retrieval Augmented Generation). Ask questions about any YouTube video and get intelligent, context-aware answers based on the video's transcript.

## ✨ Key Features

- **🎬 YouTube Support**: Works with full URLs, shortened links, or just video IDs
- **🤖 Intelligent Q&A**: Uses advanced RAG to provide accurate answers from video content
- **🎨 Modern UI**: Beautiful gradient design with real-time chat interface
- **⚙️ Customizable Pipeline**: Adjust chunk size, retrieval parameters, and more
- **💬 Chat History**: Maintain full conversation history during session
- **⚡ Fast Processing**: Efficient text chunking and vector-based similarity search
- **🛡️ Error Handling**: Graceful error messages and helpful guidance
- **🔄 Real-time Status**: Visual progress indicators during video processing
- **🗑️ Session Management**: Clear chat history with one click

## 📋 Prerequisites

- Python 3.8 or higher
- Google API Key (free tier available)
- YouTube videos with transcripts enabled
- ~500MB disk space for dependencies

## 🚀 Installation & Setup

### Step 1: Navigate to Project Directory

```bash
cd Youtube-Chatbot
```

### Step 2: Create Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Setup API Keys

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API Key" and copy it
3. Create a `.env` file in the project directory:

```bash
# Windows
echo GOOGLE_API_KEY=your_api_key_here > .env

# macOS/Linux
echo "GOOGLE_API_KEY=your_api_key_here" > .env
```

Or manually create `.env` and add:
```
GOOGLE_API_KEY=your_api_key_here
```

### Step 5: Launch the Application

```bash
streamlit run app.py
```

The application will automatically open at `http://localhost:8501`

## 📖 How to Use the App

### Basic Workflow

1. **Paste YouTube Content**: Enter a YouTube URL or video ID
   - Full URL: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
   - Shortened: `https://youtu.be/dQw4w9WgXcQ`
   - Video ID only: `dQw4w9WgXcQ`

2. **Process Video**: Click the "🚀 Process" button
   - Wait for transcript fetching (~5-15 seconds)
   - Vector embeddings are generated
   - Chat becomes available

3. **Ask Questions**: Type any question about the video
   - "What are the main topics covered?"
   - "Summarize the key points"
   - "Who are the speakers?"
   - "What does [topic] mean in this video?"

4. **Get AI Responses**: Receive context-aware answers within seconds

5. **Continue Conversation**: Ask follow-up questions naturally

6. **Clear History**: Click "🗑️ Clear Chat History" to start fresh

## ⚙️ Advanced Configuration

Located in the **left sidebar**, customize these parameters:

| Setting | Range | Default | Impact |
|---------|-------|---------|--------|
| **Chunk Size** | 300-1000 | 500 | Larger = more context, fewer chunks |
| **Chunk Overlap** | 50-300 | 100 | Prevents losing context at boundaries |
| **Top K Results** | 1-10 | 4 | More chunks = richer but slower responses |
| **Max Chunks to Index** | 20-200 | 70 | Limits API usage & indexing time |

### Recommendations

- **Long videos (>2 hours)**: Use lower chunk size (300-400) and max chunks (50)
- **Technical content**: Higher chunk size (700-1000) for better context
- **Quick answers**: Lower K retrieval (2-3) for speed
- **Detailed answers**: Higher K retrieval (6-10) for comprehensiveness

## 📁 Project Structure

```
Youtube-Chatbot/
├── app.py                      # Main Streamlit web application
├── rag_utils.py               # RAG pipeline & utility functions
├── requirements.txt           # Python dependencies (pip install)
├── .env                       # API keys (create from .env.example)
├── .env.example              # Template for environment variables
├── README_APP.md             # This file - full documentation
├── QUICKSTART.md             # Quick setup guide
├── setup.sh                  # Linux/macOS setup script
├── setup.bat                 # Windows setup script
└── .gitignore               # Git ignore rules
```

## 🔧 File Descriptions

### `app.py` - Main Application
The Streamlit frontend with:
- **Header & Navigation**: Beautiful gradient header with app title
- **Sidebar Controls**: Video processing parameters and configuration
- **Chat Interface**: Real-time chat with message history
- **Video Processing**: Status updates and progress indicators
- **Custom Styling**: Modern CSS with dark mode, gradients, and animations
- **Session Management**: Persistent state during browser session

### `rag_utils.py` - RAG Pipeline Backend

Core functions for processing:

| Function | Purpose |
|----------|---------|
| `extract_video_id()` | Parse and validate YouTube URLs |
| `fetch_youtube_transcript()` | Fetch transcript from YouTube API |
| `create_chunks()` | Split transcript using recursive splitting |
| `create_vector_store()` | Generate embeddings and create FAISS index |
| `create_retriever()` | Setup similarity-based retriever |
| `create_rag_chain()` | Build complete RAG chain with LLM |
| `answer_question()` | Process questions and generate responses |

## 🔄 How the RAG Pipeline Works

```
YouTube Video
    ↓
Transcript Extraction (YouTube API)
    ↓
Text Chunking (Recursive splitting)
    ↓
Embedding Generation (Google Generative AI)
    ↓
Vector Store Creation (FAISS)
    ↓
User Question
    ↓
Semantic Similarity Search (Top K chunks)
    ↓
LLM Processing (Google Gemini)
    ↓
AI Response
```

### Processing Steps Explained

1. **Extraction**: Download transcript from YouTube
2. **Chunking**: Split into overlapping text chunks for context
3. **Embedding**: Convert each chunk to 768-dimensional vectors
4. **Indexing**: Store vectors in FAISS for fast retrieval
5. **Retrieval**: Find most relevant chunks for each question
6. **Augmentation**: Combine retrieved chunks with the question
7. **Generation**: LLM generates answer with full context

## 🎯 Example Questions

Try these to explore the app's capabilities:

- "What is the main topic of this video?"
- "Can you summarize the key points?"
- "Who are the speakers or presenters?"
- "What time does [topic] start?"
- "Explain [concept] mentioned in the video"
- "What are the takeaways from this video?"
- "Compare [item A] and [item B] from the video"
- "What's the background story?"

## 🐛 Troubleshooting

### "No module named streamlit"
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### "GOOGLE_API_KEY not found"
- Verify `.env` file exists in project root
- Check API key format is correct (long alphanumeric string)
- Run app from the project directory
- Restart the app after adding the key

### "Transcript not found"
- Video must have captions enabled
- Some videos disable transcripts intentionally
- Try a different video
- Check if it's a live stream (usually no transcript)

### "Rate limit exceeded"
- Reduce `Max Chunks to Index` (set to 50)
- Wait 5-10 minutes before trying again
- Switch to a different Google API key
- Use with free tier sparingly

### "API Error: 429"
- Too many requests to Google API
- Reduce chunk size and max chunks
- Increase delay between requests

### Long processing time
- Video is very long
- Network connection is slow
- Try reducing max chunks in settings
- Close other applications using bandwidth

## 💡 Performance Tips

1. **Faster Processing**: Lower max chunks (40-50) and chunk size (300)
2. **Better Answers**: Increase K retrieval (6-8) for more context
3. **API Optimization**: Use max chunks of 50-70 for long videos
4. **Cost Control**: Fewer chunks = fewer API calls = lower costs
5. **Memory**: Very large videos may need reduced chunk size

## 🔐 Security & Privacy

- ✅ API keys stored locally in `.env` (never committed)
- ✅ Transcripts processed locally, not stored
- ✅ Chat history kept only in session memory
- ✅ No data sent to third parties except Google API
- ✅ Always use HTTPS with Google services

**Important**: Never share your `.env` file or commit it to git!

## 📊 Supported Models

Currently using:
- **Embeddings**: `models/embedding-001` (Google)
- **LLM**: `gemini-pro` (Google Generative AI)
- **Vector Store**: FAISS (Facebook AI Similarity Search)

Can be extended to support OpenAI, Anthropic, and other providers.

## 🚀 Advanced Customization

### Change the LLM Model

Edit `rag_utils.py`, find `create_rag_chain()`:
```python
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",  # Change model here
    temperature=0.7           # Adjust creativity (0-1)
)
```

### Adjust Response Temperature

Lower = factual, Higher = creative:
```python
temperature=0.3  # More factual
temperature=0.7  # Balanced
temperature=0.9  # More creative
```

## 📚 Tech Stack

- **Framework**: Streamlit (web UI)
- **LLM**: Google Generative AI (Gemini)
- **Embeddings**: Google Generative AI embeddings
- **Vector Store**: FAISS (Facebook AI)
- **Text Processing**: LangChain, RecursiveCharacterTextSplitter
- **Transcripts**: YouTube Transcript API
- **UI Styling**: Custom CSS with gradients

## 📄 License

This project is open source and available for educational and personal use.

## 🤝 Contributing

Found a bug or have an idea? Feel free to report issues or suggest improvements!

## 📞 Support

For issues or questions:
1. Check the Troubleshooting section above
2. Review error messages carefully
3. Verify all API keys are set correctly
4. Try a different video to isolate the issue

## 🌟 Tips for Best Results

- Use videos with clear English audio
- Videos with professional captions work best
- Educational and talk videos work better than music
- Avoid very short videos (< 30 seconds)
- Long videos (> 4 hours) may need adjusted settings

---

**Built with ❤️ using Streamlit, LangChain, and Google Generative AI**

## ⚠️ Troubleshooting

### "Transcript is disabled for this video"
- Some videos have transcripts disabled by the creator
- Try a different video

### "No transcript found"
- The video might not have English captions
- Change language settings in `rag_utils.py`

### API Rate Limits
- Reduce `Max Chunks to Index` in the sidebar
- Reduce `Chunk Size` to process fewer tokens

### Slow Performance
- Decrease `Top K Results` to retrieve fewer chunks
- Reduce `Max Chunks to Index`

## 🛠️ Customization

### Change LLM Model
Edit `rag_utils.py` in `create_rag_chain()`:
```python
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")  # Change model
```

### Change Embedding Model
Edit `rag_utils.py` in `create_vector_store()`:
```python
embedding = GoogleGenerativeAIEmbeddings(model="embedding-001")
```

### Adjust Prompt Template
Edit `rag_utils.py` in `create_rag_chain()` to customize the system prompt.

## 📊 Supported Models

**Embeddings:**
- Google Gemini Embeddings (default)
- OpenAI Embeddings

**LLM:**
- Google Gemini 2.5 Flash (default)
- OpenAI GPT models
- Groq Llama

## 🎨 Design Features

- **Gradient Header**: Purple gradient with clear branding
- **Card-based Layout**: Clean white cards with shadows
- **Color-coded Messages**: Different colors for user/bot messages
- **Responsive Design**: Works on desktop and tablet
- **Status Indicators**: Success, error, and info messages with icons

## 📝 Notes

- The app caches the vector store in session state for faster follow-up queries
- Chat history is maintained during the session
- Maximum chunk limit prevents API exhaustion
- All processing happens locally after initial vector store creation

## 🔐 Security

- API keys are loaded from `.env` file (never commit this!)
- `.env` is in `.gitignore`
- No data is stored permanently
- Transcripts are processed locally

## 🚀 Deployment

To deploy on Streamlit Cloud:

1. Push code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your repo
4. Add secrets (GOOGLE_API_KEY, etc.) in app settings
5. Deploy!

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

---

**Built with ❤️ using Streamlit, LangChain, and Google Gemini**
