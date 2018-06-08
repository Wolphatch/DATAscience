import matplotlib.pyplot as plt
import numpy as np
from matplotlib import *
from pylab import *

#线条风格
#实线：'-' ， 破折线：'--' ， 点划线：'-.' ,虚线：':'
#线条标记：
#'o'	圆圈	  '.'	点
#'D'	菱形	  's'	正方形
#'h'	六边形1	  '*'	星号
#'H'	六边形2	  'd'	小菱形
#'_'	水平线	  'v'	一角朝下的三角形
#'8'	八边形  	'<'	一角朝左的三角形
#'p'	五边形	  '>'	一角朝右的三角形
#','	像素	  '^'	一角朝上的三角形
#'+'	加号  	  '\	'竖线
#'None','',' '	无  	'x'	X



#颜色：
'''
别名	颜色	别名	颜色
b	    蓝色	 g	    绿色
r	    红色	 y	    黄色
c	    青色	 k	    黑色
m	    洋红色	 w	    白色
'''
#也可以color=(r,g,b)   r,g,b为RGB颜色


#背景色： matplotlib.pyplot.subplot()
#subplot(111,axisbg=(0.1843,0.3098,0.3098))


'''
#开始 例子1
pi=3.1415926
x=np.arange(-5*pi,5*pi,0.02)
y1=np.sin(x)
y2=np.cos(x)
#画第一幅图
plt.figure(1)
#在一个两行一列的列表中画第一幅图的第一幅图,用于合并画图
plt.subplot(2,1,1)
#设置第二张图的坐标轴范围
plt.xlim(-6*pi,6*pi)  #x坐标轴范围-6π到6π
plt.ylim(-5,5)        #x坐标轴范围-2到2
#画第一幅图第一张
plt.plot(x,y1)

#在一个两行一列的列表中画第一幅图的第二幅图,
plt.subplot(2,1,2)
#设置第二张图的坐标轴范围
plt.xlim(-6*pi,6*pi)  #x坐标轴范围-6π到6π
plt.ylim(-5,5)        #x坐标轴范围-2到2
#第一幅图第二张，并在第二张中化多条不同的线
plt.plot(x,y1,'r-.',x,y2,'r:')  #plot（1,2,3）1为x轴，2为y轴，3为线型


#画第二幅图
plt.figure(2)
plt.subplot(2,1,1)
plt.xlim(-6*pi,6*pi)  #x,y轴范围
plt.ylim(-5,10)
x2=x+1
plt.plot(x2,y1,'r--')

#画第二幅图的第二张图
plt.subplot(2,1,2)
plt.xlim(-6*pi,6*pi)  #x,y轴范围
plt.ylim(-5,10)
plt.plot(x2,y2,'r:')
#输出
plt.show()
'''



'''
#例子2 hist
#numpy.random.randn(d0, d1, …, dn)是从标准正态分布中返回一个或多个样本值。
#关于numpy模块的随机数可以参考：https://blog.csdn.net/kancy110/article/details/69665164
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
#创建画板1（fighre（1）），并在画板使用.add_subplot()创建画纸1
#还有另一种方法叫做.add_axes().ref：https://www.zhihu.com/question/51745620
fig=plt.figure(1)
ax1=fig.add_subplot(2,1,1)#两行一列的画布，第一个位置
#为x,y轴命名，添加title
plt.xlabel('Distribution')
plt.ylabel('probability')
plt.title('Histogram of normal')
#添加文字
plt.text(60,0.025,r'ASD')
#plt.axis([a,b,c,d])定制坐标轴,a,b为横坐标开始结束，c,d为纵坐标开始结束
plt.axis([25,175,0,0.03])
#创立概率分布柱形图，bins为柱子数量，alpha为透明度，facecolor为颜色
plt.hist(x,bins=50,density=1,facecolor='g',alpha=0.75)
plt.grid(True)
#plt.show()
'''
#还有另一种方法叫做.axes().   
dt=0.001
t = np.arange(0.0, 10.0, dt)
r = np.exp(-t[:1000]/0.05) # impulse response
x = np.random.randn(len(t))
s = np.convolve(x, r)[:len(x)]*dt # colored noise
#创建第二块画板的主画
ax2=plt.figure(2)
#
plt.plot(t,s)
#x,y轴的范围，定制坐标轴
plt.axis=plt.axis([0, 1, 1.1*np.amin(s), 2*np.amax(s)]) #括号里面的值前两个是轴域原点坐标（从左下角计算的），后两个是显示坐标轴的长度
#为x,y轴命名，添加title
plt.xlabel('time (s)')
plt.ylabel('current (nA)')
plt.title('Gaussian colored noise')
#内嵌图
ax2_1=plt.axes([.65, .6, .2, .2], facecolor='y')
n, bins, patches = plt.hist(s, 400, density=1)
plt.title('Probability')
plt.xticks([])
plt.yticks([])
#第二个内嵌图
a = plt.axes([0.2, 0.6, .2, .2], facecolor='y')
plt.plot(t[:len(r)], r)
plt.title('Impulse response')
plt.xlim(0, 0.2)
plt.xticks([])
plt.yticks([])
plt.show()





