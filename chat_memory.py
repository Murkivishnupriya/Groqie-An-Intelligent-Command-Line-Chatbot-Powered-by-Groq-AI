from collections import deque

class SlidingWindowMemory:
    """
    Simple sliding window memory for storing conversation turns.
    """

    def __init__(self, max_turns: int = 4):
        self.max_turns = max_turns
        self.buffer = deque(maxlen=max_turns * 2)

    def add_turn(self, user_msg: str, bot_msg: str):
        self.buffer.append(("User", user_msg))
        self.buffer.append(("Bot", bot_msg))

    def get_history(self):
        return list(self.buffer)

    def build_prompt(self, user_msg: str) -> str:
        lines = [f"{speaker}: {msg}" for speaker, msg in self.buffer]
        lines.append(f"User: {user_msg}")
        lines.append("Assistant:")
        return "\n".join(lines)
