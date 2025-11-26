import faiss
import numpy as np

class VectorStore:
    def __init__(self, embedding_dim):
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.chunks = []

    def add_embeddings(self, vectors, texts):
        self.index.add(np.array(vectors).astype("float32"))
        self.chunks.extend(texts)

    def search(self, query_vector, k=3):
        distances, indices = self.index.search(np.array([query_vector]).astype("float32"), k)
        results = []
        for idx in indices[0]:
            results.append(self.chunks[idx])
        return results
