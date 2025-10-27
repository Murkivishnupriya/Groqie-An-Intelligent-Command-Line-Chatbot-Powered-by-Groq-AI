# 🧠 Local CLI Chatbot (Groq + Python)

This project is a **command-line AI chatbot** built using Python.  
It runs directly in your terminal, remembers short conversations, and gives quick, factual replies using **Groq’s LLaMA 3.1 model**.  

The bot is designed to feel smart and interactive — it remembers what you said recently, answers politely, and even knows who created it!  

---

## 🚀 Features

- 💬 **Chat directly in your terminal** – no browser or UI needed  
- 🧠 **Sliding-window memory** – remembers your last few messages for context  
- ⚡ **Super-fast replies** – powered by **Groq’s LLaMA 3.1 Instant model**  
- 🏗️ **Clean modular code** – easy to read, modify, and extend  
- 💡 **Custom static response** – always replies  
  > “My creator is Vishnupriya M.”  
  when you ask *“Who is your creator?”* or similar questions  
- ✅ **Smooth CLI experience** – type `/exit` anytime to quit gracefully  

---

## 🧩 Project Structure

chatbot-cli/
│
├── .env # Contains your Groq API key (not shared publicly)
├── requirements.txt # All Python dependencies
├── README.md # Project documentation
└── src/
├── main.py # Entry point – loads the environment and runs the chatbot
├── interface.py # Main chatbot logic and conversation flow
├── chat_memory.py # Memory module that stores recent conversation history
└── model_loader.py # Model loader (for Groq or Hugging Face models)



**Explanation:**  
- **`__main__.py`** starts the bot and ensures your API key is loaded properly.  
- **`interface.py`** runs the chat loop, checks for special keywords, calls the Groq model, and displays responses.  
- **`chat_memory.py`** helps the bot “remember” the last few interactions.  
- **`model_loader.py`** is built for flexibility — it can load other models if you want to extend the project later.  

---

## ⚙️ Installation & Setup

### Step 1: Clone or open the project

cd Desktop/chatbot-cli

### Step 2: Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

### Step 3: Install dependencies
pip install -r requirements.txt

### Step 4: Add your Groq API Key

Create a file named .env inside the project folder and add your key like this:
GROQ_API_KEY=gsk_your_groq_api_key_here






### How to Run the Chatbot

Run this command inside the terminal:

python -m src


### How It Works

The program starts with __main__.py, which loads your .env file and initializes the chatbot.

interface.py keeps reading user input in a loop.

If the message matches “who created you”, it gives a fixed local answer instantly.

Otherwise, it builds a conversation history and sends it to Groq’s LLaMA 3.1 model through their API.

The response is printed and stored in memory so the bot remembers context for the next turn.




## Why We Used Groq API Instead of Hugging Face

We originally tested Hugging Face models like Flan-T5 and DialoGPT,
but they had two main problems:

Slow and heavy – Running those models locally on a CPU took around 20–40 seconds for each reply.

Outdated or repetitive answers – Smaller models often produced incorrect or generic responses such as “Bot is the president of India.”

The Groq API solved both issues:

Speed: Groq’s hardware (LPUs) generates responses almost instantly — usually in under one second.

Accuracy: Their LLaMA 3.1 models are fine-tuned to deliver factual, natural responses similar to GPT-3.5.

Free and stable: Groq currently offers free usage with excellent uptime, making it ideal for academic or demo projects.

Simple integration: It connects easily through their official Python SDK and supports secure environment variable setup.



## Requirements

Install everything from the file below:

requirements.txt

groq
python-dotenv
transformers
torch
accelerate



## Design Highlights

Memory-based: remembers last few messages for continuity

Error-handling: shows helpful messages if the API key is missing or connection fails

Lightweight: runs easily on a normal laptop (no GPU required)

Custom logic: local rule for “creator” question

Expandable: can easily add more static facts or switch models




### Credits

Created by: Vishnupriya M.
Built with:  Python + Groq API
Goal: A fast, accurate, and lightweight chatbot that runs entirely from your terminal.
