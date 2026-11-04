# The goal of this file is to pad images which reach their borders to have blank pixels around them, matching the images in the old repo

# TODO: figure out how much padding images currently have


from PIL import Image, ImageOps

size = (300, 300)
with Image.open("investigator.webp") as im:
    ImageOps.pad(im, size, color="#f00").save("investigator_padded.webp")