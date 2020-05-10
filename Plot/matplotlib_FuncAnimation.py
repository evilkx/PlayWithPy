import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation   # 导入负责绘制动画的接口
# 其中需要输入一个更新数据的函数来为fig提供新的绘图信息

fig, ax = plt.subplots()
x, y= [], []
line, = plt.plot([], [], '.-',color='orange')

def init():
    ax.set_xlim(-5, 40)
    ax.set_ylim(-2, 2)
    return line

def update(step):
    x = np.linspace(0,10*np.pi,100)
    y = np.cos(1.2*x+step)  #这里只改变相位
    line.set_data(x, y) #设置新的 x，y
    return line

ani = FuncAnimation(fig, update,init_func=init,interval=100)
plt.show()
