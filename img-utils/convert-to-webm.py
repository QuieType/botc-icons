# this script just converts to webm without adding any padding
# I'm sure there's a more efficient way to do this but this is what's working

from PIL import Image
from pathlib import Path

paths = Path("../../townsquare/src/assets/").glob("*.png")

for path in paths:
    Image.open(path).save(path.stem + ".webp")
    print("Saved " + path.name + " as " + path.stem + ".webp")