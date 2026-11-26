#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes one museum placard for an ordinary office object, treated as an
ancient artifact, to /output/entry.txt.

Stdlib only: the grading sandbox is plain python:3.13-slim.

The line was picked against the published judge brief, not as a first
draft. Ten candidates (stapler, sticky note, lanyard, microwave,
paperclip, whiteboard marker, coffee mug, desk chair, office plant,
elevator button) were sparred pairwise; see CANDIDATES.md in the workdir.
This microwave placard won unbeaten: it has full label craft (title,
catalogue date, three materials, donor line), the material list smuggles
the joke ("other people's fish" listed as a material), the imagined
history is specific to one object, and the deadpan close ("forgave no
one") lands without explaining itself. 147 characters.
"""

import os

PLACARD = (
    "Shrine of the Shared Lunch, c. 2020. Steel, glass, other people's "
    "fish. Heated offerings in ninety seconds; forgave no one. Loan of "
    "the Break Room."
)


def main() -> None:
    text = PLACARD.strip()
    assert 1 <= len(text) <= 180, f"placard must be 1-180 chars, got {len(text)}"
    assert text == text.strip() and "\n" not in text, "placard must be one clean line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
