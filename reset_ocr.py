import chromadb

client = chromadb.PersistentClient(
    path="./memory"
)

client.delete_collection(
    name="documentos_ocr"
)

print("Colección eliminada")