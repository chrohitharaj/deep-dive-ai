"""Filename-extension checks for the media types accepted by the app."""

from pathlib import Path
from typing import Optional


SUPPORTED_MEDIA_EXTENSIONS = frozenset(
    {".mp3", ".wav", ".m4a", ".mp4", ".webm"}
)


def is_supported_media_file(filename: Optional[str]) -> bool:
    """Return whether a filename has a supported media extension.

    This checks only the filename extension, not the file's actual contents.
    """
    if not filename:
        return False

    return Path(filename).suffix.lower() in SUPPORTED_MEDIA_EXTENSIONS
