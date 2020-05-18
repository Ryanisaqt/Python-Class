from PIL import Image, ImageFilter
import time
pic=Image.open('C:/Users/congd/Downloads/index.jpg')
print("needle will arrive soon")
time.sleep(1)
print("haha jk its dog")
time.sleep(1)
pic.show()
from PIL import ImageEnhance
enh=ImageEnhance.Contrast(pic)
#enh.enhance(-2).show()
size_tuple=pic.size
print(size_tuple)
sizelist=list(size_tuple)
newwidth=sizelist[0]*3
newheight=sizelist[1]*5
newsize=(newwidth,newheight)
img_resized=pic.resize(newsize)
img_resized.show()
