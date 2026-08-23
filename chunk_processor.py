import chromadb
from chromadb.utils import embedding_functions


# =========================
# Configuración embeddings
# =========================

embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)


# =========================
# Conectar ChromaDB
# =========================

client = chromadb.PersistentClient(
    path="./memory"
)


# Colección antigua OCR

ocr_collection = client.get_collection(
    name="documentos_ocr"
)


# Crear nueva colección con chunks

chunks_collection = client.get_or_create_collection(
    name="documentos_chunks",
    embedding_function=embedding_function
)



# =========================
# División de texto
# =========================

def crear_chunks(texto, tamaño=800, overlap=150):

    chunks = []

    inicio = 0

    while inicio < len(texto):

        fin = inicio + tamaño

        fragmento = texto[inicio:fin]

        if len(fragmento.strip()) > 50:
            chunks.append(fragmento)

        inicio = fin - overlap


    return chunks



# =========================
# Procesar documentos
# =========================

datos = ocr_collection.get()


documentos = datos["documents"]


contador = 0


for pagina, texto in enumerate(documentos):

    fragmentos = crear_chunks(texto)


    for fragmento in fragmentos:

        chunks_collection.add(
            documents=[fragmento],
            ids=[f"chunk_{contador}"],
            metadatas=[
                {
                    "pagina": pagina
                }
            ]
        )

        contador += 1


print("Proceso terminado")
print("Chunks creados:", contador)