def chunk_text(text: str, size: int = 120, overlap: int = 20) -> list[str]:
    words = text.split()
    chunks = []
    step = max(size - overlap, 1)
    for i in range(0, len(words), step):
        chunk = " ".join(words[i:i+size])
        if chunk:
            chunks.append(chunk)
    return chunks
