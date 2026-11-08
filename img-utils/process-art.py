# The goal of this file is to pad images which reach their borders to have blank pixels around them, matching the images in the old repo

# TODO: figure out how much padding images currently have


from PIL import Image, ImageOps

oldTransparent = Image.open("transparent.png")
oldTransparent.resize((300, 300)).save("transparentnew.webp")

# this doesn't work bc .pad actually only pads if it changes the aspect ratio
# idea: resize image, then paste on a transparent image instead