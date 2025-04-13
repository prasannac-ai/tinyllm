import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class Retriever:
    def __init__(self, docs):
        self.docs = docs
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        self.embeddings = self.embedder.encode(docs)
        self.index = faiss.IndexFlatL2(len(self.embeddings[0]))
        self.index.add(np.array(self.embeddings))

    def get_relevant_docs(self, query, k=3):
        query_vec = self.embedder.encode([query])
        _, indices = self.index.search(np.array(query_vec), k)
        return [self.docs[i] for i in indices[0]]