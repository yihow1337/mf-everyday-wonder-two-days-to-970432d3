#!/usr/bin/env python3
"""Write the competition entry (one sentence) to the output directory.

The program is deterministic: it emits identical bytes on every run.
"""
import os

# The entry: one sentence, <= 200 characters, grounded in a real moment.
# A fogged bathroom mirror revealing an earlier handprint, reframed as
# the glass having held your hand all day.
ENTRY = (
    "The shower fogs the mirror and this morning's handprint surfaces, "
    "as if the glass had been holding my hand all day."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
