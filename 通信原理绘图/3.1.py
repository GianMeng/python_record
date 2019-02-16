# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

N=200
A=1
P=0.5*np.pi
t = np.linspace(-10, 10,2000)
y = A*np.square(P*(t+0.5),25)
plt.subplot(2,1,1)
plt.plot(t,y)
plt.axis([-5,5,0,1.5])
plt.xticks(np.arange(-5, 5, 0.5))
plt.xlabel('时间')
plt.ylabel('幅值')
plt.title('周期矩形脉冲信号')
Y=np.fft.fft(y,N)              #傅里叶变换
fy=(np.abs(Y)*2)/N         #得到频谱
plt.subplot(2,1,2)
plt.stem(fy)
plt.axis([0,30,0,1.5])
plt.xlabel('频率')
plt.ylabel('幅值')
plt.title('周期矩形脉冲信号的幅频谱图')
plt.show()