from langchain_community.llms import Ollama

from core.memory_manager import MemoryManager


# Voice is optional and loaded only when enabled
ENABLE_VOICE = False

if ENABLE_VOICE:
    from voice.listener import VoiceListener
    voice = VoiceListener()


llm = Ollama(
    model="llama3.1"
)

memory = MemoryManager()


def should_remember(text):
    keywords = [
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

    return any(k in text for k in keywords)


def process_question(question):

    memory.add_conversation("user", question)

    if should_remember(question):
        memory.remember(question)
        print("🧠 Memoria permanente guardada")

    memories = memory.recall(question)
    conversation = memory.short_term.get_context()

    context = ""

    if memories:
        context += f"Memoria permanente del usuario:\n{memories}\n"

    context += f"Conversación actual:\n{conversation}\n"

    prompt = f"""
Eres Luna, un asistente IA local con memoria.

Usa este contexto:

{context}

Pregunta:
{question}

Responde claramente.
"""

    answer = llm.invoke(prompt)

    memory.add_conversation("assistant", answer)

    return answer


while True:

    question = input("\nTu: ")

    if question.lower() == "salir":
        break

    answer = process_question(question)

    print("\nLuna:", answer)
