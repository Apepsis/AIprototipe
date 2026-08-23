import chromadb
from chromadb.utils import embedding_functions


# Crear el mismo modelo de embeddings usado al guardar

embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)


# Conectar memoria

client = chromadb.PersistentClient(
    path="./memory"
)


# Abrir colección con embeddings

collection = client.get_collection(
    name="documentos",
    embedding_function=embedding_function
)


pregunta = input("Pregunta sobre el documento: ")


resultado = collection.query(
    query_texts=[pregunta],
    n_results=3
)


print("\nInformación encontrada:\n")


for documento in resultado["documents"][0]:

    print(documento[:1000])
    print("\n----------------\n")