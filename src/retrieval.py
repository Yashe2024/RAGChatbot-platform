import re
from collections import Counter

def tokenize(text):
    return re.findall(r"[a-zA-Z0-9]+", text.lower())

def lexical_similarity(query, document):
    q = Counter(tokenize(query))
    d = Counter(tokenize(document))
    return sum(min(q[k], d[k]) for k in q)

def retrieve(query, documents, top_k=3):
    ranked = sorted(documents, key=lambda d: lexical_similarity(query, d), reverse=True)
    return ranked[:top_k]
