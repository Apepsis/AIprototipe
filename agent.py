from router import quick_router
from tool_router import decide_tool

from config import (
    ENABLE_MEMORY,
    ENABLE_DOCUMENTS,
    ENABLE_TOOLS,
    ENABLE_VOICE
)

from langchain_community.llms import Ollama

import chromadb
from chromadb.utils import embedding_functions
import json


# =====================================================
# MODELO LOCAL
# =====================================================

llm = Ollama(
    model="llama3.1"
)


# =====================================================
# EMBEDDINGS
# =====================================================

embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)


# =====================================================
# BASE VECTORIAL
# =====================================================

client = chromadb.PersistentClient(
    path="./memory"
)

memory_db = client.get_collection(
    name="memorias"
)


document_db = client.get_collection(
    name="documentos_chunks",
    embedding_function=embedding_function
)


# =====================================================
# MEMORY / RAG
# =====================================================

def search_memory(query):
    try:
        result = memory_db.query(
            query_texts=[query],
            n_results=5
        )
        return result["documents"][0]
    except Exception:
        return []


def search_documents(query):
    try:
        result = document_db.query(
            query_texts=[query],
            n_results=5
        )
        return result["documents"][0]
    except Exception:
        return []


# =====================================================
# PLANNER IA (solo cuando router rapido falla)
# =====================================================

def planner(question):

    prompt = f"""
You are an AI planning system.

Analyze the user question.
Return ONLY JSON:

{{
"memory": true/false,
"documents": true/false
}}

Question:
{question}
"""

    response = llm.invoke(prompt)

    try:
        return json.loads(response)
    except Exception:
        return {
            "memory": False,
            "documents": False
        }


# =====================================================
# CONTEXT BUILDER
# =====================================================

def build_context(question):

    plan = quick_router(question)

    if plan is None:
        print("Planner IA activado")
        plan = planner(question)

    context = ""

    if ENABLE_MEMORY and plan.get("memory"):
        memories = search_memory(question)
        context += f"\nUSER MEMORY:\n{memories}\n"

    if ENABLE_DOCUMENTS and plan.get("documents"):
        docs = search_documents(question)
        context += f"\nDOCUMENT KNOWLEDGE:\n{docs}\n"

    return context


# =====================================================
# TOOLS LAZY LOADING
# =====================================================

def process_tool(question):

    if not ENABLE_TOOLS:
        return None

    decision = decide_tool(question)

    tool = decision.get("tool")
    argument = decision.get("argument")

    if tool and tool != "none":
        from tools.tool_manager import execute_tool
        return execute_tool(tool, argument)

    return None


# =====================================================
# CORE LOOP
# =====================================================

while True:

    mode = input("\nModo (texto/voz): ")

    if mode.lower() == "voz" and ENABLE_VOICE:
        from voice import listen
        question = listen()
        print("USER:", question)
    else:
        question = input("\nUSER: ")

    if question.lower() == "salir":
        break

    tool_result = process_tool(question)

    if tool_result:
        answer = llm.invoke(
            f"Tool result:\n{tool_result}\nExplain clearly."
        )

        print("\nAGENT:")
        print(answer)
        continue

    context = build_context(question)

    final_prompt = f"""
You are a local autonomous AI assistant.

Rules:
- Use provided context.
- Do not invent information.

CONTEXT:
{context}

USER QUESTION:
{question}

Answer:
"""

    answer = llm.invoke(final_prompt)

    print("\nAGENT:")
    print(answer)
