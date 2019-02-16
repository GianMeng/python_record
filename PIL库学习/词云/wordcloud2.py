# 生成中文
import chardet
import jieba
import os
from os import path
import numpy as np
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from PIL import Image
from matplotlib import pyplot as plt
from scipy.misc import imread
import random

# 获取当前文件路径
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
# 获取文本text,确定编码格式
text = open(path.join(d,'langchao.txt'),'rb').read()
text_charInfo = chardet.detect(text)
print(text_charInfo)
text=text.decode(text_charInfo['encoding'])
# text+=' '.join(jieba.cut(text,cut_all=False)) # cut_all=False 表示采用精确模式
# 设置中文字体
font_path = 'C:\Windows\Fonts\simfang.ttf'  # 思源黑体
# 读取背景图片
background_Image = np.array(Image.open(path.join(d, "6.jpg")))
# 提取背景图片颜色
img_colors = ImageColorGenerator(background_Image)
# 设置中文停止词
stopwords = set('')
stopwords.update(['但是','一个','自己','因此','没有','很多','可以','这个','虽然','因为','这样','已经','现在','一些','比如','不是','当然','可能','如果','就是','同时','比如','这些','必须','由于','而且','并且','他们'])


wc = WordCloud(
        font_path = font_path, # 中文需设置路径
        margin = 2, # 页面边缘
        mask = background_Image,
        scale = 2,
        max_words = 200, # 最多词个数
        min_font_size = 4, #
        stopwords = stopwords,
        random_state = 42,
        background_color = 'white', # 背景颜色
        # background_color = '#C3481A', # 背景颜色
        max_font_size = 100,
        ).generate(text.lower())

wc.generate(text)
# 获取文本词排序，可调整 stopwords
process_word = WordCloud.process_text(wc,text)
sort = sorted(process_word.items(),key=lambda e:e[1],reverse=True)
print(sort[:50]) # 获取文本词频最高的前50个词
# 设置为背景色，若不想要背景图片颜色，就注释掉
wc.recolor(color_func=img_colors)
# 存储图像
wc.to_file('傻猪4.png')
# 显示图像
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
plt.show()