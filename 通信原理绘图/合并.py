import matplotlib.pyplot as plt
import numpy as np



t1 = np.linspace(-np.pi*3, np.pi*3, 256, endpoint=True)
t2 = np.linspace(-np.pi*10, np.pi*10, 256, endpoint=True)
plt.xticks([-np.pi*10,-np.pi*8, -np.pi*6,-np.pi*4,-np.pi*2, 0,np.pi*10,np.pi*8, np.pi*6,np.pi*4,np.pi*2],
           [r'$-10\pi$', r'$-8\pi$',r'$-6\pi$',r'$-4\pi$',r'$-2\pi$', r'$0$', r'$10\pi$', r'$8\pi$',r'$6\pi$',r'$4\pi$',r'$2\pi$'])
f1,f2 = np.sinc(t1/np.pi),np.sinc(t2)
plt.plot(t1,f1,color='blue',linewidth=2,linestyle='--',label='Sa(t)')
plt.plot(t2,f2,color='red', linewidth=2, label='Sinc(t)')
plt.grid(True)
plt.xlabel('t')
plt.ylabel('f(t)')
plt.savefig("sinc.png")
plt.show()