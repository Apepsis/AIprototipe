import json
from langchain_community.llms import Ollama


llm = Ollama(
    model="llama3.1"
)


def decide_tool(question):

    prompt = f"""

Eres un planificador de herramientas.

Analiza la petición del usuario.

Herramientas disponibles:

calculator:
Para operaciones matemáticas.

file_reader:
Para leer archivos.

python:
Para ejecutar código Python.

excel:
Para analizar archivos Excel.


Devuelve SOLO JSON:

{{
"tool": "nombre o none",
"argument": "dato necesario"
}}


Usuario:

{question}

"""


    response = llm.invoke(prompt)


    try:

        return json.loads(response)

    except:

        return {
            "tool": "none",
            "argument": ""
        }