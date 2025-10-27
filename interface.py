import os
from groq import Groq
from .chat_memory import SlidingWindowMemory

SYSTEM_INSTRUCTION = (
    "You are a polite and intelligent AI assistant. "
    "Answer questions clearly and accurately in one or two sentences."
)

def run_cli(model_name: str = "llama-3.1-8b-instant", max_turns: int = 4):
    """
    Command-line chatbot using Groq's ultra-fast LLaMA 3.1 model.
    """
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    memory = SlidingWindowMemory(max_turns=max_turns)

    print("Local CLI Chatbot (Groq Llama 3). Type /exit to quit.\n")

    while True:
        user = input("User: ").strip()
        if not user:
            continue
        if user.lower() == "/exit":
            print("Exiting chatbot. Goodbye!")
            break

        # 🔹 Static custom responses (no API call)
        creator_phrases = [
            "who is your creator",
            "who created you",
            "who made you",
            "who built you",
            "who developed you"
        ]
        if any(phrase in user.lower() for phrase in creator_phrases):
            bot_reply = "My creator is Vishnupriya M."
            print(f"Bot: {bot_reply}\n")
            memory.add_turn(user, bot_reply)
            continue

        # Build conversation context for Groq API
        messages = [{"role": "system", "content": SYSTEM_INSTRUCTION}]
        for speaker, msg in memory.get_history():
            role = "user" if speaker == "User" else "assistant"
            messages.append({"role": role, "content": msg})
        messages.append({"role": "user", "content": user})

        try:
            completion = client.chat.completions.create(
                model=model_name,
                messages=messages,
                temperature=0.5,
                max_tokens=200,
            )
            bot_reply = completion.choices[0].message.content.strip()

        except Exception as e:
            bot_reply = f"(Error: {e})"

        print(f"Bot: {bot_reply}\n")
        memory.add_turn(user, bot_reply)
