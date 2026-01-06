# 🤖 Simple Chatbot with Memory

My first GenAI project - a CLI chatbot using Groq's Llama 3.1 model.

## Features

✅ Conversation memory (remembers context)  
✅ Fast responses (Groq's inference)  
✅ Free to run (no API costs)  
✅ Clean code (easy to understand)

## Tech Stack

- **Python 3.11+**
- **Groq API** (Llama 3.1 70B)
- **python-dotenv** (environment management)

## Installation
```bash
pip install -r requirements.txt
```

Add your Groq API key to `.env`:
```
GROQ_API_KEY=your-key-here
```

## Usage
```bash
python chatbot.py
```

## What I Learned

- How to use chat completion APIs
- Managing conversation history
- API key security with .env files
- Basic prompt engineering

## Next Steps

- Add web interface with Streamlit
- Support multiple LLM providers
- Add conversation export feature

---

**Date:** January 6, 2026  
**Part of:** IIT Patna GenAI Journey
