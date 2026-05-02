from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

def evaluate(query, answer):
    prompt = f"""
Sos un evaluador estricto de respuestas.

Evaluá del 1 al 10 según:

- Relevancia (¿responde la pregunta?)
- Precisión (¿es correcta según el contexto?)
- Completitud (¿es suficiente?)

Reglas IMPORTANTES:
- 9-10 → respuesta correcta, clara y completa
- 7-8 → correcta pero incompleta o mejorable
- 5-6 → parcialmente correcta
- 1-4 → incorrecta o irrelevante

Pregunta: {query}
Respuesta: {answer}

Devolvé SOLO un número entero.
"""

    result = llm.invoke(prompt)

    try:
        return int(result.content.strip())
    except:
        return 5