import chromadb


class LongTermMemory:
    """Persistent user memory using ChromaDB."""

    def __init__(self, path="./memory"):
        client = chromadb.PersistentClient(path=path)
        self.collection = client.get_or_create_collection(
            name="long_term_memory"
        )

    def save(self, text):
        count = self.collection.count()
        self.collection.add(
            documents=[text],
            ids=[str(count + 1)]
        )

    def search(self, query, limit=5):
        result = self.collection.query(
            query_texts=[query],
            n_results=limit
        )
        return result.get("documents", [[]])[0]
