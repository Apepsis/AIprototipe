import chromadb


client = chromadb.PersistentClient(
    path="./memory"
)


try:
    client.delete_collection(
        name="documentos"
    )

    print("Colección eliminada")

except:
    print("No existía")