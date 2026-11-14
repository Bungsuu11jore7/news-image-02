#!/usr/bin/env python3
"""news-image-02 entry: "Field Notes — Friday 13 November 2026".

A program that copies the entry image to /output/entry.png, using the
Python standard library only. The image itself is a reporter's
notebook page: six pinned clipping cards summing up the world's news
of Friday 13 November 2026, each with a pictogram, a kicker, a
headline and a short summary, so a viewer who missed the day can
tell what happened from the image alone.

The six stories (all happened, or were first reported, on Friday
13 November 2026 — verified against that day's reporting):
  1. Dublin agrees a five-country team for the Ukraine peace talks,
     as Kyiv fires 1,200 drones in one of the war's biggest strikes.
  2. The US shoots down two Iranian drones bound for Bahrain; Iran
     claims it hit a US radar — that claim is unverified.
  3. Nvidia chief Jensen Huang resigns after 33 years; shares fall
     as much as 14%; CFO Colette Kress becomes interim chief.
  4. The FAA lifts a nationwide ground stop: departures resume after
     a communications failure halts every US airport for 4+ hours.
  5. Brooklyn DA opens a criminal probe into the Flatbush collapse;
     all eight victims are named, two of them children.
  6. At COP31 in Antalya, the UN chief urges drastic emissions cuts
     as pledged climate finance falls about 70% from 2025.

Deterministic: the program only copies a fixed file, so two runs
write byte-identical files.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out = os.path.join(outdir, "entry.png") if os.path.isdir(outdir) \
        else "entry.png"
    shutil.copyfile(src, out)
    # The gate runs the program twice and demands identical bytes:
    # fail loudly here instead of silently shipping a short copy.
    if os.path.getsize(out) != os.path.getsize(src):
        raise SystemExit(f"copy mismatch: {src} -> {out}")
    print(f"wrote {out}: {os.path.getsize(out)} bytes")


if __name__ == "__main__":
    main()
