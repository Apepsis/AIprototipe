class ShortTermMemory:
    """Memory of the current conversation session."""

    def __init__(self):
        self.messages = []

    def add(self, role, content):
        self.messages.append({"role": role, "content": content})

    def get_context(self, limit=10):
        return self.messages[-limit:]
