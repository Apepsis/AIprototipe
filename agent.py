from tool_router import decide_tool
from tools.tool_manager import execute_tool

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



# Memoria personal
memory_db = client.get_collection(
    name="memorias"
)



# Documentos RAG
document_db = client.get_collection(
    name="documentos_chunks",
    embedding_function=embedding_function
)



# =====================================================
# BUSCAR MEMORIA
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



# =====================================================
# BUSCAR DOCUMENTOS
# =====================================================

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
# PLANNER DE INFORMACIÓN
# =====================================================

def planner(question):


    prompt = f"""

You are an AI planning system.

Analyze the user question.

Decide what information sources are needed.

Return ONLY JSON:

{{
"memory": true/false,
"documents": true/false,
"reason": "short explanation"
}}


Question:

{question}

"""


    response = llm.invoke(prompt)


    try:

        return json.loads(response)


    except:

        return {

            "memory": True,

            "documents": True

        }



# =====================================================
# CREAR CONTEXTO
# =====================================================

def build_context(question):


    plan = planner(question)


    context = ""



    if ENABLE_MEMORY and plan.get("memory"):
    memories = search_memory(question)


        context += f"""

USER MEMORY:

{memories}

"""



    if plan.get("documents"):


        docs = search_documents(question)


        context += f"""

DOCUMENT KNOWLEDGE:

{docs}

"""



    return context



# =====================================================
# PROCESAR HERRAMIENTAS
# =====================================================

def process_tool(question):


    decision = decide_tool(question)


    try:


        tool = decision.get("tool")


        argument = decision.get("argument")



        if tool and tool != "none":


            result = execute_tool(

                tool,

                argument

            )


            return result



    except Exception as e:


        return {

            "error": str(e)

        }



    return None



# =====================================================
# CORE AGENT LOOP
# =====================================================

while True:

    mode = input("\nModo (texto/voz): ")

    if mode.lower() == "voz":

    from voice import listen

    question = listen()
        print("USER:", question)

    else:
        question = input("\nUSER: ")

    if question.lower() == "salir":

        break



    # ==========================================
    # PRIMERO: VER SI NECESITA HERRAMIENTA
    # ==========================================


    tool_result = process_tool(question)



    if tool_result:


        prompt = f"""

The user requested an action.

Tool result:

{tool_result}


Explain the result clearly.

"""


        answer = llm.invoke(prompt)



        print("\nAGENT:")

        print(answer)



        continue



    # ==========================================
    # SEGUNDO: MEMORIA + RAG
    # ==========================================


    context = build_context(question)



    final_prompt = f"""

You are a local autonomous AI assistant.


Rules:

- Use the provided context.
- Do not invent information.
- If information is missing say it.


CONTEXT:

{context}



USER QUESTION:

{question}



Answer:

"""



    answer = llm.invoke(final_prompt)



    print("\nAGENT:")

    print(answer)
