import glob
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_chunks(folder="knowledge_base"):
    chunks = []
    for path in sorted(glob.glob(os.path.join(folder, "*.md"))):
        doc_id = os.path.basename(path)[:-3]
        with open(path, encoding="utf-8") as f:
            text = f.read()
        title = text.split("\n")[0].replace("# ", "")
        for section in text.split("\n## ")[1:]:
            chunks.append({"doc_id": doc_id, "text": f"{title} - {section.strip()}"})
    return chunks


chunks = load_chunks()
vectorizer = TfidfVectorizer(stop_words="english")
matrix = vectorizer.fit_transform([c["text"] for c in chunks])


def retrieve(question, k):
    scores = cosine_similarity(vectorizer.transform([question]), matrix)[0]
    top = scores.argsort()[::-1][:k]
    return [chunks[i] for i in top]
