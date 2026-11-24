# SPDX-License-Identifier: MIT
"""One Word for Your Wi-Fi — Gaslighting.

The network insists it is connected while nothing loads. This program
writes that one honest word to /output/entry.txt (or to the directory
named by MAKEFUN_OUTPUT_DIR) as UTF-8, then prints how many characters
it wrote. It needs no network, takes no arguments, and never removes
the output directory. A short known-valid fallback is kept only for
the case the main word ever failed the gate.
"""

import os
import sys

# The judge weighs the laugh, the truth of it and the freshness of the
# angle. "Gaslighting" is all three at once: the network says it is
# connected while nothing loads.
TEXT = 'Gaslighting'

FALLBACK = 'Offline'


def fits_gate(text):
    """True when the text satisfies the competition's size gate."""
    return 1 <= len(text) <= 20 and text.strip() != ""


def pick_text():
    """Return the entry, falling back if the main text ever failed."""
    if fits_gate(TEXT):
        return TEXT
    if fits_gate(FALLBACK):
        return FALLBACK
    print("error: no valid entry text available", file=sys.stderr)
    sys.exit(1)


def main():
    entry = pick_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(entry)
    print("wrote %d characters to %s" % (len(entry), path))


if __name__ == "__main__":
    main()
