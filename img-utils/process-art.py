# The goal of this file is to pad images which reach their borders to have blank pixels around them, matching the images in the old repo

# TODO: figure out how much padding images currently have


from PIL import Image, ImageOps

old = Image.open("investigator-og.png")
transparent = Image.open("transparent.webp")
transparent.paste(old)
transparent.save("investigator.webp")
