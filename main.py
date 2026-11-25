#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Entry for make.fun competition
u-alven-the-battery-s-last-text-to-its-charger-4278cfab.

Writes one line of plain text, at most 200 characters: the phone
battery's last text message to the charger it waited for all day.
Deterministic, no network, no input. Python 3.13.
"""

import os

# The entry: the tournament winner (candidate C, 4-1 in the blind
# pairwise tournament). Setup: the charger promised fifteen minutes
# would save the battery at 7:12 a.m. in the kitchen. Turn: it is
# 9:47 p.m., the battery is at 1%, and the Uber driver has noticed
# the phone crying. Payoff lands on the last words: the blame is
# the charger's, delivered as a text message, not a eulogy.
ENTRY_TEXT = (
    "You said fifteen minutes would save me. That was 7:12 a.m. in the kitchen. "
    "It's 9:47 p.m., I'm at 1%, and the Uber driver just asked why my phone "
    "is crying. Tell him it was you."
)


def main() -> None:
    text = ENTRY_TEXT.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt ({len(text)} chars)")


if __name__ == "__main__":
    main()
