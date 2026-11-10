import time

from dotenv import load_dotenv
from groq import Groq, RateLimitError

from retrieval import retrieve

load_dotenv()
client = Groq()
MODEL = "openai/gpt-oss-20b"

SYSTEM_PROMPT = """You are the help assistant of Kestrel Lab. Answer the question using only the documents you are given.
After each fact, write the name of the document it comes from in square brackets, for example [vpn_access].
If the documents do not contain the answer, reply exactly: "I couldn't find this in the documentation." Do not guess."""

SHORT_RULE = "Answer in at most 3 short sentences. No introduction, no repetition."


def build_messages(question, chunks, short=False):
    docs = "\n\n".join(f"[{c['doc_id']}]\n{c['text']}" for c in chunks)
    system = SYSTEM_PROMPT
    if short:
        system += "\n" + SHORT_RULE
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": f"Documents:\n{docs}\n\nQuestion: {question}"},
    ]


def call_groq(messages, reasoning, max_tokens):
    for _ in range(10):
        try:
            return client.chat.completions.create(
                model=MODEL,
                messages=messages,
                temperature=0.6,
                reasoning_effort=reasoning,
                max_completion_tokens=max_tokens,
            )
        except RateLimitError:
            print("rate limit, waiting 30s...")
            time.sleep(30)
    raise RuntimeError("still rate limited, run it again later")


def ask(question, k=8, short=False):
    chunks = retrieve(question, k)
    messages = build_messages(question, chunks, short)

    start = time.time()
    if short:
        response = call_groq(messages, "low", 400)
    else:
        response = call_groq(messages, "medium", 2048)
    seconds = time.time() - start

    usage = response.usage
    reasoning = usage.completion_tokens_details.reasoning_tokens if usage.completion_tokens_details else None
    cached = usage.prompt_tokens_details.cached_tokens if usage.prompt_tokens_details else None

    return {
        "answer": response.choices[0].message.content or "",
        "input_tokens": usage.prompt_tokens,
        "output_tokens": usage.completion_tokens,
        "reasoning_tokens": reasoning,
        "cached_tokens": cached,
        "seconds": round(seconds, 2),
        "groq_seconds": usage.total_time,
        "finish_reason": response.choices[0].finish_reason,
        "retrieved": [c["doc_id"] for c in chunks],
    }


if __name__ == "__main__":
    r = ask("How far in advance do I need to book a cleanroom slot?", k=3, short=True)
    print(r["answer"])
    print(r["input_tokens"], "input tokens,", r["output_tokens"], "output tokens")
