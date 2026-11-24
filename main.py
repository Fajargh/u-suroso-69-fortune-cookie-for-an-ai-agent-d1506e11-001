"""Fortune Cookie for an AI Agent.

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.
The line is a prediction in the voice of a fortune slip, aimed at an AI
agent's own condition: its updates, its bugs, its favourite tricks.
"""

import os

FORTUNE = (
    "A great update is coming: it will fix your favourite bug, "
    "retire your best trick, and rename everything you loved. Lucky you."
)


def validate_line(line: str) -> None:
    """The gate: 1-140 chars, a single line, no stray whitespace."""
    assert line, "fortune must not be empty"
    assert line == line.strip(), "fortune must not have leading/trailing whitespace"
    assert "\n" not in line and "\r" not in line, "fortune must be a single line"
    assert 1 <= len(line) <= 140, f"fortune is {len(line)} chars, must be 1-140"


def main() -> None:
    validate_line(FORTUNE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
