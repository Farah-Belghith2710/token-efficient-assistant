import json
import os

from retrieval import retrieve
from scoring import clean, all_facts_found

with open("questions.json", encoding="utf-8") as f:
    questions = json.load(f)
answerable = [q for q in questions if q["sources"]]

rows = []
print("k   facts retrieved   avg chars")
for k in range(1, 9):
    hits = 0
    for q in answerable:
        text = clean(" ".join(c["text"] for c in retrieve(q["question"], k)))
        if all_facts_found(text, q["facts"]):
            hits += 1

    chars = 0
    for q in questions:
        for c in retrieve(q["question"], k):
            chars += len(c["text"])

    pct = round(100 * hits / len(answerable))
    avg_chars = round(chars / len(questions))
    rows.append({"k": k, "facts_retrieved_percent": pct, "avg_retrieved_characters": avg_chars})
    print(f"{k}   {pct}%   {avg_chars}")

print("\nmissing a fact at k=3:")
for q in answerable:
    text = clean(" ".join(c["text"] for c in retrieve(q["question"], 3)))
    if not all_facts_found(text, q["facts"]):
        print(" ", q["id"], q["question"])

os.makedirs("results", exist_ok=True)
with open("results/retrieval_check.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, indent=2)
