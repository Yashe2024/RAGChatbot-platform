from src.retrieval import retrieve

def test_retrieval_returns_relevant_document():
    docs = ["seven year retention policy", "quarterly access review"]
    assert "retention" in retrieve("retention period", docs, 1)[0]
