import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


'''
#import data with numpy

#E.g 1
#使用seaslug.txt
# Assign filename: file
file = 'seaslug.txt'

#因为首行为str，其余为float，直接load会报错

# 第一种解决方法，将数据全部转变为str
data = np.loadtxt(file, delimiter='\t', dtype=str)


#第二种，跳过第一行
# Import data as floats and skip the first row: data_float
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1,usecols=[0,1])
print(data)
#arguments：分隔符('\t'或',')，跳过几行，使用哪几行，使用什么数据格式
#打印后发现是[['Time' 'Percent']['99' '0.067']['99' '0.133']['99' '0.067']]形式的表


# Plot a scatterplot of the data
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()
'''


'''
#E.g 2
#依旧使用seaslug
#name=True tells us there is a header（Firsr line)
data1=np.genfromtxt(file,delimiter='\t',names=True,missing_values=0,dtype=None)

#打印一下，看genfromtxt的样子，发现是一个[(a,b) (c,d)...]样式的表
print(data1)
'''

'''
#E.g 3
#读取csv文件可以用recfromcsv(),效果和genfromtxt类似
d=np.recfromcsv(file,delimiter=',',names=True,dtype=None)
'''




#Using Pandas to import data

#E.g 1
'''
# Assign the filename: file
file = 'titanic.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())
'''

'''
#E.g2
#使用pandas读取csv，并转变为DataFrame,使用matplotlib作图
# Assign the filename: file
file = 'titanic.csv'

# Read the first 5 rows of the file into a DataFrame: data
data=pd.read_csv(file,nrows=200)

# Build a numpy array from the DataFrame: data_array
#使用data.values表示去掉行标题
data_array=np.array(data.values)

# Print the datatype of data_array to the shell
print(data)

pd.DataFrame.hist(data[['Age']])
plt.show()
'''




'''
#import pickled files
#pickled文件一般都是被序列化的，即将objects转化为bytestream
#很多时候许多数据格式不知道如何存储，就可以转化为pickle file储存）

#import pickle
import pickle


#写一个简单的学生类用来存储
class student(object):
   def  __init__(self,stuname,stulesson,stuno):
          self.name=stuname
          self.lesson=stulesson
          self.no=stuno

   def __repr__(self):   #类用来返回的函数
          return 'Student:Name:%s,Lesson:%s,No:%s'%(self.name,self.lesson,self.no)

#将类实例化
Marry=student('Marry','Data Mining','01')
Candy=student('Candy','Data Mining','02')

#创建一个叫做Student的pickle文件，pickle为二进制文件，需用wb+
file=open('Student.pkl', 'wb+')

#将实例写入
pickle.dump(Marry,file)
pickle.dump(Candy,file)

#在Python中读取（pickle的读取有迭代属性，会一个一个读）
file=open('Student.pkl', 'wb+')
data=pickle.load(file)
print(data)
data=pickle.load(file)  #读第二次
print(data)
'''



'''
#使用pandas读取excel
#这里以一个股票在2017年的股价为例

#读取
file=pd.ExcelFile('sh600009.xlsx')

#读取excel里sheet名
sheetname=file.sheet_names
print(sheetname)     #['sh600009', 'Sheet1']

#对sheet的操作
#按照sheet名读取
df=file.parse('sh600009')
#按照sheet顺序读取
df1=file.parse(0)

#打印表头，即数据的index
print(df.keys())

#个性化读取
#usecols：想要用的列，需要[]。skiprows：跳过第几行。names：重命名index的名字
df2=file.parse(0,usecols=[1],skiprows=1,names=['Date'])
print(df2)
'''





#以datacamp的教程为例
'''
#importing HDF5 files


#1、
# Import packages
import numpy as np
import h5py

# Assign filename: file
file='test.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)
#output:
  #meta
  #quality
  #strain
'''



'''
# 2、Extracting data from your HDF5 file
#In this exercise, you'll extract some of the LIGO experiment's actual data from the HDF5 file and you'll visualize it.
#To do so, you'll need to first explore the HDF5 group 'strain'

#结构
#-----data:
#          ---meta
#          ---quality
#          ---strain
#                      ---Strain



#  Get the HDF5 group: group
group=data['strain']

# Check out keys of group
#查找data['strain']这个下的key
for key in group.keys():
    print(key)            #output:Strain

# Set variable equal to time series data: strain
strain=data['strain']['Strain'].value

#Strain下储存数据列表：[-1.77955839e-18 -1.76552067e-18 -1.71049117e-18 ... -1.76375155e-18 -1.72364846e-18 -1.71969299e-18]

# Set number of time points to sample: num_samples
num_samples=1000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()
'''






















