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

t = np.linspace(-np.pi*10, np.pi*10, 256, endpoint=True)
f = np.sinc(t)                          #sinc函数
p2,=plt.plot(t,f,color='red',linewidth=2)
plt.xticks([-np.pi*10,-np.pi*8, -np.pi*6,-np.pi*4,-np.pi*2, 0,np.pi*10,np.pi*8, np.pi*6,np.pi*4,np.pi*2],
           [r'$-10\pi$', r'$-8\pi$',r'$-6\pi$',r'$-4\pi$',r'$-2\pi$', r'$0$', r'$10\pi$', r'$8\pi$',r'$6\pi$',r'$4\pi$',r'$2\pi$'])
plt.xlabel('t')
plt.ylabel('Sinc(t)')
plt.legend(handles=[p2], labels=['Sinc(t)'],  loc='best')
plt.grid(True)
plt.savefig("第二题.png")
plt.show()