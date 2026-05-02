from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

def build_hr_agent(retriever):
    llm = ChatOpenAI(model="gpt-4o-mini")

    prompt = ChatPromptTemplate.from_template("""
Sos un asistente de recursos humanos.

Respondé la pregunta usando SOLO la información del contexto.
Si no está en el contexto, decí que no tenés esa información.

Contexto:
{context}

Pregunta:
{question}
""")

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    def run(query):
        docs = retriever.invoke(query)
        context = format_docs(docs)

        chain = prompt | llm

        response = chain.invoke({
            "context": context,
            "question": query
        })

        return {
            "result": response.content,
            "source_documents": docs
        }

    return run