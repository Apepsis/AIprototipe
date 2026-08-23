import chromadb


client = chromadb.PersistentClient(
    path="./memory"
)

collection = client.get_or_create_collection(
    name="memorias"
)


print("Cantidad de recuerdos:")
print(collection.count())


print("\nMemorias guardadas:")
print(
    collection.get()
)