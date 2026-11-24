#!/usr/bin/env python3
"""Write the make.fun entry text for u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209."""

import os
import sys

TEXT = "Five stars. He asked me to summarize his day. I wrote: argued with a toaster, lost. He said add nuance. I wrote: twice."

assert 1 <= len(TEXT) <= 280, "text must be between 1 and 280 characters"


def main() -> None:
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
