# 🤖 Multi-Agent RAG System for Intelligent Query Routing

## 📌 Overview

Este proyecto implementa un sistema de **multi-agent orchestration** basado en LLMs que clasifica automáticamente consultas de usuarios y las enruta a agentes especializados que responden utilizando **Retrieval-Augmented Generation (RAG)**.

El sistema está diseñado para resolver un problema real de negocio:
👉 **tickets mal enroutados entre áreas (HR, IT, Finance)**

---

## 🎯 Objetivos

* Clasificar automáticamente consultas de usuarios
* Enrutar dinámicamente a agentes especializados
* Generar respuestas basadas en documentación real (RAG)
* Proveer observabilidad completa del sistema
* Evaluar automáticamente la calidad de las respuestas

---

## 🧠 Arquitectura del sistema

```
Usuario → Orchestrator → Routing → RAG Agent → Respuesta
                            ↓
                       Langfuse (tracing)
                            ↓
                       Evaluator (scoring)
```

---

## ⚙️ Componentes principales

### 1. 🧭 Orchestrator (Routing Inteligente)

* Clasifica la intención de la consulta (`hr`, `tech`, `finance`)
* Implementado con LLM + prompt engineering

---

### 2. 🤖 RAG Agents (Especializados)

| Agente        | Dominio          | Función                |
| ------------- | ---------------- | ---------------------- |
| HR Agent      | Recursos Humanos | Vacaciones, beneficios |
| Tech Agent    | Soporte IT       | Accesos, VPN, errores  |
| Finance Agent | Finanzas         | Facturación, pagos     |

Cada agente:

* Usa su propia base de conocimiento
* Recupera documentos relevantes
* Genera respuestas grounded (sin hallucinations)

---

### 3. 📚 Vector Store + Retrieval

* Embeddings con OpenAI
* Vector DB: FAISS
* Retrieval Top-K por similitud semántica

---

### 4. 🔍 Observabilidad (Langfuse)

* Tracking completo de:

  * Routing
  * Retrieval
  * Respuesta final
* Debugging de errores en producción

---

### 5. 📊 Evaluator (Calidad automática)

* Evalúa respuestas del 1 al 10
* Métricas:

  * Relevancia
  * Precisión
  * Completitud

---

## 🗂️ Estructura del proyecto

```
multi-agent-routing/
│
├── src/
│   ├── main.py
│   ├── agents/
│   │   ├── orchestrator.py
│   │   ├── hr_agent.py
│   │   ├── tech_agent.py
│   │   ├── finance_agent.py
│   │
│   ├── rag/
│   │   ├── loader.py
│   │   ├── vector_store.py
│   │   ├── retriever.py
│   │
│   ├── evaluation/
│   │   ├── evaluator.py
│
├── data/
│   ├── hr_docs/
│   ├── tech_docs/
│   ├── finance_docs/
│
├── requirements.txt
├── .env.example
├── README.md
```

---

## 🚀 Instalación

```bash
git clone <repo-url>
cd multi-agent-routing

python -m venv venv
venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

---

## 🔐 Variables de entorno

Crear archivo `.env`:

```
OPENAI_API_KEY=your-key

LANGFUSE_PUBLIC_KEY=pk-lf-xxx
LANGFUSE_SECRET_KEY=sk-lf-xxx
LANGFUSE_HOST=https://cloud.langfuse.com
```

---

## ▶️ Ejecución

```bash
python src/main.py
```

---

## 🧪 Ejemplo de uso

```
QUERY: ¿Cuántos días de vacaciones tengo?
→ HR Agent → respuesta basada en documentos

QUERY: No puedo acceder al sistema
→ Tech Agent → respuesta con contexto técnico

QUERY: ¿Dónde veo mis facturas?
→ Finance Agent → respuesta financiera
```

---

## 📈 Observabilidad

El sistema utiliza **Langfuse** para:

* Visualizar trazas completas
* Analizar errores de routing
* Inspeccionar documentos recuperados

---

## 🧠 Decisiones técnicas

### ✔ Uso de LangChain

* Framework estándar en la industria
* Componentes reutilizables y escalables

### ✔ RAG por dominio

* Reduce ruido semántico
* Mejora precisión de respuestas

### ✔ Routing con LLM

* Flexibilidad ante lenguaje natural
* Escalable a nuevos dominios

### ✔ Arquitectura modular

* Separación clara de responsabilidades
* Facilita mantenimiento y extensión

---

## 🔥 Mejoras futuras

* Confidence score en routing
* Multi-label classification
* Re-ranking de documentos
* UI frontend para consultas
* Deployment en cloud (Railway)

---

## 📊 Evaluación del sistema

El sistema incluye un evaluator automático que asigna un score (1–10) a cada respuesta.

Esto permite:

* Monitoreo continuo de calidad
* Detección de respuestas deficientes
* Mejora iterativa del sistema

---

## 🏁 Conclusión

Este proyecto demuestra la implementación de un sistema real de IA aplicado a:

* Atención al cliente automatizada
* Orquestación multi-agente
* Uso de RAG en producción
* Observabilidad y evaluación de LLMs

---
