# The goal of this file is to pad images which reach their borders to have blank pixels around them, matching the images in the old repo
# also to convert them to webp, which I thought I'd do seperately but look! Pillow does it automatically!

# Tiny's images are 250x250 with little to no padding
# old images were 539x539 and had ~100 px of padding, but were inconsistent and seemed to have padding per image
# with tiny's art I'm just going for 75 px of padding and calling it a day
# sorry

from PIL import Image
from pathlib import Path

paths = Path("../PNG/").glob("*.png")
for path in paths:
    old = Image.open(path)
    transparent = Image.open("transparent-400.webp")
    transparent.paste(old, (75, 75))
    transparent.save(path.stem + ".webp")
    print("Saved " + path.name + " as " + path.stem + ".webp")
