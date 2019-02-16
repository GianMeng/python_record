# from tkinter import *
# root = Tk()
# root.mainloop()


# from tkinter import *
# root = Tk()
# root['background'] = 'yellow'
# root['height'] = 330
# root['width'] = 450
# root['cursor'] = 'coffee_mug'
# root.title('我的第一个窗口程序')
# root.resizable(False,False)
# root.mainloop()


# from tkinter import *
# root = Tk(className="登陆")
# label1 = Label(root)
# label1['text'] = "Hello World"
# label2 = Label(root)
# label2['text'] = "最佳拍档"
# label1.pack() # label1显示出来
# label2.pack() # label2显示出来
# root.mainloop()


# from tkinter import *
# root = Tk(className="事件处理实例") # 初始化窗口信息
# def click(event): # 定义点击事件
#     print("鼠标当前位置是[{0},{1}]".format(event.x,event.y))
#
# def keyPress(event): # 定义按键事件
#     print("按下了{0}键".format(repr(event.char)))
#
# frame = Frame(root,width=200,height=120) # 创建一个框架
# frame.bind("<Button -1>",click) # 绑定左键点击事件
# entry = Entry(root) # 添加文本框
# entry.bind("<Key>",keyPress) # 文本框添加键盘处理事件
# entry.pack() # 显示文本框
# frame.pack() # 显示框架
# root,mainloop()


# from tkinter import *
# import random
# number = random.randint(100,999)
# num = 0
# maxnum = 999
# minnum = 100
# running = True
#
# def btnCloseClick(event):
#     root.destory()
#
# def btnResetClick(event):
#     global number # 引用外部变量
#     global running # 引用外部变量
#     global num # 引用外部变量
#     global maxnum # 引用外部变量
#     global minnum # 引用外部变量
#     number = random.randint(100,999) # 重新赋值
#     running = True # 重新赋值
#     num = 0 # 重新赋值
#     labelChange("请输入100到999之间任意整数：")
#     entry_num.delete(0,'end')
#     labelRange('目前的范围是[%d，%d]'%(minnum,maxnum))
#     print(number)
#
# def btnGuessClick(event):
#     global num
#     global running
#     global maxnum
#     global minnum
#     if running:
#         answer = int(entry_num.get())
#         if answer == number:
#             labelChange("恭喜答对了！")
#             num+=1
#             running = False
#             numGuess()
#         elif answer < number:
#             num+=1
#             labelChange("小了哦")
#             if answer>minnum:
#                 minnum=answer
#         else:
#             num+=1
#             labelChange("大了哦")
#             if answer<maxnum:
#                 maxnum=answer
#         labelRange('目前的范围是[%d，%d]'%(minnum,maxnum))
#     else:
#         labelChange('你已经答对啦.')
#
# def numGuess():
#     if num == 1:
#         labelChange('好棒！一次答对！')
#
#     elif num < 9:
#         labelChange('好厉害，尝试次数：'+str(num))
#
#     elif num < 19:
#         labelChange('还行，尝试次数：'+str(num))
#     else:
#         labelChange('您都试了超过20次了。。。。尝试次数：'+str(num))
#
# def labelChange(vText): # 定义控件信息修改函数
#     label_info.config(label_info,text=vText)
#
# def labelRange(cText):
#     label_range.config(label_range,text=cText)

# import random
# secret = random.randint(1,10)
#
# temp = input("猜一下我心里想的是那个数：")
# guess = int(temp)
# times = 2
# while (guess !=secret) and (times > 0):
#   print("剩余次数" ,times)
#   guess = int(temp)
#   if guess == secret and times ==1:
#     print("卧槽，这都能猜中")
#   else:
#     if guess ==secret and times != 0:
#       print("勉强算过了")
#     else:
#       if guess > secret:
#         print("不对，不对，大了大了！")
#         times = times - 1
#       else:
#         print("哎哎，又小了小了")
#         times = times -1
#   temp = input("猜错了，再来一次吧：")
#   if times ==2:
#     print("咱俩心有灵犀啊,一下就猜对了^_^！")
#   else:
#     print("游戏结束，答案是%d,再见！"%secret)




# from tkinter import *  # 导入 Tkinter 库
#
# # 输入中文ok
# root = Tk()  # 创建窗口对象的背景色
# root.title('测试标题')
# root.geometry("500x500")
# # 创建两个列表
# li = ['C', 'python', 'php', 'html', 'SQL', 'java']
# movie = ['CSS', 'jQuery', 'Bootstrap']
# listb = Listbox(root)  # 创建两个列表组件
# listb2 = Listbox(root)
# for item in li:  # 第一个小部件插入数据
#     listb.insert(0, item)
#
# for item in movie:  # 第二个小部件插入数据
#     listb2.insert(0, item)
#
# listb.pack()  # 将小部件放置到主窗口中
# listb2.pack()
# root.mainloop()  # 进入消息循环


# import tkinter
#
#
# class Application(tkinter.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.pack()
#         self.create_widgets()
#
#     def create_widgets(self):
#         hi_there = tkinter.Button(self)
#         hi_there["text"] = "Hello World\n(点击这里)"
#         hi_there["command"] = self.say_hi
#         hi_there.pack(side="top")
#
#         button_exit = tkinter.Button(self, text="退出", fg="red", bg='blue', command=self.destroy)
#         button_exit.pack(side="bottom")
#
#         button_exit = tkinter.Button(self, text="创建输入框", fg="#ffffff", bg='#1890ff', command=self.tt)
#         button_exit.pack()
#
#     def tt(self):
#         self.entrythingy = tkinter.Entry()
#         self.entrythingy.pack()
#
#         self.contents = tkinter.StringVar()
#         self.contents.set("this is a variable")
#         self.entrythingy["textvariable"] = self.contents
#         self.entrythingy.bind('<Key-Return>', self.print_contents)
#
#     def say_hi(self):
#         print("hi there, everyone!")
#
#     def print_contents(self, event):
#         print("hi. contents of entry is now ---->", self.contents.get())
#
#
# root = tkinter.Tk()
# root.title('一个小窗口')
# root.geometry("500x500")
# app = Application(master=root)
# app.mainloop()



# from tkinter import Tk, Frame, Entry, StringVar
#
#
# class App(Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.pack()
#
#         self.entrythingy = Entry()
#         self.entrythingy.pack()
#
#         # here is the application variable
#         self.contents = StringVar()
#         # set it to some value
#         self.contents.set("this is a variable")
#         # tell the entry widget to watch this variable
#         self.entrythingy["textvariable"] = self.contents
#
#         # and here we get a callback when the user hits return.
#         # we will have the program print out the value of the
#         # application variable when the user hits return
#         self.entrythingy.bind('<Key-Return>',
#                               self.print_contents)
#
#     def print_contents(self, event):
#         print("hi. contents of entry is now ---->",
#               self.contents.get())
#
#
# root = Tk()
# root.title('一个小窗口')
# root.geometry("500x500")
# app = App(master=root)
# app.mainloop()




