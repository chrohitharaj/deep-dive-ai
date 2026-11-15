from modules.summarizer import summarize_text


def test_summarize_text_returns_first_sentences():
    text = "First sentence. Second sentence. Third sentence."

    assert summarize_text(text, max_sentences=2) == (
        "First sentence. Second sentence."
    )


def test_summarize_text_handles_empty_and_whitespace_input():
    expected = "No transcript available to summarize."

    assert summarize_text("") == expected
    assert summarize_text("   ") == expected
