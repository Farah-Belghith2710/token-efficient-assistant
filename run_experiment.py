import json
import os

from assistant import ask

SETTINGS = [
    ("baseline_k8", 8, False),
    ("optimized_k5_short", 5, True),
    ("k5", 5, False),
    ("k8_short", 8, True),
    ("k3", 3, False),
    ("optimized_k5_short_repeat", 5, True),
]

with open("questions.json", encoding="utf-8") as f:
    questions = json.load(f)

os.makedirs("results", exist_ok=True)
out_path = "results/answers.jsonl"

done = set()
if os.path.exists(out_path):
    with open(out_path, encoding="utf-8") as f:
        for line in f:
            row = json.loads(line)
            done.add((row["setting"], row["question_id"]))

for name, k, short in SETTINGS:
    print(f"\n--- {name} ---")
    for q in questions:
        if (name, q["id"]) in done:
            continue
        result = ask(q["question"], k, short)
        row = {"setting": name, "question_id": q["id"], "k": k, "short": short}
        row.update(result)
        with open(out_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
        print(f"{q['id']}  in={result['input_tokens']}  out={result['output_tokens']}  {result['seconds']}s")

print("\ndone, now run evaluate.py")
