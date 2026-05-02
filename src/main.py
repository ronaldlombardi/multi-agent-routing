from dotenv import load_dotenv
load_dotenv()
from evaluation.evaluator import evaluate
from langfuse import Langfuse

langfuse = Langfuse()

trace = langfuse.trace(name="test_connection")

span = trace.span(name="hello_span")

span.end()

print("Langfuse OK")
# loaders
from rag.loader import load_documents
from rag.vector_store import create_vector_store
from rag.retriever import get_retriever

# agents
from agents.hr_agent import build_hr_agent
from agents.tech_agent import build_tech_agent
from agents.finance_agent import build_finance_agent

# router
from agents.orchestrator import route_query

# =========================
# 1. BUILD AGENTS
# =========================

# HR
hr_docs = load_documents("data/hr_docs")
hr_vs = create_vector_store(hr_docs)
hr_retriever = get_retriever(hr_vs)
hr_agent = build_hr_agent(hr_retriever)

# TECH
tech_docs = load_documents("data/tech_docs")
tech_vs = create_vector_store(tech_docs)
tech_retriever = get_retriever(tech_vs)
tech_agent = build_tech_agent(tech_retriever)

# FINANCE
finance_docs = load_documents("data/finance_docs")
finance_vs = create_vector_store(finance_docs)
finance_retriever = get_retriever(finance_vs)
finance_agent = build_finance_agent(finance_retriever)

# =========================
# 2. ORCHESTRATION
# =========================

def handle_query(query):
    category = route_query(query)

    if category == "hr":
        return hr_agent(query)

    elif category == "tech":
        return tech_agent(query)

    elif category == "finance":
        return finance_agent(query)

    else:
        return {"result": "No se pudo clasificar la consulta", "source_documents": []}

# =========================
# 3. TEST
# =========================

queries = [
    "¿Cuántos días de vacaciones tengo?",
    "No puedo acceder al sistema",
    "¿Dónde veo mis facturas?"
]

for q in queries:
    response = handle_query(q)

    score = evaluate(q, response["result"])

    print("\n============================")
    print("QUERY:", q)
    print("RESPUESTA:", response["result"])
    print("SCORE:", score)