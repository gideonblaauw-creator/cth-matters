#!/usr/bin/env python3
"""Rasterize three-party-schema.svg to a PNG at least 2400px wide.

Requires Google Chrome and the Open Sans files in ./fonts (SIL Open Font License).
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
SVG = ROOT / "three-party-schema.svg"
PNG = ROOT / "three-party-schema.png"
WIDTH, HEIGHT = 3508, 2480

CHROME = [
    "google-chrome",
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--disable-background-networking",
    "--disable-sync",
    "--no-first-run",
    "--force-device-scale-factor=1",
    "--hide-scrollbars",
    "--timeout=15000",
    "--user-data-dir=/tmp/chrome-schema-profile",
    f"--window-size={WIDTH},{HEIGHT}",
    f"--screenshot={PNG}",
]


def assert_no_red(image: Image.Image) -> None:
    """Reject a pixel whose red channel leads green and blue by a clear margin."""
    from PIL import ImageChops

    red, green, blue = image.convert("RGB").split()
    # Saturated red only. Subpixel antialiasing can leave a warm gray fringe
    # (about 209, 158, 156) on navy text; that is not a red mark.
    high = red.point(lambda value: 255 if value > 190 else 0)
    over_green = ImageChops.subtract(red, green).point(lambda value: 255 if value > 80 else 0)
    over_blue = ImageChops.subtract(red, blue).point(lambda value: 255 if value > 80 else 0)
    lead = ImageChops.multiply(ImageChops.multiply(high, over_green), over_blue)
    if lead.getbbox():
        raise SystemExit(f"Red pixels inside {lead.getbbox()}")


def main() -> None:
    if not SVG.is_file():
        raise SystemExit(f"Missing {SVG}. Run build_schema.py first.")
    try:
        subprocess.run([*CHROME, SVG.as_uri()], check=True, timeout=8)
    except subprocess.TimeoutExpired:
        if not PNG.is_file():
            raise SystemExit("Chrome timed out before writing the PNG")
    image = Image.open(PNG)
    if image.width < 2400:
        raise SystemExit(f"PNG width {image.width} is below 2400")
    if image.size != (WIDTH, HEIGHT):
        raise SystemExit(f"Expected {WIDTH}x{HEIGHT}, got {image.size}")
    aspect = image.width / image.height
    if abs(aspect - (297 / 210)) > 0.02:
        raise SystemExit(f"Aspect {aspect:.4f} is not A4 landscape")
    assert_no_red(image)
    print(f"wrote {PNG} ({image.width}x{image.height})")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as exc:
        sys.exit(exc.returncode)
