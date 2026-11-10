import json

import matplotlib.pyplot as plt
import pandas as pd

from scoring import clean, refused, all_facts_found

with open("questions.json", encoding="utf-8") as f:
    questions = {q["id"]: q for q in json.load(f)}
with open("results/answers.jsonl", encoding="utf-8") as f:
    rows = [json.loads(line) for line in f]

LABELS = {
    "baseline_k8": "Baseline (k=8)",
    "k5": "k=5",
    "k3": "k=3",
    "k8_short": "k=8 + short answers",
    "optimized_k5_short": "Optimized (k=5 + short)",
    "optimized_k5_short_repeat": "Optimized, 2nd run",
}

for r in rows:
    q = questions[r["question_id"]]
    answer = clean(r["answer"])
    r["answerable"] = bool(q["sources"])
    if r["answerable"]:
        r["ok"] = all_facts_found(answer, q["facts"])
        r["cited"] = all(s in answer for s in q["sources"])
        r["false_refusal"] = refused(answer) and not r["ok"]
    else:
        r["ok"] = refused(answer)
        r["cited"] = None
        r["false_refusal"] = False

df = pd.DataFrame(rows)
df["reasoning_tokens"] = pd.to_numeric(df["reasoning_tokens"]).fillna(0)
df["answer_tokens"] = df["output_tokens"] - df["reasoning_tokens"]
df["total_tokens"] = df["input_tokens"] + df["output_tokens"]

summary = []
for name in LABELS:
    g = df[df["setting"] == name]
    if g.empty:
        continue
    yes = g[g["answerable"]]
    no = g[~g["answerable"]]
    summary.append({
        "setting": name,
        "questions": len(g),
        "input_tokens": round(g["input_tokens"].mean()),
        "reasoning_tokens": round(g["reasoning_tokens"].mean()),
        "answer_tokens": round(g["answer_tokens"].mean()),
        "total_tokens": round(g["total_tokens"].mean()),
        "seconds": round(g["seconds"].mean(), 2),
        "groq_seconds": round(g["groq_seconds"].mean(), 2),
        "accuracy_%": round(100 * yes["ok"].mean()),
        "citations_%": round(100 * yes["cited"].astype(bool).mean()),
        "false_refusals": int(yes["false_refusal"].sum()),
        "correct_refusals_%": round(100 * no["ok"].mean()),
        "cut_off": int((g["finish_reason"] == "length").sum()),
    })

summary = pd.DataFrame(summary)
base = summary.loc[summary["setting"] == "baseline_k8", "total_tokens"].iloc[0]
summary["tokens_saved_%"] = (100 * (1 - summary["total_tokens"] / base)).round()

print(summary.to_string(index=False))
summary.to_csv("results/summary.csv", index=False)
with open("results/summary.md", "w", encoding="utf-8") as f:
    f.write("| " + " | ".join(summary.columns) + " |\n")
    f.write("|" + "---|" * len(summary.columns) + "\n")
    for _, row in summary.iterrows():
        f.write("| " + " | ".join(str(v) for v in row) + " |\n")


def compare(first, second):
    a = df[df["setting"] == first].set_index("question_id")["ok"]
    b = df[df["setting"] == second].set_index("question_id")["ok"]
    both = a.index.intersection(b.index)
    worse = [q for q in both if a[q] and not b[q]]
    better = [q for q in both if b[q] and not a[q]]
    print(f"{first} vs {second}: worse {worse}, better {better}")


print()
compare("baseline_k8", "optimized_k5_short")
compare("baseline_k8", "k5")
compare("baseline_k8", "k3")
compare("baseline_k8", "k8_short")
compare("optimized_k5_short", "optimized_k5_short_repeat")

with open("results/answers_side_by_side.md", "w", encoding="utf-8") as f:
    f.write("# Baseline vs optimized answers\n\n")
    for qid, q in questions.items():
        b = df[(df["setting"] == "baseline_k8") & (df["question_id"] == qid)]
        o = df[(df["setting"] == "optimized_k5_short") & (df["question_id"] == qid)]
        if b.empty or o.empty:
            continue
        b, o = b.iloc[0], o.iloc[0]
        flag = "  **<- CHANGED**" if b["ok"] != o["ok"] else ""
        expected = " / ".join(fact[0] for fact in q["facts"]) or "should say it is not in the documents"
        f.write(f"## {qid}: {q['question']}{flag}\n")
        f.write(f"Expected: {expected} (sources: {', '.join(q['sources']) or '-'})\n\n")
        f.write(f"**Baseline** (ok={b['ok']}, {b['total_tokens']} tokens): {b['answer']}\n\n")
        f.write(f"**Optimized** (ok={o['ok']}, {o['total_tokens']} tokens): {o['answer']}\n\n")

table = summary.set_index("setting")
names = list(table.index)
pos = list(range(len(names)))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.4), sharey=True, gridspec_kw={"width_ratios": [1.5, 1]})

left = [0] * len(names)
parts = [("input_tokens", "#2a78d6", "Input (prompt)"),
         ("reasoning_tokens", "#eb6834", "Hidden reasoning"),
         ("answer_tokens", "#1baf7a", "Visible answer")]
for col, color, label in parts:
    ax1.barh(pos, table[col], left=left, height=0.55, color=color, label=label, edgecolor="white", linewidth=1.5)
    left = [a + b for a, b in zip(left, table[col])]
for i, total in enumerate(table["total_tokens"]):
    ax1.text(left[i] + 15, i, f"{total:,}", va="center", fontsize=8, color="#52514e")
ax1.set_xlim(0, max(left) * 1.15)
ax1.set_xlabel("Average tokens per question", color="#52514e")
ax1.xaxis.set_major_formatter("{x:,.0f}")
ax1.legend(frameon=False, fontsize=8, ncol=3, loc="lower left", bbox_to_anchor=(0, 1.0))

ax2.plot(table["accuracy_%"], [i - 0.25 for i in pos], "o", color="#0b0b0b", markersize=6, label="Correct answers")
ax2.plot(table["citations_%"], pos, "s", color="#0b0b0b", markerfacecolor="white", markersize=6,
         label="Right document cited")
ax2.plot(table["correct_refusals_%"], [i + 0.25 for i in pos], "^", color="#52514e", markersize=6,
         label="Unanswerable refused")
ax2.set_xlim(0, 105)
ax2.set_xlabel("% of questions", color="#52514e")
ax2.legend(frameon=False, fontsize=8, ncol=3, loc="lower left", bbox_to_anchor=(0, 1.0),
           handletextpad=0.2, columnspacing=1.0)

ax1.set_yticks(pos)
ax1.set_yticklabels([LABELS[n] for n in names])
ax1.invert_yaxis()
for ax in (ax1, ax2):
    ax.grid(axis="x", color="#e1e0d9", linewidth=0.8)
    ax.set_axisbelow(True)
    ax.tick_params(colors="#52514e", labelsize=8, length=0)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color("#c3c2b7")

plt.tight_layout()
plt.savefig("results/tokens_and_quality.png", dpi=200, bbox_inches="tight")
print("\nsaved everything in results/")
