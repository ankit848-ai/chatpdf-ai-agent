from sentence_transformers import SentenceTransformer
from src.vector_store import VectorStore

model = SentenceTransformer("all-MiniLM-L6-v2")

def answer_question(query, vector_db):
    query_vec = model.encode([query])[0]
    retrieved = vector_db.search(query_vec, k=3)

    context = "\n".join(retrieved)
    return f"Using the document, this is the answer:\n\n{context}"
