REFUSALS = ["couldn't find", "could not find", "not in the documentation", "no information",
            "not mentioned", "doesn't mention", "does not mention", "doesn't say", "does not say",
            "not specified", "doesn't specify", "does not specify", "not covered",
            "doesn't contain", "does not contain"]

REPLACE = [("’", "'"), ("‑", "-"), ("‐", "-"), ("–", "-"),
           (" ", " "), (" ", " "), (" ", " "), ("*", ""), ("`", "")]


def clean(text):
    text = text.lower()
    for a, b in REPLACE:
        text = text.replace(a, b)
    return text


def refused(answer):
    return any(r in answer for r in REFUSALS)


def all_facts_found(answer, facts):
    return all(any(v in answer for v in variants) for variants in facts)
