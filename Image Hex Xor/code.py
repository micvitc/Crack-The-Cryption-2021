import re
from PIL import Image
import binascii

# Read Images
def imgToHex(file):
    with open(file, 'rb') as f:
        content = f.read()
   
    return (binascii.hexlify(content))

secretHex="3b69"
file="" #give your image path
hexValue=imgToHex(file)
xorhex=hex(int(hexValue, 16)^int(secretHex, 16))
print(xorhex)

xorhex=xorhex[2:]

data = bytes.fromhex(xorhex)
with open('image.png', 'wb') as file:
    file.write(data)