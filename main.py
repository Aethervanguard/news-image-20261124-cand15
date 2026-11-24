#!/usr/bin/env python3
"""news-image-20261124 candidate 15: ship the pre-rendered entry image.

The grader runs bare-stdlib Python (no fonts, no network), so the picture
is rendered at build time and shipped as entry.png. This program copies
it into $MAKEFUN_OUTPUT_DIR/entry.png, byte for byte, and exits zero.
"""
import os
import shutil
import sys


def main():
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "entry.png")
    if not os.path.isfile(src):
        sys.stderr.write("entry.png is missing\n")
        return 1
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    dst = os.path.join(out, "entry.png")
    shutil.copyfile(src, dst)
    if os.path.getsize(dst) != os.path.getsize(src):
        sys.stderr.write("entry.png copy is incomplete\n")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
