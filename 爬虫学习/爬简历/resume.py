#coding:utf-8
import re
import os
import sys
import random
import requests
from bs4 import BeautifulSoup

url = 'http://sc.chinaz.com/jianli/free_'
headers = {'User-Agent':'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1'}
#定义列表存放多个下载源
downloadFrom = ['fjdx','xmdx','gddx','jsdx','fjlt','zjlt',
                'xmlt','gdlt','fjyd','sxyd','xmyd','zjyd']
#在当前目录下创建文件夹
try:
    os.mkdir(r'站长之家个人简历模板')
except Exception:
    pass
finally:
    os.chdir(r'站长之家个人简历模板')

for pageNumber in range(2,425):
    try:
        page = requests.get(url=url+str(pageNumber)+'.html',headers=headers)
        page.encoding = 'utf-8'
        soup = BeautifulSoup(page.text,'lxml')
        info = soup.find_all('img')[1:]
    except Exception:
        print('可能遇到了一些问题，脚本即将退出运行！')
        print('目前已经爬取到了第'+str(pageNumber)+'页，下次可从这里继续开始！')
        sys.exit()
    for tag in info:
        name = tag['alt']
        num  = re.search('jianli.*_',tag['src']).group()[:-1]
        rd = random.choice(downloadFrom)
        downloadUrl = 'http://'+rd+'.sc.chinaz.com/Files/DownLoad/'+num+'.rar'
        try:
            document = requests.get(url =downloadUrl ,headers=headers)
            filename = name + rd +'.rar'
            with open(filename,'wb') as f:
                f.write(document.content)
            print('文件 '+ filename +' 已下载完成！')
        except Exception:
            print('文件 ' + filename + ' 下载失败并忽略！')
            pass
print('目前已经爬取到了第'+str(pageNumber)+'页！')