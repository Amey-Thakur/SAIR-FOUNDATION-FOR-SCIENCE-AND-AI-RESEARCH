# ==============================================================================
# File: build_header.py
# Description: Builds the header plate for the index README. SAIR's own mark and
#   wordmark are white with transparency, so dropped straight into a README they
#   vanish on GitHub's light theme. Compositing them onto the SAIR aubergine
#   gives one image that reads correctly in both themes, which is the only
#   reason this script exists.
# Usage: python .github/scripts/build_header.py assets/sair-header.png
# Tech Stack: Python 3.10+, Pillow
# ==============================================================================

import os
import sys

from PIL import Image, ImageDraw, ImageFont

W, H = 1000, 260
SS = 3

GROUND = (0x34, 0x08, 0x25)      # the SAIR card colour
INK = (0xF5, 0xF5, 0xF5)
DIM = (0xC9, 0xA9, 0xB8)

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "..", "assets")
UI = "C:/Windows/Fonts/segoeui.ttf"

STRAP = "Foundation for Science and AI Research"


def main(out):
    im = Image.new("RGB", (W * SS, H * SS), GROUND)

    logo = Image.open(os.path.join(ASSETS, "sair-logo.png")).convert("RGBA")
    target_w = 420
    scale = target_w / logo.width
    logo = logo.resize((round(target_w * SS), round(logo.height * scale * SS)),
                       Image.LANCZOS)

    d = ImageDraw.Draw(im)
    font = ImageFont.truetype(UI, round(21 * SS))
    strap_w = d.textlength(STRAP, font=font)

    # the logo and the strapline are centred as one block
    gap = 26
    block_h = logo.height / SS + gap + 21
    top = (H - block_h) / 2

    im.paste(logo, (round((W * SS - logo.width) / 2), round(top * SS)), logo)
    d.text(((W * SS - strap_w) / 2, (top + logo.height / SS + gap) * SS),
           STRAP, font=font, fill=DIM)

    im = im.resize((W, H), Image.LANCZOS)
    im.save(out)
    print(f"  {os.path.basename(out)}: {os.path.getsize(out) // 1024} KB, {W}x{H}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else
         os.path.join(ASSETS, "sair-header.png"))
