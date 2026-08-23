from langchain_community.llms import Ollama
import chromadb


# =========================
# CONEXIÓN CON OLLAMA
# =========================

llm = Ollama(
    model="llama3.1"
)


# =========================
# CONEXIÓN CON MEMORIA
# =========================

client = chromadb.PersistentClient(
    path="./memory"
)

collection = client.get_or_create_collection(
    name="memorias"
)


# =========================
# GUARDAR MEMORIA
# =========================

def guardar_memoria(texto):

    cantidad = collection.count()

    collection.add(
        documents=[texto],
        ids=[str(cantidad + 1)]
    )


# =========================
# BUSCAR MEMORIA
# =========================

def buscar_memoria(pregunta):

    resultado = collection.query(
        query_texts=[pregunta],
        n_results=3
    )

    documentos = resultado.get("documents", [])

    if documentos and documentos[0]:
        return documentos[0]

    return []


# =========================
# DETECTOR DE MEMORIA
# =========================

def debe_guardar(texto):

    palabras = [
        "mi nombre",
        "me llamo",
        "mi proyecto",
        "estoy creando",
        "trabajo en",
        "me gusta",
        "prefiero",
        "mi objetivo"
    ]

    texto = texto.lower()

    for palabra in palabras:
        if palabra in texto:
            return True

    return False



# =========================
# AGENTE PRINCIPAL
# =========================

while True:

    pregunta = input("\nTú: ")


    if pregunta.lower() == "salir":
        break


    # Guardar información importante

    if debe_guardar(pregunta):

        guardar_memoria(pregunta)

        print("🧠 Memoria guardada")


    # Recuperar recuerdos

    recuerdos = buscar_memoria(pregunta)


    contexto = ""

    if recuerdos:

        contexto = f"""
Estos son recuerdos del usuario:

{recuerdos}

Utilízalos para responder.
"""


    # Prompt final

    prompt = f"""

Eres un asistente IA local con memoria.

{contexto}


Pregunta del usuario:

{pregunta}


Responde de forma clara.
"""


    respuesta = llm.invoke(prompt)


    print("\nIA:", respuesta)