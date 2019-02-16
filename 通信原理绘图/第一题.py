# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.axisartist as axisartist

#创建画布，可以删减，只是为了得到坐标轴的箭头
fig = plt.figure()
#使用axisartist.Subplot方法创建一个绘图区对象ax
ax = axisartist.Subplot(fig, 111)
#将绘图区对象添加到画布中
fig.add_axes(ax)
#通过set_axisline_style方法设置绘图区的底部及左侧坐标轴样式
#"-|>"代表实心箭头："->"代表空心箭头
ax.axis["bottom"].set_axisline_style("->", size = 1.5)
ax.axis["left"].set_axisline_style("->", size = 1.5)
#通过set_visible方法设置绘图区的顶部及右侧坐标轴隐藏
ax.axis["top"].set_visible(False)
ax.axis["right"].set_visible(False)


t = np.linspace(-np.pi*3, np.pi*3, 256, endpoint=True)
f = np.sinc(t/np.pi)                          #Sa函数
p1,=plt.plot(t,f,color='blue',linewidth=2,label='Sa(t)')
plt.xticks([-np.pi*3,-np.pi*2, -np.pi*1, 0,np.pi*3,np.pi*2, np.pi*1],
           [r'$-3\pi$', r'$-2\pi$',r'$-\pi$', r'$0$', r'$3\pi$', r'$2\pi$',r'$\pi$'])
plt.xlabel('t')
plt.ylabel('Sa(t)')
plt.legend(handles=[p1], labels=['Sa(t)'],  loc='best')
plt.grid(True)
plt.savefig("第一题.png")
plt.show()

