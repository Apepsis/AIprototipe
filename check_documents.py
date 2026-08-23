import chromadb


client = chromadb.PersistentClient(
    path="./memory"
)


collection = client.get_collection(
    name="documentos"
)


print("Cantidad de documentos:")
print(collection.count())


print("\nPrimeros registros:")

datos = collection.get(
    limit=3
)

print(datos)