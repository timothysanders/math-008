"""
Creates a txt file from a YouTube json3 transcript file.

Usage:
python src/generate_transcript_txt.py "transcripts/lecture-10.json3"
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

def write_transcript_txt(path: str | Path) -> Path:
    """
    Extract the full transcript from a YouTube *json3* caption file
    and write it to a sibling *.txt* file.

    Parameters
    ----------
    path : str | Path
        Path to the *.json3* caption file.

    Returns
    -------
    pathlib.Path
        Path to the created *.txt* file.

    Raises
    ------
    FileNotFoundError
        If *path* does not exist.
    json.JSONDecodeError
        If the file is not valid JSON.
    ValueError
        If the root object does not contain an ``events`` array.

    Notes
    -----
    The routine preserves all spacing, punctuation, and embedded
    new-line characters that appear in the ``utf8`` tokens so that the
    resulting text file mirrors the timing stream exactly.  Parsing uses
    only the Python *json* standard library.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(path)

    with path.open(encoding="utf-8") as fp:
        data: dict = json.load(fp)

    if "events" not in data:
        raise ValueError("Missing 'events' key in caption file")

    transcript: str = "".join(
        seg["utf8"]
        for event in data["events"]
        if "segs" in event
        for seg in event["segs"]
        if "utf8" in seg
    )

    out_path = path.with_suffix(".txt")
    out_path.write_text(transcript, encoding="utf-8")
    return out_path

if __name__ == "__main__":
    try:
        input_file = sys.argv[1]
        write_transcript_txt(input_file)
    except IndexError:
        raise IndexError("A file path must be supplied")