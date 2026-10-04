from .retrieval import retrieve

def build_context(query, documents, top_k=3):
    selected = retrieve(query, documents, top_k)
    return {"documents": selected, "context": "\n\n".join(selected)}
