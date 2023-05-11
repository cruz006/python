#   This is how you can turn an image into binary code
from PIL import Image
im = Image.open('py.webp')
pixels = list(im.getdata())
print(pixels)

#   type this: python3 convert.py>output.txt