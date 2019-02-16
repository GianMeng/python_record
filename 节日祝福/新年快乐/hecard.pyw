""" 065_新年快乐动态音乐贺卡.py
   本程序使用python3.4，需要准备枕头模块(PIL在python3中已更名为pillow模块)
   制作日期：2017年元月17日
   作者：李兴球，QQ:406273900
   
"""

from winsound import PlaySound,SND_ASYNC
from turtle import *
from time import sleep
from random import randint
import os,sys

import time
from tkinter import messagebox
import imp
 


#检测有没有安装图像处理的PIL模块，安装方法为在命令提示符里输入： pip3 install pillow
try:
    imp.find_module('PIL')
    from PIL import Image, ImageSequence
except:
    messagebox.showinfo("www.scratch8.net"," 枕头模块没有安装，请在命令提示符里输入：\n\n pip3 install pillow \n\nQQ:406273900")
    sys.exit()
    

网址="http://www.HaLiFa.net/download/heka.rar"

if not os.path.exists("turtle.cfg"):
    messagebox.showinfo("www.scratch8.net"," ' turtle.cfg' 配置文件丢失啦! \n\n请重新下载,并把此文件放到和本程序同一文件夹.\n\nQQ:406273900\n\n下载网址：" + 网址)
    sys.exit()

if not os.path.exists("新年快乐.gif"):
    messagebox.showinfo("www.scratch8.net"," '新年快乐.gif' 文件丢失啦! \n\n请重新下载,并把此文件放到和本程序同一文件夹.\n\nQQ:406273900\n\n下载网址：" + 网址)
    sys.exit()

if not os.path.exists("中国娃娃 - 发财发福中国年.wav"):
    messagebox.showinfo("www.scratch8.net"," '中国娃娃 - 发财发福中国年.wav' 文件丢失啦! \n\n请重新下载,并把这个文件放到和本程序同一文件夹.\n\nQQ:406273900\n\n下载网址：" + 网址)
    sys.exit()
    
if not os.path.exists("发财发福中国年歌词.lrc"):
    messagebox.showinfo("www.scratch8.net"," '发财发福中国年歌词.lrc' 文件丢失啦! \n\n请重新下载,并把这个文件放到和本程序同一文件夹.\n\nQQ:406273900\n\n下载网址：" + 网址)
    sys.exit()


图像 = Image.open('新年快乐.gif')  #载入图片
w,h=图像.size
#ImageSequence.Iterator(图象) 能返回图形中的每一帧。

index = 1
图形列表=[]
#解成帧放到"图形列表"中.
for frame in ImageSequence.Iterator(图像):  #对于图形中的每一帧
    文件名="新年快乐" + str(index) + ".png"
    frame.save(文件名)
    图形列表.append(文件名)
    index += 1

print( "拆分gif完毕！共拆成了" + str(index-1) + "张图片")

小虹=Turtle()
小虹.pencolor("white")
小虹.penup()
小虹.speed(0)
小虹.hideturtle()
屏幕=小虹.getscreen()    #得到小虹所在的画图屏幕,get是得到的意思，screen是屏幕的意思。
屏幕.setup(w,h)          #w,h是图像的宽度和高度
屏幕.title("中国娃娃-发财发福中国年 www.scratch8.net 星空培训(萍乡神猫科技有限公司)祝大家新年快乐.")

屏幕.bgcolor((0,0,51))

#2018年元旦加的按空格键开始
小虹.setx(-100)
for 字 in '按空格键开始':
    小虹.write(字,font=("",20,"normal"))
    sleep(0.2)
    小虹.setx(小虹.xcor()+30)
    
space_start=True

def startdemo():
    global space_start
    space_start=False
屏幕.onkey(startdemo,"space")
屏幕.listen()
while space_start:
    sleep(1)
    屏幕.update()
小虹.clear()
#按空格键开始程序段结束


for i in range(30):
    小虹.goto(randint(-300,250),randint(-150,150))
    小虹.dot(randint(1,3))

小虹.color("cyan")
小虹.goto(-150,100)
for 字 in '星空培训':
    小虹.write(字,font=("微软雅黑",44,"normal"))
    sleep(0.3)
    小虹.setx(小虹.xcor()+80)

小虹.color("yellow")
小虹.goto(-280,0)
for 字 in '祝大家新年快乐，身体健康，万事如意！':
    小虹.write(字,font=("",20,"normal"))
    sleep(0.2)
    小虹.setx(小虹.xcor()+30)


小虹.color("white")
小虹.goto(-200,-50)
for 字 in '制作日期：2017年元旦！ 作者：李兴球':
    小虹.write(字,font=("",10,"normal"))
    sleep(0.1)
    小虹.setx(小虹.xcor()+20)


小虹.color("yellow")
小虹.goto(-250,-120)
for 字 in '本python程序源代码下载网址：':
    小虹.write(字,font=("",10,"normal"))
    sleep(0.1)
    小虹.setx(小虹.xcor()+15)


小虹.color("yellow")
小虹.goto(-250,-150)

小虹.write(网址,font=("",10,"normal"))

#新建小明角色用来显示倒计时数字
小明=Turtle(visible=False)
小明.pencolor("yellow")
小明.goto(0,30)
倒数=5
for i in range(倒数,-1,-1):
    小明.clear()
    小明.write(i,align='center',font=("",50,"normal"))
    sleep(1)
    
小明.clear()
小虹.clear()


小虹.color("white")
指针=0
def 动态背景():
    global 指针
    
    屏幕.bgpic(图形列表[指针])
    指针=指针+1
    指针=指针 % 5
    屏幕.ontimer(动态背景,100)  #一百豪秒后再次调用“动态背景”，换个图片罢了。
    
动态背景()

小虹.goto(0,-230)
歌曲文件="中国娃娃 - 发财发福中国年.wav"
歌词文件="发财发福中国年歌词.lrc"
歌词列表=[]
歌词指针=0

f=open(歌词文件)
歌词=f.readlines()        #由于有换行，是多余的，所以下面要去除换行 \n
f.close()
歌词列表=[]
for 行 in 歌词:
    if 行!='\n':
        歌词列表.append(行)
  
歌词行数=len(歌词列表)
#print(歌词列表)
PlaySound(歌曲文件, SND_ASYNC) #异步播放音效

def 获取时间轴(指针):    
    songtime=歌词列表[指针]
    songtime=songtime.split("]")[0]
    songtime=songtime.split(":")
    songtimef=songtime[0][1:3]
    songtimef=int(songtimef)*60    
    songtimem=float(songtime[1])
    return int((songtimef+songtimem)*1000)

#for i in range(歌词行数):
   #print(获取时间轴(i))
print("歌词行数:" + str(歌词行数))

歌词指针=0
开始时间=time.time()
def 显示字幕():
    global 歌词指针
    global 歌词行数
    
    当前时间=time.time()
    运行时间=(当前时间-开始时间)*1000
    屏幕.title("星空培训Python少儿编程动态音乐贺卡制作。" + str(运行时间))
    if 获取时间轴(歌词指针)<运行时间:
        小虹.clear()
        显示歌词=歌词列表[歌词指针].split("]")[1]
        小虹.goto(0,-230)
        小虹.pencolor("black")
        小虹.write(显示歌词,align='center',font=("",24,"normal"))
        小虹.goto(-1,-229)
        小虹.pencolor("white")
        小虹.write(显示歌词,align='center',font=("",24,"normal"))
        
        print("当前歌词指针：" + str(歌词指针) + "，歌词：" + 显示歌词) 
        歌词指针=歌词指针+1
    if 歌词指针<歌词行数:        
        屏幕.ontimer(显示字幕,100)
        
显示字幕()

c = 小虹.getscreen()
c.mainloop()
 

