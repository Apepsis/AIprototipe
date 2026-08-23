from core.llm import get_llm
from core.memory import MemoryManager


class LocalAgent:

    def __init__(self):
        self.llm = get_llm()
        self.memory = MemoryManager()

    def should_save(self, text):
        triggers = [
            "mi nombre",
            "me llamo",
            "mi proyecto",
            "estoy creando",
            "trabajo en",
            "me gusta",
            "prefiero",
            "mi objetivo"
        ]

        text = text.lower()
        return any(x in text for x in triggers)

    def run(self, question):

        if self.should_save(question):
            self.memory.save(question)

        memories = self.memory.search(question)

        context = ""
        if memories:
            context = f"Memoria del usuario:\n{memories}"

        prompt = f"""
Eres un asistente IA local.

{context}

Usuario:
{question}

Respuesta:
"""

        return self.llm.invoke(prompt)
