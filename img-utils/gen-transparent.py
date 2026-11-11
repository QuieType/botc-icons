# this script creates new transparent images at various sizes

from PIL import Image

oldTransparent = Image.open("transparent.webp")

# replace the tuple with the size of the new image and the string with the name
oldTransparent.resize((280, 280)).save("transparent-270.webp")