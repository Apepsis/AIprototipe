import chromadb


class MemoryManager:

    def __init__(self, path="./memory"):
        self.client = chromadb.PersistentClient(path=path)
        self.collection = self.client.get_or_create_collection(
            name="memorias"
        )

    def save(self, text):
        count = self.collection.count()
        self.collection.add(
            documents=[text],
            ids=[str(count + 1)]
        )

    def search(self, query, limit=3):
        result = self.collection.query(
            query_texts=[query],
            n_results=limit
        )

        docs = result.get("documents", [])
        return docs[0] if docs else []
