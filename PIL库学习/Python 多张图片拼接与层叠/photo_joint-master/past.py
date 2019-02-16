# -*- coding: utf-8 -*-

#
# @note: 这里两张照片层叠选择的方法是：正片叠底
#   结果色 = 混合色 * 基色 / 255
#
# @description:
#   1. 明度变化：混合色不会大于255，故结果色一定小于1，混合模式之后必定比基色暗。
#   0为黑色，若混合两色中有黑色，混合之后必定是黑色。若有白色，则混合色为另外一色
#   的原色。
#   故正片叠底可以改变非黑即白，处于灰度区间的明度，变黑。
#   可以采用操作像素点，提高像素点的亮度
#

from __future__ import division

from PIL import Image, ImageFont, ImageDraw
import numpy
import os
import random
import time


STAG = time.time()      #返回当前时间的时间戳

# W_num: 一行放多少张照片
# H_num: 一列放多少张照片
# W_size: 照片宽为多少
# H_size: 照片高为多少
# root: 脚本的根目录
root = ""
root_photo = "baoer3.jpg"
W_num = 10
H_num = 10
W_size = 640
H_size = 640

# aval: 存放所有照片的路径
alpha = 0.1
aval = []


# name: transfer
# todo: 将照片转为一样的大小
def transfer(img_path, dst_width, dst_height):

    STA = time.time()
    im = Image.open(img_path)
    if im.mode != "RGBA":       #im.mode返回的是字符串,图像模式
        im = im.convert("RGBA") #将图像转化为RGBA模式
    s_w, s_h = im.size          #返回值为宽度和高度的二元组（width, height）
    #高比宽长时就旋转图像
    # if s_w < s_h:
    #     im = im.rotate(90)

    # 这4行是都压缩到同样大小，所以没有间隔
    if dst_width*0.1/s_w > dst_height*0.1/s_h:
       ratio = dst_width*0.1/s_w
    else:
       ratio = dst_height*0.1/s_h
    resized_img = im.resize((dst_width, dst_height), Image.ANTIALIAS)
    #im.resize(size, filter)重新设定大小，ANTIALIAS滤镜缩放（高质量缩放）
    resized_img = resized_img.crop((0, 0, dst_width, dst_height))
    #im.crop(box):box为图片四个角坐标
    #将resized_img表示的图片对象拷贝到resized_img中，大小为box
    print ("transfer Func Time %s" % (STAG - STA))

    return resized_img

# name: getAllPhotos
# todo: 获得所有照片的路径


def getAllPhotos():
    STA = time.time()
    root = os.getcwd() + "/"        #os.getcwd()用于返回当前工作目录
    src = root + "/photos1/"        #root下的图片文件夹路径
    for i in os.listdir(src):       #返回src路径下的文件和文件夹列表,所以i是文件名称
        if os.path.splitext(src + i)[-1] == ".jpg" or os.path.splitext(src + i)[-1] == ".png":
            aval.append(src + i)
        #os.path.splitext(src + i)是分割路径，返回路径名和文件扩展名（类似.jpg这种）
        #src+i即路径+名称，(src+i)[-1]即名称后缀（类似.jpg这种）
    print ("getAllPhotos Func Time %s" % (STAG - STA))

# name: createNevImg
# todo: 创建一张新的照片并保存


def createNevImg():
    STAA = time.time()
    iW_size = W_num * W_size    #新图片宽
    iH_size = H_num * H_size    #新图片高
    # print (root)
    I = numpy.array(transfer(root + root_photo, iW_size, iH_size)) * 1.0

    for i in range(W_num):
        for j in range(H_num):
            s = random.choice(aval)
            res = I[j * H_size:(j + 1) * H_size, i * W_size:(i + 1) * W_size] * numpy.array(transfer(s, W_size, H_size)) / 255
            #numpy.array(transfer(s, W_size, H_size)基色
            #I[j * H_size:(j + 1) * H_size, i * W_size:(i + 1) * W_size]混合色
            I[j * H_size:(j + 1) * H_size, i * W_size:(i + 1) * W_size] = res

    img = Image.fromarray(I.astype(numpy.uint8))
    img = img.point(lambda i: i * 1.5)  #对每个点进行50%的加强
    if len(img.split())==4:
        r, g, b, a = img.split()  # 利用split和merge将通道从四个转换为三个
        img = Image.merge("RGB", (r, g, b))
        img.save("createNevImg_past.jpg")
    print ("createNevImg Func time %s" % (STAG - STAA))


# name: newRotateImage
# todo: 将createnevimg中得到的照片旋转，粘贴到另外一张照片中
def newRotateImage():
    imName = "createNevImg_past.jpg"
    print ("正在将图片旋转中...")
    STA = time.time()
    im = Image.open(imName)
    im2 = Image.new("RGBA", (W_size * int(W_num + 1), H_size * (H_num + 4)))    #创建新图片
    im2.paste(im, (int(0.5 * W_size), int(0.8 * H_size)))   #图像粘贴,im.paste(region,box):粘贴box大小的region到原先的图片对象中
    im2 = im2.rotate(359)
    if len(im2.split())==4:
        r, g, b, a = im2.split()  # 利用split和merge将通道从四个转换为三个
        im2 = Image.merge("RGB", (r, g, b)) #将r,g两个通道进行翻转
        im2.save("newRotateImage_past.jpg")
    print ("newRotateImage Func Time %s" % (STAG - STA))


# name: writetoimage
# todo: 在图片中写祝福语
def writeToImage():
    print ("正在向图片中添加祝福语...")
    STA = time.time()
    img = Image.open("newRotateImage_past.jpg")
    font = ImageFont.truetype('xindexingcao57.ttf', 600)
    #加载一个TrueType或者OpenType字体文件，并且创建一个字体对象
    draw = ImageDraw.Draw(img)
    #创建一个可用来对image进行操作的对象。对所有即将使用ImageDraw中操作的图片都要先进行这个对象的创建
    draw.ink = 21 + 118 * 256 + 65 * 256 * 256  #画笔颜色

#    draw.text((0,H_size * 6),unicode("happy every day",'utf-8'),(0,0,0),font=font)

    tHeight = H_num + 1
    draw.text((W_size * 0.5, H_size * tHeight), "宝儿姐又要埋人了", font=font)
    # if len(img.split())==4:
    #     r, g, b, a = img.split()  # 利用split和merge将通道从四个转换为三个
    #     img = Image.merge("RGB", (r, g, b))
    #     img.save("final_past.jpg")
    img.save("final_past.png")
    print ("writeToImage Func Time %s" % (time.time() - STA))


# name:
# todo: 入口函数
if __name__ == "__main__":

    getAllPhotos()
    createNevImg()
    newRotateImage()
    writeToImage()
    print ("Total Time %s" % (time.time() - STAG))
