from PIL import Image, ImageDraw, ImageFont
from numpy import asarray
import numpy as np

a = []
for i in range(500):
  b = []
  for j in range(500):
    b.append((255,255,255))
  a.append(b)
img = Image.fromarray(np.array(a).astype(np.uint8))
myFont = ImageFont.truetype('FreeMono.ttf', 80)
d1 = ImageDraw.Draw(img)
d1.text((200, 300), "BOAT", font=myFont, fill =(0, 255, 0))
d1.text((200, 200), "DOG", font=myFont, fill =(255, 0, 0))
d1.text((125, 100), "PLANE", font=myFont, fill =(0, 0, 255))
img.save("words.png")

