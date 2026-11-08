# The goal of this file is to pad images which reach their borders to have blank pixels around them, matching the images in the old repo

# TODO: figure out how much padding images currently have


from PIL import Image, ImageOps

size = (300, 300)
with Image.open("Screenshot_20261108_110048.png") as im:
    ImageOps.pad(im, size, color="#ff0000").save("investigator_padded.webp")

# this doesn't work bc .pad actually only pads if it changes the aspect ratio
# idea: resize image, then paste on a transparent image instead