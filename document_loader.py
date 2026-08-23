from langchain_community.document_loaders import PyPDFLoader
import chromadb
from chromadb.utils import embedding_functions


# PDF
archivo = "documents/pdf/documento.pdf"


# Leer PDF
loader = PyPDFLoader(archivo)

documentos = loader.load()


# Crear embeddings
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)


# Base vectorial
client = chromadb.PersistentClient(
    path="./memory"
)


collection = client.get_or_create_collection(
    name="documentos",
    embedding_function=embedding_function
)


# Guardar páginas

for i, doc in enumerate(documentos):

    collection.add(
        documents=[doc.page_content],
        ids=[f"pagina_{i}"]
    )


print("Documento guardado correctamente")
print("Paginas:", len(documentos))