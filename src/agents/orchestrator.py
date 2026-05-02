# src/agents/orchestrator.py

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

prompt = ChatPromptTemplate.from_template("""
Sos un sistema de clasificación de consultas empresariales.

Clasificá la siguiente consulta en UNA de estas categorías:
- hr
- tech
- finance

Reglas:
- HR → empleados, vacaciones, beneficios
- tech → sistemas, errores, acceso, VPN
- finance → pagos, facturas, billing

Consulta:
{query}

Respondé SOLO con una palabra: hr, tech o finance.
""")

def route_query(query: str) -> str:
    chain = prompt | llm
    response = chain.invoke({"query": query})

    return response.content.strip().lower()