# Enterprise RAG Platform

A production-oriented reference architecture for enterprise knowledge retrieval using RAG.

## Pipeline
`Documents → Parsing → Chunking → Embeddings → Retrieval → Reranking → Context → LLM → Grounded Answer → Evaluation`

## Enterprise Controls
- Source metadata
- Document/version tracking
- Retrieval thresholds
- Citation requirements
- Prompt templates
- Evaluation dataset
- Cost/latency telemetry

## Architecture
```mermaid
flowchart LR
A[Documents] --> B[Ingestion]
B --> C[Chunking]
C --> D[Embeddings]
D --> E[(Vector Store)]
Q[User Query] --> F[Retriever]
F --> E
E --> G[Reranker]
G --> H[Context Builder]
H --> I[LLM]
I --> J[Grounded Answer + Citations]
J --> K[Evaluation]
```

## Scope
The included implementation provides a lightweight local retrieval layer so the architecture can be demonstrated without requiring a paid vector database.

## Run
```bash
pip install -r requirements.txt
python examples/demo.py
```
