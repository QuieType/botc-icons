# The goal of this file is to pad images which reach their borders to have blank pixels around them, matching the images in the old repo
# also to convert them to webp, which I thought I'd do seperately but look! Pillow does it automatically!

# old images were 539x539 and had 100px of padding on each side
# Tiny's images are 250x250, and thus should have around 46.38px of padding on each side, which - forgive me - I'm rounding to 46
# thus the transparent base image is now 342, a number I shamefully got by googling 250+46+46 (worse, I got the above comment's info from "100/539 is what/250")
# ^ higher education, everyone!


from PIL import Image, ImageOps

old = Image.open("investigator-og.png")
transparent = Image.open("transparent.webp")
transparent.paste(old, (46, 46))
transparent.save("investigator.webp")
