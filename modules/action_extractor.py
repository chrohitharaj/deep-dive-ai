
def extract_action_items(text):

    if not text.strip():
        return []

    action_keywords = [
        "need to",
        "must",
        "should",
        "todo",
        "action item",
        "remember to",
        "make sure to",
        "complete"
    ]

    action_items = []

    sentences = (
        text.replace("!", ".")
        .replace("?", ".")
        .split(".")
    )

    for sentence in sentences:

        sentence = sentence.strip()

        if not sentence:
            continue

        lower_sentence = sentence.lower()

        for keyword in action_keywords:

            if keyword in lower_sentence:
                action_items.append(sentence)
                break

    return action_items

