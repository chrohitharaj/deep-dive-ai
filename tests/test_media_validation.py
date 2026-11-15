import pytest

from modules.media_validation import is_supported_media_file


@pytest.mark.parametrize(
    "filename",
    [
        "lecture.mp3",
        "lecture.WAV",
        "lecture.m4a",
        "lecture.mp4",
        "lecture.WEBM",
        r"C:\recordings\lecture.mp4",
    ],
)
def test_supported_media_extensions_are_accepted(filename):
    assert is_supported_media_file(filename)


@pytest.mark.parametrize(
    "filename",
    ["lecture.txt", "lecture.mp3.exe", "lecture", "", None],
)
def test_unsupported_or_empty_filenames_are_rejected(filename):
    assert not is_supported_media_file(filename)
