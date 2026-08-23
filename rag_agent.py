from langchain_community.llms import Ollama
import chromadb
from chromadb.utils import embedding_functions


# =========================
# Ollama
# =========================

llm = Ollama(
    model="llama3.1"
)


# =========================
# Embeddings
# =========================

embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)


# =========================
# ChromaDB
# =========================

client = chromadb.PersistentClient(
    path="./memory"
)


collection = client.get_collection(
    name="documentos_chunks",
    embedding_function=embedding_function
)



# =========================
# Buscar información
# =========================

def buscar_contexto(pregunta):

    resultado = collection.query(
        query_texts=[pregunta],
        n_results=5
    )


    documentos = resultado["documents"][0]


    contexto = "\n\n".join(documentos)

    return contexto



# =========================
# Agente RAG
# =========================

while True:

    pregunta = input("\nTú: ")


    if pregunta.lower() == "salir":
        break


    contexto = buscar_contexto(pregunta)


    prompt = f"""

Eres un asistente experto.

Responde usando solamente el contexto del libro.

CONTEXTO:

{contexto}


PREGUNTA:

{pregunta}


Respuesta:
"""


    respuesta = llm.invoke(prompt)


    print("\nIA:")
    print(respuesta)