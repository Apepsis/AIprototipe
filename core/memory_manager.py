from .short_term import ShortTermMemory
from .long_term import LongTermMemory
from .preferences import UserPreferences


class MemoryManager:
    def __init__(self):
        self.short_term = ShortTermMemory()
        self.long_term = LongTermMemory()
        self.preferences = UserPreferences()

    def remember(self, text):
        self.long_term.save(text)

    def recall(self, query):
        return self.long_term.search(query)

    def add_conversation(self, role, content):
        self.short_term.add(role, content)
