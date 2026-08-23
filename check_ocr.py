import chromadb


client = chromadb.PersistentClient(
    path="./memory"
)


collection = client.get_collection(
    name="documentos_ocr"
)


print("Cantidad:")
print(collection.count())


datos = collection.get(
    limit=3
)


for i, texto in enumerate(datos["documents"]):

    print("\n--- PAGINA", i, "---")
    print(texto[:500])