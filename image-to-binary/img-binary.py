#   This is how you can turn an image into binary code, iykyk
from PIL import Image
im = Image.open('py.webp')
pixels = list(im.getdata())
print(pixels)

#   type this: python3 img-binary.py >output.txt