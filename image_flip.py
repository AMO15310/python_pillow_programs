#flip an image using python
import PIL
from PIL import Image
image1 = Image.open(r"/put the path of the image here ")
fliped_image = image1.transpose(Image.FLIP_LEFT_RIGHT)
fliped_image.show()

