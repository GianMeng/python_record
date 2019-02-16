from PIL import ImageChops,Image,ImageFilter
import os,time

image1 =Image.open('lyf.jpg')
image2 =Image.open('baoer.jpg')
aval = []
STA = time.time()
# img=ImageChops.invert(image2)
# img = ImageChops.multiply(image1, image2)
# img = ImageChops.lighter(image1, image2)
# img = ImageChops.darker(image1, image2)
# img = ImageChops.screen(image1, image2)
# img = ImageChops.add(image1, image2)
# img = image2.filter(ImageFilter.CONTOUR)
# img = img.filter(ImageFilter.EMBOSS)
# img.save("aa.jpg")

root = os.getcwd() + "/"
for i in os.listdir(root):  # 返回src路径下的文件和文件夹列表
    print(os.path.splitext(root + i)[-1])
    # print(i)
    # if os.path.splitext(root + i)[-1] == ".jpg" or os.path.splitext(root + i)[-1] == ".png":
    #     aval.append(root + i)
    # print("Time is %s" % (time.time() - STA))