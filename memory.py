import chromadb


# Crear base de memoria local
client = chromadb.PersistentClient(
    path="./memory"
)


# Crear colección
collection = client.get_or_create_collection(
    name="memorias"
)


# Guardar memoria
collection.add(
    documents=[
        "Julio está creando un agente IA local usando Python, Ollama y ChromaDB."
    ],
    ids=[
        "1"
    ]
)


# Buscar memoria
resultado = collection.query(
    query_texts=[
        "¿Qué está creando Julio?"
    ],
    n_results=1
)


print(resultado["documents"])