"""
Entry point for the local CLI chatbot.
Run using: python -m src
"""

import os
from dotenv import load_dotenv
from .interface import run_cli


def main():
    # 🔒 Load the API key securely from .env or environment variable
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        print("\n[ERROR] GROQ_API_KEY not found.")
        print("Please set your key using:")
        print('   export GROQ_API_KEY="gsk_your_key_here"\n')
        print("Or add it to a .env file as:\nGROQ_API_KEY=gsk_your_key_here\n")
        return

    try:
        run_cli(model_name="llama-3.1-8b-instant", max_turns=4)


    except KeyboardInterrupt:
        print("\nExiting chatbot. Goodbye!")

    except Exception as e:
        print(f"\n[Error] Something went wrong: {e}")
        print("Tip: Check your internet connection or API key.\n")


if __name__ == "__main__":
    main()
