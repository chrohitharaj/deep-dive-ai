from modules.action_extractor import extract_action_items


def test_extract_action_items_matches_keywords_case_insensitively():
    text = (
        "We need to prepare the slides. "
        "The meeting starts at noon. "
        "You SHOULD review the notes!"
    )

    assert extract_action_items(text) == [
        "We need to prepare the slides",
        "You SHOULD review the notes",
    ]


def test_extract_action_items_returns_empty_list_without_matching_actions():
    assert extract_action_items("") == []
    assert extract_action_items("The lecture starts at noon.") == []
