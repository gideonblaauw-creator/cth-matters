#!/usr/bin/env python3
"""Composite official CleantechHUB lockups and lock spelling on the 30s stills.

Brand sources (Google Drive folder LOGO CLEANTECHHUB,
id 1qmmGFt2lmATLSp0DAHshwzjoXyvPqSlR):
  brand/LOGO_AZUL_OSCURO.png  Drive 1h90Y06V66C-OxMBVcSbtSU17s96SN-pa
  brand/LOGO_BLANCO.png       Drive 1nf_WWiN8HPhfXeZ8bhDPhgz8kGqgeazM  (title: LOGO BLANCO ai.png)

Image models misspell Data Town / Bucaramanga / the tagline and invent swirl marks.
This script pastes the Drive PNGs and sets type in Inter.
"""

from __future__ import annotations

import os
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
BRAND = ROOT / "brand"
STILLS = ROOT / "stills"
# Masters live in stills/. Re-running type overlays on them is safe.
BASE = Path(os.environ.get("CTH_PLATES", STILLS))
OUT_DIR = Path(os.environ.get("CTH_OUT", STILLS))
QA_DIR = Path("/tmp/qa5")
FONT_DIR = Path("/usr/share/fonts/truetype/macos")

DEEP_BLUE = (12, 73, 138)  # #0C498A
TENT_BLUE = (9, 64, 152)
WALL_BLUE = (0, 45, 122)
DOME_BLUE = (44, 103, 181)
CYAN = (178, 238, 250)  # #B2EEFA
WHITE = (255, 255, 255)
PLAQUE = (252, 252, 253)


def trim_rgba(im: Image.Image) -> Image.Image:
    a = np.array(im)
    ys, xs = np.where(a[:, :, 3] > 12)
    return im.crop((int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1))


def scale_w(im: Image.Image, width: int) -> Image.Image:
    h = max(1, round(im.height * width / im.width))
    return im.resize((width, h), Image.Resampling.LANCZOS)


def paste_logo(base: Image.Image, logo: Image.Image, xy: tuple[int, int], width: int) -> tuple[int, int]:
    lg = scale_w(trim_rgba(logo), width)
    base.paste(lg, xy, lg)
    return lg.size


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_DIR / name), size)


def _clone_sky_strip(im: Image.Image, src: tuple[int, int, int, int], dest: tuple[int, int, int, int]) -> None:
    """Stretch a real sky patch over a leftover plate without flattening the gradient."""
    patch = im.crop(src).resize((dest[2] - dest[0], dest[3] - dest[1]), Image.Resampling.LANCZOS)
    im.paste(patch, (dest[0], dest[1]))


def scene_01(azul: Image.Image) -> Image.Image:
    """Official dark-blue lockup already sits on the sky plate — keep it."""
    return Image.open(BASE / "01-origen.png").convert("RGB")


def _paint_light_on_dome(im: Image.Image) -> None:
    """Replace leftover white wordmark pixels on the blue dome only."""
    arr = np.array(im)
    y0, y1, x0, x1 = 120, 200, 1032, 1225
    patch = arr[y0:y1, x0:x1]
    r, g, b = patch[:, :, 0], patch[:, :, 1], patch[:, :, 2]
    # Wordmark is pale on mid-blue dome. Sky is brighter and more cyan — skip it.
    light = (r > 170) & (g > 170) & (b > 170)
    leftover = ((r > 150) & (g > 150) & (b > 180) & (r + g + b > 520)) | light
    # Restrict to the lower dome band so we do not paint clouds.
    yy = np.arange(y0, y1)[:, None]
    on_dome = yy >= 138
    mask = leftover & on_dome
    # Dilate a little so antialiased edges go too.
    m = Image.fromarray((mask.astype(np.uint8) * 255)).filter(ImageFilter.MaxFilter(5))
    mask = np.array(m) > 127
    patch[mask, :3] = np.array(DOME_BLUE, dtype=np.uint8)
    arr[y0:y1, x0:x1] = patch
    im.paste(Image.fromarray(arr))


def scene_02(azul: Image.Image, blanco: Image.Image) -> Image.Image:
    im = Image.open(BASE / "02-town.png").convert("RGBA")
    draw = ImageDraw.Draw(im)

    # Keep the official white lockup already on the valance; replace misspelled type.
    draw.rectangle((698, 155, 1048, 258), fill=TENT_BLUE)
    draw.rectangle((688, 172, 691, 248), fill=WHITE)
    draw.text((708, 172), "Data Town", font=font("Inter-SemiBold.ttf", 30), fill=WHITE)
    draw.text((708, 212), "Bucaramanga", font=font("Inter-SemiBold.ttf", 26), fill=WHITE)

    # Restore sky where a prior pass painted a blue rectangle into the air.
    _clone_sky_strip(im, (980, 70, 1100, 155), (1168, 70, 1280, 155))
    _paint_light_on_dome(im)

    # Counter already has the official dark lockup; leave it.
    return im.convert("RGB")


def scene_03(_azul: Image.Image) -> Image.Image:
    # Sign already carries the Drive lockup.
    return Image.open(BASE / "03-lake.png").convert("RGB")


def scene_04(_azul: Image.Image) -> Image.Image:
    im = Image.open(BASE / "04-lakehouse.png").convert("RGBA")
    draw = ImageDraw.Draw(im)
    draw.rectangle((1134, 288, 1264, 330), fill=PLAQUE)
    draw.text((1144, 296), "lake house", font=font("Inter-Medium.ttf", 16), fill=DEEP_BLUE)
    return im.convert("RGB")


def scene_05(_azul: Image.Image) -> Image.Image:
    return Image.open(BASE / "05-lab.png").convert("RGB")


def scene_06(_azul: Image.Image, _blanco: Image.Image) -> Image.Image:
    """Keep the Drive white lockup; replace Inspirera / Acttúa / Weeket in Inter."""
    im = Image.open(BASE / "06-climate-week.png").convert("RGBA")
    draw = ImageDraw.Draw(im)
    draw.rectangle((360, 268, 920, 352), fill=WALL_BLUE)

    tag = "Inspira. Actúa. Transforma."
    f_tag = font("Inter-SemiBold.ttf", 28)
    f_week = font("Inter-Medium.ttf", 22)
    bbox = draw.textbbox((0, 0), tag, font=f_tag)
    tw = bbox[2] - bbox[0]
    tx = 640 - tw // 2
    ty = 276
    draw.text((tx, ty), tag, font=f_tag, fill=WHITE)
    draw.rectangle((tx, ty + 36, tx + tw, ty + 38), fill=CYAN)
    week = "Climate Data Week"
    ww = draw.textbbox((0, 0), week, font=f_week)[2]
    draw.text((640 - ww // 2, ty + 44), week, font=f_week, fill=WHITE)
    return im.convert("RGB")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    QA_DIR.mkdir(parents=True, exist_ok=True)
    STILLS.mkdir(parents=True, exist_ok=True)
    azul = Image.open(BRAND / "LOGO_AZUL_OSCURO.png").convert("RGBA")
    blanco = Image.open(BRAND / "LOGO_BLANCO.png").convert("RGBA")

    frames = {
        "01-origen.png": scene_01(azul),
        "02-town.png": scene_02(azul, blanco),
        "03-lake.png": scene_03(azul),
        "04-lakehouse.png": scene_04(azul),
        "05-lab.png": scene_05(azul),
        "06-climate-week.png": scene_06(azul, blanco),
    }
    crops = {
        "01-origen.png": (780, 0, 1280, 180),
        "02-town.png": (300, 120, 1100, 280),
        "03-lake.png": (520, 260, 860, 400),
        "04-lakehouse.png": (1050, 180, 1280, 480),
        "05-lab.png": (0, 0, 700, 160),
        "06-climate-week.png": (250, 40, 1030, 360),
    }
    extra = {
        "02-building.png": ("02-town.png", (1080, 80, 1280, 220)),
        "06-tagline.png": ("06-climate-week.png", (350, 250, 950, 370)),
    }
    for name, im in frames.items():
        dest = OUT_DIR / name
        im.save(dest, "PNG")
        im.save(STILLS / name, "PNG")
        im.crop(crops[name]).save(QA_DIR / f"crop-{name}")
        print(f"wrote {dest} {im.size}")
    for qa_name, (src, box) in extra.items():
        frames[src].crop(box).save(QA_DIR / qa_name)
        print(f"wrote qa {qa_name}")


if __name__ == "__main__":
    main()
