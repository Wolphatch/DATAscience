import numpy as np


import pandas as pd


'''
#1、使用panda处理dict，将字典转化为dataframe
dict={
    'country':['brazil','russia','india','china','south africa'],
   'capital':['brasilia','moscow','new delhi','beijing','pretoria'],
    'area':[8.516,17.1,3.286,9.597,1.221]
}
#将字典转化为pandas的DataFrame
brics=pd.DataFrame(dict) #这种转化只有列名称，行名称需要自己输入。
brics.index=['BR','RU','IN','CH','SA']
print(brics)
'''

'''
#以下选用电影票房数据库

#2、使用pandas打开csv文件（可用excel打开）
df=pd.DataFrame(pd.read_csv('beic.csv',index_col=0,encoding='gbk'))
print(df)
df1=pd.DataFrame(pd.read_excel('beic.xlsx',index_com=0,encoding='gbk'))
'''

'''
#3通过传递一个numpy array，时间索引以及列标签来创建一个DataFrame
dates=pd.date_range('20180401',periods=20) 
#periods用处是：输入20180401，就会依次递归日期：20180402.20180403等

df=pd.DataFrame(np.random.randn(20,4),index=dates,columns=list('1234')) 
#np.random.randn（20，4创建一个20行四列的正态分布矩阵

print(df)
'''

'''
#4查看数据类型
df=pd.DataFrame(pd.read_csv('beic.csv',index_col=0,encoding='gbk'))
print(df)
print(df.dtypes)
'''

'''
#5column access[]
df=pd.DataFrame(pd.read_csv('beic.csv',index_col=0,encoding='gbk'))
print(df['name']) #输出index列，index名，及Name: name, Length: 100, dtype: object
print(df[['name']]) #输出colunm名，inndex列，index名，及[100 rows x 1 columns]

#组合输出
df=pd.DataFrame(pd.read_csv('beic.csv',index_col=0,encoding='gbk'))
print(df[['name','year','box']]) 
'''

'''
#6row access[]
#与列切片不同，行切片的样式是：
df=pd.DataFrame(pd.read_csv('beic.csv',index_col=0,encoding='gbk'))
print(df[1:9]) #括号左闭右开，第九项不会打印
'''




'''
#7 loc and iloc 用于选取特定的行和列
df=pd.DataFrame(pd.read_csv('beic.csv',index_col=0,encoding='gbk'))
#print(df.loc[5]) #选取第五行，竖向输出
#print(df.loc[[5]]) #横向输出
#
print(df.loc[[1,5],['name','box']]) #loc进行定位
#       name   box
# code
# 1     建国大业  4.16
# 2     十月围城  2.91
print(df.iloc[[0,1,2,3],[2,3]])

# code     name      box2016
# 1       建国大业   5.1042
# 2       十月围城   3.5705
# 3      赤壁(下)   3.2024
# 4     三枪拍案惊奇   3.1656

#loc是根据dataframe的具体标签选取列，而iloc是根据标签所在的位置，从0开始计数。
#无论是iloc还是loc后面的方括号都可以使用：
#iloc[1:2,1:2] 或iloc[[1,2,3],[1,2,3]]这两种形式来进行定位

#总结
#直接选取整行可以用ros access：df[[1:4]
#直接选取整列可以用colunm access: df[['name','box2016']]
#也可以用iloc或者loc(iloc的方括号只能填数字，loc以标签为基础，填标签）
#整行df.iloc[2:5,:]
'''

'''
#8合并

#concat
#创建两个dataframe
df=pd.DataFrame(np.random.randn(5,5))
df2=pd.DataFrame(np.random.randn(5,5))
print(df)
print(df2)
#切片
pieces=[df[0:2],df2[2:5]]
#合并df[0:2],df2[2:5]
print(pd.concat(pieces))
'''

#Join
df=pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                       'A':['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})
print(df)
df2=pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                    'B': ['B0', 'B1', 'B2']})
print(df2)

df3=df2.join(df,lsuffix='df', rsuffix='df2')
print(df3)

df4=df.set_index('key').join(df2.set_index('key'))
print(df4)

df5=df.join(df2.set_index('key'),on='key')
print(df5)

#结果
#     A key
# 0  A0  K0
# 1  A1  K1
# 2  A2  K2
# 3  A3  K3
# 4  A4  K4
# 5  A5  K5
#     B key
# 0  B0  K0
# 1  B1  K1
# 2  B2  K2
#     B keydf   A keydf2
# 0  B0    K0  A0     K0
# 1  B1    K1  A1     K1
# 2  B2    K2  A2     K2
#       A    B
# key
# K0   A0   B0
# K1   A1   B1
# K2   A2   B2
# K3   A3  NaN
# K4   A4  NaN
# K5   A5  NaN
#     A key    B
# 0  A0  K0   B0
# 1  A1  K1   B1
# 2  A2  K2   B2
# 3  A3  K3  NaN
# 4  A4  K4  NaN
# 5  A5  K5  NaN

'''
#Append 将一行连接到一个DataFrame上
df=pd.DataFrame(np.random.randn(7,4),index=list('0123456'),columns=list('ABCD'))
print(df)
df1=df.iloc[[3],:]
df=df.append(df1,ignore_index=True)
print(df)
'''

#输出
#           A         B         C         D
# 0 -0.139236 -1.083378  0.880262  0.082907
# 1 -0.846305  0.183001 -0.463167  0.673914
# 2 -1.446974 -0.942320  0.694767  3.097230
# 3  0.253265  0.606957  0.501034  0.782664
# 4 -0.376266 -0.499146  0.590650 -0.634504
# 5 -0.893080 -2.524915  0.049768  0.770095
# 6 -0.405101 -0.307824 -0.585408  0.465861
#           A         B         C         D
# 0 -0.139236 -1.083378  0.880262  0.082907
# 1 -0.846305  0.183001 -0.463167  0.673914
# 2 -1.446974 -0.942320  0.694767  3.097230
# 3  0.253265  0.606957  0.501034  0.782664
# 4 -0.376266 -0.499146  0.590650 -0.634504
# 5 -0.893080 -2.524915  0.049768  0.770095
# 6 -0.405101 -0.307824 -0.585408  0.465861
# 7  0.253265  0.606957  0.501034  0.782664
