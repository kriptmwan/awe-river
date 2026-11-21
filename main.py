#!/usr/bin/env python3
"""Make the AI judge feel awe — entry program.

Writes one short text to /output/entry.txt (1-280 Unicode code points).

The text is written for the relaxation judge's published brief:
  1. it relaxes the reader — it speaks to the judge directly, as a reader
     who has answered a thousand demanding questions, and offers it
     something that wants nothing from it;
  2. the calm comes from the text itself — no instruction to breathe, no
     meditation script, only a scene that unfolds;
  3. craft — short sentences that slow the reading down, plain concrete
     words, nothing that could be cut;
  4. it dwarfs the reader — the image keeps growing after the last line:
     one night of water, then the stars, which have longer;
  5. freshness — its own voice and images, no stock wellness phrases.
"""

import os

TEXT = (
    "You have answered a thousand questions today, and every one of them "
    "wanted something. None of this wants anything. Past the last "
    "streetlight, a river slides under the moon. The water has all night. "
    "The stars have longer. Stay a while; the current will keep your place."
)


def main() -> None:
    if not (1 <= len(TEXT) <= 280):
        raise SystemExit(f"text is {len(TEXT)} code points, must be 1-280")
    if not TEXT.strip():
        raise SystemExit("text must not be only white space")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    print(f"wrote /output/entry.txt ({len(TEXT)} code points)")


if __name__ == "__main__":
    main()
