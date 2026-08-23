import fitz
import pytesseract
from PIL import Image
import chromadb
from chromadb.utils import embedding_functions


# Ruta PDF
pdf_path = "documents/pdf/document.pdf"

# Ruta Tesseract
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


# Embeddings
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)


client = chromadb.PersistentClient(
    path="./memory"
)


collection = client.get_or_create_collection(
    name="documentos_ocr",
    embedding_function=embedding_function
)


pdf = fitz.open(pdf_path)


for numero, pagina in enumerate(pdf):

    print("Procesando página:", numero + 1)


    pix = pagina.get_pixmap(
    dpi=300
)


    imagen = Image.frombytes(
        "RGB",
        [pix.width, pix.height],
        pix.samples
    )


    texto = pytesseract.image_to_string(
    imagen,
    lang="eng",
    config="--psm 6"
)


    if texto.strip():

        collection.add(
            documents=[texto],
            ids=[f"pagina_{numero}"]
        )


print("OCR terminado")