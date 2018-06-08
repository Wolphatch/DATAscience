#使用numpy.array计算列表
import numpy as np
import pandas as pd
#1、basic calculation(np.array)

# np_height=np.array([1.73,1.68,1.71,1.89,1.79])
# np_weight=np.array([65.4,59.2,63.6,88.4,68.7])
# bmi=(np_weight/np_height)**2
# print(bmi) #bmi:[1429.10220856 1241.72335601 1383.31794398 2187.66551888 1473.01582348]


#2、numpy arrays:contain only one type

# np_dif=np.array(['123',123,True],dtype='U32') #The type there is U32
# #details of type can be found at:https://blog.csdn.net/wc781708249/article/details/78194039?locationNum=10&fps=1
# print(np_dif)  #np_dif:['123' '123' 'True']



#3、numpy subsetting(set rules for output)

#array1=np.array([1.73,1.68,1.71,1.89,1.79])
#print(array1>1.7)
# print(array1[array1>1.7])
#you can see:you can set rules for the output with form like line 19(bool type) or line 20
#output 1:[1.73 1.71 1.89 1.79]
#output 2:[1.73 1.71 1.89 1.79]



#4 2D numpy

#np_2d=np.array([[1.73,1.68,1.71,1.89,1.79],[65.4,59.2,63.6,88.4,68.7]])
#print(np_2d.shape)  #(2,5) means 2rows and 5 columns
#*subsetting is available too

#print(np_2d[0][2])  #1.71
#above one equals to:
#print(np_2d[0,2])  #1.71

#*select
#print(np_2d[:,1:3])  #that means from row0 to row1,select column1 to column3
#output:[[1.68  1.71]
#       [59.2  63.6]]

#5 2d calculation（+，*）

#np_mat = np.array([[1, 2],
#                   [3, 4],
#                   [5, 6]])

#print(np_mat+np.array([10,10]))
#[[11 12]
# [13 14]
# [15 16]]
#print(np_mat*np.array([10,10]))
#[[10 20]
# [30 40]
# [50 60]]



# #6 calcute the mean
# np_mat = np.array([[1, 2],
#                    [3, 4],
#                    [5, 6]])
# print(np.mean(np_mat[:,1]))  #4
# #You can use np.mean(obj[a:b,c:d])like line 65 to calculate the mean
# print(np.median(np_mat[:,1])) #4
# #You can use np.median() to calculate the median number
# np_co=np.array([[1,2,3],[4,3,4]])
# print(np.cov(np_co[1,:],np_co[0,:]))  #协方差：covariance
# print(np.std(np_co[:,0]))    #标准差：standard deviation
#
# print(np.corrcoef(np_co[:,0],np_co[:,1]))  #相关系数：correlation coefficent




#7 Usinf other arrays' indices to select
# positions = ['GK', 'M', 'A', 'D' ]
# heights = [191, 184, 185, 180]
# np_positions=np.array(positions)
# np_heights=np.array(heights)
# gk_heights=np_heights[np_positions=='GK']
# print(gk_heights) #[191]


#8、

# x = np.array([[24, 13, 14, 20],
#               [5,  6,   7,  8]])
# y = np.array([[6, 22, 2, 0],
#               [5,  6, 7, 8]])
# z = np.column_stack([x,y]) #加入行序列
# z1=np.row_stack([x,y])  #加入列序列
# z2=np.vstack([x[0],y[0]])
#print(z.shape)   #np表的行列数
#print(z)
'''
[[24 13 14 20  6 22  2  0]
 [ 5  6  7  8  5  6  7  8]]
'''
#print(z1)
'''
[[24 13 14 20]
 [ 5  6  7  8]
 [ 6 22  2  0]
 [ 5  6  7  8]]
 '''
#print(z2)
'''
[[24 13 14 20]
 [ 6 22  2  0]]

'''
'''
t=[[24 ,13 ,14 ,20],
 [ 5  ,6,  7,  8],
 [ 6 ,22  ,2 , 0],
 [ 5 , 6  ,7 , 8]]
t1=np.stack(t,axis=1)
a = [[1], [2], [3]]
b = [[1], [2], [3]]
c = [[1], [2], [3]]
d = [[1], [2], [3]]
t2=np.vstack([a,b,c,d])
t3=np.hstack(t2)
'''
#print(t2)
#print(t3)
'''
[[1]
 [2]
 [3]
 [1]
 [2]
 [3]
 [1]
 [2]
 [3]
 [1]
 [2]
 [3]]
[1 2 3 1 2 3 1 2 3 1 2 3]

'''



#9 np.logical_or()  (and,not)
'''


# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house>18.5,my_house<10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house<11,your_house<11))
'''




#10
'''
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500

medium=cars[np.logical_and(cars['cars_per_cap']>100,cars['cars_per_cap']<500)]


# Print medium
print(medium)
'''


#11
'''
my_house = np.array([[18.0, 20.0, 10.75, 9.50],[14.0, 24.0, 14.25, 9.0]])
for i in np.nditer(my_house.copy(order='C')):   #先行后列
  print(i)
for j in np.nditer(my_house.copy(order='F')):   #先列后行
  print(j)
'''



#12
'''
df=pd.DataFrame(pd.read_csv('beic.csv',index_col=0,encoding='gbk'))
df1=df.iloc[[0,1,2,3,4,5],0:5]
for label,row in df1.iterrows():
  print('{0} \n {1}'.format(label,row['name']))
  print('{0} \n {1}'.format(label,row))
'''




#13通过pandas的迭代加列
'''

df=pd.DataFrame(pd.read_csv('beic.csv',index_col=0,encoding='gbk'))
df1=df.iloc[[0,1,2,3,4,5],0:5]
for lab,row in df1.iterrows():
    df1.loc[lab,'NAME']=row['name']
print(df1)
'''


