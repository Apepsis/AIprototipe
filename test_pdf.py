from langchain_community.document_loaders import PyPDFLoader


archivo = "documents/pdf/documento.pdf"

loader = PyPDFLoader(archivo)

docs = loader.load()


print("Páginas:", len(docs))

print("Primer texto:")

print(docs[0].page_content[:500])