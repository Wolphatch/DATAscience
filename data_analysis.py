# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sqlalchemy import create_engine
import numpy as np
import cmath
'''
#读取sqlite-筛选-可视化
engine=create_engine('sqlite:///Chinook.sqlite')
con=engine.connect()
rs=con.execute('SELECT * FROM Customer')
df=pd.DataFrame(rs.fetchall())
A=df.loc[:,7]
B=A.value_counts()  #计算此列各个元素出现的次数
sns.set(color_codes=True)
country=list(B.index)
count=list(B)
country=np.array(country)
count=np.array(count)
plt.scatter(country,count)
plt.xticks(fontsize=8,rotation=40)
plt.show()
'''

#swarmplot
'''
cmmd=pd.read_excel('CMMD2.0.xlsx')
cmmd=cmmd.loc[3:,:]

sns.swarmplot(x='年份',y='票房（亿元）',data=cmmd)
plt.xlabel('year')
plt.ylabel('box')
plt.show()
'''

'''
#swarmplot在数据过多的情况下有缺陷
#使用Empirical cumulative distribution functions（经验累积分布函数）
#作为一种分布，标准状态下，总体为1，有n个观测值，则每个观测值平均比例为1/n
#非标准情况下，所有观测值占比之和为1
#同样使用swarmplot数据
cmmd=pd.read_excel('CMMD2.0.xlsx')
box=cmmd.loc[3:,'票房（亿元）']
box_list=[]
for i in box:
    box_list.append(i)
boxlist=np.array(box_list)
boxlist.sort()
x=boxlist
y=np.arange(1,len(x)+1)/len(x)  #y分成n格，x有n个，积为1
plt.plot(x,y)
plt.show()
'''





'''
#percentile，mean，median
#generate
plt.figure(0)
list=np.random.randint(1,1000,100)    #产生随机整数
list=pd.DataFrame(list)  #转化为dataframe
list.loc[:,1]='Randint'
list.columns=['num','rand_type']
#print(list)
#calculate
mean=np.mean(list['num']) #list的平均数
median=np.median(list['num'])
percentile=np.percentile(list['num'],[25,50,75]) #list的百分比数，输出25%，50%。75%三档

#print
#print('The persentile of list is {0}'.format(percentile))
#print('The mean of list is {0},and median is {1}'.format(mean,median))

#use sns to make box plot
sns.boxplot(x='num',y='rand_type',data=list) 
#图像中，蓝色区域的中间那条线为中位数（50%percentile）
#边缘分别为25%和75%，25%percentile指list在从小到大排序之后在25%的数，
#如有100个数，则就是排序后第25个数
plt.show()


#图2
plt.figure(1)
plt.margins=(5)

#建立numpy随机数组，100个
x_vers=np.random.randint(1,1000,100)
x_vers.sort() #排序

#计算百分数点
pcts_point=np.array([2.5,25,50,75,97.5]) #设置5个百分数点
pcts=np.percentile(x_vers,pcts_point)    #计算百分数点具体是哪个数

#建立经验累积分布函数
y_vers=np.arange(1,len(x_vers)+1)/len(x_vers)

#画图
plt.plot(x_vers,y_vers)

#画上百分数点，红色，菱形点，无线连接
plt.plot(pcts,pcts_point/100,color='R',marker='D',linestyle='none')

#标题
plt.xlabel('Number')
plt.ylabel('Percentiles')
plt.grid()
plt.show()
'''



'''
list_x=np.random.randint(0,100,100)
list_x.sort()
list_y=np.random.randint(0,100,100)
print(list_x.var()) #方差
print(list_x.std()) #标准差

#协方差
xmean=list_x.mean()   #μx
ymean=list_y.mean()   #μy
xvar=(list_x)-np.array(xmean)  #xi-μx
yvar=(list_y)-np.array(ymean)  #yi-μy
xyvar=xvar*yvar    #(xi-μx)(yi-μy）
sum=sum(xyvar)/(len(list_x)-1)  #∑(xi-μx)(yi-μy）/(n-1)
print(sum)#协方差，描述变量之间的相互关系，cov=1/(n-1)∑(xi-μx)(yi-μy）
#cov(X,Y)=E(XY)-E(X)E(Y)

#协方差矩阵
print(np.cov(list_x,list_y))
#二维的情况下共计算四个值，分别为xx，xy，yx,yy四个数组的相关系数

#相关系数
print(np.cov(list_x,list_y)/(np.std(list_x)*np.std(list_y)))
#相关系数计算为cov(x,y)/(std(x)*std(y))
'''



'''
#伯努利概型
#在抛硬币的时候会出现两种结果，正面和反面，实验n次之后正面概率接近多少
#现在抛四个硬币，计算其全是正面和全是反面的概率

#首先使用由伯努利概型计算：4C4*(1/2)^4*(1/2)^0=0.0625

#其次使用计算机模拟，模拟次数为200次
#使用random，0-0.5之间的为反面，0.5-1为正面
probability=[]
j=0
while j<500:
   count=0
   i=0
   while i<500:
       coin_set = np.random.random(4)
       if (coin_set>=[0.5,0.5,0.5,0.5]).all():
          count+=1
       i+=1
   j+=1                           #一共执行了25万次
   probability.append(count/500)
plt.hist(probability,bins=50)
plt.axis([0,0.1,0,60])
plt.plot([0.0625,0.0625],[0,58],c='#FFDAB9')    #标出0.0625的位置
plt.annotate('0.0625',xy=(0.0625,30),xytext=(0.085,45),   #xy为被注释的点，xytest为注释的位置
             arrowprops=dict(facecolor='black', shrink=0.01),)  #个性化箭头
plt.show()                #做出的图形为正态分布，靠近0.0625的地方最密集
'''






'''
#二项分布
P(X=k)=C(k\n)p^k·(1-p)^(n-k)
#在伯努利概型中，有n个独立的事件，事件发生A的概率是p，事件发生B的概率为（1-p）
#如硬币是正面的概率为1/2，都是正面的概率为0.0625
#numpy.random的二项分布模拟二项分布的发生。如下，一共有60个事件，发生事件A（success）的概率为0.5
#那么这个函数便会输出在60个事件中，发生事件A的次数是多少。
#size的作用是将上述过程重复k次，生成一个列表记录每次的结果。
#PS,二项分布在p=0.5的时候可以近似正态分布
array=np.random.binomial(60,0.5,size=1000)
plt.hist(array,bins=500)
plt.show()

#例如如果要计算伯努利硬币问题,先运行10000次函数，计算四个硬币都为正的次数，再除以总次数
num=sum(np.random.binomial(4,0.5,size=10000)==4)/10000
print(num)  #0.0657


#二项分布累计分布函数

array=np.random.binomial(60,0.5,size=10000)
array1=np.random.binomial(60,0.2,size=10000)
array2=np.random.binomial(60,0.8,size=10000)
array1.sort()
array2.sort()
array.sort()
y=np.arange(1,len(array)+1)/len(array)
plt.plot(array,y,marker='.',linestyle='none',c='#E6E6FA')
plt.plot(array1,y,marker='.',linestyle='none',c='#FFF68F')
plt.plot(array2,y,marker='.',linestyle='none',c='#FF6A6A')
plt.show()
'''



#泊松分布
#解释：X~P(X=k)=(λ^k/k!)·e^-λ,E(X)=λ,D(X)=λ
#定义：假定一个事件在一段时间内随机发生，且符合以下条件：
#（1）将该时间段无限分隔成若干个小的时间段，在这个接近于零的小时间段里，该事件发生一次的概率与这个极小时间段的长度成正比。
#（2）在每一个极小时间段内，该事件发生两次及以上的概率恒等于零。
#（3）该事件在不同的小时间段里，发生与否相互独立。
#则该事件称为poisson process
#by作者：楚小鱼
#链接：https://www.zhihu.com/question/26441147/answer/128055090
#泊松分布也可以看做是有限的二项分布（当二项分布的p很低的时候）

#CDF及分布(双边坐标轴）
array=np.random.poisson(6,size=100000)
array.sort()
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.hist(array,bins=45,color='#E6E6FA')
ax1.axis([0,25,0,16500])

ax2=ax1.twinx()
ax2.plot(array,np.arange(1,len(array)+1)/len(array),marker='.',linestyle='none',c='#FF6A6A')
plt.xlabel('Poisson Value')
plt.ylabel('CDF')
plt.show()


#泊松与二项的比较，其期望与标准差
# Draw 10,000 samples out of Poisson distribution: samples_poisson
samples_poisson = np.random.poisson(10, 10000)

# Print the mean and standard deviation
print('Poisson:     ', np.mean(samples_poisson),
      np.std(samples_poisson)*np.std(samples_poisson))

# Specify values of n and p to consider for Binomial: n, p
n = [20, 100, 1000]
p = [0.5, 0.1, 0.01]

# Draw 10,000 samples for each n,p pair: samples_binomial
for i in range(3):
    samples_binomial = np.random.binomial(n[i], p[i], size=10000)

    # Print results
    print('n =', n[i], 'Binom:', np.mean(samples_binomial),
          np.std(samples_binomial)*np.std(samples_binomial))





























