'''
Function:
	百度翻译小爬虫
作者:
	Charles
公众号:
	Charles的皮卡丘
'''
import re
import js
import sys
import time
import js2py
import requests
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QLineEdit, QPushButton


'''
Function:
	百度翻译类
'''
class baidu():
	def __init__(self):
		self.session = requests.Session()
		self.session.cookies.set('BAIDUID', '19288887A223954909730262637D1DEB:FG=1;')
		self.session.cookies.set('PSTM', '%d;' % int(time.time()))
		self.headers = {
							'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
						}
		self.data = {
						'query': '',
						'simple_means_flag': '3',
						'sign': '',
						'token': '',
					}
		self.url = 'https://fanyi.baidu.com/v2transapi'
	def translate(self, word):
		self.data['query'] = word
		self.data['token'], gtk = self.getTokenGtk()
		self.data['token'] = '6482f137ca44f07742b2677f5ffd39e1'
		self.data['sign'] = self.getSign(gtk, word)
		res = self.session.post(self.url, data=self.data)
		return res.json()['trans_result']['data'][0]['result'][0][1]
	def getTokenGtk(self):
		url = 'https://fanyi.baidu.com/'
		res = requests.get(url, headers=self.headers)
		token = re.findall(r"token: '(.*?)'", res.text)[0]
		gtk = re.findall(r";window.gtk = ('.*?');", res.text)[0]
		return token, gtk
	def getSign(self, gtk, word):
		evaljs = js2py.EvalJs()
		js_code = js.js_code
		js_code = js_code.replace('null !== i ? i : (i = window[l] || "") || ""', gtk)
		evaljs.execute(js_code)
		sign = evaljs.e(word)
		return sign


'''
Function:
	简单的Demo
'''
class Demo(QWidget):
	def __init__(self, parent=None):
		super().__init__()
		self.setWindowTitle('有道词典')
		self.Label1 = QLabel('原文')
		self.Label2 = QLabel('译文')
		self.LineEdit1 = QLineEdit()
		self.LineEdit2 = QLineEdit()
		self.translateButton = QPushButton()
		self.translateButton.setText('翻译')
		self.grid = QGridLayout()
		self.grid.setSpacing(12)
		self.grid.addWidget(self.Label1, 1, 0)
		self.grid.addWidget(self.LineEdit1, 1, 1)
		self.grid.addWidget(self.Label2, 2, 0)
		self.grid.addWidget(self.LineEdit2, 2, 1)
		self.grid.addWidget(self.translateButton, 2, 2)
		self.setLayout(self.grid)
		self.resize(600, 150)
		self.translateButton.clicked.connect(self.translate)
		self.bd_translate = baidu()
	def translate(self):
		word = self.LineEdit1.text()
		result = self.bd_translate.translate(word)
		self.LineEdit2.setText(result)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = Demo()
	demo.show()
	sys.exit(app.exec_())