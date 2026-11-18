#!/usr/bin/env python3
"""Entry for make.fun news-image-20261118.

Copies the pre-drawn front page (entry.png, a one-page newspaper
summary of Wednesday 18 November 2026) to the output path.
Standard library only, no network, deterministic: the same bytes
every run.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    # The grader runs this twice in separate sandboxes; a plain file copy
    # keeps both runs byte-identical by construction.
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", out_dir / "entry.png")


if __name__ == "__main__":
    main()
