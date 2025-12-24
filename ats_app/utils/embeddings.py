from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_similarity(resume, jd):
    emb = model.encode([resume, jd])
    return cosine_similarity([emb[0]], [emb[1]])[0][0]
