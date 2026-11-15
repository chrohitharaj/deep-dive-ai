
def summarize_text(text, max_sentences=5):

    if not text.strip():
        return "No transcript available to summarize."

    # Split transcript into sentences
    sentences = text.replace("!", ".").replace("?", ".").split(".")

    # Remove empty sentences
    sentences = [
        sentence.strip()
        for sentence in sentences
        if sentence.strip()
    ]

    # Select the first few sentences
    summary = sentences[:max_sentences]

    return ". ".join(summary) + "."

