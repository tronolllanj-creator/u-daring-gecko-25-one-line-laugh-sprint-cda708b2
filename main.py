"""Entrypoint script for the grader. Writes a specific humorous line to entry.txt."""
# Entry validated: output is 1-200 chars, one line, deterministic.

import os
from pathlib import Path

LINE = "Staring into the fridge at midnight is basically an unboxing video where the prize is always just a tub of slightly questionable hummus."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "entry.txt"

    content = LINE + "\n"

    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Content validation failed")

    output_file.write_text(content, encoding="utf-8")

    print(output_file)
    print(len(content))


if __name__ == "__main__":
    main()
