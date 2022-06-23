import PIL 
from PIL import Image,ImageDraw
image1 = Image.open(r"/put the image path here/")
d1 = ImageDraw.Draw(image1)
d1.text((32,50),"Here's my text!!! Hello there!!",fill=(255,255,0))
image1.show()
