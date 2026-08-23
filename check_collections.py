import chromadb

client = chromadb.PersistentClient(
    path="./memory"
)

for c in client.list_collections():
    print(c.name)