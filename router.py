def quick_router(question):

    q = question.lower()


    # ==========================
    # DOCUMENTOS
    # ==========================

    document_words = [
        "pdf",
        "documento",
        "libro",
        "archivo",
        "capítulo",
        "pagina",
        "página",
        "según el documento",
        "según el libro"
    ]


    for word in document_words:

        if word in q:

            return {
                "memory": False,
                "documents": True,
                "confidence": "high"
            }



    # ==========================
    # MEMORIA PERSONAL
    # ==========================

    memory_words = [
        "recuerdas",
        "mi proyecto",
        "mi nombre",
        "me gusta",
        "mi objetivo",
        "lo que te dije",
        "mi configuración"
    ]


    for word in memory_words:

        if word in q:

            return {
                "memory": True,
                "documents": False,
                "confidence": "high"
            }



    # ==========================
    # CONVERSACIÓN NORMAL
    # ==========================

    normal_words = [
        "hola",
        "qué es",
        "que es",
        "explícame",
        "explica",
        "dime"
    ]


    for word in normal_words:

        if word in q:

            return {
                "memory": False,
                "documents": False,
                "confidence": "medium"
            }



    # ==========================
    # NO SABEMOS
    # ==========================

    return None
