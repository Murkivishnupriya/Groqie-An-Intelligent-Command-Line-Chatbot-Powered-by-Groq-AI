# 🤖 Groqie – A Fast and Intelligent Command-Line Chatbot

**Groqie** is a smart and interactive chatbot built in **Python** for the **command line**.  
It provides quick, natural, and context-aware replies powered by **Groq’s LLaMA 3.1 AI model**.  
Groqie remembers recent chats, answers instantly, and even knows who created it!

---

## 🚀 Features

- ⚡ **Ultra-fast responses** powered by Groq’s LPU technology  
- 💬 **Interactive CLI chatbot** built fully in Python  
- 🧠 **Short-term memory** that remembers the last few user turns  
- 🧩 **Modular design** — simple, clean, and easy to extend  
- 💡 **Custom rule**: replies “My creator is Vishnupriya M.” when asked about its creator  
- ✅ Lightweight — runs locally, no GPU needed  

---

## 🧩 Project Structure
chatbot-cli/
│
├── .env # Stores your Groq API key
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── src/
├── main.py # Entry point – loads and runs the chatbot
├── interface.py # Main chatbot logic
├── chat_memory.py # Conversation memory manager
└── model_loader.py # Handles AI model loading (Groq)


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
git clone https://github.com/<vishnupriya murki>/groqie.git
cd groqie

## Create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts\activate

## Install dependencies
pip install -r requirements.txt

## Add your Groq API key

Create a .env file in the project root:

GROQ_API_KEY=gsk_your_groq_api_key_here



## Run the chatbot:
python -m src


Example interaction:
Local CLI Chatbot (Groq Llama 3). Type /exit to quit.

User: hi
Bot: Hello! How can I help you today?

User: who is your creator
Bot: My creator is Vishnupriya M.

User: what is the capital of India
Bot: The capital of India is New Delhi.

User: /exit
Exiting chatbot. Goodbye!


## How It Works

Groqie loads the API key, initializes the Groq LLaMA 3.1 model, and starts a conversation loop in the terminal.
It keeps a short-term chat history for context and adds a custom rule for “Who is your creator?”.
The design is modular and clean, making it easy to maintain or upgrade with more features later.


## Why Groq API Instead of Hugging Face

We initially tested Hugging Face models like Flan-T5 and DialoGPT, but they were slow and often repetitive when run locally.
Groq’s LLaMA 3.1 model solved both problems by providing:

Speed: Replies in under a second using Groq’s LPUs.

Accuracy: Factual and natural answers, similar to GPT-3.5.

Simplicity: No GPU setup needed — just an API key.

Free Access: Ideal for student or demo projects.



## Requirements

groq==0.9.0
python-dotenv==1.0.1
transformers==4.46.3
torch==2.4.1
accelerate==1.0.1


Developed by: Vishnupriya M
Built with:  Python + Groq AI
Project Name: Groqie — “An Intelligent Command Line Chatbot”

