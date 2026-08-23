import argparse

from langchain_community.llms import Ollama
from core.memory_manager import MemoryManager


parser = argparse.ArgumentParser()
parser.add_argument("--voice", action="store_true")
args = parser.parse_args()

ENABLE_VOICE = args.voice

llm = Ollama(model="llama3.1")
memory = MemoryManager()


def should_remember(text):
    keywords = [
        "mi nombre", "me llamo", "mi proyecto",
        "estoy creando", "trabajo en",
        "me gusta", "prefiero", "mi objetivo"
    ]
    return any(k in text.lower() for k in keywords)


def process_question(question):
    memory.add_conversation("user", question)

    if should_remember(question):
        memory.remember(question)

    memories = memory.recall(question)
    conversation = memory.short_term.get_context()

    prompt = f"""
Eres Luna, un asistente IA local con memoria.

Memoria:
{memories}

Conversación:
{conversation}

Pregunta:
{question}
"""

    answer = llm.invoke(prompt)
    memory.add_conversation("assistant", answer)

    return answer


if __name__ == "__main__":

    if ENABLE_VOICE:
        from voice.background_listener import LunaListener

        luna = LunaListener()
        luna.start(process_question)

    else:
        while True:
            question = input("\nTu: ")

            if question.lower() == "salir":
                break

            print("\nLuna:", process_question(question))
