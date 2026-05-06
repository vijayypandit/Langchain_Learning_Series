# 🚀 Quick Start Guide - YouTube Chatbot

Get the AI Video Assistant running in **5 minutes**!

## ⚡ One-Command Setup

### Windows
```bash
setup.bat
```

### macOS/Linux
```bash
bash setup.sh
```

---

## 📋 Manual Setup (5 Steps)

### Step 1: Get API Key (1 minute)

1. Open [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click **"Create API Key"**
3. Copy the generated key (long alphanumeric string)

### Step 2: Install Dependencies (2 minutes)

```bash
pip install -r requirements.txt
```

**First time?** This downloads ~500MB of libraries. ☕

### Step 3: Create `.env` File (30 seconds)

Create a file named `.env` in the project root:

```
GOOGLE_API_KEY=paste_your_key_here_without_quotes
```

**Example:**
```
GOOGLE_API_KEY=AIzaSyDxxxxxxxxxxxxxxxxxxx
```

### Step 4: Start the App (30 seconds)

```bash
streamlit run app.py
```

### Step 5: Use It! 🎉

- Browser opens automatically at `http://localhost:8501`
- Or manually visit: `http://localhost:8501`

---

## 💻 Platform-Specific Instructions

### Windows 11/10

```powershell
# Step 1: Navigate to project
cd path\to\Youtube-Chatbot

# Step 2: Create virtual environment
python -m venv venv
venv\Scripts\activate

# Step 3: Install packages
pip install -r requirements.txt

# Step 4: Create .env file
notepad .env
# Paste: GOOGLE_API_KEY=your_key_here

# Step 5: Run
streamlit run app.py
```

### macOS

```bash
# Step 1: Navigate to project
cd path/to/Youtube-Chatbot

# Step 2: Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Step 3: Install packages
pip install -r requirements.txt

# Step 4: Create .env file
nano .env
# Paste: GOOGLE_API_KEY=your_key_here
# Press Ctrl+X, then Y, then Enter

# Step 5: Run
streamlit run app.py
```

### Linux (Ubuntu/Debian)

```bash
# Step 1: Navigate to project
cd path/to/Youtube-Chatbot

# Step 2: Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Step 3: Install packages
pip install -r requirements.txt

# Step 4: Create .env file
nano .env
# Paste: GOOGLE_API_KEY=your_key_here

# Step 5: Run
streamlit run app.py
```

---

## 🎯 First Time Using

### Example 1: TED Talk
```
1. Paste: https://www.youtube.com/watch?v=dQw4w9WgXcQ
2. Click "🚀 Process"
3. Wait for processing (15-30 seconds)
4. Ask: "What is this video about?"
5. Get instant AI response! 🎉
```

### Example 2: Tutorial Video
```
1. Paste: dQw4w9WgXcQ (just the video ID)
2. Click "🚀 Process"
3. Ask: "Summarize the main points"
4. Get a concise summary
```

### Example 3: News Video
```
1. Paste: https://youtu.be/dQw4w9WgXcQ
2. Click "🚀 Process"
3. Ask: "Who are the speakers?"
4. Ask: "What happened?"
5. Ask: "What's the impact?"
```

---

## ❓ Common Questions

### Q: Where do I get the API key?
**A:** Visit [Google AI Studio](https://makersuite.google.com/app/apikey) and create a free key. No credit card needed!

### Q: Is it free?
**A:** Yes! Google offers free tier with generous limits. See [Pricing](https://ai.google.dev/pricing)

### Q: Do I need internet?
**A:** Yes, you need internet for YouTube API and Google AI services.

### Q: Can I use OpenAI?
**A:** Currently configured for Google Gemini. Can be modified in `rag_utils.py` for other providers.

### Q: How long does processing take?
**A:** Typically 15-30 seconds per video depending on length and your connection.

---

## 🆘 Troubleshooting

### "GOOGLE_API_KEY not found"

**Problem**: App won't start or API key error

**Solution**:
1. Check `.env` file exists in project root
2. File should contain: `GOOGLE_API_KEY=your_key_here`
3. Restart Streamlit: Stop and run `streamlit run app.py` again

```bash
# Verify .env exists
# Windows
dir .env

# Mac/Linux
ls -la .env
```

### "No module named streamlit"

**Problem**: `ModuleNotFoundError: No module named 'streamlit'`

**Solution**: Reinstall dependencies
```bash
pip install -r requirements.txt
```

### "Transcript not found"

**Problem**: Video exists but has no transcript

**Reasons**:
- Video owner disabled transcripts
- Video has no captions
- It's a livestream
- Video is very recent

**Solution**: Try a different video with captions

### "Rate limit exceeded (429 error)"

**Problem**: API error after few requests

**Solution**:
1. Reduce `Max Chunks to Index` to 50
2. Increase `Chunk Size` to 700-1000
3. Wait 5-10 minutes
4. Try again

### "Stuck on processing"

**Problem**: Video processing never completes

**Solution**:
1. Stop Streamlit: Press `Ctrl+C`
2. Check your internet connection
3. Try a shorter video first
4. Restart: `streamlit run app.py`

### "Slow performance"

**Problem**: App is sluggish

**Solution**:
1. Reduce `Max Chunks to Index` (set to 40)
2. Reduce `Chunk Size` (set to 400)
3. Close other applications
4. Check internet speed

---

## ⚙️ Configuration Quick Tips

**Sidebar Settings**:

| Setting | Speed ↑ | Quality ↑ |
|---------|---------|-----------|
| Chunk Size | 300 | 800 |
| Chunk Overlap | 50 | 200 |
| Top K Results | 2 | 8 |
| Max Chunks | 40 | 100 |

---

## 📝 Important Files

```
Youtube-Chatbot/
├── app.py              ← Main app (don't edit unless experienced)
├── rag_utils.py        ← Core logic (advanced customization here)
├── requirements.txt    ← Dependencies (shouldn't edit)
├── .env               ← YOUR API KEY (keep secret!)
└── README_APP.md      ← Full documentation
```

---

## 🎬 Try These Videos

Great starter videos to test:

1. **TED Talks**: Usually have captions ✓
2. **Tech Tutorials**: YouTube Channel tutorials ✓
3. **News Videos**: BBC, Reuters, etc. ✓
4. **Educational**: Khan Academy, MIT OpenCourseWare ✓
5. **Podcasts**: Uploaded as videos ✓

**Avoid**:
- ❌ Music videos (mostly captions)
- ❌ Gaming streams (no captions)
- ❌ Private videos (no access)
- ❌ Videos with disabled captions

---

## 💡 Pro Tips

1. **Copy Full Transcript**: Ask "What is the complete transcript?"
2. **Get Timestamps**: Ask "When is [topic] discussed?" 
3. **Multi-question**: Ask multiple questions in one - AI combines answers
4. **Adjust personality**: Edit `temperature` in `rag_utils.py` for different response styles
5. **Longer context**: Increase `Chunk Size` for technical videos

---

## 🚀 Next Steps

1. ✅ Setup complete
2. 🎥 Try processing a video
3. 💬 Ask questions
4. 📚 Read [README_APP.md](README_APP.md) for advanced features
5. 🔧 Customize settings in sidebar
6. 🎨 Edit `app.py` for custom styling (advanced)

---

## 📞 Need Help?

1. **Setup issues**: Check platform-specific instructions above
2. **API problems**: Verify key in [Google AI Studio](https://makersuite.google.com/app/apikey)
3. **Video issues**: Try different video
4. **Performance**: Adjust sidebar settings
5. **Full docs**: See [README_APP.md](README_APP.md)

---

**🎉 You're all set! Start chatting with videos! 🎉**

[← Back to README_APP.md](README_APP.md)

**Change Embedding Model:**
```python
# Line ~58 in create_vector_store()
embedding = GoogleGenerativeAIEmbeddings(model="embedding-001")
```

**Customize Prompt:**
```python
# Lines 70-80 in create_rag_chain()
template = """Your custom template here"""
```

---

## 📚 Resources

- [Streamlit Docs](https://docs.streamlit.io/)
- [LangChain Docs](https://python.langchain.com/)
- [Google Gemini API](https://ai.google.dev/)
- [FAISS Documentation](https://github.com/facebookresearch/faiss)

---

## 🎯 Next Steps

- ✅ Get API key
- ✅ Run setup script
- ✅ Test with your first video
- ✅ Customize colors in `app.py` (CSS section)
- ✅ Deploy on Streamlit Cloud

---

**Ready to chat with videos? Let's go! 🚀**
